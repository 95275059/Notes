# PythonDjango1--基础

## 简介

### 介绍

* Django是一个基于Python的**Web应用框架**

* 和Flask的区别：

  奉行“包含一切”的哲学

  Django包含了几乎所有的Web开发功能

  例如：身份验证、URL路由、模板系统、ORM、数据库迁移等功能

* Django看上去失去了一些弹性，但是在某种程度上开发网站会更有效率

### Django工作方式

* Django是MTV框架，和MVC类似

  * MVC框架 : 业务模型（model）、用户界面（view）、控制器（controller）

    使用MVC的目的是将M和V的实现代码分离，从而使同一个程序可以使用不同的表现形式。

    比如一批统计数据可以分别用柱状图、饼图来表示。

    C存在的目的则是确保M和V的同步，一旦M改变，V应该同步更新。

  * MTV框架 : 模型（model）、模板（template）、视图（view）

    * Model(模型)： 负责业务对象与数据库的对象(ORM)。
    * Template(模板)：负责如何把页面展示给用户。
    * View(视图)：负责业务逻辑，并在适当的时候调用Model和Template。

    Django还有一个urls分发器，它的作用是将一个个URL的页面请求分发给不同的View处理，view再调用相应的Model和Templage。

  * Django将MVC中的视图进一步分解为Django视图和Django模板两部分。分别决定“展示哪些数据”和“如何展现”

    使得Django模板根据需要随时替换，而不仅仅限于内置的模板

    MVC中的Controller控制器部分，由Django框架的URL conf来实现的

* 工作流程

  ![Django1-1](E:\Notes\Python\Django1-1.png)

### Django框架的组成部分

* ORM（Object Relational Mapping，面向对象的映射器，用于数据模型和关系型数据库间的媒介）
* 一个基于正则表达式的URL分发器
* 一个视图系统，用于处理请求
* 一个模板系统
* 除此之外，还包含一些组件
  * 一个轻量级的、独立的Web服务器，用于开发和测试
  * 一个表单序列化及验证系统
  * 一个缓存框架
  * 中间件支持
  * 内置的分发系统
  * 序列化系统
  * 自动化管理界面
  * 。。。

### Django框架的优缺点

* 优点

  * 文档非常齐全

  * 全套的解决方案

    例如，cache，session，orm

  * 强大的URL路由配置

* 缺点

  * 系统紧耦合

    例如ORM，Template、SQLAlchemy

  * 自带的ORM远不如SQLAlchemy
  
  * Template功能比较弱，不能插入Python代码
  
  * URL配置虽然强大，但全部要手写

## 安装Django开发环境

```shell
pip install Django
```

* 测试

  ```shell
  >>> import django
  >>> print(django.get_version())
  3.2.5
  >>>
  ```

## 使用startproject命令创建Django Web工程

### 创建工程

* 安装完Django后，会有一个全局的脚本文件django-admin.py，该文件提供了一个命令startproject，后跟工程名字

  ```
  django-admin startproject hello
  ```

* 进入hello目录

  + hello
    + \__init__.py
    + asgi.py
    + settings.py
    + urls.py
    + wsgi.py
  + manage.py : 用于管理工程

### 启动程序

* 进入工程目录

* 启动

  ```shell
  python manage.py runserver 0.0.0.0:8000
  ```

  * runserver 0.0.0.0:8000表示将django进程使用的socket绑定ip设置为INADDR_ANY(0)，因此socket会在8000端口监听从本机所有网卡发来的数据，相当于绑定了本机的所有ip地址。

  ```shell
  E:\Python\hello>python manage.py runserver 0.0.0.0:8000
  Watching for file changes with StatReloader
  Performing system checks...
  
  System check identified no issues (0 silenced).
  
  You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
  Run 'python manage.py migrate' to apply them.
  July 28, 2021 - 20:09:30
  Django version 3.2.5, using settings 'hello.settings'
  Starting development server at http://0.0.0.0:8000/
  Quit the server with CTRL-BREAK.
  ```

  * 第一次运行，需要创建一个数据库，会出现：

    ```shell
    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    ```

    提示需要将相关信息放进去

  * 按照提示，输入：

    ```shell
    E:\Python\hello>python manage.py migrate
    Operations to perform:
      Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying admin.0002_logentry_remove_auto_add... OK
      Applying admin.0003_logentry_add_action_flag_choices... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_email_max_length... OK
      Applying auth.0004_alter_user_username_opts... OK
      Applying auth.0005_alter_user_last_login_null... OK
      Applying auth.0006_require_contenttypes_0002... OK
      Applying auth.0007_alter_validators_add_error_messages... OK
      Applying auth.0008_alter_user_username_max_length... OK
      Applying auth.0009_alter_user_last_name_max_length... OK
      Applying auth.0010_alter_group_name_max_length... OK
      Applying auth.0011_update_proxy_permissions... OK
      Applying auth.0012_alter_user_first_name_max_length... OK
      Applying sessions.0001_initial... OK
    ```

  * 然后工程目录下会出现db.sqlite3，存放着相关的信息

  * 再次运行

    ```shell
    E:\Python\hello>python manage.py runserver 0.0.0.0:8000
    Watching for file changes with StatReloader
    Performing system checks...
    
    System check identified no issues (0 silenced).
    July 28, 2021 - 20:15:59
    Django version 3.2.5, using settings 'hello.settings'
    Starting development server at http://0.0.0.0:8000/
    Quit the server with CTRL-BREAK.
    ```

  * 打开浏览器，进入网址localhost:8000测试服务器

