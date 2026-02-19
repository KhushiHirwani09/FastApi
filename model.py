from database import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__="users"
    username=Column(String,nullable=False)
    age=Column(String)
    phoneno=Column(String,nullable=False)
    id=Column(Integer,primary_key=True)
    department=Column(String,nullable=False)
