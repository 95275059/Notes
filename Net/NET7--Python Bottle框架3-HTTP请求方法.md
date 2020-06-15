# NET7--Python Bottle框架3-HTTP请求方法

1. 先验知识

   所有route默认使用GET方法，只响应GET请求。

   可以给route()函数指定method参数。或用get()，post()或delete()等函数来代替route()函数。

2. POST请求方法示例

   ```python
   from bottle import route,run,request,static_file
   
   @route('/login')
   def login():
       '''
       不指定方法时，默认GET方法
       登录页面，html代码直接返回到网页中
       '''
       return static_file('login.html',root='./')
   
   @route('/login',method='POST')
   def do_login():
       '''
       进行POST动作
       函数名不能与前后函数有同名
       登录动作，当访问login页面并且带了POST请求时，该函数将响应
       '''
       username=request.forms.get('username')
       password=request.forms.get('password')
       return '<p>账号:%s</p><p>密码:%s</p>'%(username,password)
   
   run(host='localhost',port='8080',debug=True)
   
   ```

   login.html:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <meta charset="UTF-8">
       <title>Login</title>
   </head>
   <body>
       <form action="/login" method="post">
           Username: <input name="username" type="text" />
           Password: <input name="password" type="password" />
           <input value="Login" type="submit" />
       </form>
   </body>
   </html>
   ```

3. 查询变量

   + GET方法传递键值

     ```python
     from bottle import run,route,request
     
     @route('/info')
     def info():
         id=request.query.id
         name=request.query.name
         age=request.query.age
         return "id=%s,name=%s,age=%s"%(id,name,age)
     
     run(host='localhost',port='8080')
     ```

     浏览器访问：http://localhost:8080/info?id=1&name=cxy&age=18

   + POST方法传递键值

     看第二条。

     用request.forms方法获取相关值，例如

     + username=request.forms.get('username')
     + password=request.forms.get('password')

     参数是从HTML表单传递过来的，login.html中定义了表单的方法是POST，input的name是username和password。

4. HEAD

    HEAD 方法类似于 GET 方法，但服务器不会返回 HTTP 响应正文，一般用于获取 HTTP 原数据而不用下载整个页面。

   Bottle 像处理 GET 请求那样处理 HEAD 请求，但是会自动去掉 HTTP 响应正文。无需亲自处理 HEAD 请求。 

5. ANY

   非标准的 ANY 方法做为一个低优先级的 fallback：在没有其它 route 的时候，监听 ANY 方法的route 会匹配所有请求，而不管请求的方法是什么。这对于用做代理的 route 很有用，可将所有请求都重定向给子应用。 