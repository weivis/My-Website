from app.Extensions import db
from app.Kit import GetRequestJsonData
from app import ReturnCode
from datetime import datetime

def home(request):
    return 200, 'ok', ''