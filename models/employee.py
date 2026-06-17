from sqlalchemy import Column, Integer, String, ForeignKey
from database.connection import Base

class Employee(Base):
    __tablename__ = "employee"

    idemployee = Column("idemployee", Integer, primary_key=True, autoincrement=True)
    idcity = Column("idcity", Integer, ForeignKey("city.idcity"))
    name = Column("name", String, nullable=False)
    contact = Column("contact", String, nullable=False)
    email = Column("email", String)

  