import datetime
from sqlalchemy.orm import class_mapper

from app.Kit import DateForStr, DateTimeForStr
# def DateTimeForStr(s):
#     '''
#         DateTime > Str
#         if not val out : str 00-00-00 00:00:00
#     '''
#     if not s:
#         return '00-00-00 00:00:00'
#     return datetime.strftime(s, "%Y-%m-%d %H:%M:%S")

# def DateForStr(s):
#     '''
#         Date > Str
#         if not val out : str 00-00-00
#     '''
#     if not s:
#         return '00-00-00'
#     return datetime.strftime(s, '%Y-%m-%d')

# --------------------------------------------------

class SerializeConfig:
    # 每页分多少条
    SQLALCHEMY_PAGINATE_PER = 10

def SerializeQuerySet(querys, query_page):
    '''
        预处理
        querys : 查询集
        query_page : 需要获取的页数
        return 
            1.一共查询到的数量(query_count)
            2.查询集对象 (可以用SerializeDataCalss()直接序列化)
            3.分页数
            query_count query_dataitems query_datapages
    '''
    query_count = querys.count()
    query_data = querys.paginate(query_page, per_page=SerializeConfig.SQLALCHEMY_PAGINATE_PER)
    return query_count, query_data.items, query_data.pages

def Serialize(models, obj='obj', userid=None, dataprocessing=None, notreturn = []):
    '''
        序列化器统一入口
        models

        需要使用userid的时候可传
        userid

        序列化对象类型
        obj
        list

        指定的数据持续化处理
        dataprocessing

        不需返回的字段
        notreturn
    '''

    if obj == 'obj':
        return SerializeItem(models, userid=userid, dataprocessing=dataprocessing, notreturn=notreturn)

    if obj == 'list':
        cache = []
        for model in models:
            cache.append(SerializeItem(model, userid=userid, dataprocessing=dataprocessing, notreturn=notreturn))
        return cache

    print('请先定义需要序列化的对象的类型')
    return False

def SerializeItem(model,userid=None, dataprocessing = None, notreturn = []):
    '''
        序列化单个对象
    '''
    li = []
    dicts = {}
    columns = [c.key for c in class_mapper(model.__class__).columns]

    for c in columns:
        # print(c)

        # 不需要返回的字段直接排除不返回数据
        if str(c) not in notreturn:

            try:
                # 优先处理数组和字段的对象

                cc = eval(getattr(model, c))
                if isinstance(cc, dict):
                    li.append((c,cc))

                if isinstance(cc, list):
                    li.append((c,cc))

            except:

                # 不符合数组字段类型的进入date datetime str 等类型的返回

                if type(getattr(model, c)) == datetime.datetime:
                    li.append((c, DateTimeForStr(getattr(model, c))))

                elif type(getattr(model, c)) == datetime.date:
                    li.append((c, DateForStr(getattr(model, c))))

                else:
                    if getattr(model, c) == '' or getattr(model, c) == None:
                        li.append((c, ''))
                    else:
                        li.append((c, getattr(model, c)))

                # 持续化处理--------------------------------------------
                '''
                    添加返回项的方法
                    li.append(('参数名' , 值))

                    # 获取model原有的字段名的值
                    getattr(model, 'id') 获取model id 的值
                '''

                if dataprocessing == 'getlist':
                    pass

        else:
            pass
    for s in li:
        dicts.update(dict([s]))
    return dicts

def SerializeliData(model,userid=None, dataprocessing = None, notreturn = []):
    '''
        单对象序列化器
    '''
    li = []
    dicts = {}

    from sqlalchemy.orm import class_mapper
    columns = [c.key for c in class_mapper(model.__class__).columns]

    for c in columns:
        print(c)

        if str(c) not in notreturn:

            try:
                cc = eval(getattr(model, c))
                if isinstance(cc, dict):
                    li.append((c,cc))

                if isinstance(cc, list):
                    li.append((c,cc))

            except:

                if type(getattr(model, c)) == datetime.datetime:
                    li.append((c, DateTimeForStr(getattr(model, c))))

                elif type(getattr(model, c)) == datetime.date:
                    li.append((c, DateForStr(getattr(model, c))))

                else:
                    if getattr(model, c) == '' or getattr(model, c) == None:
                        li.append((c, ''))
                    else:
                        li.append((c, getattr(model, c)))

                # 自增条件--------------------------------------------
                if c == 'author_userid' and userid != None:
                    li.append(('follow_status' ,GetFollowType(userid, getattr(model, c))))

                if c == 'parent_comment_id':
                    if int(getattr(model, 'seedtype')) == 1:
                        li.append(('parent_comment_id' , getattr(model, 'id')))

                if dataprocessing == 'queryvideo':
        
                    videotag = VideoTag.query.filter(VideoTag.videoid == getattr(model, 'id')).all()
                    dataprocessing_taglist = [{
                        'tagid':i.tagid,
                        'tagname':VideoTagName.query.filter_by(id = i.tagid).first().tagname
                    } for i in videotag]

                    li.append(('taglist' , dataprocessing_taglist))

        else:
            pass

    for s in li:
        dicts.update(dict([s]))

    return dicts
