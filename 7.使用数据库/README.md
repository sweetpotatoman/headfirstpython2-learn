## 使用数据库

---

### DB-API
> python 解释器对于处理数据库已经提供了一些支持，提供一个标准数据库API（应用编程接口）--- `DB-API`，可以用来处理基于 SQL 的数据库。所以需要一个具有数据库技术的**驱动程序**来连接 DB-API

- 定义连接属性
  - 创建一个名为 dbconfig 的字典
    ```py
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB',}
    ```
  
  - 导入数据库驱动程序
    ```py
    import mysql.connector
    ```

  - 建立与服务器的一个连接
    ```py
    conn = mysql.connector.connect(**dbconfig)
    ```
    - `connect` 调用建立连接
    - `(**dbconfig)` 传入连接属性字典
    - `**` 记法告诉 connect 函数调用一个变量提供的参数字典

  - 打开一个游标
    - 要向数据库发送 SQL 语句以及从数据库接收结果需要一个游标，可以把游标想像成是数据库中的[文件句柄]() 
      ```py
      cursor = conn.cursor()
      ```
      - 调用 cursor 方法，把所创建的游标的一个引用保存在一个变量中

  - 完成 sql 查询
    ```py
    _SQL = """show tables"""
    cursor.execute(_SQL)
    ```
    - 使用三重引号字符串是因为 sql 语句经常是多行的

    ```py
    res = cursor.fetchall()
    res
    ```
    - 通过 fetchall() 方法获取查询的所有结果，也同时赋值给 res 变量

  - 关闭游标和连接
    ```
    cursor.close()
    conn.close()
    ```
