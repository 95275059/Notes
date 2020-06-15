# NET4--WSGI框架

1. Web应用

   + 浏览器发送一个HTTP请求；

   + 服务器收到请求，生成一个HTML文档；

   + 服务器把HTML文档作为HTTP响应的Body发送给浏览器；

   + 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

   ​       所以，最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

   ​       如果要动态生成HTML，就需要把上述步骤自己来实现。不过，==接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活==，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。

   ​        正确的做法是==底层代码由专门的服务器软件实现==，我们用Python专注于生成HTML文档。==因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。==
   
   ​        这个接口就是WSGI：Web Server Gateway Interface。

2. 示例

   "Hello,web!"

   ```python
   #hello.py
   def application(environ, start_response):
       start_response('200 OK', [('Content-Type', 'text/html')])
       return [b'<h1>Hello, web!</h1>']
   ```

   + application()函数就是符合WSGI标准的一个HTTP处理函数

     + environ:包含所有HTTP请求信息的一个dict对象

     + start_response:一个发送HTTP响应的函数

       代码中发送了一个HTTP响应的Header

       **Header只能发送一次**，即只能调用一次start_response()函数。

       参数：

       + HTTP响应码

       + 一组list表示的HTTP Header,每个Header用一个包含两个str的tuple表示。（参考NET1--HTTP）

         通常情况下，都应该把Content-Type头发送给浏览器。

   ---

   WSGI服务器

   ```python
   # server.py
   # 从wsgiref模块导入:
   from wsgiref.simple_server import make_server
   # 导入我们自己编写的application函数:
   from hello import application
   
   # 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
   httpd = make_server('', 8000, application)
   print('Serving HTTP on port 8000...')
   # 开始监听HTTP请求:
   httpd.serve_forever()
   ```

   + application()函数必须由WSGI服务器来调用。

     有很多符合WSGI规范的服务器，我们可以挑选一个来用。

   + Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。

     所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

   注：hello.py和server.py需要在同一目录下。

   ---

   测试

   + 命令行输入 python server.py开启浏览器

     注：ctrl+C终止服务器

   + 打开浏览器，输入http://localhost:8000/

   + 如果`8000`端口已被其他程序占用，启动将失败，请修改成其他端口。



