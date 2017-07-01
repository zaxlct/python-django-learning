# django使用定时更新任务

### step1：安装django-crontab模块
`pip install django-crontab`
注意：django的任务计划有两个模块，一个是django-crontab，另一个是django-cron
我们使用django-crontab模块，这个配置起来非常简单


### step2：在setting.py中添加为APP
```python
INSTALLED_APPS = [
    # ...
    "django_crontab",		#注意：加载的模块名一定要注意
]
```


### step3：自定义命令函数：(重点)
在app项目下创建management目录，再在该目录下创建commands目录，在commands目录创建py文件，该文件为自定义命令
例如：
app目录名/management/commands/mysql_count.py

```python
# coding:utf-8
# 自定义django-admin命令
# python manage.py mysql_count
# 注意：在更新的时候为什么不能用get，只能用filter?
# get获取的数据是一个字段，而filter获取的是一个列表，在更新中，应该是针对列表中的字段进行更新
# 所以只能用filter

__author__ = 'eycode'
__date__ = '2017/4/11/011  11:33'

from django.core.management.base import BaseCommand 
from vpnmanage.models import VpnManage, VpnLogs


class Command(BaseCommand):	#继承BaseCommand类
    def handle(self, *args, **options):   	# 一定是handle函数
        vpnlist = VpnManage.objects.all()
        vpnlist = [ str(i).split(" ", 3)[1] for i in vpnlist ]

        for user in vpnlist:
            chk_log = VpnLogs.objects.filter(user = user)
            if len(chk_log) != 0:
        # 统计登录成功次数
                success = VpnLogs.objects.filter(user=user, status = "Successful")
                user_success = success.count()

        # 统计登录失败次数
                user_fail_list = VpnLogs.objects.filter(user=user, status="Incorrect")
                user_fail = user_fail_list.count()

        # # 统计登录总次数
                user_counnt = int(user_success) + int(user_fail)

        # 统计最近登录时间
                user_latetime = VpnLogs.objects.filter(user = user, status = "Successful").order_by('-time')[0]
                user_latetime = str(user_latetime)

                VpnManage.objects.filter(user=user).update(scount=user_success, fcount=user_fail, logincount=user_counnt, latetime=user_latetime)
                # print "%s 更新" %user
            else:
                VpnManage.objects.filter(user=user).update(scount="0", fcount="0", logincount="0", latetime="no login")

```


### step4：测试命令的执行是否正常
python manage.py mysql_count
注意：mysql_count为文件名。



### step5：添加计划任务：
在setting.py文件中：
```python
CRONJOBS = [
    ('*/5 * * * *', 'django.core.management.call_command', ['mysql_count']),
]
```

解析：
*/5 * * * *   ：每5分钟执行一次
django.core.management.call_command：相当于python manage.py
mysql_count：自定义命令函数



### step6：执行任务计划
```bash
[root@9683705d680e operation]# python manage.py crontab add      
no crontab for root
  adding cronjob: (1eb1cfc7b7f566494684323c57922190) -> ('*/5 * * * *', 'django.core.management.call_command', ['mysql_count'])
[root@9683705d680e operation]# 
[root@9683705d680e operation]# crontab -l
*/5 * * * * /usr/bin/python /Operationsmanage/operation/manage.py crontab run 1eb1cfc7b7f566494684323c57922190 # django-cronjobs for operation
[root@9683705d680e operation]# 
```


注意：需要服务器上有安装crond服务才能使用
```bash
yum -y install vixie-cron
yum -y install crontabs
```
