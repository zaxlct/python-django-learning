### Django使用redis做缓存层

参考文档：
http://django-redis-chs.readthedocs.io/zh_CN/latest/#		//官方
http://yshblog.com/blog/156					//案例实践
http://www.runoob.com/redis/redis-tutorial.html			//redis使用教程

注意：
1. 该教程的前提是已经安装了redis服务，并正常运行，没有安装的请自行百度
2. 缓存层使用了redis，如果有多个服务 需要使用到redis，请先停止，然后再测试，要不很麻烦。！！！


版本：
django：1.9
redis-server：3.0.6
python：2.7
django-redis：4.8.0
python redis：2.10.5


### step1：安装redis相关插件
```bash
pip install django-redis
pip install redis
```


### step2：配置setting文件（还有其他参数，请看官方文档）
```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/1",  //这个很重要，1是代表数据库名，如果之前使用异步需要redis的，建议分开使用
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD": "mysecret" 这个是redis登录密码
        }
    }
}
```


### step3：测试通过django-redis写入数据到redis中
```bash
[root@9683705d680e operation]# python manage.py shell  	//注意我们测试的时候用manage shell，因为这个是已经默认好环境的了
>>> from django.core.cache import cache			//导入模块
>>> cache.set("test", "test11111") 				//保存数据进redis中
True
>>> cache.get("test")					//从redis中取出数据
'test11111'
>>> 
```


### step4：查看redis是否有数据
```
[root@9683705d680e ~]# redis-cli	//连接redis，怎么操作请自行百度
127.0.0.1:6379> select 1		//选择数据库，前面是设置为1，即选择1
OK
127.0.0.1:6379> keys *
 1) ":1:test"		//这个是刚刚保存的数据
127.0.0.1:6379> 
```


### step5：测试没有问题，就可以写代码（views.py文件中写，或自定义模块导入，随便吧）
```python
from django.core.cache import cache		//导入模块
class RequestImage(View):
    def get(self, request):
        key = "apache"
        if cache.has_key(key):
            data = cache.get(key)	//找到数据就返回值
        else:			//找不到数据，就重新创建数据，并返回数据（这个逻辑很重要）
            data = "zabbxi-ssh-test"
            cache.set(key, data)
        return HttpResponse(data)	//就是有没有，都返回。
```        


### step6：返回到前端显示（部分代码）
```javascript
function select(){
	$.get("/requestimage/", function(data){
		alert(data);   //返回一个字典
		for (var i in data){
			$("#modules").append("<option value=data[i]>" + data[i] + "</option>");
			}
		});
	}
```


