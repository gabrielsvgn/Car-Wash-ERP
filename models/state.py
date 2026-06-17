from sqlalchemy import Column, Integer, String
from database.connection import Base

class State(Base):
    __tablename__ = "state"

    idstate = Column("state", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False, unique=True)

    