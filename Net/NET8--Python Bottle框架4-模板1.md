# NET8--Python Bottle框架4-模板1

1. SimpleTemplate模板引擎

   可以通过template()函数或view()修饰器来渲染一个模板。只需提供模板的名字和传递给模板的变量。

   默认情况，Bottle会在./views/目录查找模板文件。

   可在bottle.TEMPLATE_PATH这个列表中添加更多的模板路径。

   view()修饰器允许在回调函数中返回一个字典，将其传递给模板，同template()函数

   ---

2. 更换模板目录

   如果不使用./views目录作为模板目录

   + 新创建一个模板目录
   + 用 bottle.TEMPLATE_PATH.append('目录地址') 添加

   ---

3. 模板示例

   在项目目录下新建views文件夹

   + 在views文件夹下新建loginn.tpl文件夹

     ```python
     <!DOCTYPE html>
     <html>
         <head>
         <title>登陆页面</title>
         </head>
         <body>
             <p><h2>管理员登陆2</h2></p>
             <form action="/login" method="post">
                 Username: <input name="username" type="text" />
                 Password: <input name="password" type="password" />
                 <input value="Login" type="submit" />
             </form>
         </body>
     </html>
     ```

     注：关于.tpl的创建问题还有问题，创建的都是.html文件

   + template_study.py

     ```python
     from bottle import route,run
     from bottle import template
     
     @route('/login')
     def login():
         return template('loginn')
     
     run(host='localhost',port=8080)
     ```

     注：loginn是模板名，这里不需要填写后缀.tpl

   ---

4. 向模板传递数据

   将参数传递到模板中显示

   + 传递数值

     + info.html

       ```python
       <!DOCTYPE html>
       <head>
           <title>会员中心</title>
       </head>
       <body>
           <p><h2>会员信息</h2></p>
           <p>姓名：{{tname}}</p>
           <p>年龄：{{tage}}</p>
           <p>地址：{{taddress}}</p>
           <p>QQ：{{tqq}}</p>
       </body>
       </html>template_with_parameter.py
       ```

     + template_with_parameter.py

       ```python
       from bottle import route,run
       from bottle import template
       
       @route('/info')
       def info():
           name='cxy'
           age='18'
           address='China'
           qq='123456'
           return template('info',tname=name,tage=age,taddress=address,tqq=qq)
       
       run(host='localhost',port=8080)
       ```

       像刚才info.html模板中，用了{{tname}}，{{tage}}，{{tblog}}，{{tqq}}方法，这个其实就是显示后端return template('info',tname = name,tage = age,tblog = blog, tqq = qq) 传递过来的数据，在后端return的数据中，前端是tname是KEY，后面name是VALUE，所以模板中使用{{}}来表示调用数据中的KEY，如{{key}}，代码运行后，就会显示这key对应的value，这是一种字典数据类型的调用方法。  

   + 传递字典或列表类型的参数

     + info.html

       ```python
       <!DOCTYPE html>
       <head>
           <title>会员中心</title>
       </head>
       <body>
           <p><h2>会员信息</h2></p>
           <p>姓名：{{tname}}</p>
           <p>年龄：{{tage}}</p>
           <p>地址：{{taddress}}</p>
           <p>QQ：{{tqq}}</p>
           <p>book：{{tbook[0]}}</p>
           <p>price：{{tprice.get('python')}}</p>
       </body>
       </html>
       ```

     + template_with_parameter.py

       ```python
       from bottle import route,run
       from bottle import template
       
       @route('/info')
       def info():
           name='cxy'
           age='18'
           address='China'
           qq='123456'
           book=['python','linux','php']
           price={'python':40,'linux':20,'php':10}
           return template('info',tname=name,tage=age,taddress=address,tqq=qq,tbook=book,tprice=price)
       
       run(host='localhost',port=8080)
       ```

   ---

5. 使用view渲染

   + view.study.py

     ```python
     from bottle import route,run
     from bottle import view
     @route('/info')
     @view('info')
     def info():
         name='CXY'
         age='22'
         address='CHINA'
         qq='123456'
         book = ['python', 'linux', 'php']
         price = {'python': 40, 'linux': 20, 'php': 10}
         data={'tname':name,'tage':age,'taddress':address,'tqq':qq,'tbook':book,'tprice':price}
         return data
     run(host='localhost',port=8080)
     ```

     注意：

     + from bottle import view
     + @view('info')
     + data={'tname':name,'tage':age,'taddress':address,'tqq':qq,'tbook':book,'tprice':price}
     + return data

   