#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.03.19
author: wangxiaojie
'''

import os, sys

codePath = os.path.abspath(os.path.join(__file__, "..", "Code"))
if os.path.exists(codePath):
    sys.path.append(codePath)
from MysqlUtil import MySqlUtil

if __name__ == "__main__":
    mysqlUtil = MySqlUtil() #实例化一个对象实例
    mysqlUtil.connect("localhost", "root", "123456", "test", 3306) #连接数据库
    result = mysqlUtil.execute("show databases;") #执行sql语句
    print(result)