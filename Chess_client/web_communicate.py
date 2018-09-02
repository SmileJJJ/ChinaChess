import os,sys,time
import global_var
from threading import Thread
from interface_function import *

def server_message_handle(server_message):
    if server_message[0:3] == 'LOK':
        global_var.login_count = server_message[3:]
        print('登录成功')
        global_var.login_status= 1
    elif server_message == 'ROK':
        print('注册成功')
    elif server_message == 'PASSERROR':
        global_var.login_status= 2
        print('密码错误')
    elif server_message == 'NOCOUNT':
        global_var.login_status= 3
        print('账号不存在')
    elif server_message == 'ONLI':
        global_var.login_status= 4
        print('账号以在线')
    elif server_message == 'RERROR':
        print('账号已存在')
    elif server_message[0] == 'T':
        global_var.lobby_list = server_message[1:].split('#*#')
        global_var.online_num = int(global_var.lobby_list[6])
        if global_var.lobby_list[-1]:
            global_var.tset_num2 += 1
            # print('show message from web count------>',global_var.tset_num2)
            global_var.recive_chat_message.append(global_var.lobby_list[-1][1:])
    elif server_message == 'full':
        global_var.get_in_table = 1
        print('该房间人数已满')
    elif server_message == 'OK':
        global_var.get_in_table = 2
    elif server_message == 'one' and global_var.board != None:
        global_var.board.home_color = 'RED'
        global_var.room_recive_chat_message.append('system : 联网成功 \n 等待二号玩家...')
    elif server_message == 'two'and global_var.board != None:
        global_var.board.home_color = 'BLACK'
        global_var.room_recive_chat_message.append('system : 联网成功')
    elif server_message == 'ok':
        #游戏开始后，根据我方颜色重置棋盘
        global_var.room_recive_chat_message.append('system : 玩家二进入房间,1秒后游戏开始...')
        global_var.board.game_reade = True
        time.sleep(1)
        global_var.board.load_chess()
        global_var.board_status = 1
        global_var.room_recive_chat_message.append('system : 游戏开始')
    elif server_message == 'lift':
        global_var.web_message = None
        global_var.board_status = 0
        global_var.room_recive_chat_message.append('system : 对方离开了游戏，游戏结束')
        global_var.room_recive_chat_message.append('system : 您获得了游戏胜利...')
        global_var.room_recive_chat_message.append('system : 您以自动退出房间...')
    elif server_message[0] == 'I':
        global_var.web_chess_action_message = server_message[1:]
    elif server_message[0] == 'C':
        global_var.room_recive_chat_message.append(server_message[1:])

# 网络通信_接收端
def web_communitcation_receive(chess_sock):
    try:
        chess_sock.connect((global_var.IP , global_var.PORT))  # 发起连接请求   
        global_var.online_num = int(chess_sock.recv(256).decode())
        global_var.connect_status = 1 
        while True:
            try:
                server_message = chess_sock.recv(4096).decode()   
                if not server_message:
                    continue
                # print(server_message)
                server_message_handle(server_message)
            except Exception as e:
                print(e)
                print('与服务器断开链接!')
                sys.exit(0)     
    except Exception as e:
        print(e)
        print('服务器未响应!')
        sys.exit(0)
