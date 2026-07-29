from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from models.appointments import AppointmentStatus

class NewAppointment(BaseModel):
    idvehicle: int
    date_time: datetime
    observation: Optional[str]
    paid: Optional[bool]
    status: Optional[AppointmentStatus]

    model_config = ConfigDict(from_attributes = True)