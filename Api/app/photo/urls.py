from app.photo import photo, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, TokenAuthPost

@photo.route('/add', methods=["POST"])
@TokenAuthPost(user_group=[1])
def photo_add(request):
    '''photo_add

        Param:
            id 文章id

        ReturnCode:

        ReturnJson:
    '''
    c,m,d = views.photo_add(request.json)
    return ReturnRequest(c,m,d)

@photo.route('/list', methods=["POST"])
@requestPOST
def photo_list(request):
    '''photo_list

        Param:
            id 文章id

        ReturnCode:

        ReturnJson:
    '''
    c,m,d = views.photo_list(request.json)
    return ReturnRequest(c,m,d)

@photo.route('/change', methods=["POST"])
@TokenAuthPost(user_group=[1])
def photo_change(request):
    '''photo_list

        Param:
            id 文章id

        ReturnCode:

        ReturnJson:
    '''
    c,m,d = views.photo_change(request.json)
    return ReturnRequest(c,m,d)