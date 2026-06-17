from sqlalchemy import Column, Integer, String, Float
from database.connection import Base

class Service(Base):
    __tablename__ = "service"

    idservice = Column("idservice", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False, unique=True)
    price = Column("price", Float, nullable=False)