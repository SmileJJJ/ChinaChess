# -*- coding: UTF-8 -*-
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

# @staticmethod
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def email_send(to_addr,smtp_server,check_pwsd):
    from_addr = '2014896347@qq.com'
    password =  'ovlxkchfdzvdeafd'  #密码为手动打开网页版邮箱的SMTP发信功能和POP收信功能后系统提供的密码

    txt_str = '您的验证码是:'+str(check_pwsd)
    msg = MIMEText(txt_str, 'plain', 'utf-8')
    msg['From'] = _format_addr('ChinaChess <%s>' % from_addr)
    msg['To'] = _format_addr('管理员 <%s>' % to_addr)
    msg['Subject'] = Header('注册验证码', 'utf-8').encode()
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

if __name__ == '__main__':
    email_send('281206814@qq.com','smtp.qq.com',123456)