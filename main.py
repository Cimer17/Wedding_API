import json
import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean, TypeDecorator, TEXT
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from typing import List

# === Настройка базы данных ===
DATABASE_URL = "sqlite:///./database/guests.db"
origins = [os.environ.get("REACT_APP_API_URL", "https://localhost:8000")]

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

# === Кастомный тип для хранения списка (JSON) ===
class JSONEncodedList(TypeDecorator):
    impl = TEXT

    def process_bind_param(self, value, dialect):
        if value is None:
            return "[]"
        # Делаем явное преобразование в строку
        return json.dumps(value, ensure_ascii=False)

    def process_result_value(self, value, dialect):
        if value is None:
            return []
        return json.loads(value)

# === Модель данных ===
class Guests(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    presence = Column(Boolean, default=False)
    full_name = Column(String, index=True, default="")
    phone = Column(String, index=True, default="")
    guestsAllowed = Column(Boolean, default=False)
    guests = Column(JSONEncodedList, default=[])
    willDring = Column(Boolean, default=False)
    drink = Column(JSONEncodedList, default=[])

# === Pydantic модель для валидации данных запроса ===
class GuestCreate(BaseModel):
    presence: bool = False
    full_name: str = ""
    phone: str = ""
    guestsAllowed: bool = False
    guests: List[str] = []
    willDring: bool = False
    drink: List[str] = []

# === FastAPI приложение ===
app = FastAPI(root_path="/api")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Разрешить все источники
    allow_credentials=True,
    allow_methods=["*"],  # Разрешить все HTTP-методы
    allow_headers=["*"],  # Разрешить все заголовки
)

# === Зависимость для получения сессии БД ===
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# === Создание таблиц (один раз) ===
Base.metadata.create_all(bind=engine)

# === POST запрос для создания нового гостя ===
@app.post("/users")
def create_guest(guest: GuestCreate, db: Session = Depends(get_db)):
    db_guest = Guests(
        presence=guest.presence,
        full_name=guest.full_name,
        phone=guest.phone,
        guestsAllowed=guest.guestsAllowed,
        guests=guest.guests,
        willDring=guest.willDring,
        drink=guest.drink
    )
    db.add(db_guest)
    db.commit()
    db.refresh(db_guest)
    return {"message": "User added successfully", "user": guest}

# === GET запрос для просмотра всех гостей ===
@app.get("/users")
def get_guests(db: Session = Depends(get_db)):
    guests = db.query(Guests).all()
    return {"guests": guests}