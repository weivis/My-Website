from functools import wraps

from flask import request
from flask_login import current_user

from app.Common import ReturnRequest
from app.Config import (ERROR_TOKENAUTHCODE, NOT_LOGIN_ERROR_CODES,
                        REQUEST_ERROR_METHOD_CODES, USER_ERROR_GROUP_CODES)
from app.Kit import GetRequestJsonData
from app.Models import UserAccount

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
            return ReturnRequest(REQUEST_ERROR_METHOD_CODES,'请求方法不对','')
    return wrapper

def requestGET(func=None):
    '''
        [GET]通用Get请求
        条件: GET
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            return func(request, *args, **kwargs)
        else:
            return ReturnRequest(REQUEST_ERROR_METHOD_CODES,'请求方法不对','')
    return wrapper

# TokenAuthPost -------------------------------------------------------------------------------------------------------------

def UserTokenAuthPost(func=None):
    '''
        用户token验证后才能请求
        取userid
        userid = GetRequestJsonData(request, 'userKey', None)
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            userkey = GetRequestJsonData(request, 'userKey', None)
            token = GetRequestJsonData(request, 'authToken', None)
            if not userkey or not token:
                return ReturnRequest(REQUEST_ERROR_METHOD_CODES, '请求参数有误', '')

            obj = UserAccount.query.filter(UserAccount.id == userkey).first()

            if not obj:
                return ReturnRequest(REQUEST_ERROR_METHOD_CODES, '请求参数有误', '')
            
            if not token:
                ReturnRequest(REQUEST_ERROR_METHOD_CODES, '请求参数有误', '')

            if obj.token != token:
                return ReturnRequest(ERROR_TOKENAUTHCODE, 'Token已失效或不正确, 请重新登录', '')
            
            userid = obj.id
            return func(request, *args, **kwargs)

        else:
            return ReturnRequest(REQUEST_ERROR_METHOD_CODES,'请求方法不对','')
    return wrapper

def UserTokenAuthGet(func=None):
    '''
        用户token验证后才能请求
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            userkey = GetRequestJsonData(request, 'userkey', None)
            token = GetRequestJsonData(request, 'token', None)
            if not userkey or not token:
                return ReturnRequest(REQUEST_ERROR_METHOD_CODES, '请求参数有误', '')

            obj = UserAccount.query.filter(UserAccount.id == userkey).first()

            if not obj:
                return ReturnRequest(REQUEST_ERROR_METHOD_CODES, '请求参数有误', '')
            
            if not token:
                ReturnRequest(REQUEST_ERROR_METHOD_CODES, '请求参数有误', '')

            if obj.token != token:
                return ReturnRequest(ERROR_TOKENAUTHCODE, 'Token已失效或不正确, 请重新登录', '')

            userid = obj.id
            return func(request, *args, **kwargs)

        else:
            return ReturnRequest(REQUEST_ERROR_METHOD_CODES,'请求方法不对','')
    return wrapper

# 需要登录后才能请求的中间件----------------------------------------------------------------------------------------------------

def requestUserGet(func=None):
    '''
        [GET]通用用户请求
        条件: 需登录后才能请求 GET
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            if current_user.is_authenticated:
                if current_user.user_group != 0:
                    return func(request, *args, **kwargs)
                else:
                    return ReturnRequest(USER_ERROR_GROUP_CODES, '用户状态异常', '')
            else:
                return ReturnRequest(NOT_LOGIN_ERROR_CODES, '未登录', '')
        else:
            return ReturnRequest(REQUEST_ERROR_METHOD_CODES,'请求方法不对','')
    return wrapper

def requestUserPost(func=None):
    '''
        [POST]通用用户请求
        条件: 需登录后才能请求 POST
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            if current_user.is_authenticated:
                if current_user.user_group != 0:
                    return func(request, *args, **kwargs)
                else:
                    return ReturnRequest(USER_ERROR_GROUP_CODES, '用户状态异常', '')
            else:
                return ReturnRequest(NOT_LOGIN_ERROR_CODES, '未登录', '')
        else:
            return ReturnRequest(REQUEST_ERROR_METHOD_CODES,'请求方法不对','')
    return wrapper

# 需管理员登录后才能请求的中间件----------------------------------------------------------------------------------------------------

def requestAdminPost(func=None):
    '''
        [POST]需要管理员登录后才能通过的中间件
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'POST':
            if current_user.is_authenticated:
                if current_user.user_group == 100:
                    return func(request, *args, **kwargs)
                else:
                    return ReturnRequest(USER_ERROR_GROUP_CODES, '非法请求', '')
            else:
                return ReturnRequest(NOT_LOGIN_ERROR_CODES, '未登录', '')
        else:
            return ReturnRequest(REQUEST_ERROR_METHOD_CODES, '请求方法不对', '')
    return wrapper

def requestAdminGet(func=None):
    '''
        [POST]需要管理员登录后才能通过的中间件
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            if current_user.is_authenticated:
                if current_user.user_group == 100:
                    return func(request, *args, **kwargs)
                else:
                    return ReturnRequest(USER_ERROR_GROUP_CODES, '非法请求', '')
            else:
                return ReturnRequest(NOT_LOGIN_ERROR_CODES, '未登录', '')
        else:
            return ReturnRequest(REQUEST_ERROR_METHOD_CODES, '请求方法不对', '')
    return wrapper
