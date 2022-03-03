from flask import Blueprint, request, render_template

bp = Blueprint('login', __name__, '/login/')


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    login_info = None
    uname = request.form.get('uname')
    pwd = request.form.get('password')
    if uname == 'uname' and pwd == 'password':
        login_info = '登陆成功'
    elif uname:
        login_info = '登陆失败'

    return render_template('login.html', login_info=login_info)