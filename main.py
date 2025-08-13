from fastapi import FastAPI
import models
from database import engine
from routers import auth, todos


app = FastAPI()

print("Creating Tables...")
models.Base.metadata.create_all(bind=engine)


#Include Routers:
app.include_router(auth.router)
app.include_router(todos.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Todo API!"}

