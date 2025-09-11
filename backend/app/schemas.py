from typing import Optional, List, Annotated
from pydantic import BaseModel, Field
from datetime import date, datetime
from enum import Enum
from decimal import Decimal


# 🔹 Definisikan type alias pakai Annotated
Decimal12_2 = Annotated[Decimal, Field(max_digits=12, decimal_places=2)]
Decimal14_2 = Annotated[Decimal, Field(max_digits=14, decimal_places=2)]


class TxType(str, Enum):
    sale = "sale"
    purchase = "purchase"


class ProductBase(BaseModel):
    name: str
    sku: Optional[str] = None
    stock: int = 0
    price_buy: Decimal12_2 = 0
    price_sell: Decimal12_2 = 0
    expired_date: Optional[date] = None
    supplier_id: Optional[int] = None


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    stock: Optional[int] = None
    price_buy: Optional[Decimal12_2] = None
    price_sell: Optional[Decimal12_2] = None
    expired_date: Optional[date] = None
    supplier_id: Optional[int] = None


class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True


class TransactionItemIn(BaseModel):
    product_id: int
    qty: int
    price: Decimal12_2


class TransactionCreate(BaseModel):
    type: TxType
    items: List[TransactionItemIn]


class TransactionOut(BaseModel):
    id: int
    type: TxType
    total_amount: Decimal14_2
    date: datetime

    class Config:
        orm_mode = True


class DashboardDailyOut(BaseModel):
    revenue_today: Decimal14_2
    total_transactions: int
    top_products: List[dict]
    low_stock: List[dict]


class AlertsOut(BaseModel):
    low_stock: List[dict]
    expiring: List[dict]
