# DEBUG 模式
DEBUG = True

# ----------------------------------------------------------------------

# 跨域密钥
SECRET_KEY = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

# ----------------------------------------------------------------------

# 测试服数据库
SQLALCHEMY_DATABASE_URI = "mysql://root:kaluliroot123@119.23.243.25:3306/xianjunwei?charset=utf8mb4"

# 其他
SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
    如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
'''

# ----------------------------------------------------------------------

# 服务器地址
SERVER_GULAOBURL = 'http://127.0.0.1:8080'
SERVER_STATICLOADURL = SERVER_GULAOBURL + '/static'