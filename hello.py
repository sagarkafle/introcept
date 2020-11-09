import json
from flask import Flask, request


app = Flask(__name__)

books = [
    {'id': 1, 'name': 'ABC'},
    {'id': 2, 'name': 'XYZ'},
    {'id': 3, 'name': 'PQR'}
]


@app.route('/books', methods=['GET'])
def get_books():
    return json.dumps(books), 200, {'content-type': 'application/json'}


@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    for book in books:
        if book['id'] == id:
            return json.dumps(book), 200, {'content-type': 'application/json'}


@app.route('/books', methods=['POST'])
def create_book():
    id = int(request.form['id'])
    name = request.form['name']
    new_book = {'id': id, 'name': name}
    books.append(new_book)
    return '', 201, {f'location': '/books/{id}'}


@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    new_book = request.get_json()
    for book in books:
        if book['id'] == id:
            book['name'] = new_book['name']

    return '', 204


@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for book in books:
        if book['id'] == id:
            books.remove(book)

    return '', 204


app.run(debug=True)