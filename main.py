from database.connection import Base, engine
from models.appointments import Appointments, AppointmentStatus
from models.car_make import Car_make
from models.car_model import Car_model
from models.city import City
from models.color import Color
from models.customer import Customer
from models.employee import Employee
from models.service import Service
from models.state import State
from models.user import User
from models.vehicle import Vehicle

Base.metadata.create_all(bind=engine)
