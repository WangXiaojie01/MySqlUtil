#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.03.18
author: wangxiaojie
'''

import os, sys
import logging
import pymysql

__all__ = [
    "MySqlUtil", 
    "mysqlLogger"
    ]

mysqlLogger = logging.Logger("MySqlUtil")
    
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
            mysqlLogger.error("MySQL close error, error is %s", e)

    def connect(self, host, user, password, db, port=3306, charset='utf8'):
        try:
            self.close()
            self.connection = pymysql.connect(host=host, user=user, passwd=password, db=db, port=port, charset=charset)
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            mysqlLogger.error("MySQL connect error, error is %s", e)
            return False

    def execute(self, sql):
        if self.cursor == None:
            errorMsg = "execute '%s' whith a None cursor, please make sure your MysqlServer is working and please call connect first" % sql
            mysqlLogger.error(errorMsg)
            return False, 0, errorMsg
        result = ""
        try:
            resultNum = self.cursor.execute(sql)
            resultRow = self.cursor.fetchall()
            self.connection.commit()
        except Exception as e:
            mysqlLogger.error("MySQL execute  '%s' error, error is %s", sql, e)
            return False, 0, e
        return True, resultNum, resultRow
        

if __name__ == "__main__":
    print("test")
    
    mysqlUtil = MySqlUtil()
    mysqlUtil.connect("localhost", "root", "123456", "test", 3306)
    result = mysqlUtil.execute("show databases;")
    print(result)
    
    
