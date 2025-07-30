from pydantic import BaseModel, Field
from typing import Optional

class BookRequest(BaseModel):
    id: Optional[int] = None
    author: str = Field(min_length=3, max_length=6)
    title: str = Field(min_length=7, max_length=10)
    description: str = Field(min_length=4, max_length=11)
    rating: int = Field(gt=0, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "One Fine Day",
                "author": "Pallavi Mani",
                "description": "Very Informative book",
                "rating": 5,
                "published_date": 2013
            }
        }
    }
