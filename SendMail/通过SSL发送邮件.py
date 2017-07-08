# coding:utf-8
#!/usr/bin/env python

import smtplib,datetime,sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

username = sys.argv[1]
passwd = sys.argv[2]

_user = "oa@eycode.com"
_pwd  = "密码"
_to_list   = ["%s@eycode.com"%username]

msg = MIMEMultipart()

# 设置邮件编码
msg["Accept-Language"] = "zh-CN"
msg["Accept-Charset"] = "ISO-8859-1,utf-8"

# 邮件标题
msg["Subject"] = u"VPN信息，请注意保密"
msg["From"]    = _user
msg['to'] = ','.join(_to_list)

# 内容部分
part = MIMEText("""
	你好 \n
    你的VPN帐号已经开通正常 \n
    帐号：%s \n
    密码：%s \n
    压缩包密码：imay \n
    使用教程请看附件 \n
	""" % (username,passwd) ,_charset="utf-8")
msg.attach(part)

# 附件部分
part = MIMEApplication(open("VPN.rar",'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="VPN.rar")
msg.attach(part)

# 使用SSL协议进行发送邮件
server = smtplib.SMTP_SSL()
server.connect("smtp.exmail.qq.com", 465)
server.login(_user, _pwd)
server.sendmail(_user, _to_list, msg.as_string())
server.close()
