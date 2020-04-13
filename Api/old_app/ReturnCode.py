class ReturnCode:
    # 参数错误
    paramete_error = 400

    # 业务错误
    def_error = 402

    # 找不到资源
    not_found_error = 404

    # 服务器错误
    server_error = 502

    # 参数格式有误
    paramete_type_error = 401

    # 成功
    ok = 200

class SystemCode:
    # Token失效时返回
    TokenInvalid = 10000

    # 没登陆的时候返回错误码
    NotLogin = 10086

    # 黑名单用户返回值
    BlacklistUserLogin = 0000

    # 错误请求时返回
    ErrorRequestMethod = 1000