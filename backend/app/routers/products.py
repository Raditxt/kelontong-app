from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas


router = APIRouter(prefix="/products", tags=["products"])


@router.get("", response_model=list[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return db.query(models.Product).order_by(models.Product.name).all()


@router.get("/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    prod = db.get(models.Product, product_id)
    if not prod:
        raise HTTPException(404, "Product not found")
    return prod


@router.post("", response_model=schemas.ProductOut, status_code=201)
def create_product(payload: schemas.ProductCreate, db: Session = Depends(get_db)):
    prod = models.Product(**payload.dict())
    db.add(prod)
    db.commit()
    db.refresh(prod)
    # record initial price history if price_buy provided
    if payload.price_buy is not None:
        ph = models.PriceHistory(product_id=prod.id, price_buy=payload.price_buy)
        db.add(ph)
        db.commit()
    return prod


@router.put("/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, payload: schemas.ProductUpdate, db: Session = Depends(get_db)):
    prod = db.get(models.Product, product_id)
    if not prod:
        raise HTTPException(404, "Product not found")
    old_buy = prod.price_buy
    for k, v in payload.dict(exclude_unset=True).items():
        setattr(prod, k, v)
    db.commit()
    db.refresh(prod)
    # log price change if price_buy changed
    if payload.price_buy is not None and payload.price_buy != old_buy:
        ph = models.PriceHistory(product_id=prod.id, price_buy=payload.price_buy)
        db.add(ph)
        db.commit()
    return prod


@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    prod = db.get(models.Product, product_id)
    if not prod:
        raise HTTPException(404, "Product not found")
    db.delete(prod)
    db.commit()