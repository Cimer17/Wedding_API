from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.guestsSC import GuestCreate
from db.session import get_db
from crud.guest_crud import *

router = APIRouter()

@router.post("")
def create_user(guest: GuestCreate, db: Session = Depends(get_db)):
    return create_guest(db, guest)

@router.get("")
def read_guests(db: Session = Depends(get_db)):
    return get_all_guests(db)

@router.delete("/{guest_id}")
def delete_user(guest_id:int, db: Session = Depends(get_db)):
    return dellete_guest(db, guest_id)

@router.get("/check/{phone}")
def check_phone(phone: str, db: Session = Depends(get_db)):
    return check_phone_guest(db, phone)