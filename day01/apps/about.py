from flask import Blueprint, render_template

bp = Blueprint('about', __name__, '/about/')


@bp.route('/about/')
def about():
    context = {
        'username': '周杰伦',
        'books': ['红楼梦', '三国演义']
    }
    return render_template('about.html', **context)