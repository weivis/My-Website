'''

    var 0.2
    https://github.com/weivis/Flask-Email

    # SeedEmail(recipients='接收者邮箱', templeat='register', data={'email':'模板数据', 'code':'模板数据'})
    # SeedEmail(title='邮件名', recipients='接收者邮箱', body='邮件主体', html='邮件内容')

    配置发送邮件
    app.config['MAIL_SERVER'] = 'smtp.163.com'
    app.config['MAIL_PORT'] = 25
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = '发送邮箱账户'
    app.config['MAIL_PASSWORD'] = '邮箱授权密码'
'''

from flask import current_app
from app.Extensions import mail
from flask_mail import Message
from threading import Thread

class AppConfig:
    SENDER = '163@163.com'
    EMAIL_SUBJECT_PREFIX = '[COMNAME]'

def EmailTempleat(name,templeat_data={}):

    print('发送邮件>' + str(templeat_data))

    # register 模板
    if name == 'register':
        if not templeat_data.get('email') or not templeat_data.get('code'):
            print('EmailTempleat!:邮件模板缺乏参数')
            return False

        title = 'Register activation link'
        body = 'Register activation link'
        html = '{0}{1}'.format(templeat_data.get('email'), templeat_data.get('code'))
        return title, body, html

    print('EmailTempleat!:找不到对应模板')
    return False

def SeedEmail(title=None, recipients=None, body=None, html=None, templeat=None, data={}):
    '''
        title, recipients, body, html
        templeat:模板id
        data:模板数据
    '''

    if not templeat:

        if not all([title, recipients, body]):
            print('SeedEmail!:无法发送邮件 参数不齐全')

    else:
        try:
            title, body, html = EmailTempleat('register', templeat_data=data)
        except:
            print('SeedEmail!:抛出异常')
            return False

    recipientsarr = []
    recipientsarr.append(recipients)
    sender = AppConfig.SENDER
    recipients = recipientsarr
    
    app = current_app._get_current_object()
    message = Message(AppConfig.EMAIL_SUBJECT_PREFIX + title, sender=sender, recipients=recipients, html=html)
    thr = Thread(target=_send_async_mail, args=[app, message])  # pass app
    thr.start()

def _send_async_mail(app, message):  # target function
    with app.app_context():
        mail.send(message)
        print('异步邮件发送成功>')