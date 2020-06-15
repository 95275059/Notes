# NET6-- Python Bottle框架2--路由

1. 静态路由

   ```python
   from bottle import route,run
   
   @route('/hello')
   def hello():
   	return "Hello www.bootleCXY.com"
   
   run(host='localhost',port='8080')
   ```

   route()函数将一段代码绑定到一个URL。

   在浏览器请求一个URL的时候，框架自动调用与之响应的函数，接着将函数的返回值发送给浏览器。

   run()函数启动了**内置的开发服务器**。他监听localhost的8080端口并形影请求。ctrl+c可以终止。

2. 动态路由

   ```python
   from bottle import route,run
   
   @route('/hello/<name>')
   def helloName(name):
   	return "Hello %s"%name
   
   run(host='localhost',port='8080')
   ```

   ```python
   from bottle import route,run
   
   @route('/hello/:name')
   def helloName(name):
   	return "Hello %s"%name
   
   run(host='localhost',port='8080')
   ```

   动态路由：包含通配符的route，能匹配多个URL地址。

   一个通配符包含在一对尖括号中，或冒号后面，通配符之间用“/”隔开。

   URL中的通配符都会当做参数传给回调函数，直接在回调函数中使用。