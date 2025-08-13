from typing import Annotated
from pydantic import BaseModel,Field
from starlette import status
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,HTTPException,Path
from models import Todos
from database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()                          # makes fastapi quicker helps to fetch information from the database
    try:
        yield db                                 # return it to the client and
    finally:
        db.close()                              # close off the connection to the databse


db_dependency = Annotated[Session,Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_lenth=3)
    description: str = Field(min_lenth=3, max_lenth=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool


@router.get("/",status_code = status.HTTP_200_OK)
async def read_all(db:Annotated[Session,Depends(get_db)]):   # Dependency Injection means we need to do something before we execute allows to do some code bts and then inject the depedencies that function relies on
    return db.query(Todos).all()


@router.get("/todo/{todo_id}",status_code =status.HTTP_200_OK)
async def read_todo(db:  db_dependency,todo_id:int = Path (gt=0)):
    todo_model = db.query(Todos).filter(Todos.id==todo_id).first()  #return all todos that have the same id
    if todo_model is not None:
        return todo_model
    raise HTTPException(status_code=404,detail='Todo not found')

@router.put("/todos",status_code=status.HTTP_201_CREATED)
async def create_todo(db:db_dependency,todo_request:TodoRequest):
    todo_model = Todos(**todo_request.dict())

    db.add(todo_model)                #adding means getting database ready
    db.commit()                       #commiting means actually doing the transaction to the database

@router.put("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db:db_dependency,
                      todo_request:TodoRequest,
                      todo_id:int = Path(gt=0),
                      ):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')

    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.prioprity
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()

@router.delete("/todo/{todo_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db:db_dependency,todo_id:int=Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404,detail='todo not found.')
    db.query(Todos).filter(Todos.id == todo_id).delete()

    db.commit()

