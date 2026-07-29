from fastapi import FastAPI
from routers.auth_router import auth_router
from routers.user_router import users_router
from routers.appointments_router import appointments_router
from routers.vehicle.vehicle_router import vehicle_router
from routers.vehicle.make_router import make_router
from routers.zip_code_router import zip_code
from routers.vehicle.model_router import model_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(appointments_router)
app.include_router(vehicle_router)
app.include_router(zip_code)
app.include_router(make_router)
app.include_router(model_router)



