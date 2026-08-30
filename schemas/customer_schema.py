from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date

class CustomerSchema(BaseModel):
    idcity: int
    name: str
    contact: str
    email: str
    tax_id: str
    birth_date: date
    observation: Optional[str]
    
    model_config = ConfigDict(from_attributes=True)

class CustomerResponseSchema(BaseModel):
    idcustomer: int
    idcity: int
    name: str
    contact: str
    email: str
    tax_id: str
    birth_date: date
    observation: str

class CustomerUpdate(BaseModel):
    idcustomer: Optional[int] = None
    idcity: Optional[int] = None
    name: Optional[str] = None
    contact: Optional[str] = None
    email: Optional[str] = None
    tax_id: Optional[str] = None
    birth_date: Optional[date] = None
    observation: Optional[str] = None