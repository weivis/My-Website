from datetime import date, datetime
from app.Extensions import db
from app.ReturnCode import ReturnCode
from app.Config import SERVER_GULAOBURL, SERVER_STATICLOADURL
from app.Models.db_System import ApiMoreArticle
from app.Models.db_Article import Article
from app.ModelSerialize import Serialize
from app.Models.db_Account import Account

def list_more_article(request):
    admin = request.get('admin', None)

    if admin:
        # print('admin')
        querys = ApiMoreArticle.query.filter().order_by(ApiMoreArticle.sort.desc())
    else:
        # print('nore')
        querys = ApiMoreArticle.query.filter(ApiMoreArticle.status == 1).order_by(ApiMoreArticle.sort.desc()).limit(4)
        
    ret = []
    for i in querys:
        if i.line_type == 0:
            article = Article.query.filter(Article.id == i.articleid).first()
            ret.append({
                'id':int(i.id),
                'title':str(article.title),
                'cover':SERVER_STATICLOADURL + str(article.cover),
                'introduce': str(article.introduce),
                'link':'/opus/design?id=' + str(article.id),
                'line_type':int(i.line_type),
                'sort':int(i.sort),
                'status':int(i.status)
            })

        else:
            ret.append({
                'id':int(i.id),
                'title':i.title,
                'cover':SERVER_STATICLOADURL+i.cover,
                'introduce': i.introduce,
                'link':i.link,
                'line_type':int(i.line_type),
                'sort':int(i.sort),
                'status':int(i.status)
            })
    return 200, '', ret

def add_more_article(request):
    articleid = request.get('articleid', None)

    add = ApiMoreArticle()
    if not articleid:
        title = request.get('title', None)
        cover = request.get('cover', None)
        introduce = request.get('introduce', None)
        link = request.get('link', None)
        
        if not title:
            return 201, '标题不能为空', {}

        if not cover:
            return 202, '封面不能为空', {}

        if not introduce:
            return 203, '介绍不能为空', {}

        if not link:
            return 204, '链接地址不能为空', {}

        add.line_type = 1
        
    else:
        art = Article.query.filter(Article.id == articleid).first()
    
        add.line_type = 0
        add.articleid = art.id
        title = art.title
        cover = art.cover
        introduce = art.introduce
        link = '/page?id=' + str(art.id)

    add.title = title
    add.cover = cover
    add.introduce = introduce
    add.link = link
    add.status = 1
    add.sort = 0
    db.session.add(add)
    try:
        db.session.commit()
        return ReturnCode.ok, '成功', {}

    except:
        db.session().rollback()
        return ReturnCode.server_error, '系统出错', ''

def change_more_article(request):
    # print(request)
    change = request.get('change_type', None)
    if not change:
        return 201, '操作类型不能为空', {}

    id = request.get('id', None)
    if not id:
        return 202, 'id不能为空', {}

    change = int(change)
    obj = ApiMoreArticle.query.filter(ApiMoreArticle.id == id).first()

    if not obj:
        return 203, '被操作的推荐地址不存在', {}

    if change == 1:
        obj.status = 1

    if change == 2:
        obj.status = 0
        
    if change == 3:
        db.session.delete(obj)
        
    if change == 4:
        sort = request.get('sort', None)
        if not sort:
            return 204, 'sort排序不能为空', {}
        obj.sort = int(sort)

    try:
        db.session.commit()
        return ReturnCode.ok, '成功', {}

    except:
        db.session().rollback()
        return ReturnCode.server_error, '系统出错', ''

def index_dynamics_data(request):
    project = Article.query.filter(Article.article_type == 3, Article.index == True, Article.is_delete == False).order_by(Article.upload_time.desc()).limit(6)
    article = Article.query.filter(Article.article_type == 2, Article.index == True, Article.is_delete == False).order_by(Article.upload_time.desc()).limit(6)
    projectlist = []
    articlelist = []
    for i in project:
        projectlist.append(Serialize(i, obj='obj', dataprocessing='getarticlelist', notreturn=['content']))

    for s in article:
        articlelist.append(Serialize(s, obj='obj', dataprocessing='getarticlelist', notreturn=['content']))

    return 200, '', {
        'project':projectlist,
        'article':articlelist
    }