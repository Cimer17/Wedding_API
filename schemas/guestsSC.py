from pydantic import BaseModel
from typing import List

# === Pydantic модель для валидации данных запроса ===
class GuestCreate(BaseModel):
    presence: bool = False
    full_name: str = ""
    phone: str = ""
    guestsAllowed: bool = False
    guests: List[str] = []
    willDring: bool = False
    drink: List[str] = []