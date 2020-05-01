from app.auth import auth, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenAuthPost

# 注册------------------------------------------------------------------------------------

@auth.route('/register', methods=["POST"])
@requestPOST
def register(request):
    '''游客注册
        Param:
            username 用户名
            email 邮箱
            password 密码
            repassword 重复密码

        ReturnCode:
            200 注册成功
            400 邮箱或用户名密码输入不正确
                该邮箱已被注册
                该用户名已被注册
                两次密码输入不一致
            502 系统出错

        ReturnJson:
    '''
    c, m, d = views.register(request.json)
    return ReturnRequest(c, m, d)

# 登录------------------------------------------------------------------------------------

@auth.route('/login', methods=["POST"])
@requestPOST
def login(request):
    '''登录接口
        Param:
            email 邮箱
            password 密码

        ReturnCode:
            200 登录成功
            400 用户不存在
                邮箱或密码不正确
            1000 黑名单用户 禁止登录
            502 系统出错

        ReturnDoc:
            Token
            userID
            username
            head
            group

        ReturnJson:

    '''
    c, m, d = views.login(request.json)
    return ReturnRequest(c, m, d)

# 退出------------------------------------------------------------------------------------

@auth.route('/Logout', methods=["POST"])
@TokenAuthPost(user_group=[1, 2])
def Logout(request):
    '''登出接口
        Param:
            Token

        ReturnCode:
            200 退出登录成功
            400 系统出错

        ReturnDoc:
        ReturnJson:
    '''
    c, m, d = views.Logout(request.json)
    return ReturnRequest(c, m, d)
