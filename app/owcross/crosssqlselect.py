# /usr/bin/python
#coding:utf-8

__Date__ = "2016-07-22 10:45"
__Author__ = 'eyu Fanne'

import MySQLdb
import sys
reload( sys )
sys.setdefaultencoding('utf-8')

import dbinfo


def runSql(dbhost,serverid,sql):
    try:
        conn=MySQLdb.connect(host=dbhost,user=dbinfo.owdb['user'],passwd=dbinfo.owdb['password'],db='owcross',port=3306)
        cur=conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
        cur.execute(sql)
        cur_res = cur.fetchall()
        # print cur_res
        cur_res = list(cur_res)
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
        cur_res = []
        cur_res_dic = {}
        errmsg_k = "Mysql Error %d" %e.args[0]
        errmsg_v = "%s" %e.args[1]
        errmsg = "Mysql Error %d: %s" % (e.args[0], e.args[1])
        cur_res_dic[errmsg_k] = errmsg_v
        cur_res.append(cur_res_dic)
    return cur_res