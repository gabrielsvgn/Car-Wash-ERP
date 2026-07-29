from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies.session import get_session
from models.user import User
from schemas.vehicle_schema import MakeSchema, ModelSchema, VehicleSchema, VehicleResponseSchema, ModelResponseSchema, MakeResponseSchema, ChangeMakeNameSchema
from dependencies.verify_token import verify_token
from models.car_make import Car_make
from models.car_model import Car_model
from models.color import Color
from models.customer import Customer
from models.vehicle import Vehicle

vehicle_router = APIRouter(prefix="/vehicle", tags=["Vehicle"])

@vehicle_router.post("/vehicles")
async def create_vehicle(vehicle_schema: VehicleSchema, user: User = Depends(verify_token), session: Session = Depends(get_session)):
     color = session.query(Color).filter(Color.idcolor==vehicle_schema.idcolor).first() 
     car_model = session.query(Car_model).filter(Car_model.idcar_model==vehicle_schema.idcar_model).first() 
     customer = session.query(Customer).filter(Customer.idcustomer==vehicle_schema.idcustomer).first() 
     plate = session.query(Vehicle).filter(Vehicle.plate==vehicle_schema.plate).first()
     if not car_model:
          raise HTTPException(status_code=404, detail="The car's model was not found")
     if not color:
          raise HTTPException(status_code=404, detail="The color was not found")
     if not customer:
          raise HTTPException(status_code=404, detail="the customer was not found")
     if plate:
          raise HTTPException(status_code=409, detail="The plate already exists")
     vehicle = Vehicle(idcar_model=vehicle_schema.idcar_model, idcolor=vehicle_schema.idcolor, idcustomer=vehicle_schema.idcustomer, plate=vehicle_schema.plate)
     session.add(vehicle)
     session.commit()
     return {"message": "The vehicle was successffully created"}

@vehicle_router.get("/vehicles", response_model=list[VehicleResponseSchema])
async def list_vehicles(user: User = Depends(verify_token), session: Session = Depends(get_session)):
    vehicles = session.query(Vehicle).all()
    return vehicles

         