#!/usr/bin/env python
# -*- coding: utf-8 -*-        
# @Time    : 2019/10/5 20:35   
# @Author  : Eric Wang         
# @File    : interfaceTestPost.py        

import flask,json

server = flask.Flask(__name__)

def my_db(sql):
    import pymysql
    coon = pymysql.connect(host='localhost',
                           user='root',
                           passwd = 'root',
                           port = 3306,
                           db = 'test')
                           # charset = 'utf-8' 会报错。
    cur = coon.cursor() # 新建游标
    cur.execute(sql)

    if sql.strip()[:6].upper() == 'SELECT':
        res = cur.fetchall()
    else:
        coon.commit()
        res = 'ok'
    cur.close()
    coon.close()
    return res


@server.route('/reg', methods=['post'])
def reg():
    username = flask.request.values.get('username')
    passwd = flask.request.values.get('passwd')

    if username and passwd:
        sql = "select * from my_user where username = '%s'; " % username
        if my_db(sql):
            res = {'msg':'用户已经存在',
                   'msg_code':'2001'}
        else:
            insert_sql = "insert into my_user(username, passwd, is_admin) values('%s','%s',0);"%(username, passwd)
            my_db(insert_sql)
            res = {'msg':'注册成功',
                   'msg_code':0000}
    else:
        res = {'msg':'必填字段未填，请查看接口文档！', 'msg_code':1001}

    return json.dumps(res, ensure_ascii=False)

server.run(port=8888,debug=True,host='0.0.0.0')
