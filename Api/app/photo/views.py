from app.Extensions import db
from app.ReturnCode import ReturnCode
from datetime import datetime
from app.ModelSerialize import Serialize, SerializeQuerySet
from app.Models.db_Account import Account
from app.Models.db_Photo import Photo
from app.Config import SERVER_STATICLOADURL

def photo_add(request):
    link = request.get('link', None)
    title = request.get('title', None)

    if not link:
        return 201, '图片地址不存在', {}

    add = Photo()
    add.sort = 0
    add.link = link
    add.status = 1

    db.session.add(add)
    try:
        db.session.commit()
        return ReturnCode.ok, '成功', {}

    except:
        db.session().rollback()
        return ReturnCode.server_error, '系统出错', ''

def photo_list(request):
    querys = Photo.query.filter().order_by(Photo.sort.desc())
    return 200, '', [{
        'id':i.id,
        'sort':i.sort,
        'link':SERVER_STATICLOADURL + i.link
    }for i in querys]

def photo_change(request):
    '''
        1 = 修改权重
        2 = 删除
    '''
    id = request.get('id', None)
    change_type = request.get('change_type', None)
    sort = request.get('sort', None)
    if not id:
        return 201, 'id不能为空', {}

    if not change_type:
        return 202, '类型不能为空', {}

    if int(change_type) == 2:
        if not sort:
            return 203, '权重不能为空', {}

    obj = Photo.query.filter(Photo.id == id).first()
    
    if int(change_type) == 2:
        obj.sort = sort

    if int(change_type) == 1:
        db.session.delete(obj)

    try:
        db.session.commit()
        return ReturnCode.ok, '成功', {}

    except:
        db.session().rollback()
        return ReturnCode.server_error, '系统出错', ''
    
    

    