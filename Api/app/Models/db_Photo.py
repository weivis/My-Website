from app.Extensions import db
from datetime import datetime

from sqlalchemy.dialects.mysql import LONGTEXT

class Photo(db.Model):
    
    __tablename__ = 'Photo'

    id = db.Column(db.Integer, primary_key=True)
    sort = db.Column(db.Integer) # 权重
    link = db.Column(db.String(255)) # 地址
    status = db.Column(db.Integer) # 是否生效
    '''
        1生效 0隐藏
    '''