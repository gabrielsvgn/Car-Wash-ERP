from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database.connection import Base

class User(Base):
    __tablename__ = "user"

    idusuario = Column("iduser", Integer, primary_key=True, autoincrement=True)
    email = Column("email", String, nullable=False)
    contact = Column("contact", String, nullable=False)
    password = Column("password", String, nullable=False)
    tax_id = Column("tax_id", String)
    admin = Column("admin", Boolean, default=False)
    idcity = Column("idcity", Integer, ForeignKey("city.idcity"))
    street = Column("street", String)
    house_number = ("house_number", Integer)
