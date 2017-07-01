# django使用redis+celery异步执行任务

参考地址：
http://docs.jinkan.org/docs/celery/index.html		官方网站文档
http://www.cnblogs.com/aguncn/p/4947092.html	大神作品
http://python.jobbole.com/81953/			大神作品
http://www.mamicode.com/info-detail-986285.html	大神作品


安装以下扩展包：
```bash
pip install celery
pip install celery-with-redis
pip install django-celery
```

安装Redis服务 （不说了，自己百度）

### steup1：在seting.py文件中设置关联
```python
import djcelery			# 导入模块


djcelery.setup_loader()
CELERY_TIMEZONE='Asia/Shanghai'			//设置启动celery服务的时间
TIME_ZONE= 'Asia/Shanghai'			//设置本地时间，celery时间要与本地时间一致
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  	//Redis 中存储任务的状态和返回值(如果使用redis缓存层，就注释掉)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
```


### steup2：在seting.py文件同目录下创建celery.py文件
```python
from __future__ import absolute_import		# 这句代码一定是文件的第一行，一定要在第一句，否则报错

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '项目名.settings')   	#项目名

app = Celery('celerytest')						# 定义项目名（django的项目名）

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)						# 这段代码是打印信息
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
```


### Steup3：在celery.py文件同目录下的__init__.py中写以下代码：
```python
from __future__ import absolute_import
from .celery import app as celery_app					# 重命名模块名将app重名为celery_app
```


### Step4：在需要添加任务的app目录下创建tasks.py文件，这个文件负责处理相关的函数
```javascript
# coding:utf-8

from operation import celery_app	#导入模块
# from celery import shared_task
from django.core.mail import EmailMessage
from operation.settings import EMAIL_FROM

@celery_app.task			# 使用装饰器，注入app中使用
```


# 以下就是任务的代码，很简单，就是发送邮件。
```python
def SendMailFile(email, user, password):
    email_title = "VPN信息，请注意保密"
    email_body = "你好 \n 你的VPN帐号已经开通正常 \n帐号：{0} \n密码：{1} \n压缩包密码：imay \n使用教程请看附件".format(user, password)
    message = EmailMessage(email_title, email_body, EMAIL_FROM, [email])

    keyfile = open("/sh/KeyFile.rar", 'r')
    message.attach("KeyFile.rar", keyfile.read(), 'application/x-rar-compressed')
    status = message.send()
    return status
```    


### Step5：在views.py文件中调用异步函数（部分代码）
```python
from vpnmanage.tasks import SendMailFile				# 导入tasks文件中的函数
# 发送邮件(测试异步发送邮件)
sendmail_status = SendMailFile.delay(email, user, password)		# 注意：函数需要的参数由delay()提供
```


### Step6：启动异步任务
```python
celery -A operation worker -l info		# operation是项目，在celery文件定义的
```

注意：如果提示celery命令没有，你就去软连接一下即可
`ln -fs /usr/local/python2.7/bin/celery /usr/bin/ 即可`



注意：添加一个任务就要重启一次异步任务
以下例子是同一个app下的多个任务：

tasks.py文件：
```python
# coding:utf-8

from operation import celery_app
# from celery import shared_task
from django.core.mail import EmailMessage
from operation.settings import EMAIL_FROM

import paramiko

@celery_app.task
def SendMailFile(email, user, password):
    email_title = "VPN信息，请注意保密"
    email_body = "你好 \n 你的VPN帐号已经开通正常 \n帐号：{0} \n密码：{1} \n压缩包密码：imay \n使用教程请看附件".format(user, password)
    message = EmailMessage(email_title, email_body, EMAIL_FROM, [email])

    keyfile = open("/sh/KeyFile.rar", 'r')
    message.attach("KeyFile.rar", keyfile.read(), 'application/x-rar-compressed')
    status = message.send()
    return status

@celery_app.task()
def SshClient(user, password):
    username = "root"
    passwd = "imay2016"
    host = "192.168.0.220"
    port = 22
    remotefile = "/vpn/psw-file"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host, port, username, passwd)
    ssh.exec_command("echo {0} {1} >> {2}".format(user, password, remotefile))
    ssh.close()
```    


views.py文件：
```python
from vpnmanage.tasks import SendMailFile, SshClient
 # 发送邮件(测试异步发送邮件)
            sendmail_status = SendMailFile.delay(email, user, password)


# 写入VPN文件(测试异步写入文件)
            SshClient.delay(user, password)
```            



启动脚本：
```python
#!/bin/bash
# Author:eycode
# Date:2017-5-17
# 该脚本是celeryd服务启动
# celeryd服务为异步服务
# 需要
# django项目路径
# celery文件路径
# celery项目名

django_poject_path="/webstatus/webstatus"
celery_path="/usr/local/python2.7/bin/celery"
django_poject="webstatus"


if [ ! -f $celery_path ]
then
	echo "celery command not found"
	exit 1
fi


start(){
	cd $django_poject_path
	$celery_path -A $django_poject worker -l info  &> /dev/null &
	sleep 2
	ps xau |grep celery | grep -v "grep" &> /dev/null
	if [ $(echo $?) -eq 0 ]
	then
		echo "start celeryd server success !"
	else
		echo "start celeryd server faild !"
	fi
}



stop(){
	pid_list=$(ps xau |grep celery |grep -v "grep" |awk '{print $2}')
	for i in $pid_list
	do
		kill $i &> /dev/null
	done
}

case $1 in
start)
	start ;;
restart)
	stop
	start ;;
stop)
	stop ;;
*)
	echo "Used: service celeryd {start | restart | stop}"
esac
```

