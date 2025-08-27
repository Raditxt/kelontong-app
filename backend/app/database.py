from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./toko.db")

engine = create engine (
    DATABASE URL,
    connect args={"check_same_thread": False} if DATABASE_URL.startwith("sqlite://") else {},
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(declarative_base()):
    pass

# Dependency for routes
from fastapi import Depends
from typing import Generator

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        