from app.article import article, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenAuthPost

# 获取文章
@article.route('/query-article', methods=["POST"])
@requestPOST
def query_article(request):
    '''
        获取文章
        id
    '''
    c,m,d = views.query_article(request.json)
    return ReturnRequest(c,m,d)

# 获取列表
@article.route('/query-list', methods=["POST"])
@requestPOST
def query_article_list(request):
    '''
        获取列表
        article_type

        if article_type == 1:
            content_type 1 设计， 2 视频
    '''
    c,m,d = views.query_article_list(request.json)
    return ReturnRequest(c,m,d)

# 发表文章
@article.route('/upload', methods=["POST"])
@TokenAuthPost(user_group=[1])
def upload_article(request):
    c,m,d = views.upload_article(request.json)
    return ReturnRequest(c,m,d)