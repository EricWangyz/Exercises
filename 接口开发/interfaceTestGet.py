#!/usr/bin/env python          
# -*- coding: utf-8 -*-        
# @Time    : 2019/10/5 20:26   
# @Author  : Eric Wang         
# @File    : interfaceTestGet.py

import flask, json

server = flask.Flask(__name__) # 把当前这个python文件，当做一个服务，__name__代表当前这个python文件

@server.route("/index", methods = ['get']) # 定义接口路径，以及接口请求方法
def index():
    res = {'msg':'这是我开发的第一个接口',
           'msg_code':100}
    return json.dumps(res, ensure_ascii=False)

server.run(port=8888, debug=True, host = '0.0.0.0') # 启动服务
