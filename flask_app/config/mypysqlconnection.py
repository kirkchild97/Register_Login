import pymysql.cursors

class mySQLConnection:
    def __init__(self, db) -> None:
        connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'root',
            db = db,
            charset = 'utf8mb4',
            cursorclass = pymysql.cursors.DictCursor,
            autocommit = True
        )
        self.connection = connection

    def query_db(self, query : str, data : dict = None):
