from app.index import index, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenAuthPost

@index.route('/more_article/list', methods=["POST"])
@requestPOST
def list_more_article(request):
    '''更多文章-获取
        Param:
            {}
        ReturnCode:
            200 成功
        ReturnJson:
    '''
    c, m, d = views.list_more_article(request.json)
    return ReturnRequest(c, m, d)

@index.route('/more_article/add', methods=["POST"])
@TokenAuthPost(user_group=[1])
def add_more_article(request):
    '''更多文章-添加
        Param:
            articleid   文章id
            title       标题
            cover       封面
            introduce   介绍
            link        地址

        ReturnCode:
            200 成功
            201 标题不能为空
            202 封面不能为空
            203 介绍不能为空
            204 链接地址不能为空
            502 系统出错
        ReturnJson:
    '''
    c, m, d = views.add_more_article(request.json)
    return ReturnRequest(c, m, d)

@index.route('/more_article/change', methods=["POST"])
@TokenAuthPost(user_group=[1])
def change_more_article(request):
    '''更多文章-变更
        Param:
            id 需要修改的文章id
            change_type 1生效 2隐藏 3删除 4排序
            sort 排序

        ReturnCode:
            200 成功
            201 操作类型不能为空
            202 被操作的推荐地址不存在
            203 sort排序不能为空
            502 系统出错
            
        ReturnJson:
    '''
    c, m, d = views.change_more_article(request.json)
    return ReturnRequest(c, m, d)