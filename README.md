
# FastAPI Book API

This is a simple RESTful API project built with FastAPI, designed for educational purposes. It provides a hands-on environment to discover and learn about FastAPI features, including CRUD operations and error handling.

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone <https link>
   cd fastapi-book-api
   ```

2. **Install dependencies:**
   ```bash
   pip install -r app/requirements.txt
   ```

3. **Run the application:**
   ```bash
   uvicorn app.main:app --reload
   ```
   Access the API at `http://127.0.0.1:8000`.
   Also the Swagger UI at `http://127.0.0.1:8000/docs`.

## API Cheat Sheet

- **GET /books**: Retrieve all books.
- **GET /books/{book_id}**: Get a book by ID.
- **POST /books**: Add a new book (send JSON data).

## License

MIT License.

Enjoy exploring FastAPI!
