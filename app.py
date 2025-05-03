from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import guests
from db.init_db import init_db

app = FastAPI(root_path="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация БД
init_db()

# Подключаем роуты
app.include_router(guests.router, prefix="/users", tags=["Guests"])
