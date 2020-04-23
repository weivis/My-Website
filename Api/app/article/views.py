from app.Extensions import db
from app.Kit import PaginatePages
from app.ReturnCode import ReturnCode
from datetime import datetime
from app.Models.db_Article import Article
from app.ModelSerialize import Serialize, SerializeQuerySet

def query_article(request):
    id = request.get('id', None)
    article = Article.query.filter(Article.id == id).first()
    if not article:
        return ReturnCode.paramete_error, '文章不存在或参数有误', ''
    serialize = Serialize(article, obj='obj', dataprocessing='getarticlelist')
    return ReturnCode.ok, '', serialize

def query_article_list(request):
    article_type = request.get('article_type', None)
    query_pages = PaginatePages(request,None)

    if not article_type:
        return ReturnCode.paramete_error, '获取的文章类型缺乏', ''

    querys = Article.query.filter(Article.status == 0).order_by(Article.upload_time.desc())

    # 作品
    if int(article_type) == 1:
        querys = querys.filter(Article.article_type == article_type)

        content_type = request.get('content_type', None)
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
        'list':Serialize(query_dataitems,obj='list', dataprocessing='getarticlelist', notreturn=['content']),
        'queryCount': query_count,
        'dataPges': query_datapages,
        'nowPage': query_pages
        }

def upload_article(request):
    current_account = request['current_account']
    title = request.get('title', None)
    introduce = request.get('introduce', None)
    content = request.get('content', None)
    article_type = request.get('article_type', None)
    content_type = request.get('content_type', None)
    status = request.get('status', 0)
    cover = request.get('cover', None)
    print(content_type)

    if not title:
        return ReturnCode.paramete_error, '标题不能为空', ''

    if not introduce:
        return ReturnCode.paramete_error, '介绍不能为空', ''

    if not str(content):
        return ReturnCode.paramete_error, '内容不能为空', ''

    if not article_type:
        return ReturnCode.paramete_error, '发布类型不能为空', ''  

    if not cover:
        return ReturnCode.paramete_error, '封面不能为空', ''  

    if int(article_type) == 1:
        if not content_type:
            return ReturnCode.paramete_error, '作品类型不能为空', ''  
    else:
        content_type = 0

    new = Article()
    new.upload_userid = current_account.id
    new.upload_time = datetime.now()
    new.article_type = int(article_type)
    new.title = str(title)
    new.introduce = str(introduce)
    new.content = str(content)
    new.content_type = int(content_type)
    new.cover = str(cover)
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