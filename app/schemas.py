from typing import Optional
from datetime import datetime
from pydantic import BaseModel, constr, Field, conint

class TodoBase(BaseModel):
    title: constr(min_length=6)                                #Pyndate for data validation and data parsing
    description: constr(max_length=40)
    completed: Optional[datetime] = datetime.now()
class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoOut(TodoBase):
    id: conint(gt=100)

    model_config = {
        "from_attributes": True
    }
