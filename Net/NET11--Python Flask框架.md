# NET11--Python Flask框架

## 简介

+ Flask是由python实现的一个web微框架，让我们可以使用Python语言快速实现一个网站或Web服务
+ Flask基于Werkzeug WSGI工具包和Jinja2模板引擎。两者都是Pocco项目
+ 对应的有python3及python2版本

## 参考网址

https://www.jianshu.com/p/6452596c4edb

https://www.w3cschool.cn/flask/Flask-3ask1yho.html

## 安装

```shell
yum install -y flask
```

## 目录结构

```shell
flask-demo/
  ├ run.py           # 应用启动程序
  ├ config.py        # 环境配置
  ├ requirements.txt # 列出应用程序依赖的所有Python包
  ├ tests/           # 测试代码包
  │   ├ __init__.py 
  │   └ test_*.py    # 测试用例
  └ myapp/
      ├ admin/       # 蓝图目录
      ├ static/
      │   ├ css/     # css文件目录
      │   ├ img/     # 图片文件目录
      │   └ js/      # js文件目录
      ├ templates/   # 模板文件目录
      ├ __init__.py    
      ├ forms.py     # 存放所有表单，如果多，将其变为一个包
      ├ models.py    # 存放所有数据模型，如果多，将其变为一个包
      └ views.py     # 存放所有视图函数，如果多，将其变为一个包
```

## Hello world

```python
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World'
if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run()
```

+ 这是flask框架制作的一个最小的应用。使用python运行后访问localhost:5000就能看到网页显示Hello world。
+ 这里首先引入了Flask类，然后给这个类创建了一个实例，\_\_name\_\_代表这个模块的名字。因为这个模块是直接被运行的所以此时\_\_name\_\_的值是\_\_main\_\_。然后用route()这个修饰器定义了一个路由，告诉flask如何访问该函数。最后用run()函数使这个应用在服务器上运行起来。

## 模板

