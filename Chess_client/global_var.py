#************************************
# 线程全局变量管理
#
#************************************

# 访问服务器ip
# IP = '172.60.20.135'
IP = '192.168.1.104'
# IP = '172.20.246.24'
# 访问服务器端口
PORT = 8999

#注册首页
# WEB_ADD = 'http://172.20.40.234:8000/register.html'
WEB_ADD = 'http://192.168.1.105:8000/register.html'

# 棋子碰撞消息
web_message = None
# 登录信息
login_message = None
login_count = None
# 服务器返回的在线人数--->QT显示
online_num = 0

# 登录状态
# 0 未知状态
# 1 登录成功
# 2 密码错误
# 3 账号不存在
login_status = 0 

# 选桌信息
# 1 人满
get_in_table = 0
get_table_num = 0

# 大厅信息列表
lobby_list = list()

#界面等级
#1:一级界面
#2:二级界面
#3:三级界面
interface_rank = 1

# 大厅聊天信息
send_chat_message = ''
recive_chat_message = list()

# 房间聊天信息
room_send_chat_message = ''
room_recive_chat_message = list()

#服务器信息
server_message = ''
web_chess_action_message = None

#链接状态
# 0 未链接
# 1 以链接
connect_status = 0 

# 棋盘
board = None

# 棋局状态 1：对战中  0：结束
board_status = 0

#image grab path
grab_path = 'GRAB\\'

#皮肤序号
skin = 0
skin_all = 0

# 全局变量（测试用）
tset_num = 0
tset_num2 = 0