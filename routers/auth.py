from datetime import timedelta, datetime, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field,EmailStr
from sqlalchemy.orm import Session
from starlette import status
from database import SessionLocal
from models import Users
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import jwt,JWTError


router = APIRouter(

    prefix='/auth',
    tags=['auth']
)

SECRET_KEY = '1de0d597a8892a764da70af51d473d593b6be0b0fefaf6db57605c58628e962d'         #openssl rand hex 32
ALGORITHM = 'HS256'

bcrypt_context= CryptContext(schemes=['bcrypt'],deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

class CreateUserRequest(BaseModel):
    username:str=Field(...,min_length=3,max_length=20)        #pydantic Validations for user table
    email:EmailStr=Field(...,description='Enter Valid email with @')
    first_name:str=Field(...,min_length=3,max_length=20)
    last_name:str=Field(...,min_length=2,max_length=30)
    password:str=Field(...,min_length=5,max_length=10,description='Password with uppercase,lowercase,number,special char')
    role:str=Field(...,description="Role must be admin or user")



#class CreateUserResponse(BaseModel):
#   username:str=Field(...,min_length=3,max_length=20)
#   email:EmailStr=Field(...,description='Enter Valida email with @')
#   first_name:str=Field(...,min_length=2,max_length=20)



class Token(BaseModel):
    access_token:str
    token_type:str

def get_db():
    db = SessionLocal()                          # makes fastapi quicker helps to fetch information from the database
    try:
        yield db                                 # return it to the client and
    finally:
        db.close()                              # close off the connection to the databse


db_dependency = Annotated[Session,Depends(get_db)]

def authenticate_user(email:EmailStr, password:str,db):
    user = db.query(Users).filter(Users.email == email).first()
    print(f"user is in auth funct {user}")
    if not user:
        raise HTTPException(404, "User doesn't exist")
    if not bcrypt_context.verify(password,user.hashed_password):
        raise HTTPException(403, "Password Incorrect")
    return user

def create_access_token(username:str,user_id:int,expires_delta:timedelta):
    encode = {'sub':username,'id':user_id}
    expires = datetime.now(timezone.utc)+expires_delta
    encode.update({'exp':expires})
    return jwt.encode(encode,SECRET_KEY,algorithm= ALGORITHM)

async def get_current_user(token: Annotated[str,Depends(oauth2_bearer)]):    #verifies token
    try:
        payload = jwt.decode(token,SECRET_KEY, algorithms=[ALGORITHM])        #Authencity of token
        username:str = payload.get('sub')
        user_id:int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not Validate user.')
        return {'username': username,'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
        detail = 'Could not Validate user.')


@router.post("/",status_code = status.HTTP_201_CREATED)
async def create_user(db: db_dependency,
                      create_user_request:CreateUserRequest):
    create_user_model = Users(
        username=create_user_request.username,
        email=create_user_request.email,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        hashed_password= bcrypt_context.hash(create_user_request.password),
        role=create_user_request.role,
        is_active=True
    )


    db.add(create_user_model)
    db.commit()                    #this actually do the transaction to the database
    db.refresh(create_user_model)
    return create_user_model
    #return CreateUserResponse(
     #   username=create_user_response.username,
     #   email=create_user_response.email,
     #   first_name=create_user_response.first_name


@router.post("/token",response_model= Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm,Depends()],
                                 db: db_dependency):
    print(f"user: {form_data.username}, password: {form_data.password}")
    user = authenticate_user(form_data.username,form_data.password,db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail = 'Could not Validate user.')

    token = create_access_token(user.username,user.id,timedelta(minutes=20))

    return {'access_token':token,'token_type':'bearer'}

