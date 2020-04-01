from app.opus import opus, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, requestGET

# article
@opus.route('/', methods=["POST","GET"])
@requestGET
def home(request):
    c,m,d = views.home(request)
    return ReturnRequest(c,m,d)