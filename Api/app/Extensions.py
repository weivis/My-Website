from flask_caching import Cache
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from app import Config
from flask_docs import ApiDoc
from flask_mail import Mail

# celery!
# from celery import Celery
# celery = Celery(__name__, broker=Config.CELERY_BROKER_URL, backend=Config.CELERY_RESULT_BACKEND)
# from flask import current_app
# from app.Extensions import celery
# celery.conf.update(app.config)
# @celery.task()
# with app.app_context():
# delay

db = SQLAlchemy()
mail = Mail()
cache = Cache()
apidoc = ApiDoc()

# 初始化
def config_extensions(app):

    CORS(app, supports_credentials=True)

    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

    db.init_app(app)
    
    mail.init_app(app)

    apidoc.init_app(app)
