注意以下条件：
1. 在django项目中已经新创建了一个static目录，并在setting.py文件中指向了该目录
2. 运行环境使用apache+django，在apache配置文件中指定了static目录的路径为新项目下的路径！！！！！

符合以上两个条件后出现django后台CSS文件找不到情况！

解决方案：
1. 找到django的安装目录：
```bash
Python 2.7.3 (default, Mar 10 2017, 02:35:03) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-17)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import django
>>> django.__file__
'/usr/local/python2.7/lib/python2.7/site-packages/Django-1.9.10-py2.7.egg/django/__init__.pyc'
```


2. 进入Django安装目录中
```bash
[root@9683705d680e static]# pwd
/usr/local/python2.7/lib/python2.7/site-packages/Django-1.9.10-py2.7.egg/django/contrib/admin/static
[root@9683705d680e static]# 
```


3. 复制文件到新的static目录中
```
[root@9683705d680e static]# cp -a admin /webstatus/webstatus/static/
[root@9683705d680e static]# ll /webstatus/webstatus/static/
total 16
drwxr-xr-x 6 root root 4096 Mar 10 02:35 admin
drwxr-xr-x 2 root root 4096 Mar 13 07:53 css
drwxr-xr-x 2 root root 4096 Mar 13 04:11 images
drwxr-xr-x 2 root root 4096 Mar 13 07:56 js
[root@9683705d680e static]# 
```

4. 解决！！！！刷新下地址即可！！！


