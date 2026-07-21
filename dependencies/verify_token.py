from security.auth2_schema import oauth2_schema
from dependencies.session import get_session
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from fastapi import HTTPException, Depends
from models.user import User
from dotenv import load_dotenv
import os

load_dotenv()

ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")

def verify_token(token: str = Depends(oauth2_schema), session: Session = Depends(get_session)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        user_id = int(dic_info.get("sub"))
    except JWTError:
        raise HTTPException (status_code=401, detail="Access denied, verify the token's validaty")
    user = session.query(User).filter(User.idusuario==user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="Access denied")
    return user