from app.Extensions import db
from datetime import datetime

from sqlalchemy.dialects.mysql import LONGTEXT

class ApiMoreArticle(db.Model):
    
    __tablename__ = 'api-more-article'

    id = db.Column(db.Integer, primary_key=True)
    line_type = db.Column(db.Integer)
    '''
        0 = 站内文章
        1 = 站外链接
    '''
    sort = db.Column(db.Integer) # 排序
    link = db.Column(db.String(255)) # 地址
    articleid = db.Column(db.Integer) # 文章id
    introduce = db.Column(db.String(255)) # 介绍
    title = db.Column(db.String(255)) # 标题
    cover = db.Column(db.String(255)) # 封面
    status = db.Column(db.Integer) # 是否生效
    '''
        1生效 0隐藏
    '''