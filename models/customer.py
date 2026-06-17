from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from database.connection import Base

class Customer(Base):
    __tablename__ = "customer"

    idcustomer = Column("idcustomer", Integer, primary_key=True, autoincrement=True)
    idcity = Column("idcity", Integer, ForeignKey("city.idcity"))
    name = Column("name", String, nullable=False)
    contact = Column("contact", String, nullable=False)
    email = Column("email", String, nullable=False)
    tax_id = Column("tax_id", String)
    birth_date = Column("birth_date", Date)
    observation = Column("observation", String)

 