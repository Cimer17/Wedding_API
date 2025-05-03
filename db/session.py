import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


data_dir = "./data"

# Проверка существования и создание при необходимости
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# DATABASE_URL = "sqlite:///./db/guests.db"
DATABASE_URL = "sqlite:///./data/guests.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
