from sqlalchemy import Column, Integer, String, ForeignKey
from database.connection import Base

class City(Base):
    __tablename__ = "city"

    idcity = Column("idcity", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False, unique=True)
    idstate = Column("idstate", Integer, ForeignKey("state.idstate"))

   
  
