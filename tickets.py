from fastapi import APIRouter
from pydantic import BaseModel

from backend.database import SessionLocal
from backend.models import Ticket

# ==========================================
# Router
# ==========================================

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

# ==========================================
# Request Model
# ==========================================

class StatusUpdate(BaseModel):

    status: str

# ==========================================
# Get All Tickets
# ==========================================

@router.get("")
def get_tickets():

    db = SessionLocal()

    tickets = db.query(
        Ticket
    ).all()

    result = []

    for ticket in tickets:

        result.append({

            "id":
                ticket.id,

            "title":
                ticket.title,

            "status":
                ticket.status,

            "priority":
                ticket.priority
        })

    db.close()

    return result

# ==========================================
# Update Ticket Status
# ==========================================

@router.put("/{ticket_id}")
def update_ticket(
    ticket_id: int,
    data: StatusUpdate
):

    db = SessionLocal()

    ticket = db.query(
        Ticket
    ).filter(
        Ticket.id == ticket_id
    ).first()

    if ticket:

        ticket.status = data.status

        db.commit()

    db.close()

    return {
        "message":
            "Ticket Updated"
    }