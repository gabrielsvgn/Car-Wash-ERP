from fastapi import FastAPI
from routers.auth_router import auth_router
from routers.users_router import users_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)




