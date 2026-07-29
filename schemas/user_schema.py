from pydantic import BaseModel, ConfigDict
from typing import Optional

class UserSchema(BaseModel):
    name: str
    email: str
    contact: str
    password: str
    tax_id: str
    idcity: Optional[int] 
    street: Optional[str] 
    house_number: Optional[int] 

    model_config = ConfigDict(from_attributes = True)
