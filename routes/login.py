from fastapi import APIRouter,Depends as _depends,HTTPException,status
import schema as _schema, database as _database,models as _models
from sqlalchemy.orm import Session as _Session
from hashpassword import Hash,verify
from routes import jwt_token
from userrepo import userrepo

# login
from hashpassword import Hash,verify
from routes import jwt_token
import schema as _schema, database as _database,models as _models
from sqlalchemy.orm import Session as _Session
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter(
    tags=['authentication'],
    prefix='/login'
)

@router.post('')
def loginuser(request:OAuth2PasswordRequestForm= _depends(),db:_Session=_depends(_database.get_db)):
    
    user=db.query(_models.User).filter(_models.User.email==request.username).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalide Credential")
    # if not verify(user.password,request.password):
    #     # incorrect password
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalide Credential")
    # # generate jwt token and return it
    # # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # access_token = jwt_token.create_access_token(
    #     data={"sub": user.email}#expires_delta=access_token_expires
    # )
    # return {"access_token": access_token, "token_type": "bearer"}
    return userrepo.loginuser(request,db)