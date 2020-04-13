import datetime as datetimes
import hashlib
from datetime import date, datetime

from flask_bcrypt import check_password_hash, generate_password_hash

from app.Extensions import db
from app.Kit import (Check_EmailStr, DateTimeForStr, GetRequestJsonData,
                     RandomStr)
from app.Models.db_Account import Account
from app.ReturnCode import ReturnCode
from app.Config import SERVER_GULAOBURL

def register(request):

    username = request.get('username', None)
    email = request.get('email', None)
    password = request.get('password', None)
    repassword = request.get('repassword', None)

    print(username, email, password, repassword)

    if not all([username, email, password, repassword]):
        return ReturnCode.paramete_error, '邮箱或用户名密码输入不正确', ''

    if Account.query.filter(Account.email == email).first():
        return ReturnCode.paramete_error, '该邮箱已被注册', ''

    if Account.query.filter(Account.username == username).first():
        return ReturnCode.paramete_error, '该用户名已被注册', ''

    if password != password:
        return ReturnCode.paramete_error, '两次密码输入不一致', ''

    addacc = Account()
    addacc.email = email
    addacc.password = generate_password_hash(password)
    addacc.username = username
    addacc.status = 1
    addacc.account_group = 2
    addacc.profile = 'default.png'
    addacc.reg_time = datetime.now()
    db.session.add(addacc)

    try:
        db.session.commit()
        return ReturnCode.ok, '注册成功', ''

    except:
        db.session().rollback()
        return ReturnCode.server_error, '系统出错', ''

def login(request):

    hmduserreturncode = 1000
    email = request.get('email', None)
    password = request.get('password', None)

    account = Account.query.filter(Account.email == email).first()

    if not account:
        return ReturnCode.paramete_error, '用户不存在', ''

    if account.status == 2:
        return hmduserreturncode, '黑名单用户 禁止登录', ''

    if check_password_hash(str(account.password), password):
        md5 = hashlib.md5((account.email + DateTimeForStr(datetime.now())).encode()).hexdigest()
        account.token = str(md5)
        db.session.commit()
        # return 400, '登录成功', {'Token':md5, 'userID': str(user.id)}
        return ReturnCode.ok, '登录成功', {'Token':md5, 'userID': str(account.id), 'username':account.username, 'head':SERVER_GULAOBURL + '/static/head/' + account.profile, 'group':account.account_group}
        
    return ReturnCode.paramete_error, ' 邮箱或密码不正确', ''

def Logout(request):
    current_account = request['current_account']
    current_account.token = ''

    try:
        db.session.commit()
        return ReturnCode.ok, '退出登录成功', ''

    except:
        db.session.rollback()
        return ReturnCode.server_error, '系统出错', ''