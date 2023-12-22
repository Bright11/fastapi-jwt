from pydantic import BaseModel as _BaseModel
from typing import List



class BlogBase(_BaseModel):
    title:str 
    body:str

class Blog(BlogBase):
    class Config():
       orm_mode=True
    
    

        

# user schema
class User(_BaseModel):
    name:str
    email:str
    password:str
    
class ShowUser(_BaseModel):
    name:str
    email:str
    blogs:List[Blog]=[]
    class Config():
       orm_mode=True
       
# setting up the type of data you want to display
class ShowBlog(_BaseModel):
    title:str
    body:str
    creator:ShowUser
    class Config():
        orm_mode=True
        

# login schema
class Login(_BaseModel):
    username:str
    password:str
    
    
# gernerating jwt token

class Token(_BaseModel):
    access_token: str
    token_type: str


class TokenData(_BaseModel):
    username: str | None = None