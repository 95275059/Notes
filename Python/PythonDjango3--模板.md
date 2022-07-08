# PythonDjango3--模板

## 模板

* 使用 django.http.HttpResponse() 来输出 "Hello World！"。该方式将数据与视图混合在一起，不符合 Django 的 MVC 思想。

* 模板是一个文本，用于分离文档的表现形式和内容。

* 模板是包含了静态（HTML, CSS）和动态内容（包含变量）的文本，Django在将模板发送给客户端之前需要将动态部分替换成相应的值

* 在shell中使用Django模板，不应该直接使用Python REPL(读取-评估-打印-循环 (REPL))

* 应该进入项目目录

  ```
  python manage.py shell
  
  from django import template
  t = template.Template("My name is {{name}}.")  # 创建模板实例Template，然后封装模板
  c = template.Context({'name': 'CXY'})
  t.render(c)
  ```

  或者：Tools - Python or Debug Console

## 第一个Django模板应用

* MyTemplate.py

  ```python
  from django.http import HttpResponse
  from django import template
  
  
  def simpleTemplate(request):
      t = template.Template("My name is {{name}}.")
      c = template.Context({'name': 'CXY'})
      return HttpResponse(t.render(c))
  ```

* urls.py

  ```python
  re_path(r'^simpleTemplate/$', MyTemplate.simpleTemplate)
  ```

## 同一个模板，多个上下文（Context）

* MyTemplate.py

  ```python
  def multiContext(request):
      html = '<ul>'
      t = template.Template('<li>Today is {{day}}.</li>')
      for day in ('Mon', 'Tue', 'Wed'):
          c = t.render(template.Context({'day': day}))
          html += c
      html += '</ul>'
      return HttpResponse(html)
  ```

* urls.py

  ```python
  re_path(r'^multiContext/$', MyTemplate.multiContext)
  ```

## 向上下文传递字典和列表

* MyTemplate.py

  ```python
  def transdict(result):
      person = {'name':'CXY', 'age':18}
      t = template.Template("{{person.name}} is {{person.age}} years old.")
      c = template.Context({'person': person})
      return HttpResponse(t.render(c))
  
  def translist(result):
      person = ['CXY', 18]
      t = template.Template("{{person.0}} is {{person.1}} years old.")
      c = template.Context({'person': person})
      return HttpResponse(t.render(c))
  ```

* urls.py

  ```python
  re_path(r'^transDict/$', MyTemplate.transdict),
  re_path(r'^transList/$', MyTemplate.translist),
  ```

## 向上下文传递对象（多级深度嵌套）

* 变量查找顺序

  以{{person.name}}为例

  1. 字典：person[‘name’]
  2. 对象属性：person.name
  3. 对象方法：person.name()
  4. person[name]

* MyTemplate.py

  ```python
  def transobj(request):
      person = Person()
      t = template.Template("Hello, {{person.name.upper}}!")
      c = template.Context({'person': person})
      return HttpResponse(t.render(c))
  ```

* urls.py

  ```python
  re_path(r'^transObj/$', MyTemplate.transobj),
  ```

* 测试

  ```
  Hello, BILL!
  ```

## 如何处理无效变量

* 无效变量：是指在模板中指定了，但并没有在上下文中指定

  相当于只定义了，没有赋值

* 如果存在无效变量，会被自动忽略

* 且变量区分大小写

* 示例

  ```python
  t = template.Template("My name is {{name}}.")
  c = template.Context()
  print(t.render(c))
  ```

  输出：My name is .

## 按照字典方式向Context添加或删除变量

```python
from django.template import Template, Context
t = Template('This is {{field1}}. That is {{field2}}')
c = Context({'field1': 'Banana', 'field2': 'Car'})
t.render(c)
Out[6]: 'This is Banana. That is Car'
c['field1']   # 通过字典方式获取上下文中的键值
Out[7]: 'Banana'
del c['field1']   # 删除变量
c['field1']   # 不存在‘field1’，因此报错
Traceback (most recent call last):
  File "C:\Users\CXY\Anaconda3\envs\python36\lib\site-packages\IPython\core\interactiveshell.py", line 3343, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-9-974290fca182>", line 1, in <module>
    c['field1']
  File "C:\Users\CXY\Anaconda3\envs\python36\lib\site-packages\django\template\context.py", line 83, in __getitem__
    raise KeyError(key)
KeyError: 'field1'
c.get('field1')   # 不存在‘field1’，返回空值

t.render(c)
Out[11]: 'This is . That is Car'
c['field1'] = 'Apple'   # 添加变量
t.render(c)
Out[13]: 'This is Apple. That is Car'
```

## 装载模板文件与修改默认模板文件目录

* 默认将模板文件放到工程目录下的templates目录中

