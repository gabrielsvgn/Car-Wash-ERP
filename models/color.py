from sqlalchemy import Column, String, Integer
from database.connection import Base

class Color(Base):
    __tablename__ = "color"

    idcolor = Column("idcolor", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    