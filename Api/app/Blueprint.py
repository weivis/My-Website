from app.auth import auth
from app.opus import opus
from app.article import article
from app.photo import photo

DEFAULT_BLUEPRINT = (
    (auth, '/auth'),
    (opus, '/opus'),
    (article, '/article'),
    (photo, '/photo')
)

# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)