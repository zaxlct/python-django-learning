# python-django-learning
python 和 diango 学习资料，书籍，文章，以及实战项目等等



## Python 基础

当你学到 Django 的时候，我们默认你已经有了 Python 基础。如果你没有 Python 基础，或者认为自己还需要在 Python 基础上多花一些时候，你可以选择从以下三本书着手。

* [《Python编程 从入门到实践》](https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B01ION3VWI/ref=sr_1_1?ie=UTF8&qid=1498793018&sr=8-1&keywords=python+crash+course) （[Python Crash Course: A Hands-On, Project-Based Introduction to Programming](https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036/ref=sr_1_1?ie=UTF8&qid=1498793322&sr=8-1&keywords=python+crash+course)）这本书的作者就是 Django 项目的维护者之一。本书在学习 Python 基础的同时，可以学到一些 Python 的最佳实践（当然谈到最佳实践，有更多的进阶书籍的选择）。推荐本书的另一个原因是书籍质量不错，在美国亚马逊的 Python programming 排行榜上荣获“Best seller“，194个读者综合评分为4.4的高分（满分5分）。
* [《"笨办法"学Python(第3版)》](https://www.amazon.cn/%E5%9B%BE%E4%B9%A6/dp/B00P6OJ0TC/ref=sr_1_1?ie=UTF8&qid=1498793029&sr=8-1&keywords=python+%E7%AC%A8%E5%8A%9E%E6%B3%95) ([Learn Python the Hard Way](https://learnpythonthehardway.org/book/)) 这本书简称“LPHW”，是经久不衰的 Python 入门书。本书强调的是肌肉记忆，强调的是编程犹如弹吉他，需要亲手实践、加强肌肉记忆。如果你对编程也没有太多概念，这本书会比较轻松的带你入门，增强你的编程自信心。
* [Python学习手册(第4版)](https://www.amazon.cn/Python%E5%AD%A6%E4%B9%A0%E6%89%8B%E5%86%8C-%E9%B2%81%E7%89%B9%E5%85%B9/dp/B004TUJ7A6/ref=sr_1_1?ie=UTF8&qid=1498793035&sr=8-1&keywords=python+%E5%AD%A6%E4%B9%A0%E6%89%8B%E5%86%8C) （[Learning Python, 5th Edition](Learning Python, 5th Edition)）本书中文是第四版，英文已经更新到第五版。该作者长期从事 Python 教育，他知道学习者通常会问什么问题，所以讲解也是比较详细。如果你需要快速入门 Python ，不推荐这本书。但是相信你在 Python 进阶过程中，迟早会遇到一些很 Pythonic 的问题，比如：字典的三种创建方式、列表推导式（list comprehension）和装饰器（decorator）。你可以在这里快速找到详细的讲解。作者的另外还有两本高质量的 Python 书值得一读：[Python Pocket Reference: Python In Your Pocket (Pocket Reference (O'Reilly))](https://www.amazon.com/Python-Pocket-Reference-Your-OReilly/dp/1449357016/ref=la_B000APH2C4_1_2?s=books&ie=UTF8&qid=1498794090&sr=1-2) 以及[Programming Python: Powerful Object-Oriented Programming](https://www.amazon.com/Programming-Python-Powerful-Object-Oriented/dp/0596158106/ref=la_B000APH2C4_1_3?s=books&ie=UTF8&qid=1498794090&sr=1-3)。




## Django 与 Python 开发环境问题

**注意：[目前在维护 Django 版本](https://en.wikipedia.org/wiki/Django_(web_framework))为：Django 1.8（长期支持版，LTS），Django 1.10，Django 1.11（最新版，长期支持版，LTS，也是最后一个支持 Python2的版本）。**

如果学习资料是这些版本以前的版本，比如 DJango 1.7，则不建议再学习已经过时的资料。对于书籍是否已经过时，Two Scoops 的作者 Daniel R. Greenfeld（也是Django的项目维护者）有一个书籍清单供参考（[Current Django Books](https://www.twoscoopspress.com/pages/current-django-books)）。

Django 的版本以及 Python 开发环境至关重要，请在最开始学习 Django 的时候就引起重视。由于 Python、Django以及其他第三方包的版本不同，有时候会产生与学习资料不一样的结果。建议学习过程中注意两点：

* 为每一个项目建立虚拟环境，建立相对独立的开发环境
* 严格按照学习资料的版本进行开发。注意是 Python 2 还是 Python 3，Django 的版本、以及第三方包的版本号。



## Django 基础

### 1. 视频

推荐使用慕课网的两门免费在线视频课程作为入门：

* [django初体检](http://www.imooc.com/learn/458)
* [django入门与实践](http://www.imooc.com/learn/790)

这两门课基本涵盖了 Django 最核心、同时也是最常用的部分，他们会给你建立一个 Django 的整体概念，便于消除你对 Django 的陌生感和恐惧感。

### 2. 文档

在有了视频的感性认识之后，建议马上阅读完 Django 文档的新手入门6个部分的内容，并亲手实践让代码能跑起来。文档是最权威也是最全面的 Django 参考资料。

* [Getting started](https://docs.djangoproject.com/en/1.11/intro/) Django 1.11 英文原版文档的新手入门部分。
* [Django 中文文档 1.8](https://wizardforcel.gitbooks.io/django-chinese-docs-18/content/) Django 1.8 的中文文档（gitbook在线书）。

### 3. 书籍与博客

#### 3.1 英文

* [Mastering Django: Core: The Complete Guide to Django 1.8 LTS](https://www.amazon.com/Mastering-Django-Core-Complete-Guide-ebook/dp/B01KR6F4Z2/ref=pd_sim_351_1?_encoding=UTF8&psc=1&refRID=FGPD50FMR491T393ZV8K) 这本书就是大名鼎鼎的 Django Book 的最新版本。本书前7章是连贯的学习教程，可作为入门教材，后面的章节以讲解概念为主。[《中文版的 Django Book》](http://djangobook.py3k.cn/2.0/) 使用的是 Django 1.1 版本，已经严重过时，中文版本仅供参考。作者的主页是  [djangobook.com](http://djangobook.com/)。
* [Hello Web App](https://www.amazon.com/Hello-Web-App-Tracy-Osborn/dp/0986365912?tag=tsp0c2-20) 作者之前主要从事前段工作，以一个新手的视角来完成本书。整书叙述流畅，以及跟着书完成代码。作者还有一本后续的书籍 [Hello Web App: Intermediate Concepts](https://www.amazon.com/Hello-Web-App-Intermediate-Concepts/dp/0986365920/ref=pd_bxgy_14_2?_encoding=UTF8&pd_rd_i=0986365920&pd_rd_r=9PT5VMN8HB8TZ0NH9HTP&pd_rd_w=sw4hX&pd_rd_wg=LsbKy&psc=1&refRID=9PT5VMN8HB8TZ0NH9HTP) ，内容稍微深一些。

另外有人也经常推荐以下内容，供参考：

*  [Tango With Django: A beginner's Guide to Web Development With Python / Django 1.9](https://www.amazon.com/gp/product/B01N91N65Y/?tag=tsp0c2-20) 值得注意的是这本书被列为 Two Scoops 的作者列为过时书籍。
*  [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) Django Girl严格来说已经相当于是一个商业组织，因为该组织在卖周边、做培训，但是入门教程还是不错的，内容基本与 Tango with Django 类似。最近还推出该入门教程的[扩展部分](https://djangogirls.gitbooks.io/django-girls-tutorial-extensions/)。



#### 3.2 中文

* [自强学堂：Django 教程](http://code.ziqiangxuetang.com/django/django-tutorial.html) 内容详实免费。值得一提的是作者使用 Django 建站，完全是在实践 Django 的使用，而且作者从2015年至今一直在根据 Django 版本升级而更新教学内容，从最初的 Django 1.6 更新到了 Django 1.10。作者称最新版本的 Django 1.11 内容马上就要推出。


* [Django Girls 教程](https://tutorial.djangogirls.org/zh/) Django Girls 的中文版，使用 Django 1.8。


* [追梦人物的博客](http://zmrenwu.com/?page=5) 以 Django 1.10 为基础开发博客到部署的完整教程。



## Django 进阶

### 1. 视频

中文视频内容有很多，但是从内容的深度、广度、教学实践、教学质量来看，推荐慕课网的强力 Django 内容。

* [强力django+杀手级xadmin打造上线标准的在线教育平台](http://coding.imooc.com/class/78.html) 慕课网付费课程。虽然收费，但是课程质量上佳。内含一个 refresh 的小项目和一个较大的系统项目，涉及 Django 的内容较广，完成后可以达到上线标准。常被誉为“Django课程的良心之作”。

英文视频中，美国的 Justin Mitchel 长期专注于做 Django 培训。他的部分教学视频也放在 YouTube 上。推荐三门系列课程，分别是完成一个基本博客，增加复杂功能，到使用 django-rest-framework。内容详实，值得一看。

* [Try Django 1.9](https://www.youtube.com/watch?v=yfgsklK_yFo&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy)
* [Advancing the Blog](https://www.youtube.com/watch?v=Vp7Oa7nAXJ4&list=PLEsfXFp6DpzQB82YbmKKBy2jKdzpZKczn)
* [Blog API with Django Rest Framework](https://www.youtube.com/watch?v=XMu0T6L2KRQ&list=PLEsfXFp6DpzTOcOVdZF-th7BS_GYGguAS)

### 2. 书籍


* Two Scoops of Django：目前有两个版本 [Two Scoops of Django: Best Practices for Django 1.11](https://www.twoscoopspress.com/products/two-scoops-of-django-1-11) 和 [Two Scoops of Django: Best Practices for Django 1.8](https://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342/ref=pd_bxgy_14_img_3?_encoding=UTF8&pd_rd_i=0981467342&pd_rd_r=FJBAW39ZPPH73AXZQRP0&pd_rd_w=qPOZk&pd_rd_wg=caiaO&psc=1&refRID=FJBAW39ZPPH73AXZQRP0) 。这本书在 Django 的名气也是非常大，基本可以说影响过大多数 Django 开发人员，如果要进阶称为 Django 专业开发者，这本书是绕不过去的必看书籍。内容主要涵盖 Django 的最佳实践。
* [Django Unleashed](https://www.amazon.com/Django-Unleashed-Andrew-Pinkham/dp/0321985079/ref=pd_sim_14_13?_encoding=UTF8&pd_rd_i=0321985079&pd_rd_r=FJBAW39ZPPH73AXZQRP0&pd_rd_w=qkuw5&pd_rd_wg=caiaO&psc=1&refRID=FJBAW39ZPPH73AXZQRP0) 内容覆盖较广，很多内容在其他书籍中并没有提及，比如密码的hash与加密等。但是没有实战项目。





## Django RESTful API

### 1. 文档



### 2. 视频



### 3. 书籍









## Django 业界最新信息






