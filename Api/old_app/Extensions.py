from flask_caching import Cache
from flask_cors import CORS
#from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#login_manager = LoginManager()
cache = Cache()

# 初始化
def config_extensions(app):

    CORS(app, supports_credentials=True)

    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

    db.init_app(app)

    #指定登录的端点
    # login_manager.login_view = 'auth.auth'

    #需要登录时的提示信息
    # login_manager.login_message = '需要先登录'
    # 设置session保护级别
    # None：禁用session保护
    # 'basic'：基本的保护，默认选项
    # 'strong'：最严格的保护，一旦用户登录信息改变，立即退出登录

    # login_manager.session_protection = 'strong'
