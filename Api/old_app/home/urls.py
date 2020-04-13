from app.home import home, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, requestGET

# home
@home.route('/', methods=["POST","GET"])
@requestGET
def home(request):
    c,m,d = views.home(request)
    return ReturnRequest(c,m,d)