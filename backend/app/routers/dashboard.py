from fastapi import APIRouter, Depends
# top products today (by qty)
top_rows = db.execute(
select(models.Product.name, func.sum(models.TransactionItem.qty).label("qty"))
.join(models.TransactionItem, models.Product.id == models.TransactionItem.product_id)
.join(models.Transaction, models.TransactionItem.transaction_id == models.Transaction.id)
.where(func.date(models.Transaction.date) == today, models.Transaction.type == models.TxType.sale)
.group_by(models.Product.name)
.order_by(func.sum(models.TransactionItem.qty).desc())
.limit(5)
).all()
top_products = [{"name": r[0], "qty": int(r[1])} for r in top_rows]


# low stock list (threshold 5)
lows = db.execute(
select(models.Product.id, models.Product.name, models.Product.stock)
.where(models.Product.stock <= 5)
.order_by(models.Product.stock.asc())
.limit(10)
).all()
low_stock = [{"id": r[0], "name": r[1], "stock": int(r[2])} for r in lows]


return {
"revenue_today": revenue,
"total_transactions": int(total_tx),
"top_products": top_products,
"low_stock": low_stock,
}


@router.get("/alerts", response_model=schemas.AlertsOut)
def alerts(threshold: int = 5, exp_days: int = 30, db: Session = Depends(get_db)):
# low stock
lows = db.execute(
select(models.Product.id, models.Product.name, models.Product.stock)
.where(models.Product.stock <= threshold)
.order_by(models.Product.stock.asc())
).all()
low_stock = [{"id": r[0], "name": r[1], "stock": int(r[2])} for r in lows]


# expiring within exp_days
from datetime import timedelta
today = date.today()
cutoff = today + timedelta(days=exp_days)
exp = db.execute(
select(models.Product.id, models.Product.name, models.Product.expired_date)
.where(models.Product.expired_date.is_not(None))
.where(models.Product.expired_date <= cutoff)
.order_by(models.Product.expired_date.asc())
).all()
expiring = [
{"id": r[0], "name": r[1], "expired_date": r[2].isoformat() if r[2] else None}
for r in exp
]


return {"low_stock": low_stock, "expiring": expiring}