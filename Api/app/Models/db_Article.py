from app.Extensions import db
from datetime import datetime

from sqlalchemy.dialects.mysql import LONGTEXT

# 文章表----------------------------------------------------------------------------------------

class Article(db.Model):
    
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    upload_userid = db.Column(db.Integer)
    upload_time = db.Column(db.DateTime) # 上传时间

    article_type = db.Column(db.Integer)
    '''
        1 = 作品分类
        2 = 文章分类
        3 = 项目分类
    '''
    content_type = db.Column(db.Integer)
    '''
        作品{
            1 设计
            2 视频
        }
        文章{

        }
        项目{

        }
    '''
    title = db.Column(db.String(255))
    cover = db.Column(db.String(255))
    introduce = db.Column(db.String(255))
    content = db.Column(LONGTEXT) # content
    status = db.Column(db.Integer)
    '''
        0 = 正常
        1 = 下架
    '''
    index = db.Column(db.Boolean, default=False)
    '''
        true的为在首页展示
    '''
    is_delete = db.Column(db.Boolean, default=False)
    '''
        是否删除
    '''