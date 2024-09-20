from fastapi.testclient import TestClient
from app.main import app  

client = TestClient(app)

def test_read_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)  # Check if dict

def test_read_book_by_id():
    response = client.get("/books/1")  # different values should be tested
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "year": 1949
    }

def test_create_book():
    new_book = {
        "title": "New Book",
        "author": "New Author",
        "year": 2023
    }
    response = client.post("/books", json=new_book)
    assert response.status_code == 200
    assert response.json()["title"] == new_book["title"]
