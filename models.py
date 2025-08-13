from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True,nullable=False)
    username = Column(String,nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)                        #password is encryted or hashed
    is_active = Column(Boolean,default=True)                              #user account is active or not
    role = Column(String,default='user')                                  #uses role admin or not admin

class Todos(Base):
    __tablename__= 'todos'


    id = Column(Integer,primary_key=True,index=True)
    title=Column(String)
    priority = Column(Integer)
    complete = Column(Boolean,default = False)
    owner_id = Column(Integer,ForeignKey("users.id"))


