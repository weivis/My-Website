from app.auth import auth, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST, requestGET, UserTokenAuthPost

@auth.route('/register', methods=["POST"])
@requestPOST
def register(request):
    c,m,d = views.register(request)
    return ReturnRequest(c,m,d)

@auth.route('/login', methods=["POST"])
@requestPOST
def login(request):
    c,m,d = views.login(request)
    return ReturnRequest(c,m,d)

@auth.route('/Logout', methods=["POST"])
@UserTokenAuthPost
def Logout(request):
    c,m,d = views.Logout(request)
    return ReturnRequest(c,m,d)