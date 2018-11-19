# python-django-learning
- python 和 django 学习资料，书籍，文章，以及实战项目等等
- [仿照慕课网搭建的在线编程学习平台](https://github.com/zaxlct/imooc-django)
- [基于flask框架开发的微信小程序后端，用于构建小程序商城](https://github.com/bodanli159951/mini-shop-server)
- QQ 群 163801325

## 项目贡献规范
- 务必先阅读 [中文文案排版指北](https://github.com/mzlogin/chinese-copywriting-guidelines)
- 请遵守上面规范里的格式和排版


## Python 基础

当你学到 Django 的时候，我们默认你已经有了 Python 基础。如果你没有 Python 基础，或者认为自己还需要在 Python 基础上多花一些时间，你可以选择从以下三本书着手。

* [《Python编程 从入门到实践》](https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B01ION3VWI/ref=sr_1_1?ie=UTF8&qid=1498793018&sr=8-1&keywords=python+crash+course) （[Python Crash Course: A Hands-On, Project-Based Introduction to Programming](https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036/ref=sr_1_1?ie=UTF8&qid=1498793322&sr=8-1&keywords=python+crash+course)）这本书的作者就是 Django 项目的维护者之一。本书在学习 Python 基础的同时，可以学到一些 Python 的最佳实践（当然谈到最佳实践，有更多的进阶书籍的选择）。推荐本书的另一个原因是书籍质量不错，在美国亚马逊的 Python programming 排行榜上荣获“Best seller“，194个读者综合评分为4.4的高分（满分5分）。

* [《"笨办法"学Python(第3版)》](https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B00P6OJ0TC/ref=sr_1_1?ie=UTF8&qid=1498793029&sr=8-1&keywords=python+%E7%AC%A8%E5%8A%9E%E6%B3%95) ([Learn Python the Hard Way](https://learnpythonthehardway.org/book/)) 这本书简称“LPHW”，是经久不衰的 Python 入门书。本书强调的是肌肉记忆，强调的是编程犹如弹吉他，需要亲手实践、加强肌肉记忆。如果你对编程也没有太多概念，这本书会比较轻松的带你入门，增强你的编程自信心。

* [《Python 基础教程》](https://www.amazon.cn/%E5%9B%BE%E7%81%B5%E7%A8%8B%E5%BA%8F%E8%AE%BE%E8%AE%A1%E4%B8%9B%E4%B9%A6-Python%E5%9F%BA%E7%A1%80%E6%95%99%E7%A8%8B-%E8%B5%AB%E7%89%B9%E5%85%B0/dp/B00KAFX65Q/ref=sr_1_1?ie=UTF8&qid=1508737548&sr=8-1&keywords=python+novice)([Beginning Python: From Novice to Professional](https://www.amazon.cn/Beginning-Python-From-Novice-to-Professional-Hetland-Magnus-Lie/dp/1484200292/ref=sr_1_4?ie=UTF8&qid=1508737548&sr=8-4&keywords=python+novice)) 如果在这三本中选一本必看的基础书，个人更偏好、也更推荐这一本。作者对基础知识的讲解清晰明了，内容简单但是并不肤浅。讲解过程通畅，基本不存在费解的情况。代码小片段实例比比皆是，马上就可以动手实践来理解概念，可以让人更容易记得住，学习的效果也是相当好。较深的概念有延展的接口，提供方向供后期自己去扩展。值得一提的是，目前这本书中文翻译仍然是[2009年英文版的 Python 2.7](https://www.amazon.com/Beginning-Python-Novice-Professional-Experts/dp/1590599829/ref=sr_1_2?ie=UTF8&qid=1508738718&sr=8-2&keywords=beginning+Python%3A+from+novice+to+professional)，而今年（2017年）4月Apress出版社继续推出了[该书最新的第三版](https://www.amazon.com/Beginning-Python-Professional-Magnus-Hetland/dp/1484200292/ref=sr_1_1?ie=UTF8&qid=1508738718&sr=8-1&keywords=beginning+Python%3A+from+novice+to+professional)，已经使用 Python 3 的版本（暂无中文版）。作者 Magnus Lie Hetland 在 2006 年开始写作第一版至今，时隔11年还能继续推出最新版，而且内容质量靠谱，实在难能可贵。

如果你觉得看视频入门更适合自己，那么我推荐：
[Python3 入门与进阶](https://coding.imooc.com/class/136.html)
（付费课程，但是质量非常高，具体可以看用户评价）

## Django 与 Python 开发环境问题

**注意：[目前在维护 Django 版本](https://en.wikipedia.org/wiki/Django_(web_framework))为：Django 1.8（长期支持版，LTS），Django 1.10，Django 1.11（最新版，长期支持版，LTS，也是最后一个支持 Python2的版本）。**

如果学习资料是这些版本以前的版本，比如 Django 1.7，则不建议再学习已经过时的资料。对于书籍是否已经过时，Two Scoops 的作者 Daniel R. Greenfeld（也是Django的项目维护者）有一个书籍清单供参考（[Current Django Books](https://www.twoscoopspress.com/pages/current-django-books)）。

Django 的版本以及 Python 开发环境至关重要，请在最开始学习 Django 的时候就引起重视。由于 Python、Django以及其他第三方包的版本不同，有时候会产生与学习资料不一样的结果。建议学习过程中注意两点：

* 为每一个项目建立虚拟环境，建立相对独立的开发环境
* 严格按照学习资料的版本进行开发。注意是 Python 2 还是 Python 3，Django 的版本、以及第三方包的版本号。



## Django 基础

### 1. 视频

推荐使用慕课网的两门免费在线视频课程作为入门：

* [django初体检](http://www.imooc.com/learn/458)
* [django入门与实践](http://www.imooc.com/learn/790)

这两门课基本涵盖了 Django 最核心、同时也是最常用的部分，他们会给你建立一个 Django 的整体概念，便于消除你对 Django 的陌生感和恐惧感。

如果想进一步详细的了解 Django，有个综合性的教程名叫
* [《Django 企业开发实战》](http://django-practice-book.com)

该教程包含 gitbook 电子书（免费）以及视频部分（收费）。该教程之所以比较推荐，作者是搜狐的胡阳（[博客地址](https://www.the5fire.com)）。阳哥长期在搜狐大量实际使用 Django，而且对源码比较熟悉，所以该教程讲得深入浅出，有不少独到的见解。

### 2. 文档

在有了视频的感性认识之后，建议马上阅读完 Django 文档的新手入门6个部分的内容，并亲手实践让代码能跑起来。文档是最权威也是最全面的 Django 参考资料。

* [Getting started](https://docs.djangoproject.com/en/1.11/intro/) Django 1.11 英文原版文档的新手入门部分。
* [Django 中文文档 1.8](https://wizardforcel.gitbooks.io/django-chinese-docs-18/content/) Django 1.8 的中文文档（gitbook在线书）。

### 3. 书籍与博客

#### 3.1 英文

* [Mastering Django: Core: The Complete Guide to Django 1.8 LTS](https://www.amazon.com/Mastering-Django-Core-Complete-Guide-ebook/dp/B01KR6F4Z2/ref=pd_sim_351_1?_encoding=UTF8&psc=1&refRID=FGPD50FMR491T393ZV8K) 这本书就是大名鼎鼎的 Django Book 的最新版本。本书前7章是连贯的学习教程，可作为入门教材，后面的章节以讲解概念为主。[《中文版的 Django Book》](http://djangobook.py3k.cn/2.0/) 使用的是 Django 1.1 版本，已经严重过时，中文版本仅供参考。作者的主页是  [djangobook.com](http://djangobook.com/)。图灵社区于今年（2017年）5月出版了这本书的[中文翻译版](http://www.ituring.com.cn/book/2401)。

* [Hello Web App](https://www.amazon.com/Hello-Web-App-Tracy-Osborn/dp/0986365912?tag=tsp0c2-20) 作者之前主要从事前段工作，以一个新手的视角来完成本书。整书叙述流畅，以及跟着书完成代码。作者还有一本后续的书籍 [Hello Web App: Intermediate Concepts](https://www.amazon.com/Hello-Web-App-Intermediate-Concepts/dp/0986365920/ref=pd_bxgy_14_2?_encoding=UTF8&pd_rd_i=0986365920&pd_rd_r=9PT5VMN8HB8TZ0NH9HTP&pd_rd_w=sw4hX&pd_rd_wg=LsbKy&psc=1&refRID=9PT5VMN8HB8TZ0NH9HTP) ，内容稍微深一些。

另外有人也经常推荐以下内容，供参考：

*  [Tango With Django: A beginner's Guide to Web Development With Python / Django 1.9](https://www.amazon.com/gp/product/B01N91N65Y/?tag=tsp0c2-20) 值得注意的是这本书被 Two Scoops 的作者列为过时书籍。
*  [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) Django Girl严格来说已经相当于是一个商业组织，因为该组织在卖周边、做培训，但是入门教程还是不错的，内容基本与 Tango with Django 类似。最近还推出该入门教程的[扩展部分](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/)。



#### 3.2 中文

* [自强学堂：Django 教程](http://code.ziqiangxuetang.com/django/django-tutorial.html) 内容详实免费。值得一提的是作者使用 Django 建站，完全是在实践 Django 的使用，而且作者从2015年至今一直在根据 Django 版本升级而更新教学内容，从最初的 Django 1.6 更新到了 Django 1.10。作者称最新版本的 Django 1.11 内容马上就要推出。


* [Django Girls 教程](https://tutorial.djangogirls.org/zh/) Django Girls 的中文版，使用 Django 1.8。


* [追梦人物的博客](http://zmrenwu.com/?page=5) 以 Django 1.10 为基础开发博客到部署的完整教程。



## Django 进阶

### 1. 视频

中文视频内容有很多，但是从内容的深度、广度、教学实践、教学质量来看，推荐慕课网的强力 Django 课程作为进阶必看课程。

* [强力django+杀手级xadmin打造上线标准的在线教育平台](http://coding.imooc.com/class/78.html) 慕课网付费课程。虽然收费，但是课程质量上佳。内含一个 refresh 的小项目和一个较大的系统项目，涉及 Django 的内容较广，完成后可以达到上线标准。常被誉为“Django课程的良心之作”。

英文视频中，美国的 Justin Mitchel 长期专注于做 Django 培训。他的部分教学视频也放在 YouTube 上。推荐三门系列课程，分别是完成一个基本博客，增加复杂功能，到使用 django-rest-framework。内容详实，值得一看。

* [Try Django 1.9](https://www.youtube.com/watch?v=yfgsklK_yFo&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy)
* [Advancing the Blog](https://www.youtube.com/watch?v=Vp7Oa7nAXJ4&list=PLEsfXFp6DpzQB82YbmKKBy2jKdzpZKczn)
* [Blog API with Django Rest Framework](https://www.youtube.com/watch?v=XMu0T6L2KRQ&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS)

### 2. 书籍


* Two Scoops of Django：目前有两个版本 [Two Scoops of Django: Best Practices for Django 1.11](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11) 和 [Two Scoops of Django: Best Practices for Django 1.8](https://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342/ref=pd_bxgy_14_img_3?_encoding=UTF8&pd_rd_i=0981467342&pd_rd_r=FJBAW39ZPPH73AXZQRP0&pd_rd_w=qPOZk&pd_rd_wg=caiaO&psc=1&refRID=FJBAW39ZPPH73AXZQRP0) 。这本书在 Django 的名气也是非常大，基本可以说影响过大多数 Django 开发人员（可类比的是 Flask 界的[『狗书』](https://www.amazon.cn/Flask-Web%E5%BC%80%E5%8F%91-%E5%9F%BA%E4%BA%8EPython%E7%9A%84Web%E5%BA%94%E7%94%A8%E5%BC%80%E5%8F%91%E5%AE%9E%E6%88%98-%E6%A0%BC%E6%9E%97%E5%B8%83%E6%88%88/dp/B00QT2TQCG/ref=sr_1_1?ie=UTF8&qid=1508804881&sr=8-1&keywords=flask+web%E5%BC%80%E5%8F%91)作者 [Miguel Gringberg](https://blog.miguelgrinberg.com/index)）。如果要进阶成为 Django 专业开发者，这本书是绕不过去的必看书籍。内容主要涵盖 Django 的最佳实践。

* [Django By Example](https://www.amazon.com/Django-Example-Antonio-Mele/dp/1784391913/ref=sr_1_1?ie=UTF8&qid=1499261611&sr=8-1&keywords=django+by+example) 在进阶的课程中，本书算是不错的。虽然一些章节（比如第7章）部分代码仍然存在 bug，但是一方面作者正在该书主页不断进行代码更正，另一方面也是对中国读者最好的是，这本书已经由同在简书的 [@夜夜月](http://www.jianshu.com/u/390b6edb26a8) 进行了全书翻译：[《Django By Example》中文版](http://www.jianshu.com/c/a1fbca21af87)。

* [Django Unleashed](https://www.amazon.com/Django-Unleashed-Andrew-Pinkham/dp/0321985079/ref=pd_sim_14_13?_encoding=UTF8&pd_rd_i=0321985079&pd_rd_r=FJBAW39ZPPH73AXZQRP0&pd_rd_w=qkuw5&pd_rd_wg=caiaO&psc=1&refRID=FJBAW39ZPPH73AXZQRP0) 内容覆盖较广，很多内容在其他书籍中并没有提及，比如密码的hash与加密等。但是没有实战项目。

* [《Python Web 测试驱动方法》](https://www.amazon.cn/Python-Web%E5%BC%80%E5%8F%91-%E6%B5%8B%E8%AF%95%E9%A9%B1%E5%8A%A8%E6%96%B9%E6%B3%95-%E7%8F%80%E8%A5%BF%E7%93%A6%E5%B0%94/dp/B016I9T8SQ/ref=sr_1_fkmr0_3?ie=UTF8&qid=1508740219&sr=8-3-fkmr0&keywords=%E6%B5%8B%E8%AF%95%E9%A9%B1%E5%8A%A8%E5%BC%80%E5%8F%91+django) 虽然测试驱动的开发方法（Test-Driven Development，TDD）并不是每个项目都会采用，但是测试的思想与方法还是值得去掌握。Python 作为一门动态语言，没有静态类型检测的情况下，测试的重要性就显得尤为重要。本书使用 Django 的整个开发流程作为实例，作者不仅讲了开发过程单元测试和 Selenium 测试，同时也把部署的内容也覆盖到。内容始于 Django，但不仅仅是 Django，相信使用其他框架的 Python 开发者也可以从中获益匪浅。


### 3. 博客

* [Vitor Freitas: Simple is better than complex](https://simpleisbetterthancomplex.com/) 作者是旅居芬兰的巴西人，博客上有76篇关于 Python、Django 以及网络开发的文字。文章质量较高，可以邮件订阅。

* [Huang Huang 的博客](https://mozillazg.github.io/) 之所以提到这个博客，主要因为作者认真写了三篇关于《High Perfomance Django》的阅读笔记：[笔记一](https://mozillazg.github.io/2015/09/high-performance-django-note-1.html)、[笔记二](https://mozillazg.github.io/2015/09/high-performance-django-note-2.html)、[笔记三](https://mozillazg.github.io/2015/09/high-performance-django-note-3.html)。从数据库优化、缓存、容灾、后台视图完善，这些一点一滴的内容都是 Django 项目开发过程中迟早会遇到的瓶颈，看一下这些内容也许就会对后面的解决方案有更深的理解。比如[『话说Django orm性能为什么比原生的mysqldb慢』](http://xiaorui.cc/2015/09/24/%E8%AF%9D%E8%AF%B4django-orm%E6%A8%A1%E5%9E%8B%E4%B8%BA%E4%BB%80%E4%B9%88%E6%AF%94%E5%8E%9F%E7%94%9F%E7%9A%84mysqldb%E6%85%A2/)这篇文章就遇到了后台报表页面打开很慢的坑，这也是完善提高 Django 性能的地方。

### 4. 开源项目
- [强力django+杀手级xadmin打造上线标准的在线教育平台](https://github.com/zaxlct/imooc-django)
- [《强力django+杀手级xadmin打造...》视频教程笔记](http://blog.mtianyan.cn/post/8b4c6c13.html)，详细记录了每一章的步骤和重点


## Django RESTful API

Django 的 REST 化主要是两个第三方包：[django-rest-framework](http://www.django-rest-framework.org/) 和 [django-tastypie](https://github.com/django-tastypie/django-tastypie)。虽然后者开发时间较早，但是最推荐的是前者，即 django-rest-framework。该框架内容更全，调试也方便。

### 1. 文档

django-rest-framework 的文档分为英文和中文。英文就是原版的网站，中文有两个作者的翻译，但都是只翻译了入门部分。

* [英文版文档](http://www.django-rest-framework.org/tutorial/quickstart/)
* 中文文档有两个，可以对照看：[中文文档 Roy 版本](http://www.hi-roy.com/) 以及 [中文文档 Eason版本](https://whatwewant.gitbooks.io/django-rest-framework-tutorial-cn/content/index.html)。

### 2. 视频

* [Vue+Django REST framework 打造生鲜电商项目](http://coding.imooc.com/class/131.html) 可能是目前中文 Django 教学视频中最好的课程，教学时间长度与内容都有相当的保证。视频作者 Bobby 详细阐述了自己对的 Django 的理解，可以让人知道多种递进式 rest API 开发方式。得益于 Bobby 精益求精的态度，个人觉得干货的程度即使与国外的内容比较也是不逞多让。另外再加上与 Vue 前端的整体交互综合开发，已经可以初步满足一个中小企业的网络解决方案。

* [Build Your Own Backend REST API using Django REST Framework](https://www.udemy.com/django-python/learn/v4/overview) 作者是英国人 Mark Winterbottom，编程专业，而且讲课细致到位。


* [Blog API with Django Rest Framework](https://www.youtube.com/watch?v=XMu0T6L2KRQ&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS) 仍然是之前提到的美国人 Austin Mitchel 的 YouTube 课程。

### 3. 书籍与博客

* [《轻量级Django》](https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B01M4S72G0/ref=sr_1_1?ie=UTF8&qid=1498801619&sr=8-1&keywords=%E8%BD%BB%E9%87%8F%E7%BA%A7+django) 英文版是[Lightweight Django: Using REST, WebSockets, and Backbone](https://www.amazon.com/Lightweight-Django-Using-WebSockets-Backbone/dp/149194594X/ref=sr_1_1?s=books&ie=UTF8&qid=1498801565&sr=1-1&keywords=python+lightweight)，严格来说这不是一本完全讲 rest-framework 的书，而是讲解如何从传统的 Django 过渡到前后端分离 Django 。
* [Building RESTful Python Web Services](https://www.amazon.com/Building-RESTful-Python-Web-Services/dp/1786462257/ref=sr_1_3?s=books&ie=UTF8&qid=1498801570&sr=1-3&keywords=python+rest) 内容涉及 Python 三大网络框架：Django，Flask以及Tornado。


* [Haiiiiiyun：Django REST 框架 V3 教程](http://www.atjiang.com/tags/#djangorestframework)，讲到 rest 的7门课程。


## Django 与 Vue 的结合
- [《Django + Vue 单页面应用的开发环境搭建步骤》](https://www.jianshu.com/p/fe74907e16b9)
- 开源项目：[hello-vue-django](https://github.com/zaxlct/hello-vue-django)

## Django 业界最新信息

* [Django: Under The Hood](https://www.djangounderthehood.com/) 专注于 Django 的内容，虽然著名的 PyCon 经常请 Django 专家去演讲，但是 Django: Under The Hood 基本都是 Django 的大牛，比如2016年压轴演讲是邀请了 Instgram 的后端去讲解 INS 如何用 Django 做成了如此规模巨大的社交图片分享网站。该组织近两年的演讲内容都分享在 YouTube 上可以找到。[Django Under The Hood：YouTube地址](https://www.youtube.com/channel/UC9T1dhIlL_8Va9DxvKRowBw)
* PyCon 也非常关注 Django 的发展。Django 并非完美无缺，在网络技术高速发展的今天，Django 也需要及时的进化以适应形势。在 PyCon 上，对 Django 热爱程序员们，提出了尖锐的 Django 问题，随后也有新的解决方案出来。的有代表性的演讲包括：
  * [Why Django Sucks - PyCon SE 2015](https://www.youtube.com/watch?v=Niq-HoraNPo) 作者提出 Django 在某些方面跟不上网络技术的发展趋势，提出了自己的三点建议。
  * [Reinventing Django for the Real-Time Web - PyCon 2016](https://www.youtube.com/watch?v=2sEPipctTxw&t=574s) 作者是 Django 的 Channel 部分的开发者，专注于 Socket 的包装与编程，以实现 Django 的服务器推送、异步 Socket 等功能。
  * [Building Dynamic Dashboards With Django and D3 - PyCon US 2016](https://www.youtube.com/watch?v=XXG-ESzB9Q8&t=407s) 比较好的把 Django 与 React 以及 D3 结合在一起为警局提供数据看板项目。



## 修改记录

### 2017-10-23 更新内容
* Python 基础部分：不再推荐《Python学习手册(第4版)》。基础书籍数量保持三本，增加推荐新书籍，本书不再推荐。

被删除内容：

>[《Python学习手册(第4版)》](https://www.amazon.cn/Python%E5%AD%A6%E4%B9%A0%E6%89%8B%E5%86%8C-%E9%B2%81%E7%89%B9%E5%85%B9/dp/B004TUJ7A6/ref=sr_1_1?ie=UTF8&qid=1498793035&sr=8-1&keywords=python+%E5%AD%A6%E4%B9%A0%E6%89%8B%E5%86%8C) （[Learning Python, 5th Edition](https://www.amazon.com/Learning-Python-5th-Mark-Lutz/dp/1449355730/ref=sr_1_1?ie=UTF8&qid=1498803998&sr=8-1&keywords=learning+python)）本书中文是第四版，英文已经更新到第五版。该作者长期从事 Python 教育，他知道学习者通常会问什么问题，所以讲解也是比较详细。如果你需要快速入门 Python ，不推荐这本书。但是相信你在 Python 进阶过程中，迟早会遇到一些很 Pythonic 的问题，比如：字典的三种创建方式、列表推导式（list comprehension）和装饰器（decorator）。你可以在这里快速找到详细的讲解。作者的另外还有两本高质量的 Python 书值得一读：[Python Pocket Reference: Python In Your Pocket (Pocket Reference (O'Reilly))](https://www.amazon.com/Python-Pocket-Reference-Your-OReilly/dp/1449357016/ref=la_B000APH2C4_1_2?s=books&ie=UTF8&qid=1498794090&sr=1-2) 以及[Programming Python: Powerful Object-Oriented Programming](https://www.amazon.com/Programming-Python-Powerful-Object-Oriented/dp/0596158106/ref=la_B000APH2C4_1_3?s=books&ie=UTF8&qid=1498794090&sr=1-3)。

* Python 基础部分：增加推荐《Python 基础教程》

* Django 进阶部分，2. 书籍：增加《Python Web 测试驱动方法》。

* Django 进阶部分，3. 博客：增加 "Huang Huang 的博客"。

* Django RESTful API，2. 视频：增加 "Vue+Django REST framework 打造生鲜电商项目"。

* 修改部分格式错误。




