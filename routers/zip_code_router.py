from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencies.session import get_session
from models.user import User
from dependencies.verify_token import verify_token
from schemas.zip_code_schema import CitySchema, StateSchema, CityResponseSchema, StateResponseModel
from models.state import State
from models.city import City

zip_code = APIRouter(prefix="/zip_code", tags=["Zip_code"])

@zip_code.get("/states", response_model=list[StateResponseModel])
async def list_states(user: User = Depends(verify_token), session: Session = Depends(get_session)):
    list_states = session.query(State.name.label("state")).all()
    return list_states

@zip_code.get("/states/{idstate}", response_model=StateResponseModel)
async def list_state(idstate: int, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    state = session.query(State.name.label("state")).filter(State.idstate==idstate).first()
    if not state:
        raise HTTPException(status_code=404, detail="The state was not found")
    return state

@zip_code.post("/states")
async def create_state(state_schema: StateSchema, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    state = session.query(State).filter(State.name==state_schema.name).first()
    if state:
        raise HTTPException(status_code=409, detail="This state already exists")
    new_state = State(name=state_schema.name)
    session.add(new_state)
    session.commit()
    return {"message": "The state was successffully created"}

@zip_code.put("/states/{idstate}", response_model=StateResponseModel)
async def update_state(idstate: int, state_schema: StateSchema, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    state = session.query(State).filter(State.idstate==idstate).first()
    if not state:
        raise HTTPException(status_code=404, detail="The state was not found")
    state.name = state_schema.name
    session.commit()
    return {"message": "The state was successffully updated"}

@zip_code.post("/cities")
async def create_city(city_schema: CitySchema, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    city = session.query(City).filter(City.name==city_schema.name).filter(City.idstate==city_schema.idstate).first()
    state = session.query(State).filter(State.idstate==city_schema.idstate).first()
    if not state:
        raise HTTPException(status_code=404, detail="The state was not found")
    if city:
        raise HTTPException(status_code=409, detail="The city already exists")
    new_city = City(name=city_schema.name, idstate=city_schema.idstate)
    session.add(new_city)
    session.commit()
    return {"message": "The city was successffully created"}

@zip_code.get("/cities", response_model=list[CityResponseSchema])
async def list_cities(user: User = Depends(verify_token), session: Session = Depends(get_session)):
    city = session.query(City.name.label("city"), State.name.label("state")).join(State, City.idstate==State.idstate).all()
    return city

@zip_code.get("/cities/{idcity}", response_model=CityResponseSchema)
async def list_city_id(idcity: int, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    city = session.query(City.name.label("city")).filter(City.idcity==idcity).first()
    if not city:
        raise HTTPException(status_code=404, detail="The city was not found")
    return city

