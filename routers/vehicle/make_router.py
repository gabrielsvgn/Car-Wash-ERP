from fastapi import APIRouter, Depends, HTTPException
from schemas.vehicle_schema import MakeSchema, MakeResponseSchema, ChangeMakeNameSchema
from sqlalchemy.orm import Session
from dependencies.verify_token import verify_token
from dependencies.session import get_session
from models.car_make import Car_make
from models.user import User

make_router = APIRouter(prefix="/make", tags=["Make"])

@make_router.get("/makes", response_model=list[MakeResponseSchema])
async def list_car_makes(user: User = Depends(verify_token), session: Session = Depends(get_session)):
     makes = session.query(Car_make).all()
     if not makes:
          raise HTTPException(status_code=404, detail="The car's makes was not found")
     return makes

@make_router.get("/makes/{idcar_make}", response_model=MakeResponseSchema)
async def list_car_make_id(idcar_make: int, user: User = Depends(verify_token), session: Session = Depends(get_session)):
     make = session.query(Car_make).filter(Car_make.idcar_make==idcar_make).first()
     if not make:
          raise HTTPException(status_code=404, detail="The car's make was not found")
     return make

@make_router.post("/makes")
async def create_car_make(make_schema: MakeSchema, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    car_make = session.query(Car_make).filter(Car_make.name==make_schema.name).first()
    if car_make:
         raise HTTPException(status_code=409, detail="The car's make already exists")
    new_car_make = Car_make(name=make_schema.name)
    session.add(new_car_make)
    session.commit()
    return {"message": "The car make was successfully created"}

@make_router.put("/makes/{idcar_make}")
async def update_car_make(idcar_make: int, name_schema: ChangeMakeNameSchema, user: User = Depends(verify_token), session: Session = Depends(get_session)):
     make = session.query(Car_make).filter(Car_make.idcar_make==idcar_make).first()
     if not make:
          raise HTTPException(status_code=404, detail="The car's make was not found")
     make.name = name_schema.name
     session.commit()
     return {"message": "The make's name has been successffully changed"}