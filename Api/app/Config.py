# DEBUG 模式
DEBUG = True

# ----------------------------------------------------------------------

# 跨域密钥
SECRET_KEY = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

# ----------------------------------------------------------------------

SQLALCHEMY_DATABASE_URI = "mysql://root:weivimysql@0.0.0.0:3306/my-website?charset=utf8mb4"
# 测试服数据库
# SQLALCHEMY_DATABASE_URI = "\x6d\x79\x73\x71\x6c\x3a\x2f\x2f\x72\x6f\x6f\x74\x3a\x6b\x61\x6c\x75\x6c\x69\x72\x6f\x6f\x74\x31\x32\x33\x40\x31\x31\x39\x2e\x32\x33\x2e\x32\x34\x33\x2e\x32\x35\x3a\x33\x33\x30\x36\x2f\x78\x69\x61\x6e\x6a\x75\x6e\x77\x65\x69\x3f\x63\x68\x61\x72\x73\x65\x74\x3d\x75\x74\x66\x38\x6d\x62\x34"

# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_TRACK_MODIFICATIONS = False

# ----------------------------------------------------------------------

# 服务器地址
SERVER_GULAOBURL = 'http://www.weivird.com'
SERVER_STATICLOADURL = SERVER_GULAOBURL + '/static'
# ----------------------------------------------------------------------

MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 25
MAIL_USE_TLS = True
MAIL_USERNAME = 'kol_email@163.com'
MAIL_PASSWORD = 'Kolemail123456'

# ----------------------------------------------------------------------

# CELERY_REDISDB = 'redis://localhost:6379/0'
# CELERY_RESULT_BACKEND = CELERY_BROKER_URL = CELERY_REDISDB

# ----------------------------------------------------------------------

API_DOC_MEMBER = ['auth','article','upload', 'index', 'photo']

# 需要排除的 RESTful Api 文档
RESTFUL_API_DOC_EXCLUDE = []