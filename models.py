from sqlalchemy import Column,String,Integer,ForeignKey

import database as _database
from sqlalchemy.orm import relationship

class Blog(_database.Base):
    __tablename__='blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer,ForeignKey('users.id'))
    creator=relationship("User",back_populates="blogs")
    
    
# user models
class User(_database.Base):
    __tablename__ ='users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    blogs=relationship("Blog",back_populates="creator")