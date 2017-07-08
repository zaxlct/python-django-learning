## 通过Python发邮件

#### 描述：

在自动化监控中，经常用到通过Python脚本或Linux原带的Sendmail来发送监控邮件

1.  Python脚本邮件：代码简单，功能强大，例如：发送图片，附件，以Html形式展开，报表等等。最为骄傲的是主要是安装python的系统都可以使用脚本

2.  Linux自带的sendmail等邮件软件：功能强大，但一般新手或非专业管理员是玩不转的，配置文件复杂，一个简单的功能可能需要几个依赖才能玩转， 不兼容主流的邮箱服务器，配置SSL协议更加复杂，所以不建议使用。

#### 应用场景

1.  常用于监控邮件发送（Zabbix，rrdtool等等）
2.  后台发送注册邮件（Django），不过Django已经集成了，更加方便使用。

#### 环境：

1.  Python 2.6 + （最低要求）

2.  任何系统


#### 参考文档：

1.  smtplib模块官方文档：[https://docs.python.org/2/library/email-examples.html](https://docs.python.org/2/library/email-examples.html)

2.  廖雪峰Python2.7 发送邮件：
[http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000)