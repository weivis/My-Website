import hashlib
import os
import random
from datetime import datetime

from app.Common import GetRequestFormData, GetRequestJsonData
from app.Config import (ERROR_TOKENAUTHCODE, NOT_LOGIN_ERROR_CODES,
                        REQUEST_ERROR_METHOD_CODES, SERVER_GULAOBURL,
                        UPLOAD_KEY, UPLOAD_KEY_FLOAD, USER_ERROR_GROUP_CODES)
from app.Extensions import db
from app.Models import UserAccount

def CreateNewFilename(ext):
    '''生成新的文件名'''
    return datetime.strftime(datetime.now(),'%Y%m%d%H%M%S') + '{:03d}'.format(random.randint(0, 999)) + ext

def QueryFileName(filestr):
    '''
        获取文件名
        返回
            1.文件名(不包含文件后缀)
            2.后缀
    '''
    pach , filename = os.path.split(filestr)
    return os.path.splitext(filename)

def FileExtLegitimate(ext, uploadtype):
    print(ext)
    if ext:
        if uploadtype == 'image':
            if str(ext) not in ['.jpeg','.jpg','.png', '.jpg']:
                return False
            else:
                return True
        return False
    return False

def upload_file(request):
    try:
        file = request.files['file']
    except:
        return 400, '错误: 没有文件', ''

    # userkey = GetRequestFormData(request, 'userKey', None)
    # token = GetRequestFormData(request, 'authToken', None)

    # if not userkey or not token:
    #     return REQUEST_ERROR_METHOD_CODES, '请求参数有误1', ''

    # obj = UserAccount.query.filter(UserAccount.id == userkey).first()

    # if not obj:
    #     return REQUEST_ERROR_METHOD_CODES, '请求参数有误2', ''
    
    # if not token:
    #     return REQUEST_ERROR_METHOD_CODES, '请求参数有误3', ''

    # if obj.token != token:
    #     return ERROR_TOKENAUTHCODE, 'Token已失效或不正确, 请重新登录', ''

    upload_key = GetRequestFormData(request, 'uploadKey', None)

    if not upload_key:
        return 400, '错误: Key值不能为空', {}

    filename, ext = QueryFileName(file.filename)
    if not FileExtLegitimate(ext, 'image'):
        return 400, '文件类型不允许', {}

    if upload_key not in UPLOAD_KEY:
        return 400, '错误: 不允许使用的Key值', {}

    newfilename = CreateNewFilename(ext)
    file.save(os.path.join(os.path.abspath('app/static/' + UPLOAD_KEY_FLOAD[str(upload_key)] + "/"), newfilename))

    return 200, 'ok', {
        'lodpath': SERVER_GULAOBURL + '/static/' + UPLOAD_KEY_FLOAD[str(upload_key)] + '/' + newfilename,
        'ospath': UPLOAD_KEY_FLOAD[str(upload_key)] + '/' + newfilename
    }
