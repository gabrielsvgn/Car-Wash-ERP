from pydantic import BaseModel, ConfigDict
from typing import Optional

class MakeSchema(BaseModel):
    name: str

    class Config:
        from_attributes = True

class ChangeMakeNameSchema(BaseModel):
    name: str

class MakeResponseSchema(BaseModel):
    idcar_make: int
    name: str

class ModelSchema(BaseModel):
    name: str
    idcar_make: int

class ModelResponseSchema(BaseModel):
    idcar_model: int
    name: str

    model_config = ConfigDict(from_attributes = True)

class VehicleSchema(BaseModel):
    idcar_model: int
    idcolor: int
    idcustomer: int
    plate: str

    model_config = ConfigDict(from_attributes = True)

class VehicleResponseSchema(BaseModel):
    idcar_model: int
    idcolor: int
    idcustomer: int
    plate: str

    model_config = ConfigDict(from_attributes=True)

        





   