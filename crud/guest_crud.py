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

def get_all_guests(db: Session):
    guests = db.query(Guests).all()
    return {"guests": guests}
