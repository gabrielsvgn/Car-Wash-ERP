from pydantic import BaseModel, ConfigDict

class ChangePasswordSchema(BaseModel):
    current_password: str
    new_password: str

    model_config = ConfigDict(from_attributes = True)
