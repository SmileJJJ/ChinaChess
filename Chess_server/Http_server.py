from socket import *
from threading import Thread
from emailsend import *
import re
import random
from Chess_MySql import *


HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)

#设置静态网页文件夹
STATIC_DIR = './static'

class HTTPServer(object):
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) 
        self.chess_db = Chess_sql('root','123456','Chess_sql','chess2')
        self.chess_db.open()

    def bind(self,addr):
        self.ip =  addr[0]
        self.port = addr[1]
        self.sockfd.bind(addr)

    def serve_forever(self):
        self.sockfd.listen(10)
        print('listen the port %s'%self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print('connect from ',addr)
            handle_client = Thread(target=self.handle_client,args=(connfd,))
            handle_client.setDaemon(True)
            handle_client.start()

    def handle_client(self,connfd):
        request = connfd.recv(4096)
        requests = request.splitlines()
        request_line = requests[0].decode('utf-8')
        method,path = re.findall(r'^(\w+)\s+(/\S*)',request_line)[0]

        if path == '/' or path[-5:] == '.html':
            response = self.get_html(path)
            connfd.send(response.encode())
            connfd.close()

    def get_html(self,path):
        if path == '/':
            get_file = STATIC_DIR + '/index.html'
        else:
            get_file = STATIC_DIR + path
        try:
            fd = open(get_file,'r')
        except IOError:
            responseHeaders = 'HTTP/1.1 404 not found\r\n'
            responseHeaders += '\r\n'
            responseBody = '===sorry page not found==='
        else:
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders += '\r\n'
            responseBody = fd.read()
            # print(responseBody)
        finally:
            response = responseHeaders + responseBody
            self.sql_operate('22222222@qq.com','徐涛','123456')
            return response

    # self.sql_operate('1111111@qq.com','shenjian','123456')
    def sql_operate(self,email_acount,name,password):
        if self.chess_db.select_email(email_acount):
            print('帐号已存在')
            return 0 #帐号已存在
        if self.chess_db.select_name(name):
            print('昵称已存在')
            return 1 #昵称已存在
        self.chess_db.insert([email_acount,name,password])
        print('注册成功')
        return 2 #注册成功


    def send_check_random(self,to_addr,smtp_server,check_pwsd):
        email_send(to_addr,smtp_server,check_pwsd)



if __name__ == '__main__':
    http = HTTPServer()
    http.bind(ADDR)
    http.serve_forever()
