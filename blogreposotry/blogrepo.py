from fastapi import APIRouter, Depends as _depends,status,HTTPException,Response
import schema as _schema,database as _database,models as _models
from typing import List
from sqlalchemy.orm import Session as _session

def gat_all_blog(db:_session):
     blogs=db.query(_models.Blog).all()
     return blogs
 
 
def create(request:_schema.Blog,db:_session):
     new_blog=_models.Blog(title=request.title,body=request.body,user_id=2)
     db.add(new_blog)
     db.commit()
     db.refresh(new_blog)
     return new_blog
 
 
def single_blog(id:int,db:_session):
    blog=db.query(_models.Blog).filter(_models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with this id {id} is not available")
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'details': f"Blog with this id {id} is not available"}
    return blog

# update
def updatedata(id:int,request:_schema.Blog,db:_session):
      blog=db.query(_models.Blog).filter(_models.Blog.id == id).first()
      if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with id {id} no found")
      blog.title=request.title
      blog.body=request.body
      db.commit()
      return "updated"
     
# delete data
def destroy(id:int,db:_session):
    blog=db.query(_models.Blog).filter(_models.Blog.id==id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Blog with this id {id} is not available")
    db.commit()
    
    return (f"Blog with this id {id} is deleted")