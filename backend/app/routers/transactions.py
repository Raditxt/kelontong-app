from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from decimal import Decimal
from ..database import get_db
from .. import models, schemas


router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("", response_model=list[schemas.TransactionOut])
def list_transactions(db: Session = Depends(get_db)):
    txs = db.execute(
        select(models.Transaction)
        .order_by(models.Transaction.date.desc())
        .limit(200)
    ).scalars().all()
    return txs


@router.post("", response_model=schemas.TransactionOut, status_code=201)
def create_transaction(payload: schemas.TransactionCreate, db: Session = Depends(get_db)):
    # Basic transaction handling: update stock & compute total
    total = Decimal("0.00")
    tx = models.Transaction(type=payload.type)
    db.add(tx)
    db.flush()  # get tx.id

    for item in payload.items:
        prod = db.get(models.Product, item.product_id)
        if not prod:
            raise HTTPException(400, f"Product {item.product_id} not found")
        
        if payload.type == models.TxType.sale:
            if prod.stock < item.qty:
                raise HTTPException(400, f"Insufficient stock for {prod.name}")
            prod.stock -= item.qty
        else:  # purchase
            prod.stock += item.qty
            # update last buy price to the price in this purchase
            prod.price_buy = item.price
            db.add(models.PriceHistory(product_id=prod.id, price_buy=item.price))

        total += (Decimal(item.price) * item.qty)
        db.add(models.TransactionItem(
            transaction_id=tx.id, 
            product_id=prod.id, 
            qty=item.qty, 
            price=item.price
        ))

    tx.total_amount = total
    db.commit()
    db.refresh(tx)
    return tx