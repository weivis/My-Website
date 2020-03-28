from app.page1 import page1, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, requestGET

# 关注
@page1.route('/', methods=["POST","GET"])
@requestGET
def home(request):
    c,m,d = views.home(request)
    return ReturnRequest(c,m,d)