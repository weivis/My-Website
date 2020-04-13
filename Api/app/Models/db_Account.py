'''
    ### SQLAlchemy常用数据类型：
    Integer：整形，映射到数据库中是int类型。
    Float：浮点类型，映射到数据库中是float类型。他占据的32位。
    Double：双精度浮点类型，映射到数据库中是double类型，占据64位。
    String：可变字符类型，映射到数据库中是varchar类型.
    Boolean：布尔类型，映射到数据库中的是tinyint类型。
    DECIMAL：定点类型。是专门为了解决浮点类型精度丢失的问题的。在存储钱相关的字段的时候建议大家都使用这个数据类型。并且这个类型使用的时候需要传递两个参数，第一个参数是用来标记这个字段总能能存储多少个数字，第二个参数表示小数点后有多少位。
    Enum：枚举类型。指定某个字段只能是枚举中指定的几个值，不能为其他值。在ORM模型中，使用Enum来作为枚举 
    Date：存储时间，只能存储年月日。映射到数据库中是date类型。在Python代码中，可以使用`datetime.date`来指定 
    DateTime：存储时间，可以存储年月日时分秒毫秒等。映射到数据库中也是datetime类型。在Python代码中，可以使用`datetime.datetime`来指定。示例代码如下：

    Time：存储时间，可以存储时分秒。映射到数据库中也是time类型。在Python代码中，可以使用`datetime.time`来至此那个。 
    Text：存储长字符串。一般可以存储6W多个字符。如果超出了这个范围，可以使用LONGTEXT类型。映射到数据库中就是text类型。
    LONGTEXT：长文本类型，映射到数据库中是longtext类型。

    price = Column(Float)
    is_delete = Column(Boolean)
    money = Column(DECIMAL(10, 4))
    language = Column(Enum('python', 'flask'))
    create_date = Column(Date)
    create_datetime = Column(DateTime)
    content = Column(String(100))
    create_time = Column(Time)
    content_text = Column(Text)
    long_text = Column(LONGTEXT)
'''

'''
    db.Column(db.Text)
    db.Column(db.String(255))
    db.Column(db.Integer)
    db.Column(db.DateTime)
    db.Column(db.Date)
    db.Column(db.Boolean)
'''

from app.Extensions import db
from datetime import datetime

# 用户----------------------------------------------------------------------------------------

# 用户账户表
class Account(db.Model):
    
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)

    # Token认证
    token = db.Column(db.Text)                  # 登录token

    # 账户信息
    reg_time = db.Column(db.DateTime)           # 注册时间
    email = db.Column(db.String(255))   # 注册邮箱
    username = db.Column(db.String(255))    # 账户名
    profile = db.Column(db.String(255))         # 头像

    # 账户
    password = db.Column(db.String(255))        # 密码
    account_group = db.Column(db.Integer)       # 用户组
    '''
        1 = 站长
        2 = 游客
    '''
    status = db.Column(db.Integer)              # 账户状态
    '''
        1 = 正常
        2 = 黑名单
    '''