# user registration
# password becripts



from fastapi import FastAPI, Depends as _depends,status,Response,HTTPException,APIRouter
import schema as _schema, models as _models, database as _database
from userrepo import userrepo
from sqlalchemy.orm import Session as _session
from userrepo import oauth2

router=APIRouter(
    tags=['users'],
    prefix="/user"
)
get_db=_database.get_db

# user creation
@router.post("/",response_model=_schema.ShowUser)
def create_user(request:_schema.User,db:_session=_depends(get_db)):
    return userrepo.newuser(request,db)
    

# getting user by id
@router.get('/{id}',response_model=_schema.ShowUser)
def get_user(id:int,db:_session=_depends(get_db),current_user:_schema.User=_depends(oauth2.get_current_user)):
   return userrepo.get_single_user(id,db)
