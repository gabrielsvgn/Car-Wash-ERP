from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine,
                       autocommit=False,
                       autoflush=False)
session = Session()

Base = declarative_base()

# Criação do banco
Base.metadata.create_all(bind=engine)