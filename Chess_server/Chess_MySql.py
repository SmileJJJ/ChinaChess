from pymysql import *

'''
chess1  
    int     name    passwd
'''

class Chess_sql:

    def __init__(self,user,passwd,dbname,table,
                 host = 'localhost',
                 port = 3306,
                 charset = 'utf8'
                 ):
        self.user = user
        self.passwd = passwd
        self.db = dbname
        self.table = table
        self.host = host
        self.port = port
        self.charset = charset

    def open(self):
        self.conn = connect(user = self.user,
                            passwd = self.passwd,
                            db = self.db,
                            host = self.host,
                            port = self.port,
                            charset = self.charset
                            )
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def perform(self,sql,par = []):
        try:
            # print(sql)
            # print(par)
            self.cur.execute(sql,par)
            self.conn.commit()
            return 1
        except Exception as error:
            self.conn.rollback()
            print('SQL操作错误',error)
            return 0 

    def insert(self,par = []):
        sql = 'insert into ' + self.table + ' values(null,%s,%s,%s)'
        result = self.perform(sql,par)
        return result

    def select_name(self,name):
        sql = 'select * from ' + self.table + ' where name = %s'
        par = [name]
        result = self.perform(sql,par)
        r = self.cur.fetchone()
        # print(r)
        if r == None:
            return 0
        else:
            return 1

    def select_email(self,email):
        sql = 'select * from ' + self.table + ' where email = %s'
        par = [email]
        result = self.perform(sql,par)
        r = self.cur.fetchone()
        # print(r)
        if r == None:
            return 0
        else:
            return (r[2],r[3])