## 手动打造第一个Django Web应用

```python
import os
import sys
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on' # 显示相关调试信息
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32)) # 随机生成一个32位的加密字符串，加密Web相关信息

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',') # 获取允许访问的host列表，默认是localhost

settings.configure(
    DEBUG = DEBUG,
    SECRET_KEY = SECRET_KEY,
    ALLOWED_HOSTS = ALLOWED_HOSTS,
    ROOT_URLCONF = __name__
)    # 配置settings


from django.conf.urls import re_path
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

urlpatterns = [
    re_path(r'^$', index) # 根路径
]

if __name__ == '__main__':
	from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
```

* 启动服务

  ```java
  E:\Python\hello>python first.py runserver
  Watching for file changes with StatReloader
  Performing system checks...
  
  System check identified no issues (0 silenced).
  July 28, 2021 - 21:11:33
  Django version 3.2.5, using settings None
  Starting development server at http://127.0.0.1:8000/
  Quit the server with CTRL-BREAK.
  ```

* 访问：127.0.0.1:8000

## 用PyCharm开发Django Web应用

* 直接选择Django项目进行新建
* 首次运行同样需要执行`python manage.py migrate`命令

### 进行简单的开发

* 创建views目录

* 在views目录下新建First.py

  ```python
  from django.http import HttpRequest
  
  def index(request):
      return HttpRequest('PyCharm')
  ```

* 修改urls.py

  ```python
  from django.contrib import admin
  from django.urls import path, re_path
  from FirstDjango.views import First
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      re_path(r'^hh/', First.index)
  ]
  ```

  * 注意：需要用到正则表达式的，用re_path，否则用path

## 使用WSGI启动Server

* 之前使用runserver启动应用，但是是用来测试应用的，并不适合产品部署的安全性

### WSGI(Web Server Gateway Interface)

* **Web服务器网关接口**（**Python Web Server Gateway Interface**，缩写为WSGI）是为Python语言定义的Web服务器和Web应用程序或框架之间的一种简单而通用的接口。

* 是一份有关Web服务器如何与Django一类的应用框架通信的规范，由PEP333制定
* 使用WSGI规范的服务器：
  * Apache 下的 mod_wsgi
  * gunicorn
  * uWSGI
  * ...

### 安装gunicorn（仅支持linux系统）

```shell
pip install gunicorn
```

* 测试

  ```python
  from django.core.wsgi import get_wsgi_application
  ```

### 安装apache+mod_wsgi

https://kaspar.blog.csdn.net/article/details/99463038?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-13.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-13.control

https://www.cnblogs.com/wcwnina/p/9974642.html

https://blog.csdn.net/weixin_40754816/article/details/80955817

* http.conf

  ```shell
  LoadFile "c:/users/cxy/anaconda3/envs/python36/python36.dll"
  LoadModule wsgi_module "c:/users/cxy/anaconda3/envs/python36/lib/site-packages/mod_wsgi/server/mod_wsgi.cp36-win_amd64.pyd"
  WSGIPythonHome "c:/users/cxy/anaconda3/envs/python36"
  
  WSGIScriptAlias / E:/Python/MyDjango36/MyDjango36/wsgi.py
  WSGIPythonPath  E:/Python/MyDjango36
  
  <Directory E:/Python/MyDjango36/MyDjango36>  
  <Files wsgi.py>  
      Require all granted  
  </Files>  
  </Directory>  
  
  
  Alias /static E:/Python/MyDjango36/MyDjango36/static
  <Directory E:/Python/MyDjango36/MyDjango36/static>  
      AllowOverride None  
      Options None  
      Require all granted  
  </Directory>  
    
  
  Alias /media E:/Python/MyDjango36/MyDjango36/media
  <Directory E:/Python/MyDjango36/MyDjango36/media>  
      AllowOverride None  
      Options None  
      Require all granted  
  </Directory> 
  ```

* apache安装过程中的问题：

  * apache启动错误 AH00072: make_sock: could not bind to address [::]:443

    打开httpd-ahssl.conf  listen的端口改成442

  * 以管理员身份打开cmd
  
  * 修改系统环境变量后，需重启才能生效
  
* 数据库换成mysql

  https://blog.csdn.net/qq_38680405/article/details/118684617

  https://blog.csdn.net/G_whang/article/details/118650839

* 报错：
  * 报错 raise RuntimeError("populate() isn't reentrant
    * 可能是数据库没安装
  
* 启动服务

  ```
  net start mysql
  net stop mysql
  ```

  ```shell
  net start apache
  net stop apache
  httpd -k start -n apache
  httpd -k stop -n apache
  ```

### 使程序first.py支持WSGI

```python
import os
import sys
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on' # 显示相关调试信息
SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32)) # 随机生成一个32位的加密字符串，加密Web相关信息

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',') # 获取允许访问的host列表，默认是localhost

settings.configure(
    DEBUG = DEBUG,
    SECRET_KEY = SECRET_KEY,
    ALLOWED_HOSTS = ALLOWED_HOSTS,
    ROOT_URLCONF = __name__
)    # 配置settings


from django.conf.urls import re_path
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application   

application = get_wsgi_application()   

def index(request):
    return HttpResponse('Hello World')

urlpatterns = [
    re_path(r'^$', index) # 根路径
]

if __name__ == '__main__':
	from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
```

添加：

```python
from django.core.wsgi import get_wsgi_application   

application = get_wsgi_application()   
```

### 运行

* gunicorn

  ```shell
  gunicorn first.py
  ```

* mod_wsgi

  ```shell
  httpd -k start -n apache
  ```











