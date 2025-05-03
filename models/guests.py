import json
from sqlalchemy import Column, Integer, String, Boolean, TypeDecorator, TEXT
from sqlalchemy.orm import declarative_base

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