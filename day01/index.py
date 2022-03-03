from flask import Flask, render_template
from day01.config import config
from day01.apps.book import bp as bp_book
from day01.apps.about import bp as bp_about
from day01.apps.login import bp as bp_login
from flask_sqlalchemy import SQLAlchemy

# 部署蓝图至index
app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(bp_book)
app.register_blueprint(bp_login)
app.register_blueprint(bp_about)

# 数据库配置项
db = SQLAlchemy(app)


class Article(db.Model):
    __tablename = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)


db.create_all()


@app.route('/article/')
def article():
    # # 1、添加数据
    # article = Article(title='惠子君是猪么', content='她是世界上最可爱最傻的猪猪猪猪猪猪猪组合组合组织租户智族汉族')
    # db.session.add(article)
    # db.session.commit()

    # 2、查询数据
    article = Article.query.filter_by(id=1)[0]
    print(article.title)
    return '修改成功'


@app.route('/hello_world/')
def hello_world():
    db_engine = db.get_engine()
    with db_engine.connect() as conn:
        result = conn.execute('select * from hzj')
        print(result.fetchone())
    return 'hello world'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=9000)
