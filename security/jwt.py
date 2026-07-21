from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
from jose import jwt, JWTError

load_dotenv()
ACCESS_EXPIRED_TOKEN = int(os.getenv("ACCESS_EXPIRED_TOKEN"))
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def create_token(user_id, token_duration = timedelta(minutes = ACCESS_EXPIRED_TOKEN)):
    exp_date = datetime.now(timezone.utc) + token_duration
    dic_info = {"sub": str(user_id), "exp": exp_date}
    jwt_encoded = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    return jwt_encoded
