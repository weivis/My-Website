from app.auth import auth
from app.article import article
from app.upload import upload
from app.index import index
from app.photo import photo

DEFAULT_BLUEPRINT = (
    (index, '/api/index'),
    (auth, '/api/auth'),
    (article, '/api/article'),
    (upload, '/api/upload'),
    (photo, '/api/photo')
)

# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)