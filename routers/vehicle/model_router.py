from fastapi import APIRouter, Depends, HTTPException
from schemas.vehicle_schema import ModelResponseSchema, ModelSchema
from sqlalchemy.orm import Session
from dependencies.verify_token import verify_token
from dependencies.session import get_session
from models.car_model import Car_model
from models.car_make import Car_make
from models.user import User

model_router = APIRouter(prefix="/model", tags=["Model"])

@model_router.post("/models")
async def create_car_model(model_schema: ModelSchema, user: User = Depends(verify_token), session: Session = Depends(get_session)):
     car_make = session.query(Car_make).filter(Car_make.idcar_make==model_schema.idcar_make).first()
     car_model = session.query(Car_model).filter(Car_model.name==model_schema.name).filter(Car_model.idcar_make==model_schema.idcar_make).first()
     if not car_make:
          raise HTTPException(status_code=404, detail="The car's make was not found")
     if car_model:
          raise HTTPException(status_code=409, detail="The car's model already exists")
     new_car_model = Car_model(name=model_schema.name, idcar_make=model_schema.idcar_make)
     session.add(new_car_model)
     session.commit()
     return {"message": "The car's model was successffully created"}