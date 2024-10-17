from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)

# In-memory storage for books
books = {}
last_id = 0

# Swagger configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Book Management API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/api/books', methods=['GET'])
def get_all_books():
    return jsonify(list(books.values())), 200


@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return jsonify(book), 200
    return jsonify({"error": "Book not found"}), 404


@app.route('/api/books', methods=['POST'])
def create_book():
    global last_id
    data = request.get_json()

    if not all(key in data for key in ['title', 'author', 'year']):
        return jsonify({"error": "Missing required fields"}), 400

    last_id += 1
    new_book = {
        'id': last_id,
        'title': data['title'],
        'author': data['author'],
        'year': data['year']
    }
    books[last_id] = new_book
    return jsonify(new_book), 201


@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    if book_id not in books:
        return jsonify({"error": "Book not found"}), 404

    data = request.get_json()
    if not all(key in data for key in ['title', 'author', 'year']):
        return jsonify({"error": "Missing required fields"}), 400

    books[book_id].update({
        'title': data['title'],
        'author': data['author'],
        'year': data['year']
    })
    return jsonify(books[book_id]), 200


@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id not in books:
        return jsonify({"error": "Book not found"}), 404

    del books[book_id]
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)