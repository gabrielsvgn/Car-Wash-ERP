from dependencies.verify_token import verify_token
from fastapi import Depends, HTTPException
from models.user import User

def verify_admin(user: User = Depends(verify_token)):
    if not user.admin:
        raise HTTPException(status_code=403, detail="Access Denied")
    return user



