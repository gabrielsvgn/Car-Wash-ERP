from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database.connection import Base

class User(Base):
    __tablename__ = "user"

    idusuario = Column("iduser", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, nullable=False)
    email = Column("email", String, nullable=False)
    contact = Column("contact", String, nullable=False)
    password = Column("password", String, nullable=False)
    tax_id = Column("tax_id", String, unique=True)
    admin = Column("admin", Boolean, default=False)
    idcity = Column("idcity", Integer, ForeignKey("city.idcity"))
    street = Column("street", String)
    house_number = Column("house_number", Integer)

    def __init__(self, name, email, contact, password, tax_id, idcity, street, house_number, admin = False):
        self.name = name
        self.email = email
        self.contact = contact
        self.password = password
        self.tax_id = tax_id
        self.admin = admin
        self.idcity = idcity
        self.street = street
        self.house_number = house_number

