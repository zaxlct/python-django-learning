# coding:utf-8
# author:eycode
# 该文件用于提供测试接口
# Flask + API模块

# 在本代码案例中必须安装两个模块：
# flask模块：pip install flask
# http认证模块(flask-httpauth)：pip install flask-httpauth
 
# 参考地址：
# RESTful API中文版：http://www.pythondoc.com/flask-mega-tutorial/index.html
# RESTful API快速入门：http://www.cnblogs.com/kaituorensheng/p/4645080.html
# RESTful API官方版本：http://flask-restless.readthedocs.io/en/stable/api.html
# Flask官方：http://www.pythondoc.com/flask-mega-tutorial/index.html

from flask import Flask, jsonify

# 简单版本：
# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return "Hello Python"

# if __name__ == "__main__":
# 	app.run(debug=True)
# 或
# 	app.run(host='0.0.0.0',port=9000)



# 测试：打开浏览器输入：http://127.0.0.1:5000
# 返回结果：
# Hello Python



# 简单分析：
# 第9行：app是Flask的实例，它接收包或者模块的名字作为参数，但一般都是传递__name__。 
# 让flask.helpers.get_root_path函数通过传入这个名字确定程序的根目录，以便获得静态文件和模板文件的目录

# 第11~13行：使用app.route装饰器会将URL和执行的视图函数的关系保存到app.url_map属性上。 
# 处理URL和视图函数的关系的程序就是路由，这里的视图函数就是hello_world。

# 第16行：执行app.run就可以启动服务了。默认Flask只监听虚拟机的本地127.0.0.1这个地址，端口为5000。 
# 而我们对虚拟机做的端口转发端口是9000，所以需要制定host和port参数，0.0.0.0表示监听所有地址，这样就可以在本机访问了。 
# 服务器启动后，会调用werkzeug.serving.run_simple进入轮询，默认使用单进程单线程的werkzeug.serving.BaseWSGIServer处理请求， 
# 实际上还是使用标准库BaseHTTPServer.HTTPServer，通过select.select做0.5秒的“while TRUE”的事件轮询。 
# 当我们访问“http://127.0.0.1:9000/”,通过app.url_map找到注册的“/”这个URL模式,就找到了对应的hello_world函数执行，返回“hello world!”,状态码为200。 
# 如果访问一个不存在的路径，如访问“http://127.0.0.1:9000/a”,Flask找不到对应的模式，就会向浏览器返回“Not Found”，状态码为404




# 构建一个简单的入口
# app = Flask(__name__)

# tasks = [
# 	{
# 	'id':1,
# 	'name':"eycode",
# 	'age':23,
# 	'sex':"男"
# 	},
# 	{
# 	'id':2,
# 	'name':"imay",
# 	'age':1,
# 	'sex':'女'
# 	}
# ]

# @app.route("/api/v1.0/tasks", methods=['GET'])
# def _tasks():
# 	return jsonify({'tasks':tasks})

# if __name__ == "__main__":
# 	app.run(host='0.0.0.0', port=9000, debug=True)


# 打开浏览器输入：http://127.0.0.1:9000/api/v1.0/tasks
# 返回结果：
# {
#   "tasks": [
#     {
#       "age": 23, 
#       "id": 1, 
#       "name": "eycode", 
#       "sex": "\u7537"
#     }, 
#     {
#       "age": 1, 
#       "id": 2, 
#       "name": "imay", 
#       "sex": "\u5973"
#     }
#   ]
# }




# GET方式递交参数，返回值
# from flask import abort, make_response

# app = Flask(__name__)

# tasks = [
# 	{
# 	'id':1,
# 	'name':"eycode",
# 	'age':23,
# 	'sex':"男"
# 	},
# 		{
# 	'id':2,
# 	'name':"imay",
# 	'age':23,
# 	'sex':"男"
# 	},
# 		{
# 	'id':3,
# 	'name':"benet",
# 	'age':23,
# 	'sex':"男"
# 	}
# ]

# @app.route('/api/v1.0/<int:task_id>', methods=['GET'])
# def get_tasks(task_id):

# 	# 当传进的id是多少就读取字典的哪个部分
# 	task = filter(lambda t:t['id'] == task_id, tasks)
# 	if len(task) == 0:
# 		"""判断是否存在，如果不存在，则返回404页面"""
# 		abort(404)
# 	return jsonify({'task':task[0]})

# # 自定义404信息(以json的方式返回数据)
# @app.errorhandler(404)
# def not_found(error):
# 	return make_response(jsonify({'error': 'Not found'}), 404)

# if __name__ == "__main__":

# 	# 关闭调试
# 	app.run(debug=False)



# 测试：http://127.0.0.1:5000/api/v1.0/1
# 返回结果：
# {
#   "task": {
#     "age": 23, 
#     "id": 1, 
#     "name": "eycode", 
#     "sex": "\u7537"
#   }
# }

# 测试: http://127.0.0.1:5000/api/v1.0/5
# 返回结果：
# {
#   "error": "Not found"
# }




# 通过Post方式提交数据
# from flask import request

# app = Flask(__name__)

# tasks = [
# 	{
# 	'id':1,
# 	'name':"eycode",
# 	'age':23,
# 	'sex':"男"
# 	},
# 		{
# 	'id':2,
# 	'name':"imay",
# 	'age':23,
# 	'sex':"男"
# 	},
# 		{
# 	'id':3,
# 	'name':"benet",
# 	'age':23,
# 	'sex':"男"
# 	}
# ]


# @app.route('/api/v1.0/tasks', methods=['POST'])
# def create_task():
# 	if not request.json or not 'title' in request.json:
# 		abort(404)

# 	task = {
# 	'id': tasks[-1]['id'] + 1,
# 	'title': request.json['title'],
# 	'sex': request.json.get('sex', ""),
# 	'done': False
# 	}
# 	tasks.append(task)
# 	return jsonify({'task':task}), 201

# if __name__ == "__main__":
# 	app.run(debug=False)


# 测试：curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:5000//api/v1.0/tasks
# 一些参数：
# -i :显示信息
# -H：指定http头
# -X：提交方式不区分大小写
# -d：字典


# API安全性使用
from flask.ext.httpauth import HTTPBasicAuth
from flask import abort, make_response
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == "eycode":
		return 'python'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error':'Unauthorized access'}), 403)

tasks = [
	{
	'id':1,
	'name':"eycode",
	'age':23,
	'sex':"男"
	},
		{
	'id':2,
	'name':"imay",
	'age':23,
	'sex':"男"
	},
		{
	'id':3,
	'name':"benet",
	'age':23,
	'sex':"男"
	}
]

app = Flask(__name__)

@app.route('/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == "__main__":
	app.run()


# 测试：http://127.0.0.1:5000/api/v1.0/tasks
# 返回结果：
# {
#   "error": "Unauthorized access"
# 

# 测试：curl -u eycode:python -i http://localhost:5000/api/v1.0/tasks
# 一些参数：
# -u：用户名：密码

# 返回结果：
	# {
	# 'id':1,
	# 'name':"eycode",
	# 'age':23,
	# 'sex':"男"
	# },
	# 	{
	# 'id':2,
	# 'name':"imay",
	# 'age':23,
	# 'sex':"男"
	# },
	# 	{
	# 'id':3,
	# 'name':"benet",
	# 'age':23,
	# 'sex':"男"
	# }













