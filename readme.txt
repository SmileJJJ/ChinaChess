创建数据库：
create database Chess_sql character set utf8

create table chess1( id int primary key auto_increment, name varchar(32), passwd varchar(32) )character set utf8;

create table chess2( id int primary key auto_increment,email varchar(32) ,name varchar(32), passwd varchar(32) )character set utf8;


create table chess_member( id int primary key auto_increment, name varchar(32) not null, email varchar(20) not null, passwd varchar(20) default '000000') character set utf8;


安装支持包(客户端)
pip install pygame
pip install PyQt5
pip install qdarkstyle
pip install webbrowser
pip install wheel
pip install (client_support文件夹下的Pillow-3.4.2-cp36-cp36m-win_amd64.whl)








