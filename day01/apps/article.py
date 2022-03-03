from flask import Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from day01.index import Article

bp = Blueprint('article', __name__, '/article/')


@bp.route('/article/')
def article():
    # # 1、添加数据
    # article = Article(title='惠子君是猪么', content='她是世界上最可爱最傻的猪猪猪猪猪猪猪组合组合组织租户智族汉族')
    # db.session.add(article)
    # db.session.commit()

    # # 2、查询数据
    # article = Article.query.filter_by(id=1)[0]
    # print(article.title)

    # # 3、修改数据
    article = Article.query.filter_by(id=1)[0]
    
    return '修改成功'