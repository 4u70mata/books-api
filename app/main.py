import json
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel, Field
from starlette.responses import JSONResponse
from models import Book

app = FastAPI()

# Load books data from JSON file
with open("books.json") as f:
    books_data = json.load(f)

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    book = next((book for book in books_data if book["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.get("/authors/{author_id}")
async def read_author(author_id: int):
    # Placeholder for authors; update as necessary
    return {
        "author_id": author_id,
        "name": "Ernest Hemingway",
    }

@app.get("/books")
async def read_books(year: int = None):
    if year:
        return {
            "year": year,
            "books": [book for book in books_data if book.get("year") == year],
        }
    return {"books": books_data}

@app.post("/books")
async def create_book(book: Book):
    book_dict = book.dict()
    book_dict["id"] = len(books_data) + 1
    books_data.append(book_dict)
    return book_dict

@app.get("/allbooks")
async def read_all_books() -> list:
    return books_data

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "Oops! Something went wrong"}
    )

@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    return PlainTextResponse(
        "This is a plain text response:" f"\n{json.dumps(exc.errors(), indent=2)}",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
