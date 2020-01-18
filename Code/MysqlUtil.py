#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.18
author: wangxiaojie
'''

import MySQLdb

__all__ = [
    "MySqlUtil", 
    ]
    
class MySqlUtil(object):
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __del__(self):
        self.close()

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
                self.cursor = None
            if self.connection:
                self.connection.close()
                self.connection = None
        except Exception as e:
            print("MySQL close error %s", e.message)

    def connect(self, host, user, password, db, port=3306, charset='utf8'):
        try:
            self.close()
            self.connection = MySQLdb.connect(host=host, user=user, passwd=password, db=db, port=port, charset=charset)
            self.cursor = self.connection.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            return True
        except Exception as e:
            print("MySQL connect error %s", e.message)
            return False

    def execute(self, sql):
        if self.cursor == None:
            errorMsg = "execute '%s' whith a None cursor, please make sure your MysqlServer is working and please call connect first" % sql
            print(errorMsg)
            return errorMsg
        result = ""
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            self.connection.commit()
        except Exception as e:
            print("MySQL -- %s -- Execute Error %s", sql, e.message)
            return e.message
        return result

if __name__ == "__main__":
    mysqlUtil = MySqlUtil()
    mysqlUtil.connect("localhost", "root", "123456", "test", 3306)
    databases = mysqlUtil.execute("show databases;")
    print(databases)
    
