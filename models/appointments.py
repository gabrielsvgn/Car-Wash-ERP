from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Float, Boolean, Enum
import enum
from database.connection import Base

class AppointmentStatus(enum.Enum):
        scheduled = "Scheduled"
        finished = "Finished"
        canceled = "Canceled"

class Appointments(Base):
    __tablename__ = "appointments"


    idappointment = Column("idappointment", Integer, primary_key=True, autoincrement=True)
    idvehicle = Column("idvehicle", Integer, ForeignKey("vehicle.idvehicle"))
    date_time = Column("date_time", DateTime, nullable=False)
    observation = Column("observation", String)
    paid = Column("paid", Boolean, default=False)
    status = Column(Enum(AppointmentStatus), nullable=False, default=AppointmentStatus.scheduled)


