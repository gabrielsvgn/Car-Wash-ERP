from sqlalchemy import Column, Integer, String, ForeignKey
from database.connection import Base

class Car_model(Base):
    __tablename__ = "car_model"
    
    idcar_model = Column("idcar_model", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False, unique=True)
    idcar_make = Column("idcar_make", Integer, ForeignKey("car_make.idcar_make"))

 