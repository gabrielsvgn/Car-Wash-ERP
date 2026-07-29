from fastapi import APIRouter, Depends, HTTPException
from schemas.appointment_schema import NewAppointment
from dependencies.session import get_session
from sqlalchemy.orm import Session
from dependencies.verify_token import verify_token
from models.user import User
from models.appointments import Appointments

appointments_router = APIRouter(prefix="/appointments", tags=["appointments"])

@appointments_router.post("/appointment")
async def new_appointment(appointment_schema: NewAppointment, user: User = Depends(verify_token),  session: Session = Depends(get_session)):
    vechicle = session.query(Appointments).filter(Appointments.idvehicle==appointment_schema.idvehicle)
    if not vechicle:
        raise HTTPException(status_code=404, detail="Vehicle not found") 
    session.add(appointment_schema.idvehicle, appointment_schema.date_time, appointment_schema.observation, appointment_schema.paid, appointment_schema.status)
    session.commit()
    return {"message": "Appointment successffully scheduled"}