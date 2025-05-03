from sqlalchemy.orm import Session
from models.guests import Guests
from schemas.guestsSC import GuestCreate

def create_guest(db: Session, guest: GuestCreate):
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

def dellete_guest(db: Session, guest_id: int):
    db_guest = db.query(Guests).filter(Guests.id == guest_id).first()
    if db_guest:
        db.delete(db_guest)
        db.commit()
        return {"message": "Гость удален"}
    else:
        return {"message": "Гость не найден"}

def check_phone_guest(db: Session, phone: str):
    db_guest = db.query(Guests).filter(Guests.phone == phone).first()
    if db_guest:
        return {"message": "Yes", "guest": db_guest}
    else:
        return {"message": "No"}

def get_all_guests(db: Session):
    guests = db.query(Guests).all()
    return {"guests": guests}
