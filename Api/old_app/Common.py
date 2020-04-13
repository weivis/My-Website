from flask import jsonify

def ReturnRequest(code, msg, data):
    '''
        统一返回请求的处理结果
    '''
    if not msg:
        msg = 'OK'
    jso = {'code':code, 'msg': msg,'data': data}
    print('Return : ' + str(code) + ' => ' + str(jso))
    return jsonify(jso)