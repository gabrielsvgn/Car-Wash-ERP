from pydantic import BaseModel, ConfigDict
from typing import Optional

class LoginSchema(BaseModel):
    email: str
    password: str

    model_config = ConfigDict(from_attributes = True)

