from sqlalchemy import Column, Integer, String
from database.connection import Base

class Car_make(Base):
    __tablename__ = "car_make"

    idcar_make = Column("idcar_make", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False, unique=True)

   