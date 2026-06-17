from sqlalchemy import Column, String, Integer, ForeignKey
from database.connection import Base

class Vehicle(Base):
    __tablename__ = "vehicle"

    COLOR = (
        ("VERMELHO", "VERMELHO"),
        ("VERDE", "VERDE"),
        ("AZUL", "AZUL"),
        ("AMARELO", "AMARELO"),
        ("BRANCO", "BRANCO"),
        ("PRETO", "PRETO")
    )

    idvehicle = Column("idvehicle", Integer, primary_key=True, autoincrement=True)
    idcar_model = Column("idcar_model", Integer, ForeignKey("car_model.idcar_model"))
    idcustomer = Column("idcustomer", Integer, ForeignKey("customer.idcustomer"))
    plate = Column("plate", String, nullable=False, unique=True)
    color = Column("color", String, choices=COLOR)