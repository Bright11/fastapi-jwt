from fastapi import FastAPI, Depends as _depends,status,Response,HTTPException
import models as _models, database as _database



# import routes
from routes import blogrouter,userrouter,login



app=FastAPI()

_models._database.Base.metadata.create_all(_database.engine)

app.include_router(blogrouter.router)
app.include_router(userrouter.router)
app.include_router(login.router)
# def get_db():
#     db=_database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
# creating blog



