from app.auth import auth
from app.article import article
from app.upload import upload
from app.index import index

DEFAULT_BLUEPRINT = (
    (index, '/index'),
    (auth, '/auth'),
    (article, '/article'),
    (upload, '/upload')
)

# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)