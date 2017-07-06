# coding:utf-8
# Author:eycode
# 使用SVN接口
# 安装模块：pip install svn
# 参考文档：https://pypi.python.org/pypi/svn
# 建议操作系统：Linux、Unix

# CheckoutSVN:
import svn.remote
r = svn.remote.RemoteClient("http://192.168.0.220:54162/svn/eycode/", username="eycode", password="eycode")
r.checkout("/tmp")

# 分析：
# svn.remote.RemoteClient(url, username, password)
# checkout(path)

# 注意：直接生成SVN中的目录，即自动更新数据

# 查看该目录：
# [root@16bf6ea74dc8 sh]# ll /tmp/
# total 8
# drwxr-xr-x 3 root root 4096 Jul  6 10:19 0302-1.5.0

# 0302-1.5.0目录是SVNcheckout后自动更新生成的目录




# 查看日志：
import svn.local
log = svn.local.LocalClient("/tmp/0302-1.5.0")
for i in log.log_default():
	print i

# 返回结果：
# LogEntry(date=datetime.datetime(2017, 7, 4, 6, 26, 54, 671678, tzinfo=tzutc()), msg=None, revision=5, author='eycode', changelist=None)




# 获取更新文件列表（文件名模式）
import svn.local
l = svn.local.LocalClient("/tmp/0302-1.5.0")
for i in l.list():
	print i


# 返回结果：
# GisApp-Ybo-release.apk
# GisApp-vivo-release.apk
# GisApp-xiaomi-release.apk

# 值得注意的是：
# 当某个客户端提交数据，本地客户端重新更新数据在同一个目录下时，会将之前的数据名同样显示出来



# 获取更新文件列表（字典模式）
import svn.local
l = svn.local.LocalClient("/tmp/0302-1.5.0")
for i in l.list(extended=True):
	print i

# 返回结果：
# {'kind': 'file', 'is_directory': False, 'name': 'GisApp-Ybo-release.apk', 'author': 'eycode', 'date': datetime.datetime(2017, 7, 4, 6, 26, 54, 671678, tzinfo=tzutc()), 'timestamp': datetime.datetime(2017, 7, 4, 6, 26, 54, 671678, tzinfo=tzutc()), 'commit_revision': 5, 'size': 56060566}
# {'kind': 'file', 'is_directory': False, 'name': 'GisApp-vivo-release.apk', 'author': 'eycode', 'date': datetime.datetime(2017, 7, 4, 6, 26, 54, 671678, tzinfo=tzutc()), 'timestamp': datetime.datetime(2017, 7, 4, 6, 26, 54, 671678, tzinfo=tzutc()), 'commit_revision': 5, 'size': 55504787}
# {'kind': 'file', 'is_directory': False, 'name': 'GisApp-xiaomi-release.apk', 'author': 'eycode', 'date': datetime.datetime(2017, 7, 4, 6, 26, 54, 671678, tzinfo=tzutc()), 'timestamp': datetime.datetime(2017, 7, 4, 6, 26, 54, 671678, tzinfo=tzutc()), 'commit_revision': 5, 'size': 55504678}
# {'kind': 'file', 'is_directory': False, 'name': 'test.txt', 'author': 'eycode', 'date': datetime.datetime(2017, 7, 6, 2, 47, 39, 273350, tzinfo=tzutc()), 'timestamp': datetime.datetime(2017, 7, 6, 2, 47, 39, 273350, tzinfo=tzutc()), 'commit_revision': 6, 'size': 0}