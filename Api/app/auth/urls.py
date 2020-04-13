from app.auth import auth, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenAuthPost

# 注册------------------------------------------------------------------------------------


@auth.route('/register', methods=["POST"])
@requestPOST
def register(request):
    '''
        username
        email
        password
        repassword
    '''
    c, m, d = views.register(request.json)
    return ReturnRequest(c, m, d)

# 登录------------------------------------------------------------------------------------


@auth.route('/login', methods=["POST"])
@requestPOST
def login(request):
    '''
        email
        password
    '''
    c, m, d = views.login(request.json)
    return ReturnRequest(c, m, d)

# 退出------------------------------------------------------------------------------------


@auth.route('/Logout', methods=["POST"])
@TokenAuthPost(user_group=[1, 2])
def Logout(request):
    '''
        Token
    '''
    c, m, d = views.Logout(request.json)
    return ReturnRequest(c, m, d)
