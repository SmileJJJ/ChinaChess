import os
import sys
import time
from multiprocessing import Pipe, Process
from socket import *
from threading import Thread

import global_var
from first_interface import *
from interface_function import *
from web_communicate import *


def app_order(chess_sock):
    while True:
        # 注册和登录 (一级界面)
        if global_var.interface_rank == 1:
            login_handle(chess_sock) 

        # 大厅信息 (二级界面)
        if global_var.interface_rank == 2:
            lobby_handle(chess_sock)  
    
        #游戏内部提示和聊天 (三级界面)
        if global_var.interface_rank == 3:
            room_handle(chess_sock)  


def main():

    chess_sock  =  socket()

    #开线程管理网络通信
    web_thread = Thread(target = web_communitcation_receive,args = (chess_sock,))
    web_thread.daemon = True
    web_thread.start()

    # 开线程管理软件
    app_thread = Thread(target = app_order,args = (chess_sock,))
    app_thread.daemon = True
    app_thread.start()

    # 启动程序，进入一级登录界面
    first_interface_main()
    print('程序结束')
        
if __name__ == '__main__':
    main()
