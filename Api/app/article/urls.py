from app.article import article, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenAuthPost

# 获取文章
@article.route('/query-article', methods=["POST"])
@requestPOST
def query_article(request):
    '''获取单篇文章

        Param:
            id 文章id

        ReturnCode:
            200 成功
            400 文章不存在或参数有误

        ReturnJson:
            {
                "code": 200, 
                "data": {
                    "article_type": 2, 
                    "content": "<p>\u6d4b\u8bd5\u6587\u7ae02222222</p>", 
                    "content_type": 0, 
                    "cover": "http://127.0.0.1:8080/static/article/cover/20200423074048225.jpg", 
                    "id": 6, 
                    "introduce": "\u6d4b\u8bd5\u6587\u7ae02222222", 
                    "status": 0, 
                    "title": "\u6d4b\u8bd5\u6587\u7ae02", 
                    "upload_time": "2020-04-23 07:41:03", 
                    "upload_userid": 1
                }, 
                "msg": "OK"
            }
    '''
    c,m,d = views.query_article(request.json)
    return ReturnRequest(c,m,d)

# 获取列表
@article.route('/query-list', methods=["POST"])
@requestPOST
def query_article_list(request):
    '''获取文章列表

        Param:
            article_type 获取的文章类型
                1 作品
                    content_type
                        1 设计
                        2 视频
                2 文章
                3 项目

        ReturnCode:
            200 成功
            400 文章不存在或参数有误
                获取的文章类型缺乏

        ReturnJson:
            {
            "code": 200, 
            "data": {
                "dataPges": 1, 
                "list": [
                    {
                        "article_type": 1, 
                        "content_type": 1, 
                        "cover": "http://127.0.0.1:8080/static/article/cover/20200414031426497.jpg", 
                        "id": 4, 
                        "introduce": "\u5927\u8bf7\u6c42\u4f53\u6d4b\u8bd5", 
                        "status": 0, 
                        "title": "\u5927\u8bf7\u6c42\u4f53\u6d4b\u8bd5", 
                        "upload_time": "2020-04-14 03:15:14", 
                        "upload_userid": 1
                    }
                ], 
                "nowPage": 1, 
                "queryCount": 4
            }, 
            "msg": "OK"
            }
    '''
    c,m,d = views.query_article_list(request.json)
    return ReturnRequest(c,m,d)

# 发表文章
@article.route('/upload', methods=["POST"])
@TokenAuthPost(user_group=[1])
def upload_article(request):
    '''发表文章

        Param:
            title 文章标题
            introduce 介绍
            content 内容
            article_type 发布类型
                1 作品
                2 文章
                3 项目
            content_type 内容类型
            cover 封面
            content_type 内容类型 # article_type为1时 content_type为必填项
                1 设计
                2 视频

        ReturnCode:
            200 成功
            400 标题不能为空
                介绍不能为空
                内容不能为空
                发布类型不能为空
                封面不能为空
                作品类型不能为空

        ReturnJson:
    '''
    c,m,d = views.upload_article(request.json)
    return ReturnRequest(c,m,d)

# 发表文章
@article.route('/change', methods=["POST"])
@TokenAuthPost(user_group=[1])
def change_article(request):
    '''更改文章状态

        Param:
            id 文章id
            to 修改的状态
                1 上架
                2 下架
                3 删除
                4 恢复
                5 首页展示
                6 取消首页展示
        ReturnCode:
            200 成功
            201 文章id不能为空
            202 文章不存在
            203 修改的状态不存在
            502 系统出错
        ReturnJson:
    '''
    c,m,d = views.change_article(request.json)
    return ReturnRequest(c,m,d)