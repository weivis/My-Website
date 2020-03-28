# Flask-Cli

## 自己常用的Flask项目架构快速搭建脚手架

## [ 动态 ]
> 2020/3/23.3独立化工具包

> 2020/3/23.3独立化SetCache模块

> 2020/3/23发布

## [ 生态 ]
> 自己写的常用序列化器 https://github.com/weivis/Flask-SQLAlchemySerialize

> 自己写的快速持续化储存 https://github.com/weivis/Flask-SetCache

> 自己常用的工具包 https://github.com/weivis/Flask-Kit

### 目录结构

    |-doc 文档目录
    |-app
        |-page1 示范蓝图模块1
        |-upload 上传模块
        |-static 静态目录

    Common 全局通用方法
    Blueprint 路由蓝图模块
    Middleware 请求中间件
    Config 全局配置模块
    ReturnCode 统一返回码定义
    Extensinons 框架统一引用库启动载入地址
    Models 数据库类
    manager 入口文件
    Kit 工具包

### 工具包说明
    工具包内是我个人常用的一些方法
    cii内默认自带0.1版本的Flask-Kit 需要更新可以在
    https://github.com/weivis/Flask-Kit 内下载最新版

### 使用Flask-Login的时候需要去掉Extensions内的注释解开封印
    Extensions.py
        # from flask_login import LoginManager
        # login_manager = LoginManager()

        #指定登录的端点
        # login_manager.login_view = 'auth.auth'

        #需要登录时的提示信息
        # login_manager.login_message = '需要先登录'
        # 设置session保护级别
        # None：禁用session保护
        # 'basic'：基本的保护，默认选项
        # 'strong'：最严格的保护，一旦用户登录信息改变，立即退出登录

        # login_manager.session_protection = 'strong'

    __init__ .py
        from app import login_manager
        login_manager

### 更改统一返回结构
    默认
    {
        "code": 业务码,
        "data": 数据,
        "msg": "消息"
    }
    在Common内的ReturnRequest下修改

### 上传模块使用方法

    Config内设置
    UPLOAD_KEY = ['head'] 允许上传使用的key值
    UPLOAD_KEY_FLOAD = {'head':'image/head'} key值对应的储存目录

### 安装基础依赖
    pip install -r requirements.txt

### 启动方法
    python manager.py runserver

    打开 http://127.0.0.1/ 看到
    {
        "code": 200, 
        "data": "", 
        "msg": "ok"
    }
    代表部署成功

### 创建数据库和迁移数据库

    python manager.py db init
    python manager.py db migrate
    python manager.py db upgrade
