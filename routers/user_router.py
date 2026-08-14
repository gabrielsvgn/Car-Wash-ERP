from fastapi import APIRouter, HTTPException, Depends
from dependencies.session import get_session
from dependencies.verify_token import verify_token
from dependencies.verify_admin import verify_admin
from sqlalchemy.orm import Session
from models.user import User
from schemas.user_schema import UserResponseSchema


users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.put("/admin/{iduser}")
async def set_admin(iduser: int, user: User = Depends(verify_admin), session: Session = Depends(get_session)):
    user_admin = session.query(User).filter(User.idusuario==iduser).first() 
    if not user_admin:
        raise HTTPException(status_code=404, detail="The user was not found")
    if user_admin.admin:
        raise HTTPException(status_code=409, detail="User is already an admin")
    user_admin.admin = True
    session.commit()
    return {"message": f"The user {user_admin.name} was set as admin"}

@users_router.put("/admin{iduser}/remove")
async def remove_admin(iduser: int, user: User = Depends(verify_admin), session: Session = Depends(get_session)):
    user_admin = session.query(User).filter(User.idusuario==iduser).first()
    if not user_admin:
        raise HTTPException(status_code=404, detail="The user was not found")
    if not user_admin.admin:
            raise HTTPException(status_code=409, detail="User is not an admin")
    user_admin.admin = False
    session.commit()
    return {"message": f"The user {user_admin.name} has been removed as an admin"}

@users_router.get("/admin/user", response_model=list[UserResponseSchema])
async def list_users(user: User = Depends(verify_admin), session: Session = Depends(get_session)):
     users = session.query(User).all()
     return users


