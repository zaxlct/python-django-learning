## django开发中，有不同的返回给前端的函数，下面介绍几个，在开发中遇到的小情况：
``` python
return render(request, "vpn_add.html")			#最常用的
return HttpResponseRedirect(reverse('vpn_add'))		#比较常用的（提交页面或跳转时常用）
return render_to_response("vpn_add.html", {"meg": 1})	#一般用的
```


### 第一种： `render(request, "页面地址", 返回值)`
常用场景：get页面的时候最常用
依赖模块：`from django.shortcuts import render`

例子：（部分代码）
```python
class test(Views):
	def get(self, request):
		return render(request, "index.html", {"test": "返回值"})
```    

分析：当用户访问一个页面时，首先使用get提交方式获取页面数据，加载数据，在这个方面上render()函数是一个很方便很使用的函数

注意：页面跳转的时候需要注意
直接使用rander()函数跳转：页面是跳转了，但是是一种伪跳转，页面已经显示了跳转的内容，但是留意URL地址后发现。
依然是使用着注册页面的URL地址，刷新页面后依然跳回到原地址问题（这个问题导致的原因是url.py文件指定的URL函数导致）


### 第二种：`HttpResponseRedirect(reverse('地址名'))`	
常用场景：在提交表单时使用情况很多
依赖模块：
```python
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
```

例子：（部分代码）
```python
def post(self, request):
        loginform = UserLoginForm(request.POST)
        if loginform.is_valid():
            user = request.POST.get("username", "")
            passwd = request.POST.get("password", "")
            auth = authenticate(username = user, password = passwd)
            if auth is not None:
                if auth.is_active:
                    login(request, auth)
                    return HttpResponseRedirect(reverse('video'))
```                    

分析：这个场景很重要，当一个用户提交信息后，正常来说提交成功后会自动刷新页面然后等待下一次提交状态，在三种返回机制中
第一种和第三种机制是没有办法实现，都会出现一个情况“在页面刷新后，无端端重新提交一次”，导致重新刷新一次数据库，这样用户体验和对服务器压力不好，但是奇怪的是，这种情况不是经常出现，会偶然出现一次。

注意：
1. 这个函数是没有办法传递参数到前端页面的，也就是说，这个完完整整是路径重定向作用。
2. 使用 `HttpResponseRedirect()`函数跳转，这是真实的跳转方式，从一个地址只向另一个地址，从一个页面指向另一个页面。
对比：如果是原页面跳转使用`rander()`，如果交互完成后跳转到指定URL使用`HttpResponseRedirect()`


### 第三种：`render_to_response`（“跳转页面”， 参数）
常用场景：post和get刷新时都可以，比render()函数高级，灵活使用
依赖模块：
```
from django.shortcuts import render_to_response
```
例子：无