* 模板文件可以是任何形式的文本文件，一般都是HTML格式

  例如：test.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
  </head>
  <body>
      It is now {{ current_date }}
  </body>
  </html>
  ```

### 方案一

* 装载模板文件

  ```python
  from django.template.loader import get_template
  
  def loadTemplateFile(request):
      now = datetime.datetime.now()
      t = get_template('test.html')
      html = t.render({'current_date': now})  # 直接传入字典
      return HttpResponse(html)
  ```

* urls.py

  ```python
  re_path(r'^loadTemplateFile/$', MyTemplate.loadTemplateFile),
  ```

### 方案二

* 使用django.shortcuts提供的render

  ```python 
  from django.shortcuts import render
  def loadTemplateFile1(request):
      now = datetime.datetime.now()
      return render(request, 'test.html', {'current_date': now})
  ```

* urls.py

  ```python
  re_path(r'^loadTemplateFile1/$', MyTemplate.loadTemplateFile1),
  ```

### 传递多个变量

* 示例:test1.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>"Test1"</title>
  </head>
  <body>
  It is now {{ current_date }}
  <ul>
      <li>{{ field1 }}</li>
      <li>{{ field2 }}</li>
      <li>{{ field3 }}</li>
  </ul>
  </body>
  </html>
  ```

* MyTemplate.py

  ```python
  def loadTemplateFile2(request):
      current_date = datetime.datetime.now()
      field1 = 'hello'
      field2 = 'world'
      field3 = 'cxy'
      return render(request, 'test1.html', locals()) # 获取全局的变量，并自动转换成字典，但必须先保证变量一致
  ```

* urls.py

  ```python
  re_path(r'^loadTemplateFile2/$', MyTemplate.loadTemplateFile2),
  ```

### 修改或添加模板目录

* settings.py

  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [os.path.join(BASE_DIR, 'templates')]
          ,
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

  在修改DIRS键值

* 模板搜索顺序是从前往后

## if-else标签的简单应用

* 示例:test2.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>"Test2"</title>
  </head>
  <body>
      {% if today_is_weekend %}
          <p>Today is weekend!</p>
      {% elif field1 %}
          <p>今天什么情况</p>
      {% else %}
          <p>Today is not weekend!</p>
      {% endif %}
  It is now {{ current_date }}
  <ul>
      <li>{{ field1 }}</li>
      <li>{{ field2 }}</li>
      <li>{{ field3 }}</li>
  </ul>
  </body>
  </html>
  ```

* MyTemplate.py

  ```python
  def ifelseTemplate(request):
      current_date = datetime.datetime.now()
      field1 = 'hello'
      field2 = 'world'
      field3 = 'cxy'
      today_is_weekend = True
      return render(request, 'test2.html', locals())
  ```

  注：today_is_weekend 为0，[]（空列表），()（空元祖），{}（空字典），""（空字符串），None，False时，相当于布尔值为False

* urls.py

  ```python
  re_path(r'^ifelseTemplate/$', MyTemplate.ifelseTemplate),
  ```

## if-else标签多值条件与嵌套

* 使用 and or not ,和python一样

  ```html
  {% if ... %}
  	...
  {% elif ... %}
  	...
  {% else ... %}
  	...
  {% endif %}
  ```

* 示例：test3.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>"Test3"</title>
  </head>
  <body>
      {% if field1 and field2 %}
          {% if field3 %}
              {{ field3 }}
          {% endif %}
      {% elif field1 or field2 or field3 %}
          <ul>
              <li>{{ field1 }},{{ field2 }},{{ field3 }}</li>
          </ul>
      {% elif not field1 %}
          <ul>
              <li>{{ field2 }}</li>
              <li>{{ field3 }}</li>
          </ul>
      {% endif %}
  </body>
  </html>
  ```

## for标签

* 和python中的for类似，但不支持continue和break

  ```html
  {% for X in Y %}
  {% endfor %}
  ```

  

* for标签内置变量

  * forloop
    * forloop.counter   获得当前循环的计数，从1开始
    * forloop.counter0   获得当前循环的计数，从0开始
    * forloop.revcounter   获得当前循环剩余项的计数，初始值为迭代对象的长度n
    * forloop.revcounter0   获得当前循环剩余项的计数，初始值为迭代对象的长度n-1
    * forloop.first   为布尔值，第一次执行for为True
    * forloop.last   为布尔值，最后一次执行for为False

* 示例:test4.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>test4</title>
  </head>
  <body>
      <ul>
          {% for person in persons %}
              {% if forloop.first %}
                  <li style="color: red">
              {% elif forloop.last %}
                  <li style="color: blue">
              {% else %}
                  <li>
              {% endif %}
              {{ forloop.counter }}-{{ person.name }}-{{ person.age }}</li>
          {% endfor %}
      <p>
          {% for person in persons %}
              {{ person.name }}
              {% if not forloop.last %}
                  ,
              {% endif %}
          {% endfor %}
      </p>
      </ul>
  </body>
  </html>
  ```

## ifequal和ifnotequal标签

* ifequal和ifnotequal标签用于判断两个值是否相等

  ```html
  {% ifequal x y %}
  	...
  {% else %}
  	...
  {% endifequal %}
  
  {% ifnotequal x y %}
  	...
  {% endifnotequal %}
  ```

  支持else

* 这两个标签只能使用字符串，整数和浮点数，不能使用字典，列表，元组，布尔，可以使用if替代

* 示例:test5.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>test5</title>
  </head>
  <body>
      {% ifequal user currentUser %}
          <h1>用户已经登录</h1>
      {% else %}
          <h1>用户未登录</h1>
      {% endifequal %}
      {% ifequal user 'CXY' %}
          <h1>用户是CXY</h1>
      {% endifequal %}
  </body>
  </html>
  ```

