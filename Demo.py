#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.18
author: wangxiaojie
'''

import os, sys

codePath = os.path.abspath(os.path.join(__file__, "..", "Code"))
if os.path.exists(codePath):
    sys.path.append(codePath)
from MysqlUtil import MySqlUtil

if __name__ == "__main__":
    mysqlUtil = MySqlUtil()
    mysqlUtil.connect("localhost", "root", "123456", "test", 3306)
    databases = mysqlUtil.execute("show databases;")
    print(databases)