from fastapi import APIRouter, HTTPException, Depends
from dependencies.session import get_session
from sqlalchemy.orm import Session
from models.user import User


users_router = APIRouter(prefix="/users", tags=["Users"])

