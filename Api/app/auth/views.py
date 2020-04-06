from app.Extensions import db
from app.Kit import GetRequestJsonData
from app.ReturnCode import ReturnCode 
from datetime import datetime

from app.Kit import DateTimeForStr
from flask_bcrypt import generate_password_hash, check_password_hash
import hashlib
from app.Models import User
from app.Config import SERVER_GULAOBURL

def register(request):

    username = GetRequestJsonData(request, 'username', None)
    email = GetRequestJsonData(request, 'email', None)
    password = GetRequestJsonData(request, 'password', None)
    repassword = GetRequestJsonData(request, 'repassword', None)

    print(username, email, password, repassword)

    if not all([username, email, password, repassword]):
        return ReturnCode.paramete_error, '邮箱或用户名密码输入不正确', ''

    if User.query.filter(User.email == email).first():
        return ReturnCode.paramete_error, '该邮箱已被注册', ''

    if User.query.filter(User.username == username).first():
        return ReturnCode.paramete_error, '该用户名已被注册', ''

    if password != password:
        return ReturnCode.paramete_error, '两次密码输入不一致', ''

    adduser = User(
        reg_time = datetime.now(),
        password = generate_password_hash(str(password)),
        email = str(email),
        username = str(username),
        token = '',
        head = 'default.png',
        userstatus = 0
    )
    db.session.add(adduser)

    try:
        db.session.commit()
        return ReturnCode.ok, '注册成功', ''

    except:
        db.session().rollback()
        return ReturnCode.server_error, '系统出错', ''

def login(request):

    hmduserreturncode = 1000

    email = GetRequestJsonData(request, 'email', None)
    password = GetRequestJsonData(request, 'password', None)

    user = User.query.filter(User.email == email).first()
    if not user:
        return ReturnCode.paramete_error, '用户不存在', ''

    if user.userstatus == 2:
        return hmduserreturncode, '黑名单用户 禁止登录', ''

    if check_password_hash(str(user.password), password):
        md5 = hashlib.md5((user.email + DateTimeForStr(datetime.now())).encode()).hexdigest()
        user.token = str(md5)
        db.session.commit()
        # return 400, '登录成功', {'Token':md5, 'userID': str(user.id)}
        return ReturnCode.ok, '登录成功', {'Token':md5, 'userID': str(user.id), 'username':user.username, 'head':SERVER_GULAOBURL + '/static/head/' + user.head, 'userstatus':user.userstatus}
        

    return ReturnCode.paramete_error, ' 邮箱或密码不正确', ''

def Logout(request):
    userid = GetRequestJsonData(request, 'userid', None)
    user = User.query.filter(User.id == userid).first()
    if not user:
        return ReturnCode.paramete_error, '用户不存在', ''

    user.token = ''

    try:
        db.session.commit()
        return ReturnCode.ok, '退出登录成功', ''

    except:
        db.session.rollback()
        return ReturnCode.server_error, '系统出错', ''