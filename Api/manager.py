# -*- coding: utf-8 -*-
import os
from app import create_app
from app.Extensions import db
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager, Server, Command
from app.Models import db_Account, db_Article, db_Photo, db_System

from flask_bcrypt import generate_password_hash
from datetime import datetime

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

# 输入赋值
@manager.option('-e', '-email', dest='email')
@manager.option('-p', '-password', dest='password')
@manager.option('-n', '-name', dest='name')

# python manager.py create_admin -e weivi@qq.com -p whw.1889394
def create_admin(email ,password, name):
    if not all([email, password, name]):
        print('参数不齐全')

    else:
        newadmin = db_Account()
        newadmin.reg_time = datetime.now()
        newadmin.username = name
        newadmin.account_group = 1
        newadmin.password = generate_password_hash(password)
        newadmin.status = 1
        
        db.session.add(newadmin)

        try:
            db.session.commit()
            print('成功创建管理员 : ', name)
            print('登录账号:',email)
            print('登录密码:',password)

        except Exception as e:
            print(e)
            db.session.rollback()
            print('添加管理员失败')


manager.add_command('db',MigrateCommand)
manager.add_command("runserver", Server(host='127.0.0.1', port=8080, use_debugger=True))

if __name__ == '__main__':
    manager.run()
