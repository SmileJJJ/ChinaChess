# ******************************
# 三个界面的数据服务函数
# ******************************

import global_var
import sys
import pygame
import pygame.locals as pygl
from Board_Obj import *

# 注册和登录 (一级界面)
def login_handle(chess_sock):
    while global_var.interface_rank==1:
        if global_var.login_message:
            try:
                message = global_var.login_message[0]
                count = global_var.login_message[1]
                pswd = global_var.login_message[2]
                # global_var.login_count = count
                push_message = message + ' ' + count + ' ' + pswd
                global_var.login_message = []
                chess_sock.send(push_message.encode())
            except Exception:
                print('服务器未响应!')
                sys.exit(0)

# 大厅信息(二级界面)
def lobby_handle(chess_sock):
    while global_var.interface_rank == 2:
        if global_var.send_chat_message:
            mes = 'C'+ global_var.login_count + ' ： ' + global_var.send_chat_message
            chess_sock.send(mes.encode())
            global_var.send_chat_message = ''
        if global_var.get_table_num != 0:
            # print('T'+str(global_var.get_table_num))
            chess_sock.send(('T'+str(global_var.get_table_num)).encode())
            global_var.get_table_num = 0
    if global_var.interface_rank == 1:
        chess_sock.send(b'quit_to_1')
        
#房间信息(三级界面)
def room_handle(chess_sock):
    pygame.init()
    image_icon = pygame.image.load('./BMP/r_jiang.bmp')
    pygame.display.set_icon(image_icon)
    global_var.board = Board()  #创建棋盘   
    global_var.room_recive_chat_message.append('system : 棋盘载入成功')
    while True:
        if global_var.room_send_chat_message:
            mes = 'C'+ global_var.login_count + ' ： ' + global_var.room_send_chat_message
            chess_sock.send(mes.encode())
            global_var.room_send_chat_message = ''
        if global_var.interface_rank == 2:
            chess_sock.send(b'quit')
            pygame.quit() 
            break
        try :
            pygame.display.set_caption('象棋游戏:{}'.format(global_var.board.home_color),)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    if event.button == 1 and global_var.board.chess_action == True:
                        crash_upload = global_var.board.sursor_move(event.pos) 
                        if crash_upload and global_var.board.game_reade:
                            message = str(crash_upload[0][0])+str(crash_upload[0][1])+ \
                                    str(crash_upload[1][0])+str(crash_upload[1][1])
                            message = 'I'+message
                            chess_sock.send(message.encode())
                            global_var.board.chess_action = False   #换边
            if not global_var.board.chess_action:  
                if global_var.web_chess_action_message:
                    x_1 = 8 - int(global_var.web_chess_action_message[0])
                    y_1 = 9 - int(global_var.web_chess_action_message[1])
                    x_2 = 8 - int(global_var.web_chess_action_message[2])
                    y_2 = 9 - int(global_var.web_chess_action_message[3])
                    L = [(x_1,y_1),(x_2,y_2)]
                    global_var.board.crash(L,'web')
                    global_var.web_chess_action_message = None
                    global_var.board.chess_action = True   #换边
            #刷新棋盘
            global_var.board.refresh()
            pygame.display.update()
            pygame.time.delay(100)
        except Exception:
            continue