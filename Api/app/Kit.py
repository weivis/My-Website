'''
    v0.1
    个人Flask工具包
    Github:https://github.com/weivis/Flask-Kit
'''

from datetime import datetime
import math

# 列表操作-------------------------------------------------------------

def Paginator(data, page, num=10):
    '''
        列表分页
        Paginator(列表对象, 分页数, num=单页分页条数(选填 默认为10))

        return
            切片列表, 数据总量，分页总页数
    '''
    num = num
    page = page
    total = len(data)
    pages = math.ceil(total/num)
    ret = []
    if num*page < total:
        for i in range((page-1)*num, num*page):
            ret.append(data[i])
    elif (page-1)*num < total <= num*page:
        for i in range((page-1)*num, total):
            ret.append(data[i])

    return ret, total, pages

# 字符串转date,datetime------------------------------------------------------
def StrForDate(s):
    '''
        Str转Date类型(str > Date)
        yyyy-mm-dd(1999-04-19)
        return
            date
    '''
    if not s:
        return datetime(int(1), int(1), int(1))
    year_s, mon_s, day_s = s.split('-')
    return datetime(int(year_s), int(mon_s), int(day_s))

def StrForDateTime(s):
    '''
        Str转Date类型(str > Datetime)
        yyyy-mm-dd hh-mm-ss(2019-03-17 11:00:00)
        return
            datetime
    '''
    if not s:
        pass
    return datetime.strftime(s, "%Y-%m-%d %H:%M:%S")

# date,datetime转字符串------------------------------------------------------

def DateTimeForStr(s):
    '''
        Datetime转字符串 (DateTime > Str)
        如果值为空则返回:
            return
                00-00-00 00:00:00
    '''
    if not s:
        return '00-00-00 00:00:00'
    return datetime.strftime(s, "%Y-%m-%d %H:%M:%S")

def DateForStr(s):
    '''
        Datetime转字符串 (Date > Str)
        如果值为空则返回:
            return
                00-00-00
    '''
    if not s:
        return '00-00-00'
    return datetime.strftime(s, '%Y-%m-%d')

# 获取请求体内的字符串 --------------------------------------------------------

def GetRequestArgsData(request,key,nones):
    '''
        Args
        获取请求体内的字段对应值
        GetRequestArgsData(request, '字段', '默认值')
    '''
    if nones:
        return request.args.get(str(key),nones)
    else:
        return request.args.get(str(key),None)

def GetRequestJsonData(request,key,nones):
    '''
        Json
        获取请求体内的字段对应值
        GetRequestJsonData(request, '字段', '默认值')
    '''
    if nones:
        return request.json.get(str(key),nones)
    else:
        return request.json.get(str(key),None)

def GetRequestFormData(request,key,nones):
    '''
        Form
        获取请求体内的字段对应值
        GetRequestFormData(request, '字段', '默认值')
    '''
    if nones:
        return request.form.get(str(key),nones)
    else:
        return request.form.get(str(key),None)

# 分页数获取---------------------------------------------------------------------------

def PaginatePages(request, key):
    '''
        Json
        获取分页数
        key = 自定义参数名 or 默认 : queryPage
    '''
    if key == None:
        key = 'queryPage'
    pages = request.json.get(str(key), 1)

    if pages == 0 or str(pages) == '':
        pages = 1

    return pages

def PaginatePagesArgs(request, key):
    '''
        Json
        获取分页数
        key = 自定义参数名 or 默认 : queryPage
    '''
    if key == None:
        key = 'queryPage'
    pages = request.args.get(str(key), 1)

    if pages == 0 or str(pages) == '':
        pages = 1

    return pages