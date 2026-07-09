from fastapi import APIRouter, HTTPException, Depends
from dependencies.session import get_session
from sqlalchemy.orm import Session
from models.user import User


users_router = APIRouter(prefix="/users", tags=["users"])

@users_router.get("/view_users")
async def view_users(session: Session= Depends(get_session)):
    users = session.query(User).all()
    if users: 
        return[{
            "name": user.name,
            "email": user.email
        }
            for user in users
            ]
    else:
        raise HTTPException(status_code=404, detail="Users not found")