"""The UseDatabase context manager for working with MySQL/MariaDB.

For more information, see Chapters 7, 8, 9, and 11 of the 2nd edition of
Head First Python.

Simple example usage:

    from DBcm import UseDatabase, SQLError

    config = { 'host': '127.0.0.1',
               'user': 'myUserid',
               'password': 'myPassword',
               'database': 'myDB' }

    with UseDatabase(config) as cursor:
        _SQL = "select * from log"
        cursor.execute(_SQL)
        data = cursor.fetchall()

Enjoy, and have fun.  (Sorry: Python 3 only, due to type hints and new syntax).
"""

##############################################################################
# Context manager for connecting/disconnecting to a database.
##############################################################################

import mysql.connector

class ConnectionError(Exception):  # 将这个定制异常定义为一个继承 "exception" 的空类
    """Raised if the backend-database cannot be connected to."""
    pass


class CredentialsError(Exception):
    """Raised if the database is up, but there's a login issue."""
    pass


class SQLError(Exception):
    """Raised if the query caused problems."""
    pass



class UseDatabase:
    def __init__(self, config: dict): # Dunder "init" 接收一个 config 字典
        """Add the database configuration parameters to the object.

        This class expects a single dictionary argument which needs to assign
        the appropriate values to (at least) the following keys:

            host - the IP address of the host running MySQL/MariaDB.
            user - the MySQL/MariaDB username to use.
            password - the user's password.
            database - the name of the database to use.

        For more options, refer to the mysql-connector-python documentation.
        """
        self.configuration = config # "config" 参数的值赋给一个名为 "configuration" 的属性。

    def __enter__(self) -> 'cursor':
        """Connect to database and create a DB cursor.

        Return the database cursor to the context manager.
        """
        try:
            self.conn = mysql.connector.connect(**self.configuration) # 不是使用 dbconfig
            self.cursor = self.conn.cursor()
            return self.cursor # 返回游标
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err) from err
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err) from err

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Destroy the cursor as well as the connection (after committing).
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        elif exc_type:
            raise exc_type(exc_value)
