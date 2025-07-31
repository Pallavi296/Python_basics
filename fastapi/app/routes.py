from fastapi import APIRouter, Path, Query, HTTPException
from starlette import status
from .models import Book
from .schemas import BookRequest
from .database import books

router = APIRouter()

@router.get("/books", status_code=status.HTTP_200_OK)
async def read_recommended_books():
    return [book.__dict__ for book in books]

@router.get("/books/by_rating", status_code=status.HTTP_200_OK)
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    return [book.__dict__ for book in books if book.rating == book_rating]


@router.get("/books/{book_id}", status_code=status.HTTP_200_OK)
async def read_book(book_id: int = Path(gt=0)):          #path parameter
    for book in books:
        if book.id == book_id:
            return book.__dict__
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/books/by_publish_date", status_code=status.HTTP_200_OK)
async def read_book_by_published_date(published_date: int = Query(gt=1999, lt=2031)):      #query parameter
    return [book.__dict__ for book in books if book.published_date == published_date]

@router.post("/create-books", status_code=status.HTTP_201_CREATED)
async def create_book(book_request: BookRequest):
    new_id = books[-1].id + 1 if books else 1
    new_book = Book(new_id, book_request.author, book_request.title, book_request.description, book_request.rating, book_request.published_date)
    books.append(new_book)
    return {"message": "Book added successfully", "book": new_book.__dict__}

@router.post("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    for i, b in enumerate(books):
        if b.id == book.id:
            books[i] = Book(book.id, book.author, book.title, book.description, book.rating, book.published_date)
            return
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
 try:
    for i, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(i)
            return {"message": "Book Deleted", "book": deleted_book.__dict__}
    raise HTTPException(status_code=404, detail="Book not found")
 except Exception as e:
    raise HTTPException(status_code=500, detail=f"Error deleting book:str(e)")
 