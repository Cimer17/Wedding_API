from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.guestsSC import GuestCreate
from db.session import get_db
from crud.guest_crud import create_guest, get_all_guests

router = APIRouter()

@router.post("")
def create_user(guest: GuestCreate, db: Session = Depends(get_db)):
    return create_guest(db, guest)

@router.get("")
def read_guests(db: Session = Depends(get_db)):
    return get_all_guests(db)
