
from fastapi import FastAPI, Depends as _depends,status,Response,HTTPException,APIRouter
import schema as _schema, models as _models, database as _database
from sqlalchemy.orm import Session as _session
from hashpassword import Hash
# login
from hashpassword import Hash,verify
from routes import jwt_token
import schema as _schema, database as _database,models as _models
from sqlalchemy.orm import Session as _Session
from fastapi.security import OAuth2PasswordRequestForm


def newuser(request:_schema.User,db:_session):
    # hash password
    new_user=_models.User(name=request.name,email=request.email,password=Hash.bcript(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_single_user(id:int,db:_session):
     user =db.query(_models.User).filter(_models.User.id==id).first()
     if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=f"Usrr with the id {id} is not available")
    
     return user
 
#  login
def loginuser(request:OAuth2PasswordRequestForm= _depends(),db:_Session=_depends(_database.get_db)):
     user=db.query(_models.User).filter(_models.User.email==request.username).first()
     if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalide Credential")
     if not verify(user.password,request.password):
        # incorrect password
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalide Credential")
    # generate jwt token and return it
    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
     access_token = jwt_token.create_access_token(
        data={"sub": user.email}#expires_delta=access_token_expires
    )
     return {"access_token": access_token, "token_type": "bearer"}