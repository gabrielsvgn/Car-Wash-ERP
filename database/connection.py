from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db = create_engine("postgresql://postgres:26a09b2003F#@localhost:5432/gestao_estetica")

Base = declarative_base()