# MySqlUtil
一个封装了mysql连接的工具类

####使用
1. 先将MysqlUtil导入你的源码
  `from MysqlUtil import MySqlUtil`

2. 先实例化一个MysqlUtil对象
  `mysqlUtil = MySqlUtil()`

3. 连接数据库
  `mysqlUtil.connect("localhost", "root", "123456", "test", 3306)`

4. 执行要执行的sql语句
  `databases = mysqlUtil.execute("show databases;")`