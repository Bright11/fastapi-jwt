# for securing routes
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import schema as _schema, models as _models, database as _database
from sqlalchemy.orm import Session as _session
from fastapi import FastAPI, Depends as _depends,status,Response,HTTPException,APIRouter
from routes import jwt_token

oauth2_schema=OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(data: str= _depends(oauth2_schema)):
     credentials_exception=HTTPException(
         status_code=status.HTTP_401_UNAUTHORIZED,
         detail="Could not validate credentials",
         headers={"WWW-Authenticate":"Bearer"}
     )
     
     return jwt_token.verify_token(data,credentials_exception)