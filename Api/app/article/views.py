from app.Extensions import db
from app.Kit import GetRequestJsonData, GetRequestFormData, GetRequestArgsData
from app.ReturnCode import ReturnCode
from datetime import datetime
from app.Models import Article
from app.ModelSerialize import Serialize

def query_article(request):
    id = GetRequestArgsData(request, 'id', None)
    article = Article.query.filter(Article.id == id).first()
    if not article:
        return ReturnCode.paramete_error, '文章不存在或参数有误', ''
    serialize = Serialize(article, obj='obj')
    return ReturnCode.ok, '', serialize

def upload_article(request):
    userid = GetRequestJsonData(request, 'userid', None)
    title = GetRequestJsonData(request, 'title', None)
    introduce = GetRequestJsonData(request, 'introduce', None)
    content = GetRequestJsonData(request, 'content', None)
    article_type = GetRequestJsonData(request, 'article_type', None)
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