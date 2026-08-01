from fastapi import APIRouter, HTTPException, Depends
from dependencies.session import get_session
from dependencies.verify_token import verify_token
from dependencies.verify_admin import verify_admin
from sqlalchemy.orm import Session
from models.user import User


users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.put("/admin/{idusuario}")
async def set_admin(idusuario: int, user: User = Depends(verify_admin), session: Session = Depends(get_session)):
    set_user = session.query(User).filter(User.idusuario==idusuario).first() 
    if not set_user:
        raise HTTPException(status_code=404, detail="The user was not found")
    if set_user.admin:
        raise HTTPException(status_code=409, detail="User is already an admin")
    set_user.admin = True
    session.commit()
    return {"message": f"The user {set_user.name} was set as admin"}




