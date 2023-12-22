from fastapi import APIRouter, Depends as _depends,status,HTTPException,Response
import schema as _schema,database as _database,models as _models
from typing import List
from sqlalchemy.orm import Session as _session
from blogreposotry import blogrepo
from userrepo import oauth2

router=APIRouter(
    tags=['blogs'],
    prefix="/blog"
)


# getting all blogs
@router.get("/",response_model=List[_schema.ShowBlog])
def allblog(db:_session=_depends(_database.get_db),current_user:_schema.User=_depends(oauth2.get_current_user)):
   return blogrepo.gat_all_blog(db)



@router.post("/",status_code=status.HTTP_201_CREATED)
def create(request:_schema.Blog,db: _session=_depends(_database.get_db),current_user:_schema.User=_depends(oauth2.get_current_user)):
   return blogrepo.create(request,db)




# getting single data
@router.get('/{id}',status_code=200,response_model=_schema.ShowBlog)
def show(id:int,response: Response,db:_session=_depends(_database.get_db),current_user:_schema.User=_depends(oauth2.get_current_user)):
    return blogrepo.single_blog(id,db)

# deleting data
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,response: Response,db:_session=_depends(_database.get_db),current_user:_schema.User=_depends(oauth2.get_current_user)):
    return blogrepo.destroy(id,db)

# updating data
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:_schema.Blog,db:_session=_depends(_database.get_db),current_user:_schema.User=_depends(oauth2.get_current_user)):
    
  return blogrepo.updatedata(id,request,db,)
