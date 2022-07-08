# PythonDjango8--Session和Cookie

## Cookie

* Cookie：保存在客户端的数据，可以通过Cookie来区分不同的客户端

* 如何将数据从服务端保存到客户端？

  服务端通过HTTP响应头发送Cookies到客户端，客户端将Cookie写入本地

  Http Response Headers 中对应字段：

  ```python
  Set-Cookie: key=value; key=value
  ```

* 客户端在后续访问服务端时，需要将保存在本地的Cookie数据发送给服务端

  客户端通过HTTP请求头发送Cookie数据到服务端

  HTTP Request Headers 中对应字段：

  ```python
  Cookie: key=value; key=value
  ```

### 在Django使用Cookie

```python
from django.http import HttpResponse


def set_value(request):
    if 'value' in request.GET:
        response = HttpResponse('Your Value is now %s.' % request.GET.get('value'))
        response.set_cookie('value', request.GET.get('value'))
        return response
    return HttpResponse('You didn\'t give a value.')


def show_value(request):
    if 'value' in request.COOKIES:
        return HttpResponse('Your value is %s.' % request.COOKIES.get('value'))
    else:
        return HttpResponse('You did\'t have a value.')
```

## 会话（Session）

* Session：保存在服务端的数据，因此也可以将Session称为服务端的Cookie，都以字典形式保存

* 一个Session对应一个客户端

  例如：一个服务端server，用户的同一台机子上分别安装了不同的两个客户端：Firefox和Chrome，用同一个IP分别通过这两个客户端访问同一个服务端，服务端会为这两个客户端创建两个单独的Session，是完全格力的

* Session是高度依赖于Cookie

  Session会创建一个ID，这个ID是通过Cookie来传递的

  一开始客户端访问服务端，服务端会产生一个ID，然后通过Set-Cookie返回给客户端；客户端接收到Cookie后会将数据保存到本地；之后客户端再次访问服务端时，会通过Cookie将这个ID(键为sessionid)发送到服务端；服务端收到Session ID后，会在整个的Session字典中搜索特定的对应的Session对象。

### 在Django中使用Session

* 在setings.py中确认配置：

  ```python
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',   # here
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'mydjango'
  ]
  
  MIDDLEWARE = [
      'django.middleware.security.SecurityMiddleware',
      'django.contrib.sessions.middleware.SessionMiddleware',   # here
      'django.middleware.common.CommonMiddleware',
      'django.middleware.csrf.CsrfViewMiddleware',
      'django.contrib.auth.middleware.AuthenticationMiddleware',
      'django.contrib.messages.middleware.MessageMiddleware',
      'django.middleware.clickjacking.XFrameOptionsMiddleware',
  ]
  ```

* 示例

  ```python
  def set_data(request):
      if 'data' in request.GET:
          response = HttpResponse('Your data is now %s.' % request.GET.get('data'))
          request.session['data'] = request.GET.get('data')
          return response
      else:
          return HttpResponse('Your did\'t provide a data.')
  
  def show_data(request):
      if 'data' in request.session:
          response = HttpResponse('Your data is now %s.' % request.session.get('data'))
          return response
      else:
          return HttpResponse('You did\'t have a data.')
  ```

## 用会话实现免登录页面

* 内部实现原理：

  当用户输入用户名和密码登录后，服务端判断用户名和密码正确之后，将在客户端对应的session中放入已登录的标志

  当用户再次访问时服务端时，将重新获取session对象的标志，若是已登录，则直接跳入主页面

* 示例：test15.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>免登录测试</title>
  </head>
  <body>
      <form action="/login_action_CS/" method="post">
          username:<input name="username"><p></p>
          password:<input name="password" type="password"><p></p>
          <input type="submit" value="登录">
      </form>
  </body>
  </html>
  ```

  ```python
  from django.shortcuts import render
  
  # 显示登录页面
  def loginCS(request):
      return render(request, 'test15.html')
  
  # 处理登录动作
  from django.views.decorators.csrf import csrf_exempt
  
  @csrf_exempt
  def login_action_CS(request):
      if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          if username == 'cxy' and password == '123456':
              request.session['login'] = True
              return HttpResponse('Login success!')
          else:
              return HttpResponse('Your username and password did\'t match.')
      else:
          return HttpResponse('Only post are allowed.')
  
  # 主页
  def home_CS(request):
      if 'login' in request.session:
          if request.session.get('login') == True:
              return HttpResponse('HOME PAGE')
          else:
              return HttpResponse('DID NOT LOGIN')
      else:
          return HttpResponse('DID NOT LOGIN')
  
  # 注销
  def logout_CS(request):
      if 'login' in request.session:
          request.session['login'] = False
      return HttpResponse('Logout success.')
  ```

  