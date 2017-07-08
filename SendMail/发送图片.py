#!/bin/env python
#coding:utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# 邮件服务器
host = "smtp.163.com"

# 邮件标题
title = u"服务器日常流量监控"

# 收件人
send_to = "******@eycode.com"

# 发件人
send_from = "******@163.com"


# 读取图片文件，值得注意是读取图片！！
def addimg(src,imgid):
	fp = open(src,'rb')
	msgImage = MIMEImage(fp.read())
	fp.close()
	msgImage.add_header('Content-ID',imgid)
	return msgImage

msg = MIMEMultipart('related')


# 邮件以html格式展示
msgtext = MIMEText("""<table>及图片<img> 
<table width="600" border="0" cellspacing="0" cellpadding="4"> 
      <tr bgcolor="#CECFAD" height="20" style="font-size:14px"> 
        <td colspan=2>*官网性能数据  <a href="monitor.domain.com">更多>></a></td> 
      </tr> 
      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px"> 
        <td> 
         <img src="cid:io"></td><td>
      </tr> 
    </table>""","html","utf-8")  
 
now = datetime.datetime.now()

# 获取图片地址
image_file = "%s-eth0.png" % now.strftime('%Y-%m-%d')

# 文本
msg.attach(msgtext)

# 将图片文件
msg.attach(addimg(image_file,"io"))

msg['Subject'] = title
msg['From']= send_from 
msg['To']= send_to

try:  
    server = smtplib.SMTP() 

    # 协议端口 
    server.connect(HOST,"25")
    server.starttls()

    # 登陆 
    server.login("***@eycode.com","****密码*****")  
    server.sendmail(FROM, TO, msg.as_string())  
    server.quit()
    print "邮件发送成功！"  
except Exception, e:  
    print "失败："+str(e)
