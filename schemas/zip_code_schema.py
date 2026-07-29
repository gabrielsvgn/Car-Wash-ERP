from pydantic import BaseModel, ConfigDict

class CityResponseSchema(BaseModel):
    city: str
    state: str

    model_config = ConfigDict(from_attributes=True)

class CitySchema(BaseModel):
    name: str
    idstate: int

    model_config = ConfigDict(from_attributes=True)

class StateSchema(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)

class StateResponseModel(BaseModel):
    state: str

    model_config = ConfigDict(from_attributes=True)

    

