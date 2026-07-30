from fastapi import APIRouter, HTTPException, Depends
from dependencies.session import get_session
from dependencies.verify_token import verify_token
from sqlalchemy.orm import Session
from models.user import User


users_router = APIRouter(prefix="/users", tags=["Users"])

@users_router.put("/admin/{idusuario}")
async def set_admin(idusuario: int, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    user_admin = session.query(User).filter(User.idusuario==idusuario).first()
    if not user.admin:
            raise HTTPException(status_code=403, detail="Access denied, the user is not an admin") 
    if not user_admin:
        raise HTTPException(status_code=404, detail="User not found")
    if user_admin.admin:
        raise HTTPException(status_code=409, detail="User is already an admin")
    user_admin.admin = True
    session.commit()
    return {"message": f"The user {user_admin.name} was set as admin"}

