from app.article import article, views
from app.Common import ReturnRequest
from app.Middleware import requestGET, UserTokenAuthPost

# 获取文章
@article.route('/query-article', methods=["GET"])
@requestGET
def query_article(request):
    c,m,d = views.query_article(request)
    return ReturnRequest(c,m,d)

# 获取列表
@article.route('/query-list', methods=["GET"])
@requestGET
def query_article_list(request):
    c,m,d = views.query_article_list(request)
    return ReturnRequest(c,m,d)

# 发表文章
@article.route('/upload', methods=["POST"])
@UserTokenAuthPost
def upload_article(request):
    c,m,d = views.upload_article(request)
    return ReturnRequest(c,m,d)