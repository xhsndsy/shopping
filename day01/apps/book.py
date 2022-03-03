from flask import Blueprint, url_for, jsonify

bp = Blueprint('book', __name__, '/book/')


books = [
    {'id': 1, 'name': '三国演义'},
    {'id': 2, 'name': '水浒传'},
    {'id': 3, 'name': '西游记'},
    {'id': 4, 'name': '红楼梦'}
]


@bp.route('/book/<int:book_id>')
def book_detail(book_id):
    for book in books:
        if book_id == book:
            return book

    return f'id为{book_id}的图书没有找到'


@bp.route('/book/list')
def book_list():
    for book in books:
        book['url'] = url_for('book_id', book_id=book['id'])
    return jsonify(books)
