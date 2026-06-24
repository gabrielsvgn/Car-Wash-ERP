from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("postgresql://postgres:26a09b2003F#@localhost:5432/gestao_estetica")
Session = sessionmaker(bind=engine,
                       autocommit=False,
                       autoflush=False)
session = Session()

Base = declarative_base()

# Criação do banco
Base.metadata.create_all(bind=engine)