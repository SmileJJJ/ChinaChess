# import gevent
# from gevent import monkey
# monkey.patch_all()
import os,sys
import time
# import random
#多进程TCP并发
from threading import Thread
from socketserver import *
from Chess_MySql import *

chat_message = ''
interface_rank = 1

online_player_list = list()

online_account_list_1 = list()
online_account_list_2 = list()
online_account_list_3 = list()

def login(chess_db,data_list):
    global online_player_list
    name = data_list[1]
    passwd = chess_db.select_email(name)
    if not passwd:
        return 3    #账号不存在
    elif data_list[2] == passwd[1]:
        if passwd[0] in online_player_list:
            return 4 #账号已在线
        return passwd[0]    #密码正确
    else:
        return 2    #密码错误

def register(chess_db,data_list):
    name = data_list[1]
    passwd = data_list[2]
    result = chess_db.select(name)
    if result == 0:
        consequence = chess_db.insert([name,passwd])
        if consequence == 1:
            return True 
        else:
            return False 
    else:
        return False        #账号已存在

def interface_message():
    global chat_message
    global interface_rank
    global online_account_list_2
    while True:
        for sock in online_account_list_2:
            try:
                tables_message = 'T'
                for i in tables.keys():
                    table_mes = str(i) + ' '
                    for j in tables_name[i]:
                        table_mes += j     
                        table_mes += ' '
                    table_mes += '#*#'
                    tables_message += table_mes
                tables_message += str(len(online_account_list_2) + len(online_account_list_3))
                tables_message += '#*#'
                tables_message += chat_message
                # print(tables_message)
                sock.send(tables_message.encode())     
            except OSError:
                break
        chat_message = ''
        time.sleep(0.5) 

def enter_into_rank3(sock,table_num,player_name): 
    interface_rank = 3              
    time.sleep(0.2)
    sock.send(b'OK') 
    print(tables_name)
    print(tables)
    time.sleep(1.5)
    if sock == tables[table_num][0]:    #一号玩家的套接字
        sock.send(b'one')
        print('welecome player1')
        try:
            while True:
                data = sock.recv(4096)
                if data.decode()[0] == 'C':
                    for i in tables[table_num]:
                        i.send(data)
                    continue
                elif (not data) or data == b'quit':
                    try:
                        tables[table_num][1].send(b'lift')
                    except (AttributeError,IndexError):
                        pass 
                    tables[table_num]=[]       
                    tables_name[table_num]=[]
                    break                  
                tables[table_num][1].send(data)
        except Exception:
            try:
                tables[table_num][1].send(b'lift')
            except (AttributeError,IndexError):
                pass 
            tables[table_num]=[]           
            tables_name[table_num]=[]
            online_player_list.remove(player_name)
            online_account_list_3.remove(sock)
            print('paly1 lost connection')
            sys.exit(0)

    elif sock == tables[table_num][1]:  #二号玩家的套接字
        sock.send(b'two')
        print('welecome player2')
        time.sleep(2)
        #通知游戏双方开始游戏
        tables[table_num][0].send(b'ok')
        tables[table_num][1].send(b'ok')
        try:
            while True:
                data = sock.recv(4096)
                if data.decode()[0] == 'C':
                    for i in tables[table_num]:
                        i.send(data)
                    continue
                elif (not data) or data == b'quit':
                    try:
                        tables[table_num][0].send(b'lift')
                    except (AttributeError,IndexError):
                        pass 
                    tables[table_num]=[]           #*********test
                    tables_name[table_num]=[]
                    break
                tables[table_num][0].send(data)
        except Exception:
            try:
                tables[table_num][0].send(b'lift')
            except (AttributeError,IndexError):
                pass 
            tables[table_num]=[]           #*********test
            tables_name[table_num]=[]        
            online_player_list.remove(player_name)
            online_account_list_3.remove(sock)
            print('paly1 lost connection')
            sys.exit(0)

def enter_into_rank2(sock,player_name):
    global chat_message
    global interface_rank
    global online_account_list_2
    global online_account_list_3
    interface_rank = 2  #进入二级界面
    online_account_list_2.append(sock)
    # 大厅信息与选桌
    while True:
        try :
            # 在大厅中等待选桌信息和接收聊天信息
            print('wiat for client message')
            client_message = sock.recv(4096).decode()
            print(client_message)
            if client_message[0] == 'C':
                chat_message = client_message
            elif client_message[0] == 'T':
                table_num = client_message[1:]
                if table_num in tables.keys():
                    if len(tables[table_num]) >= 2:
                        sock.send(b'full')
                        time.sleep(0.5)
                        continue
                    tables[table_num].append(sock)     
                    tables_name[table_num].append(player_name)

                    online_account_list_2.remove(sock)
                    online_account_list_3.append(sock)
                    # 进入游戏房间
                    enter_into_rank3(sock,table_num,player_name)

                    online_account_list_3.remove(sock)
                    online_account_list_2.append(sock)

                    # tables[table_num].remove(sock)
                    # tables_name[table_num].remove(player_name)
                else:
                    sock.send(b'ERROR')
                    time.sleep(0.5)
            elif client_message == 'quit_to_1':
                interface_rank = 1
                online_account_list_2.remove(sock)
                break
        except (BrokenPipeError,ConnectionResetError):
            online_player_list.remove(player_name)
            online_account_list_2.remove(sock)
            sys.exit(0)

class Server(ThreadingTCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        global chat_message
        global interface_rank
        global online_player_list
        print('connect from ',self.request.getpeername())
        self.request.send(str(len(online_account_list_2) + len(online_account_list_3)).encode())
        while True:
            #登录注册
            while True:
                try :
                    print('wait for load')
                    data = self.request.recv(4096).decode()
                    if not data:
                        continue
                    print(data)
                    data_list = data.split(' ')
                    # player_name = data_list[1]
                    if data_list[0] == 'L':
                        result = login(chess_db,data_list)
                        if result == 2:
                            self.request.send(b'PASSERROR')
                        elif result == 3:
                            self.request.send(b'NOCOUNT')
                        elif result == 4:
                            self.request.send(b'ONLI')
                        else:
                            msg = 'LOK' + result
                            self.request.send(msg.encode())
                            player_name = result
                            time.sleep(1)
                            online_player_list.append(player_name)
                            # 进入游戏大厅（二级界面）
                            enter_into_rank2(self.request,player_name)
                            online_player_list.remove(player_name) 
                except (BrokenPipeError,ConnectionResetError):
                    sys.exit(0)
            
def main():
    #生成服务器对象
    TCPServer.allow_reuse_address = True
    ThreadingMixIn.daemon_threads = True
    server = Server(('0.0.0.0',8999),Handler)
    #启动服务器
    server.serve_forever()

if __name__ == '__main__':
    chess_db = Chess_sql('root','123456','Chess_sql','chess2')
    chess_db.open()
    tables_name = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[]}
    tables = {'1':[],'2':[],'3':[],'4':[],'5':[],'6':[]}

    # 开启群发线程
    app = Thread(target = interface_message)
    app.setDaemon = True
    app.start()

    try:
        main()
    except KeyboardInterrupt:
        print('服务器退出')
        sys.exit(0)
    except Exception:
        print('服务器发生未知错误')
        sys.exit(0)