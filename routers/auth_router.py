from fastapi import APIRouter, Depends, HTTPException
from models.user import User
from dependencies.session import get_session
from security.password import bcrypt_context
from schemas.user_schema import UserSchema
from sqlalchemy.orm import Session
from schemas.login_schema import LoginSchema
from services.auth_service import auth_user
from security.jwt import create_token
from datetime import timedelta
from dependencies.verify_token import verify_token
from fastapi.security import OAuth2PasswordRequestForm
from schemas.change_password_schema import ChangePasswordSchema

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
        return {"message": "user successfully registered"}
    
    
@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(get_session)):
    user = auth_user(login_schema.email, login_schema.password, session)
    if not user:
        raise HTTPException(status_code=401, detail="User not found or invalid credentials")
    access_token = create_token(user.idusuario)
    refresh_token = create_token(user.idusuario, timedelta(days=7))
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer"
    }

@auth_router.post("/login-form")
async def login_form(data_form: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    user = auth_user(data_form.username, data_form.password, session)
    if not user:
        raise HTTPException(status_code=401, detail="User not found or invalid credentials")
    access_token = create_token(user.idusuario)
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
    
@auth_router.post("/refresh")
async def refresh_token(user: User = Depends(verify_token)):
    access_token = create_token(user.idusuario)
    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }

@auth_router.put("/change-password")
async def change_password(password_schema: ChangePasswordSchema, user: User = Depends(verify_token), session: Session = Depends(get_session)):
    password_is_valid = bcrypt_context.verify(password_schema.current_password, user.password)
    if not password_is_valid:
        raise HTTPException(status_code=400, detail="The password is not valid")
    new_password = bcrypt_context.hash(password_schema.new_password)
    if password_schema.new_password == password_schema.current_password:
        raise HTTPException(status_code=400, detail="The entered password cannot be the same as the old password.")
    user.password = new_password
    session.commit()
    return {"message": "Password successffully changed"}