## 单行注释和多行注释

* 单行注释：模板注释

  ```html
  {# This is comment #}
  ```

* 多行注释：模板注释

  ```html
  {% comment %}
      comment...
      comment
  {% endcomment %}
  ```

* 另外一种注释：HTML注释

  ```html
  <!-- abcd -->
  ```

  也不会在页面显示

  但是右击显示页面源代码后，会看到这种注释内容

  HTML注释和普通的HTML代码都会发送到客户端，但模板注释不会发送到客户端

## 过滤器

* 过滤器：对模板变量的二次加工
* 种类
  * lower : 将模板变量的值都变成小写
  * upper : 将模板变量的值都变成大写
  * truncatewords : 截取模板变量的前n个单词
  * addslashes : 在任何的反斜杠，单引号或双引号前面添加反斜杠
  * date : 按指定的格式化字符串参数格式化date或datetime对象
  * length : 返回模板变量的长度

* 示例：test6.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Filter</title>
  </head>
  <body>
      <ul>
          <li>{{ name|lower }}</li>
          <li>{{ name|upper }}</li>
          <li>{{ productName|truncatewords:"3" }}</li>
          <li>{{ mytime|date:"F j,Y" }}</li>
          <li>{{ name|length }}</li>
      </ul>
  </body>
  </html>
  ```

  ```python
  def filterTemplate(request):
      mytime = datetime.datetime.now()
      name = 'Cxy'
      productName = 'AA BB CC DD EE FF'
      return render(request, 'test6.html', locals())
  ```

## 引用模板（include标签）

* 引用格式

  ```html
  {% include 'templateName.html' %}
  ```

* 模板搜索顺序

  依照模板目录进行搜索，和render一样

* 示例：test7_main.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>include</title>
  </head>
  <body>
      <ul>
          <li>{{ main }}</li>
          <li>{% include 'test7_t1.html' %}</li>
          <li>{{ main1 }}</li>
          <li>{% include 'test7_t2.html' %}</li>
          <li>{{ main2 }}</li>
          <li>{% include 'test7_t3.html' %}</li>
      </ul>
  </body>
  </html>
  ```

  test7_t1.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>test7_t1</title>
  </head>
  <body>
      {{ t1 }}
  </body>
  </html>
  ```

  test7_t2.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>test7_t2</title>
  </head>
  <body>
      {{ t2 }}
  </body>
  </html>
  ```

  test7_t3.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>test7_t3</title>
  </head>
  <body>
      {{ t3 }}
  </body>
  </html>
  ```

  ```python
  def includeTemplate(request):
      main = 'Hello World!'
      main1 = 'I love you'
      main2 = 'You love me'
      t1 = 'This is subtemplate t1.'
      t2 = 'This is subtemplate t2.'
      t3 = 'This is the last subtemplate t3.'
      return render(request, 'test7_main.html', locals())
  ```

## 模板继承

* 模板继承

  * 类似python中的继承
  * 代码重用的两种方式：模板继承（推荐），引用模板

* 格式

  ```html
  {% block blockName %}{% endbloack %}
  ```

  * 在同一个模板中，blockName不可重复

* 示例:test8_main.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>{% block test8_base %}{% endblock %}</title>
  </head>
  <body>
      {% block content %}
      {% endblock %}
      {% block footer %}
          <p>Welcome!</p>
      {% endblock %}
  
  </body>
  </html>
  ```

  test_product1.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      {% extends 'test8_base.html' %}
      <meta charset="UTF-8">
      <title>{% block test8_base %}phone site{% endblock %}</title>
  </head>
  <body>
      {% block content %}
      <ul>
          <li>{{ phone_product1 }}</li>
          <li>{{ phone_product2 }}</li>
      </ul>
      {% endblock %}
  </body>
  </html>
  ```

  test_product2.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      {% extends 'test8_base.html' %}
      <meta charset="UTF-8">
      <title>{% block test8_base %}car site{% endblock %}</title>
  </head>
  <body>
      <li>{{ name }}</li>    {# 并不会显示，因为没有放到block中 #}
      {% block content %}
      <ul>
          <li>{{ car_product1 }}</li>
          <li>{{ car_product2 }}</li>
      </ul>
      {% endblock %}
      {% block footer %}
          <p>Welcome car website!</p>
      {% endblock %}
  </body>
  </html>
  ```

  ```python
  def extendTemplate_sub1(request):
      phone_product1 = 'Apple'
      phone_product2 = 'Huawei'
      return render(request, 'test8_product1.html', locals())
  
  def extendTemplate_sub2(request):
      name = 'Hello'
      car_product1 = 'Fort'
      car_product2 = 'Tesla'
      return render(request, 'test8_product2.html', locals())
  ```

  

  