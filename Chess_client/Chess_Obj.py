# ********************************************************
#·棋子类：棋子类，产生棋子，类包含各项棋子信息
#.移动判断流程：  move(移子)-----------judge(准备判断)-----Rules_XXX(判断规则)
#               banpick(吃子)--------|
# ********************************************************


import pygame
import pygame.locals as pygl
import os,sys
import global_var

#棋子类
class Chess():

    active_allow = False   #棋子动作是否非法

    Blck_Chess = {'JU':'b_ju','MA':'b_ma','PAO':'b_pao','XIANG':'b_xiang','SHI':'b_shi','JIANG':'b_jiang','BING':'b_bing'}
    Red_Chess =  {'JU':'r_ju','MA':'r_ma','PAO':'r_pao','XIANG':'r_xiang','SHI':'r_shi','JIANG':'r_jiang','BING':'r_bing'}

    @staticmethod
    def coordinates_algo(coord):
        return(coord[0] * 50 + 5 ,coord[1] * 50 + 15)

    #产生一个棋子
    def __init__(self,name,color,coordinate):
        self.name = name
        self.color = color
        self.coordinate = coordinate 
        if name == 'BING':
            self.river = False   #过河判定，默认为false(未过河)
        if color == 'BLACK':
            path = './BMP/'+ Chess.Blck_Chess[name] + '.bmp'
        elif color == 'RED':
            path = './BMP/'+ Chess.Red_Chess[name] + '.bmp'
        #产生图片对象
        self.image = pygame.image.load(path)
        #产生图片对应的外框对象，top代表y，left代表x
        self.image_rect = self.image.get_rect()
        self.image.set_colorkey(0xffffff,0)

        #初始化棋子外框的位置
        self.image_rect.left = Chess.coordinates_algo(coordinate)[0]
        self.image_rect.top = Chess.coordinates_algo(coordinate)[1]
    
    def move(self,target,all_chess,message_com):
        res = self.judge(target,all_chess)
        if not res and message_com == 'local':
            global_var.room_recive_chat_message.append('system : 走位无效')
            return False
        self.image_rect.left = Chess.coordinates_algo(target)[0]
        self.image_rect.top = Chess.coordinates_algo(target)[1]
        self.coordinate = (target[0],target[1])
        return True

    def banpick(self,target,all_chess,message_com):
        res = self.judge(target.coordinate,all_chess,1)
        if not res and message_com == 'local':
            global_var.room_recive_chat_message.append('system : 走位无效')
            return False

        if self.color == target.color:
            return 1
        else:
            self.coordinate = target.coordinate
            self.image_rect.left = Chess.coordinates_algo(target.coordinate)[0]
            self.image_rect.top = Chess.coordinates_algo(target.coordinate)[1]
            return 2
        
    def judge(self,target,all_chess,flg = 0):  #flg 移动撞击标志位　０为默认　移动
        if self.name == 'JU':
            if self.Rules_JU(target,all_chess):
                return True
        elif self.name == 'MA':
            if self.Rules_MA(target,all_chess):
                return True
        elif self.name == 'PAO': 
            if flg == 1:
                if self.Rules_PAO(target,all_chess):
                    return True
            elif flg == 0:
                if self.Rules_JU(target,all_chess):
                    return True
        elif self.name == 'XIANG':
            if self.Rules_XIANG(target,all_chess):
                return True
        elif self.name == 'SHI':
            if self.Rules_SHI(target,all_chess):
                return True
        elif self.name == 'JIANG':
            if self.Rules_JIANG(target,all_chess):
                return True
        elif self.name == 'BING':
            if self.Rules_BING(target,all_chess):
                return True
        else:
            return True

    def Rules_JU(self,target,all_chess):   #self.coordinate--->棋子坐标，target--->目标坐标
        if self.coordinate[0] == target[0] and self.coordinate[1] > target[1]:
            for chess in all_chess:
                if chess.coordinate[0] == self.coordinate[0] and (target[1] <chess.coordinate[1] < self.coordinate[1]):
                    #路上有棋子
                    return False
        elif self.coordinate[0] == target[0] and self.coordinate[1] < target[1]: 
            for chess in all_chess:
                if chess.coordinate[0] == self.coordinate[0] and (self.coordinate[1] <chess.coordinate[1] < target[1]):
                    #路上有棋子
                    return False
        elif self.coordinate[1] == target[1] and self.coordinate[0] > target[0]:
            for chess in all_chess:
                if chess.coordinate[1] == self.coordinate[1] and (target[0] <chess.coordinate[0] < self.coordinate[0]):
                    #路上有棋子
                    return False
        elif self.coordinate[1] == target[1] and self.coordinate[0] < target[0]: 
            for chess in all_chess:
                if chess.coordinate[1] == self.coordinate[1] and (self.coordinate[0] <chess.coordinate[0] < target[0]):
                    #路上有棋子
                    return False
        elif self.coordinate[0] != target[0] and self.coordinate[1] != target[1]:
            return False
        return True

    def Rules_MA(self,target,all_chess):   #self.coordinate--->棋子坐标，target--->目标坐标
        if target[0] - self.coordinate[0] == 2 and abs(target[1] - self.coordinate[1]) == 1:
            for chess in all_chess:
                if chess.coordinate ==  (self.coordinate[0] + 1 , self.coordinate[1]):
                    return False
            return True
        elif target[0] - self.coordinate[0] == -2 and abs(target[1] - self.coordinate[1]) == 1:
            for chess in all_chess:
                if chess.coordinate ==  (self.coordinate[0] - 1 , self.coordinate[1]):
                    return False
            return True
        elif target[1] - self.coordinate[1] == 2 and abs(target[0] - self.coordinate[0]) == 1:
            for chess in all_chess:
                if chess.coordinate ==  (self.coordinate[0] , self.coordinate[1] + 1):
                    return False
            return True
        elif target[1] - self.coordinate[1] == -2 and abs(target[0] - self.coordinate[0]) == 1:
            for chess in all_chess:
                if chess.coordinate ==  (self.coordinate[0] , self.coordinate[1] - 1):
                    return False
            return True
        return False

    def Rules_PAO(self,target,all_chess):   #self.coordinate--->棋子坐标，target--->目标坐标
        gap_chess_con = 0
        if self.coordinate[0] == target[0] and self.coordinate[1] > target[1]:
            for chess in all_chess:
                if chess.coordinate[0] == self.coordinate[0] and (target[1] <chess.coordinate[1] < self.coordinate[1]):
                    #路上有棋子
                    gap_chess_con += 1
        elif self.coordinate[0] == target[0] and self.coordinate[1] < target[1]: 
            for chess in all_chess:
                if chess.coordinate[0] == self.coordinate[0] and (self.coordinate[1] <chess.coordinate[1] < target[1]):
                    #路上有棋子
                    gap_chess_con += 1
        elif self.coordinate[1] == target[1] and self.coordinate[0] > target[0]:
            for chess in all_chess:
                if chess.coordinate[1] == self.coordinate[1] and (target[0] <chess.coordinate[0] < self.coordinate[0]):
                    #路上有棋子
                    gap_chess_con += 1
        elif self.coordinate[1] == target[1] and self.coordinate[0] < target[0]: 
            for chess in all_chess:
                if chess.coordinate[1] == self.coordinate[1] and (self.coordinate[0] <chess.coordinate[0] < target[0]):
                    #路上有棋子
                    gap_chess_con += 1
        elif self.coordinate[0] != target[0] and self.coordinate[1] != target[1]:
            return False

        if gap_chess_con == 1:
            return True
        return False

    def Rules_XIANG(self,target,all_chess):   #self.coordinate--->棋子坐标，target--->目标坐标
        if target[1] < 5:
            return False
        elif target[0] - self.coordinate[0] == 2 and target[1] - self.coordinate[1] == 2:
            for chess in all_chess:
                if chess.coordinate ==  (self.coordinate[0] + 1 , self.coordinate[1] + 1):
                    return False
            return True
        elif target[0] - self.coordinate[0] == -2 and target[1] - self.coordinate[1] == 2:
            for chess in all_chess:
                if chess.coordinate ==  (self.coordinate[0] - 1 , self.coordinate[1] + 1):
                    return False
            return True
        elif target[0] - self.coordinate[0] == 2 and target[1] - self.coordinate[1] == -2:
            for chess in all_chess:
                if chess.coordinate ==  (self.coordinate[0] + 1 , self.coordinate[1] - 1):
                    return False
            return True
        elif target[0] - self.coordinate[0] == -2 and target[1] - self.coordinate[1] == -2:
            for chess in all_chess:
                if chess.coordinate ==  (self.coordinate[0] - 1 , self.coordinate[1] - 1):
                    return False
            return True
        return False

    def Rules_SHI(self,target,all_chess):   #self.coordinate--->棋子坐标，target--->目标坐标
        if 2 < target[0] < 6 and 6 < target[1] < 10:
            if abs(target[0] - self.coordinate[0]) == 1 and abs(target[1] - self.coordinate[1]) == 1:
                return True
        return False

    def Rules_JIANG(self,target,all_chess):   #self.coordinate--->棋子坐标，target--->目标坐标
        if 2 < target[0] < 6 and 6 < target[1] < 10:
            if (abs(target[0] - self.coordinate[0]) == 1 and abs(target[1] - self.coordinate[1]) == 0) or \
               (abs(target[0] - self.coordinate[0]) == 0 and abs(target[1] - self.coordinate[1]) == 1):
                return True 
        return False

    def Rules_BING(self,target,all_chess):   #self.coordinate--->棋子坐标，target--->目标坐标
        if self.river == False:
            if target[0] == self.coordinate[0] and self.coordinate[1] - target[1] == 1:
                if target[1] == 4:
                    self.river = True
                return True
        elif self.river == True:
            # print(abs(target[1] - self.coordinate[1]))
            # print(self.coordinate[0] - target[0])
            if (abs(target[0] - self.coordinate[0]) == 1 and self.coordinate[1] == target[1]) or \
               (self.coordinate[1] - target[1] == 1 and self.coordinate[0] == target[0]): 
                return True
        return False

            