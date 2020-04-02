# 主要模块
from app.auth import auth

# 内容模块
from app.home import home
from app.opus import opus
from app.article import article
from app.photo import photo
from app.proj import proj

DEFAULT_BLUEPRINT = (
    (auth, '/auth'),
    
    (home, '/home'),
    (opus, '/opus'),
    (article, '/article'),
    (photo, '/photo'),
    (proj, '/proj')
)

# 封装配置蓝本的函数
def config_blueprint(app):
    # 循环读取元组中的蓝本
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)