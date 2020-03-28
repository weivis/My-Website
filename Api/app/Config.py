# DEBUG 模式
DEBUG = True

# ----------------------------------------------------------------------

# 跨域密钥
SECRET_KEY = '\x12my\x0bVO\xeb\xf8\x18\x15\xc5_?\x91\xd7h\x06AC'

# ----------------------------------------------------------------------

# 测试服数据库
SQLALCHEMY_DATABASE_URI = "mysql://root:@localhost:3306/my-website?charset=utf8mb4"

# 其他
SQLALCHEMY_TRACK_MODIFICATIONS = False
'''
    如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
'''

# ----------------------------------------------------------------------

# Token失效时候返回
ERROR_TOKENAUTHCODE = 10000

# 没登陆的时候返回错误码
NOT_LOGIN_ERROR_CODES = 10086

# 黑名单用户返回值
USER_ERROR_GROUP_CODES = 0000

# 错误请求时返回
REQUEST_ERROR_METHOD_CODES = 1000

# ----------------------------------------------------------------------

# 统一数据库返回分页数量 
SQLALCHEMY_PAGINATE_PER = 12

# ----------------------------------------------------------------------

# 关于 UPLOAD_KEY和UPLOAD_KEY_FLOAD的用法
UPLOAD_KEY = ['head']
UPLOAD_KEY_FLOAD = {'head':'image/head'}
'''
    UPLOAD_KEY 是上传时候要使用的key
    UPLOAD_KEY_FLOAD 是上传的key对于的文件储存跟目录
'''

# ----------------------------------------------------------------------

# 服务器地址
SERVER_GULAOBURL = 'http://127.0.0.1'