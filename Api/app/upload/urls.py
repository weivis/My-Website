from app.upload import upload, views
from app.Common import ReturnRequest
from app.Middleware import requestPOST

# 上传文件
@upload.route('/', methods=["POST"])
@requestPOST
def upload_file(request):
    c,m,d = views.upload_file(request)
    return ReturnRequest(c,m,d)