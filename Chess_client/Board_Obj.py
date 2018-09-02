# ********************************************************
#·棋盘类----生成一个棋盘
#.调用棋子类，生成所有棋子--->生成棋子字典--->翻译坐标--->检测光标坐标--->生成碰撞列表
# ********************************************************
import global_var
import pygame
import pygame.locals as pygl
import os,sys
from Chess_Obj import *
from PIL import ImageGrab
import datetime

#棋盘类
class Board():  

    crash_list = [None,None]

    @staticmethod
    def coordinates_algo(coord):
        return(coord[0] * 50 + 5 ,coord[1] * 50 + 15)

    #载入棋盘：棋盘背景和游标
    def __init__(self):
        self.screen = pygame.display.set_mode((460,532)) 
        self.game_reade = False
        self.home_color = 'RED'
        self.background = []
        for root, dirs, files in os.walk('BACKGROUND'): 
            for f in files:
                path = './' + 'BACKGROUND' + '/' + f
                convert = pygame.image.load(path).convert()
                self.background.append(convert)
                global_var.skin_all += 1
        self.cursor = pygame.image.load('./BMP/curPos.bmp').convert()
        self.cursor_rect = self.cursor.get_rect()
        self.cursor.set_colorkey(0xffffff,0) 
        self.cursor_old_pos = (0,0)
        self.load_chess()
        self.reset_board()

    def load_chess(self):
        #生成32个棋子
        if self.home_color == 'BLACK':
            self.chess_action = False
            r_jiang = Chess('JIANG','RED',(4,0))
            b_jiang = Chess('JIANG','BLACK',(4,9))

            r_ju_1 = Chess('JU','RED',(0,0))
            r_ju_2 = Chess('JU','RED',(8,0))
            b_ju_1 = Chess('JU','BLACK',(0,9))
            b_ju_2 = Chess('JU','BLACK',(8,9))

            r_ma_1 = Chess('MA','RED',(1,0))
            r_ma_2 = Chess('MA','RED',(7,0))
            b_ma_1 = Chess('MA','BLACK',(1,9))
            b_ma_2 = Chess('MA','BLACK',(7,9))

            r_xiang_1 = Chess('XIANG','RED',(2,0))
            r_xiang_2 = Chess('XIANG','RED',(6,0))
            b_xiang_1 = Chess('XIANG','BLACK',(2,9))
            b_xiang_2 = Chess('XIANG','BLACK',(6,9))

            r_shi_1 = Chess('SHI','RED',(3,0))
            r_shi_2 = Chess('SHI','RED',(5,0))
            b_shi_1 = Chess('SHI','BLACK',(3,9))
            b_shi_2 = Chess('SHI','BLACK',(5,9))

            r_pao_1 = Chess('PAO','RED',(1,2))
            r_pao_2 = Chess('PAO','RED',(7,2))
            b_pao_1 = Chess('PAO','BLACK',(1,7))
            b_pao_2 = Chess('PAO','BLACK',(7,7))

            r_bing_1 = Chess('BING','RED',(0,3))
            r_bing_2 = Chess('BING','RED',(2,3))
            r_bing_3 = Chess('BING','RED',(4,3))
            r_bing_4 = Chess('BING','RED',(6,3))
            r_bing_5 = Chess('BING','RED',(8,3))
            b_bing_1 = Chess('BING','BLACK',(0,6))
            b_bing_2 = Chess('BING','BLACK',(2,6))
            b_bing_3 = Chess('BING','BLACK',(4,6))
            b_bing_4 = Chess('BING','BLACK',(6,6))
            b_bing_5 = Chess('BING','BLACK',(8,6))
        elif self.home_color == 'RED':
            self.chess_action = True
            r_jiang = Chess('JIANG','RED',(4,9))
            b_jiang = Chess('JIANG','BLACK',(4,0))

            r_ju_1 = Chess('JU','RED',(0,9))
            r_ju_2 = Chess('JU','RED',(8,9))
            b_ju_1 = Chess('JU','BLACK',(0,0))
            b_ju_2 = Chess('JU','BLACK',(8,0))

            r_ma_1 = Chess('MA','RED',(1,9))
            r_ma_2 = Chess('MA','RED',(7,9))
            b_ma_1 = Chess('MA','BLACK',(1,0))
            b_ma_2 = Chess('MA','BLACK',(7,0))

            r_xiang_1 = Chess('XIANG','RED',(2,9))
            r_xiang_2 = Chess('XIANG','RED',(6,9))
            b_xiang_1 = Chess('XIANG','BLACK',(2,0))
            b_xiang_2 = Chess('XIANG','BLACK',(6,0))

            r_shi_1 = Chess('SHI','RED',(3,9))
            r_shi_2 = Chess('SHI','RED',(5,9))
            b_shi_1 = Chess('SHI','BLACK',(3,0))
            b_shi_2 = Chess('SHI','BLACK',(5,0))

            r_pao_1 = Chess('PAO','RED',(1,7))
            r_pao_2 = Chess('PAO','RED',(7,7))
            b_pao_1 = Chess('PAO','BLACK',(1,2))
            b_pao_2 = Chess('PAO','BLACK',(7,2))

            r_bing_1 = Chess('BING','RED',(0,6))
            r_bing_2 = Chess('BING','RED',(2,6))
            r_bing_3 = Chess('BING','RED',(4,6))
            r_bing_4 = Chess('BING','RED',(6,6))
            r_bing_5 = Chess('BING','RED',(8,6))
            b_bing_1 = Chess('BING','BLACK',(0,3))
            b_bing_2 = Chess('BING','BLACK',(2,3))
            b_bing_3 = Chess('BING','BLACK',(4,3))
            b_bing_4 = Chess('BING','BLACK',(6,3))
            b_bing_5 = Chess('BING','BLACK',(8,3))
        #载入棋子库
        self.boardChess = [
                            r_jiang,b_jiang,r_ju_1,r_ju_2,b_ju_1,b_ju_2,r_ma_1,r_ma_2,b_ma_1,b_ma_2,r_xiang_1,  \
                            r_xiang_2,b_xiang_1,b_xiang_2,r_shi_1, r_shi_2,b_shi_1,b_shi_2,r_pao_1,r_pao_2,     \
                            b_pao_1,b_pao_2,r_bing_1,r_bing_2,r_bing_3,r_bing_4,r_bing_5,b_bing_1,b_bing_2,     \
                            b_bing_3,b_bing_4,b_bing_5
                          ]
        #额外记录将帅，用来对照
        self.redJiang = r_jiang
        self.blackJiang = b_jiang

    def reset_board(self):
        #载入棋盘
        self.screen.blit(self.background[0],(0,0))
        #将棋子库里的32个棋子摆上棋盘
        for chess in self.boardChess:
            self.screen.blit(chess.image,chess.image_rect)
        #初始化光标位置
        self.cursor_rect.left = Board.coordinates_algo((-2,-2))[0]
        self.cursor_rect.top = Board.coordinates_algo((-2,-2))[1]

    def sursor_move(self,pos):
        self.cursor_pos = ((pos[0]-5)//50,(pos[1]-15)//50)
        # mov_pos = (self.cursor_new_pos[0] - self.cursor_old_pos[0],\
        #            self.cursor_new_pos[1] - self.cursor_old_pos[1])
        # self.cursor_rect = self.cursor_rect.move(Board.coordinates_algo(mov_pos)[0],\
        #                                          Board.coordinates_algo(mov_pos)[1])
        # print(Board.coordinates_algo(mov_pos)[0])
        # print(Board.coordinates_algo(mov_pos)[1])
        # print(Board.coordinates_algo(self.cursor_new_pos[0] - self.cursor_old_pos[0])[0])
        # self.screen.fill((0,0,0))  
        self.cursor_rect.left = Board.coordinates_algo(self.cursor_pos)[0]
        self.cursor_rect.top = Board.coordinates_algo(self.cursor_pos)[1]
        # self.screen.blit(self.cursor,self.cursor_rect)
        # self.cursor_old_pos = self.cursor_new_pos

        if  Board.crash_list[0] is None:
            Board.crash_list[0] = self.cursor_pos
            return None
        else:
            Board.crash_list[1] = self.cursor_pos
            L = self.crash(Board.crash_list,'local')
            if L:
                return L        #返回网络同步目标
        

    def crash(self,crash_list,message_com):
        crash_member = [0,0]  #碰撞成员成分  0 为 空 ， 1 为 棋
        for chess in self.boardChess:
            if message_com == 'local':
                if chess.coordinate == crash_list[0] and chess.color == self.home_color:
                    crash_list[0] = chess
                    crash_member[0] = 1
                if chess.coordinate == crash_list[1]:
                    crash_list[1] = chess
                    crash_member[1] = 1
            elif message_com == 'web':
                if chess.coordinate == crash_list[0] and chess.color != self.home_color:
                    crash_list[0] = chess
                    crash_member[0] = 1
                if chess.coordinate == crash_list[1]:
                    crash_list[1] = chess
                    crash_member[1] = 1

        #处理光标移动的结果，只有移动棋子和撞击需要返回坐标列表
        #其他光标结果均不反回
        if crash_member == [0,0]:    #光标转移
            Board.crash_list = [None,None]
        elif crash_member == [0,1]:  #光标转移
            Board.crash_list = [self.cursor_pos,None]
        elif crash_member == [1,0]:  #移子 
            L = [crash_list[0].coordinate,crash_list[1]]
            results = crash_list[0].move(crash_list[1],self.boardChess,message_com)      
            if results:
                Board.crash_list = [None,None]
                return L     #返回移动列表记录
            else:
                pass
        elif crash_member == [1,1]:
            L = [crash_list[0].coordinate,crash_list[1].coordinate]
            results = crash_list[0].banpick(crash_list[1],self.boardChess,message_com)
            if results == 1:         #光标转移
                Board.crash_list = [self.cursor_pos,None]
            elif results == 2:        #撞击
                self.boardChess.remove(crash_list[1])
                return L      #返回撞击列表记录

    def refresh(self):
        self.screen.blit(self.background[global_var.skin],(0,0))
        for chess in self.boardChess:
            self.screen.blit(chess.image,chess.image_rect)
        self.screen.blit(self.cursor,self.cursor_rect)  
        if (self.redJiang not in self.boardChess) and global_var.board_status == 1 :
            global_var.board_status = 0
            global_var.room_recive_chat_message.append('system : 黑棋获胜！！！')
            name = datetime.datetime.now().strftime('%Y-%m-%H-%M-%S')
            path = global_var.grab_path + name + '.png'
            ImageGrab.grab().save(path)
        elif (self.blackJiang not in self.boardChess) and global_var.board_status == 1:
            global_var.board_status = 0
            global_var.room_recive_chat_message.append('system : 红棋获胜！！！')
            name = datetime.datetime.now().strftime('%Y-%m-%H-%M-%S')
            path = global_var.grab_path + name + '.png'
            ImageGrab.grab().save(path) 