+ Flask的模板功能是基于[Jinja2模板引擎](http://jinja.pocoo.org/)实现的

### 示例

```python
from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/hello')

@app.route('/hello/<name>')

def hello(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.debug = True # 设置调试模式，生产模式的时候要关掉debug
    app.run(host='0.0.0.0', debug=True)
```

+ 这段代码”hello()”函数并不是直接返回字符串，而是调用了”render_template()”方法来渲染模板。方法的第一个参数”hello.html”指向你想渲染的模板名称，第二个参数”name”是你要传到模板去的变量，变量可以传多个。

+ 接下来我们创建模板文件。

  + 在当前目录下，创建一个子目录”templates”（注意，一定要使用这个名字）。

  + 在”templates”目录下创建文件”hello.html”，内容如下：

    ```html
    <!doctype html>
    
    <title>Hello Sample</title>
    
    {% if name %}
    
      <h1>Hello {{ name }}!</h1>
    
    {% else %}
    
      <h1>Hello World!</h1>
    
    {%  endif  %}
    ```

    它就是一个HTML模板，根据”name”变量的值，显示不同的内容。

    变量或表达式由”{{ }}”修饰，而控制语句由”{% %}”修饰，其他的代码，就是我们常见的HTML。

+ 查看网页源码

  + 例如，打开http://localhost:5000/hello/cxy

  + 点击查看源代码

    ```html
    <!doctype html>
    
    <title>Hello Sample</title>
    
      <h1>Hello cxy!</h1>
    ```

  + Jinja2的模板引擎还有更多强大的功能，包括for循环，过滤器等。模板里也可以直接访问内置对象如request, session等

## 模板继承

+ 一般我们的网站虽然页面多，但是很多部分是重用的，比如页首，页脚，导航栏之类的。对于每个页面，都要写这些代码，很麻烦。
+ Flask的Jinja2模板支持模板继承功能，省去了这些重复代码。

### 示例

+ 基于上面的例子，在”templates”目录下，创建一个名为”layout.html”的模板：

  ```html
  <!doctype html>
  
  <title>Hello Sample</title>
  
  <link rel="stylesheet"  type="text/css"  href="{{ url_for('static', filename='style.css') }}">
  
  <div class="page">
  
      {% block body %}
  
      {% endblock %}
  
  </div>
  ```

+ 再修改之前的”hello.html”，把原来的代码定义在”block body”中，并在代码一开始”继承”上面的”layout.html”：

  ```html
  {%  extends  "layout.html"  %}
  
  {%  block  body  %}
  
  {%  if  name  %}
  
    <h1>Hello {{ name }}!</h1>
  
  {% else %}
  
    <h1>Hello World!</h1>
  
  {%  endif  %}
  
  {%  endblock  %}
  ```

+ 打开http://localhost:5000/hello/cxy查看源代码

  ```html
  
  <!doctype html>
  
  <title>Hello Sample</title>
  
  <link rel="stylesheet"  type="text/css"  href="/static/style.css">
  
  <div class="page">
  
    <h1>Hello cxy!</h1>
  
  </div>
  ```

+ 虽然”render_template()”加载了”hello.html”模板，但是”layout.html”的内容也一起被加载了。而且”hello.html”中的内容被放置在”layout.html”中”{% block body %}”的位置上。形象的说，就是”hello.html”继承了”layout.html”。

## HTML自动转义

+ HTML标签会自动进行转义，但是如果不想某些标签转义的话，可以引入Markup类

### 示例

```python
@app.route('/')

def  index():

    return  '<div>Hello %s</div>'  %  '<em>Flask</em>'
```

+ 显示：Hello *Flask*
+ 此时\<em>标签被自动转义

```python
from  flask import  Flask,  Markup

app  =  Flask(__name__)

@app.route('/')

def  index():

    return  Markup('<div>Hello %s</div>')  %  '<em>Flask</em>'
```

+ 显示：Hello \<em>Flask\</em>
+ 此时\<em>标签没有被转义

## Request对象

```python
from flask import Flask,url_for,request,render_template

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    title = request.args.get('title', 'Default')
    return render_template('login.html', title=title)
if __name__ == "__main__":
    app.run(debug=True)
```

+ layout.html:

  ```html
  <!doctype html>
  <title>Hello Sample</title>
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
  <div class="page">
      {% block body %}
      {% endblock %}
  </div>
  ```

+ login.html

  ```html
  {% extends "layout.html" %}
  {% block body %}
  <form name="login" action="/login" method="post">
      Hello {{ title }}, please login by:
      <input type="text" name="user" />
  </form>
  {% endblock %}
  ```

+ request中”method”变量可以获取当前请求的方法

  即”GET”, “POST”, “DELETE”, “PUT”等；

+ ”form”变量是一个字典，可以获取Post请求表单中的内容

  在上例中，如果提交的表单中不存在”user”项，则会返回一个”KeyError”，你可以不捕获，页面会返回400错误（想避免抛出这”KeyError”，你可以用request.form.get(“user”)来替代）。

+ 而”request.args.get()”方法则可以获取Get请求URL中的参数

  该函数的第二个参数是默认值，当URL参数不存在时，则返回默认值。

## 会话session

+ 会话可以用来保存当前请求的一些状态，以便于在请求之前共享信息

### 示例

```python
from flask import Flask, Markup, url_for, request, render_template, redirect, session

app = Flask(__name__)
@app.route('/')
def index():
    return Markup('<dev>Hello %s</dev>') % '<em>Flask</em>'

@app.route('/hello')

@app.route('/hello/<name>')

def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        title = request.args.get('title', 'Default')
        return render_template('login.html', title=title)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

app.secret_key = '123456'
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

+ ”admin”登陆成功后，再打开”login”页面就不会出现表单了。

+ 然后打开logout页面可以登出。

+ session对象的操作就跟一个字典一样。

+ 特别提醒，使用session时一定要设置一个密钥”app.secret_key”

  如上例，不然你会得到一个运行时错误，内容大致是”RuntimeError: the session is unavailable because no secret key was set”。

  密钥要尽量复杂，最好使用一个随机数，这样不会有重复，上面的例子不是一个好密钥。

## 构建响应

在之前的例子中，请求的响应我们都是直接返回字符串内容，或者通过模板来构建响应内容然后返回。其实我们也可以先构建响应对象，设置一些参数（比如响应头）后，再将其返回。

### 示例

```python
from flask import Flask, Markup, url_for, request, render_template, redirect, session, make_response

app = Flask(__name__)
@app.route('/')
def index():
    return Markup('<dev>Hello %s</dev>') % '<em>Flask</em>'

@app.route('/hello')

@app.route('/hello/<name>')

def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            return 'Admin login successfully!'
        else:
            return 'No such user!'
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        title = request.args.get('title', 'Default')
        response = make_response(render_template('login.html', title=title), 200)
        response.headers['key'] = 'value'
        return response

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

app.secret_key = '123456'
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

+ 打开浏览器调试，在Get请求用户未登录状态下，你会看到响应头中有一个”key”项。
+ ”make_response”方法就是用来构建response对象的，第二个参数代表响应状态码，缺省就是200。

## Cookie的使用

+ 提到了Session，当然也要介绍Cookie

```python
from flask import Flask, Markup, url_for, request, render_template, redirect, session, make_response
import time

app = Flask(__name__)
@app.route('/')
def index():
    return Markup('<dev>Hello %s</dev>') % '<em>Flask</em>'

@app.route('/hello')

@app.route('/hello/<name>')

def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'))        
        else:
            return 'No such user!'
    else:
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hello %s, you logged in on %s' % (session['user'], login_time))
        else:
            title = request.args.get('title', 'Default')
            response = make_response(render_template('login.html', title=title), 200)
            response.headers['key'] = 'value'
    return response

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

app.secret_key = '123456'
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

+ 引入time模块来获取当前系统时间。

+ 我们在返回响应时，通过”response.set_cookie()”函数，来设置Cookie项，之后这个项值会被保存在浏览器中。

  这个函数的第三个参数（max_age）可以设置该Cookie项的有效期，单位是秒，不设的话，在浏览器关闭后，该Cookie项即失效。

+ 在请求中，”request.cookies”对象就是一个保存了浏览器Cookie的字典，使用其”get()”函数就可以获取相应的键值。

## 错误处理

+ 使用”abort()”函数可以直接退出请求，返回错误代码

```python
rom flask import Flask,abort

app = Flask(__name__)
@app.route('/error')
def error():
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)
```

```html
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
```

+ 上例会显示浏览器的404错误页面。
+ 有时候，我们想要在遇到特定错误代码时做些事情，或者重写错误页面，可以用下面的方法

### 示例

```python
@app.route('/error')
def error():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
```

+ 不过，在实际开发过程中，我们并不会经常使用”abort()”来退出，常用的错误处理方法一般都是异常的抛出或捕获。

+ 装饰器”@app.errorhandler()”除了可以注册错误代码外，还可以注册指定的异常类型。

+ 让我们来自定义一个异常：

  ```python
  class InvalidUsage(Exception):
      status_code = 400
      def __init__(self, message, status_code=400):
          Exception.__init__(self)
          self.message = message
          self.status_code = status_code
  ```

  ```python
  @app.errorhandler(InvalidUsage)
  def invalid_usage(error):
      response = make_response(error.message)
      response.status_code = error.status_code
      return response
  
  @app.route('/exception')
  def exception():
      raise InvalidUsage('No privilege to access to the resource', status_code=403)
  ```

  我们在上面的代码中定义了一个异常”InvalidUsage”，同时我们通过装饰器”@app.errorhandler()”修饰了函数”invalid_usage()”，装饰器中注册了我们刚定义的异常类。这也就意味着，一但遇到”InvalidUsage”异常被抛出，这个”invalid_usage()”函数就会被调用.

## url重定向

+ Flask的URL规则是基于Werkzeug的路由模块。

+ 模块背后的思想是基于 Apache 以及更早的 HTTP 服务器主张的先例，保证优雅且唯一的 URL。

+ 示例

  ```python
  @app.route('/projects/')
  def projects():
      return 'The project page'
  
  @app.route('/about')
  def about():
      return 'The about page'
  ```

  + 访问第一个路由不带/时，Flask会自动重定向到正确地址
  + 访问第二个路由时末尾带上/后Flask会直接报404 NOT FOUND错误。

+ 重定向”redirect()”函数的使用在上面例子中已有出现。作用就是当客户端浏览某个网址时，将其导向到另一个网址。常见的例子，比如用户在未登录时浏览某个需授权的页面，我们将其重定向到登录页要求其登录先。

  ```python
  @app.route('/')
  def index():
      if 'user' in session:
          return 'Hello %s!' % session['user']
      else:
          return redirect(url_for('login'), 302)
  ```

  + “redirect()”的第二个参数是HTTP状态码，可取的值有301, 302, 303, 305和307，默认即302

## 完整测试代码

```python
from flask import Flask, Markup, url_for, request, render_template, redirect, session, make_response, abort
import time

class InvalidUsage(Exception):
    status_code = 400
    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

app = Flask(__name__)
@app.route('/')
def index():
    if 'user' in session:
        return 'Hello %s!' % session['user']
    else:
        return redirect(url_for('login'), 302)

@app.route('/hello')

@app.route('/hello/<name>')

def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['user'] == 'admin':
            session['user'] = request.form['user']
            response = make_response('Admin login successfully!')
            response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'))        
        else:
            return 'No such user!'
    else:
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hello %s, you logged in on %s' % (session['user'], login_time))
        else:
            title = request.args.get('title', 'Default')
            response = make_response(render_template('login.html', title=title), 200)
            response.headers['key'] = 'value'
    return response

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/error')
def error():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    return response

@app.route('/exception')
def exception():
    raise InvalidUsage('No privilege to access to the resource', status_code=403)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

app.secret_key = '123456'
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

