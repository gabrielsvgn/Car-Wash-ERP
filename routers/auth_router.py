from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from dependencies.session import get_session
from security.password import bcrypt_context
from schemas.user_schema import UserSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/create_account")
async def create_account(user_schema: UserSchema, session: Session = Depends(get_session)):
    user = session.query(User).filter(User.email==user_schema.email).first()
    tax_id = session.query(User).filter(User.tax_id==user_schema.tax_id).first()
    if user:
        raise HTTPException(status_code=400, detail="user already registered")
    if tax_id:
        raise HTTPException(status_code=400, detail="tax_id already registered")
    else:
        encrypted_password = bcrypt_context.hash(user_schema.password)
        new_user = User(name=user_schema.name, email=user_schema.email, contact=user_schema.contact, password=encrypted_password, tax_id=user_schema.tax_id, admin=user_schema.admin, idcity=user_schema.idcity, street=user_schema.street, house_number=user_schema.house_number)
        session.add(new_user)
        session.commit()
        return {"message": "email successfully registered"}

