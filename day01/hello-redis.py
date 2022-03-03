from flask import Flask, url_for, redirect, request, render_template

app = Flask(__name__)


# @app.route('/login/')
# def login_error():
#     return render_template('login.html')


# @app.route('/login/', methods=['POST'])
# def login():
#     uname = request.form['uname']
#     password = request.form['password']
#     if uname == 'uname' and password == 'password':
#         return redirect(url_for('hello_world'))
#     else:
#         return render_template('login.html', login_error='用户名或密码错误，请重新尝试')


@app.route('/hello_world/')
def hello_world():
    return 'hello_world'


@app.route('/')
def index():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)