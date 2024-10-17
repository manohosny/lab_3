# Book Management API

A simple REST API for managing books, built with Flask and documented with Swagger.

## Features

- CRUD operations for books
- Swagger documentation
- Postman collection for testing
- Input validation
- Error handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/manohosny/lab_3.git
cd book-api
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask flask-swagger-ui
```

## Running the API

1. Start the Flask server:
```bash
python app.py
```

2. The API will be available at `http://localhost:5000/api`
3. Access Swagger documentation at `http://localhost:5000/api/docs`

## API Endpoints

- GET /api/books - Get all books
- GET /api/books/{id} - Get a specific book
- POST /api/books - Create a new book
- PUT /api/books/{id} - Update a book
- DELETE /api/books/{id} - Delete a book


## Testing

The Postman collection includes the following test cases:

1. Get all books (empty list)
2. Create a new book (valid input)
3. Create a new book (invalid input - missing fields)
4. Get a specific book (existing)
5. Get a specific book (non-existing)
6. Update a book (valid input)
7. Delete a book
