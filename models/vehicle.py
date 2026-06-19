from sqlalchemy import Column, String, Integer, ForeignKey
from database.connection import Base

class Vehicle(Base):
    __tablename__ = "vehicle"

    idvehicle = Column("idvehicle", Integer, primary_key=True, autoincrement=True)
    idcar_model = Column("idcar_model", Integer, ForeignKey("car_model.idcar_model"))
    idcolor = Column("idcolor", Integer, ForeignKey("color.idcolor"))
    idcustomer = Column("idcustomer", Integer, ForeignKey("customer.idcustomer"))
    plate = Column("plate", String, nullable=False, unique=True)