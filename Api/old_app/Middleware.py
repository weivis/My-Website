from functools import wraps

from flask import request

from app.Common import ReturnRequest
from app.ReturnCode import SystemCode, ReturnCode

from app.Kit import GetRequestJsonData
from app.Models import User as UserAccount

# 基础请求----------------------------------------------------------------------------------------------------

def requestPOST(func=None):
    '''
        [POST]通用Post请求
        条件: POST
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            return func(request, *args, **kwargs)
        else:
            return ReturnRequest(SystemCode.ErrorRequestMethod,'请求方法不对','')
    return wrapper

# TokenAuthPost -------------------------------------------------------------------------------------------------------------

def TokenAuthPost(user_group):
    '''
        @UserTokenAuthPost
            Token
            user_group
        return
            current_account = request['current_account']
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if request.method == 'POST':

                token = GetRequestJsonData(request, 'Token', None)

                if not token:
                    return ReturnRequest(ReturnCode.paramete_error, '非法请求', '')

                account = UserAccount.query.filter(UserAccount.token == token).first()

                if not account:
                    return ReturnRequest(SystemCode.TokenInvalid, 'Token已失效或不正确, 请重新登录', '')

                if not user_group:
                    print('注意！@UserTokenAuthPost: 未设置可访问的用户权限')
                    return ''

                if account.userstatus not in user_group:
                    return ReturnRequest(ReturnCode.paramete_error, '你没有权限访问该接口', '')
                
                request.json['current_account'] = account

                return func(request, *args, **kwargs )

                # try:
                # except:
                #     return ReturnRequest(ReturnCode.paramete_type_error, '请求参数格式有误', '')

            else:
                return ReturnRequest(SystemCode.ErrorRequestMethod,'请求方法不正确','')
        return wrapper
    return decorator