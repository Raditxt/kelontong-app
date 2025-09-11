from sqlalchemy import Column, Integer, String, Numeric, Date, DateTime, Enum, ForeignKey, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
import enum
from .database import Base

class RoleEnum(str, enum.Enum):
    admin = "admin"
    kasir = "kasir"
    viewer = "viewer"


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[RoleEnum] = mapped_column(Enum(RoleEnum), default=RoleEnum.admin, nullable=False)
    
    transactions: Mapped[list["Transaction"]] = relationship(back_populates="user")


class Supplier(Base):
    __tablename__ = "suppliers"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    contact: Mapped[str | None] = mapped_column(String(100))
    products: Mapped[list["Product"]] = relationship(back_populates="supplier")


class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), index=True, nullable=False)
    sku: Mapped[str | None] = mapped_column(String(60), unique=True)
    stock: Mapped[int] = mapped_column(Integer, default=0)
    price_buy: Mapped[Numeric] = mapped_column(Numeric(12,2), default=0)
    price_sell: Mapped[Numeric] = mapped_column(Numeric(12,2), default=0)
    expired_date: Mapped[Date | None] = mapped_column(Date)
    supplier_id: Mapped[int | None] = mapped_column(ForeignKey("suppliers.id"))
    supplier: Mapped[Supplier | None] = relationship(back_populates="products")
    price_history: Mapped[list["PriceHistory"]] = relationship(back_populates="product", cascade="all, delete-orphan")
    items: Mapped[list["TransactionItem"]] = relationship(back_populates="product")


class TxType(str, enum.Enum):
    sale = "sale"
    purchase = "purchase"


class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"))
    type: Mapped[TxType] = mapped_column(Enum(TxType), nullable=False)
    total_amount: Mapped[Numeric] = mapped_column(Numeric(14,2), default=0)
    date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    user: Mapped[User | None] = relationship(back_populates="transactions")
    items: Mapped[list["TransactionItem"]] = relationship(back_populates="transaction", cascade="all, delete-orphan")


class TransactionItem(Base):
    __tablename__ = "transaction_items"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    transaction_id: Mapped[int] = mapped_column(ForeignKey("transactions.id"), index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), index=True)
    qty: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[Numeric] = mapped_column(Numeric(12,2), nullable=False) # per item
    transaction: Mapped[Transaction] = relationship(back_populates="items")