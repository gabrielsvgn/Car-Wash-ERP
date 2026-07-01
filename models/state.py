from sqlalchemy import Column, Integer, String
from database.connection import Base

class State(Base):
    __tablename__ = "state"

    idstate = Column("idstate", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    