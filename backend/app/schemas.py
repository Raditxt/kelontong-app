from pydantic import BaseModel, condecimal
class Config:
orm_mode = True


class ProductBase(BaseModel):
name: str
sku: Optional[str] = None
stock: int = 0
price_buy: condecimal(max_digits=12, decimal_places=2) = 0
price_sell: condecimal(max_digits=12, decimal_places=2) = 0
expired_date: Optional[date] = None
supplier_id: Optional[int] = None


class ProductCreate(ProductBase):
pass


class ProductUpdate(BaseModel):
name: Optional[str]
sku: Optional[str]
stock: Optional[int]
price_buy: Optional[condecimal(max_digits=12, decimal_places=2)]
price_sell: Optional[condecimal(max_digits=12, decimal_places=2)]
expired_date: Optional[date]
supplier_id: Optional[int]


class ProductOut(ProductBase):
id: int
class Config:
orm_mode = True


class TransactionItemIn(BaseModel):
product_id: int
qty: int
price: condecimal(max_digits=12, decimal_places=2)


class TransactionCreate(BaseModel):
type: TxType
items: List[TransactionItemIn]


class TransactionOut(BaseModel):
id: int
type: TxType
total_amount: condecimal(max_digits=14, decimal_places=2)
date: datetime
class Config:
orm_mode = True


class DashboardDailyOut(BaseModel):
revenue_today: condecimal(max_digits=14, decimal_places=2)
total_transactions: int
top_products: List[dict]
low_stock: List[dict]


class AlertsOut(BaseModel):
low_stock: List[dict]
expiring: List[dict]