from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import products, transactions, dashboard
import os


Base.metadata.create_all(bind=engine) # for dev; use Alembic for real migrations


app = FastAPI(title="Toko Kelontong API", version="0.1.0")


# CORS
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
app.add_middleware(
CORSMiddleware,
allow_origins=[o.strip() for o in origins],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)


@app.get("/")
def root():
return {"message": "API OK"}


# Routers
app.include_router(products.router)
app.include_router(transactions.router)
app.include_router(dashboard.router)