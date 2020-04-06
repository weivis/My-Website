from app.Extensions import db
from app.Kit import GetRequestJsonData, GetRequestFormData, GetRequestArgsData, PaginatePages, PaginatePagesArgs
from app.ReturnCode import ReturnCode
from datetime import datetime
from app.Models import Article
from app.ModelSerialize import Serialize, SerializeQuerySet

def query_article(request):
    id = GetRequestArgsData(request, 'id', None)
    article = Article.query.filter(Article.id == id).first()
    if not article:
        return ReturnCode.paramete_error, '文章不存在或参数有误', ''
    serialize = Serialize(article, obj='obj')
    return ReturnCode.ok, '', serialize

def query_article_list(request):
    article_type = GetRequestArgsData(request, 'article_type', None)
    query_pages = PaginatePagesArgs(request,None)

    if not article_type:
        return ReturnCode.paramete_error, '获取的文章类型缺乏', ''

    querys = Article.query.filter(Article.status == 0).order_by(Article.upload_time.desc())

    # 作品
    if int(article_type) == 1:
        querys = querys.filter(Article.article_type == article_type)

        content_type = GetRequestArgsData(request, 'content_type', None)
        if content_type:
            querys = querys.filter(Article.content_type == content_type)

    # 文章
    if int(article_type) == 2:
        querys = querys.filter(Article.article_type == article_type)

    # 项目
    if int(article_type) == 3:
        querys = querys.filter(Article.article_type == article_type)

    query_count, query_dataitems, query_datapages = SerializeQuerySet(querys, query_pages, per_page=100)
    return ReturnCode.ok, '', {
        'list':Serialize(query_dataitems,obj='list'),
        'queryCount': query_count,
        'dataPges': query_datapages,
        'nowPage': query_pages
        }

def upload_article(request):
    userid = GetRequestJsonData(request, 'userid', None)
    title = GetRequestJsonData(request, 'title', None)
    introduce = GetRequestJsonData(request, 'introduce', None)
    content = GetRequestJsonData(request, 'content', None)
    article_type = GetRequestJsonData(request, 'article_type', None)
    content_type = GetRequestJsonData(request, 'content_type', None)
    status = GetRequestJsonData(request, 'status', 0)

    if not userid:
        return ReturnCode.paramete_error, '用户id异常', ''

    if not title:
        return ReturnCode.paramete_error, '标题不能为空', ''

    if not introduce:
        return ReturnCode.paramete_error, '介绍不能为空', ''

    if not str(content):
        return ReturnCode.paramete_error, '内容不能为空', ''

    if not article_type:
        return ReturnCode.paramete_error, '发布类型不能为空', ''  

    new = Article()
    new.upload_userid = userid
    new.upload_time = datetime.now()
    new.article_type = int(article_type)
    new.title = str(title)
    new.introduce = str(introduce)
    new.content = str(content)
    new.content_type = int(content_type)
    new.status = status

    db.session.add(new)
    try:
        db.session.commit()
        return ReturnCode.ok, '上传成功', {
            'id':new.id
        }

    except:
        db.session().rollback()
        return ReturnCode.server_error, '系统出错', ''