# PythonDjango--表单

## 获取客户端请求的相关信息

### request常用方法

* request.path : 获取当前url,(但不含参数)

* request.get_full_path() : 获取当前url,(包含参数)

  * 对比示例：请求一个http://127.0.0.1:8000/200/?type=10

    request.get_full_path()返回的是【/200/?type=10】

    request.path返回的是 【/200/】

* request.get_host() : 获取主机地址

* request.get_port() : 获取端口号

* request.is_secure() : 是否是安全的url

* request.is_ajax() : 是否通过ajax访问

* request.META : 返回一个Python字典，包含所有HTTP请求头

* 示例：test9.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>request</title>
  </head>
  <body>
      <ul>
          <li>path : {{ request.path }}</li>
          <li>full_path : {{ full_path }}</li>
          <li>host : {{ host }}</li>
          <li>port : {{ port }}</li>
          <li>is_secure : {{ is_secure }}</li>
          <li>is_ajax : {{ is_ajax }}</li>
          <li>Accept : {{ accept }}</li>
      </ul>
      <table border="1">
          <tr>
              <th>Key</th>
              <th>Value</th>
          </tr>
          {% for key, value in request_meta_items %}
              <tr>
                  <td>{{ key }}</td>
                  <td>{{ value }}</td>
              </tr>
          {% endfor %}
      </table>
  </body>
  </html>
  ```
  
  ```python
  def requestForm(request):
      full_path = request.get_full_path()
      host = request.get_host()
      port = request.get_port()
      is_secure = request.is_secure()
      is_ajax = request.is_ajax()
      request_meta = request.META
      request_meta_items = request_meta.items()
      # 可能不存在HTTP_ACCEPT字段，需要包一个try
      try:
          accept = request_meta['HTTP_ACCEPT']
      except KeyError:
          accept = 'ACCEPT NOT FOUND'
      return render(request, 'test9.html', locals())
  ```
  
  ![Django5-1](E:\Notes\Python\Django5-1.jpg)

## 获取GET请求的参数

https://www.cnblogs.com/daibeisi/p/14601288.html

## 处理表单（Form）提交的数据

### 示例：test10.html，test10_result.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>search</title>
</head>
<body>
    <form action="/search" method="get">
        <input type="text" name="student_grade">
        <input type="submit" value="search">
    </form>
</body>
</html>
```

* action : 提交到服务端的url路径，该url路径会接收form提交的数据
* method : 使用的方法

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>test10_result</title>
</head>
<body>
    <p>You have searched for : <strong>{{ stu_grade }}</strong></p>
    {% if stu_objs %}
        <p>Found {{ stu_objs|length }} students.</p>
        <ul>
        {% for stu in stu_objs %}
            <li>{{ stu.name }} - {{ stu.age }} - {{ stu.gender }} - {{ stu.grade }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No student matched.</p>
    {% endif %}
</body>
</html>
```

```python
def searchForm(request):
    return render(request, 'test10.html')

def search(request):
    if request.method == 'GET':
        if 'student_grade' in request.GET:
            stu_grade = request.GET.get('student_grade')
            stu_objs = Student.objects.filter(grade=int(stu_grade))
            return render(request, 'test10_result.html', locals())
        else:
            return HttpResponse('Please submit a search term.')
```

```python
    re_path(r'^searchForm/$', Form.searchForm),
    re_path(r'^search/$', Form.search),
```

注：点击search后其实直接跳转的url是：http://127.0.0.1:8000/search/?student_grade=4

## 改进表单

* 目标：希望搜索页面和搜搜结果在同一个页面表示

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>search</title>
</head>
<body>
    <form action="/search" method="get">
        <input type="text" name="student_grade">
        <input type="submit" value="search">
    </form>
    {% if error %}
        <p style="color: red">Please submit valid student grade</p>
    {% elif stu_objs %}
        <p>Found {{ stu_objs|length }} students.</p>
        <ul>
        {% for stu in stu_objs %}
            <li>{{ stu.name }} - {{ stu.age }} - {{ stu.gender }} - {{ stu.grade }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No student matched.</p>
    {% endif %}
</body>
</html>
```

```python
def searchForm(request):
    return render(request, 'test10.html')

def search(request):
    if request.method == 'GET':
        if 'student_grade' in request.GET:
            stu_grade = request.GET.get('student_grade')
            if not stu_grade:
                return render(request, 'test10.html', {'error':True})
            stu_objs = Student.objects.filter(grade=int(stu_grade))
            return render(request, 'test10.html', locals())
        else:
            return render(request, 'test10.html', {'error':True})
```

## 简单的表单校验

* 对表单的值的有效性进行校验
* 例如对于上例，限制student_grade不能为空且必须为1-4之间的整数

test10.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>search</title>
</head>
<body>
    <form action="/search" method="get">
        <input type="text" name="student_grade">
        <input type="submit" value="search">
    </form>
    {% if errors %}
        <ul style="color: red">
        {% for err in errors %}
            <li>{{ err }}</li>
        {% endfor %}
        </ul>
    {% elif stu_objs %}
        <p>Found {{ stu_objs|length }} students.</p>
        <ul>
        {% for stu in stu_objs %}
            <li>{{ stu.name }} - {{ stu.age }} - {{ stu.gender }} - {{ stu.grade }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No student matched.</p>
    {% endif %}
</body>
</html>
```

```python
def searchForm(request):
    return render(request, 'test10.html')

def search(request):
    errors = []
    if request.method == 'GET':
        if 'student_grade' in request.GET:
            stu_grade = request.GET.get('student_grade')
            if stu_grade == '':
                errors.append('请输入年级')
            elif not stu_grade.isdigit() or 1 > int(stu_grade) or int(stu_grade) > 4:
                errors.append('请输入1-4的整数')
            else:
                stu_objs = Student.objects.filter(grade=int(stu_grade))
                return render(request, 'test10.html', locals())
        else:
            errors.append('请输入年级')
        return render(request, 'test10.html', locals())
```

## 对表单中多个字段进行校验

示例：test11.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>search</title>
</head>
<body>
    <form action="/search" method="get">
        <p>grade : <input type="text" name="student_grade"></p>
        <p>gender : <input type="text" name="student_gender"></p>
        <p>age : <input type="text" name="student_age"></p>
        </p><input type="submit" value="search"></p>
    </form>
    {% if errors %}
        <ul style="color: red">
        {% for err in errors %}
            <li>{{ err }}</li>
        {% endfor %}
        </ul>
    {% elif stu_objs %}
        <p>Found {{ stu_objs|length }} students.</p>
        <ul>
        {% for stu in stu_objs %}
            <li>{{ stu.name }} - {{ stu.age }} - {{ stu.gender }} - {{ stu.grade }}</li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No student matched.</p>
    {% endif %}
</body>
</html>
```

```python
def searchForm(request):
    return render(request, 'test11.html')

def search(request):
    errors = []
    if request.method == 'GET':
        stu_grade = request.GET.get('student_grade')
        stu_gender = request.GET.get('student_gender')
        stu_age = request.GET.get('student_age')
        if not stu_grade:
            errors.append("请输入年级")
        elif not stu_grade.isdigit() or 1 > int(stu_grade) or int(stu_grade) > 4:
            errors.append('请在年级输入1-4的整数')
        if not stu_gender:
            errors.append("请输入性别")
        elif stu_gender not in ['G', 'B']:
            errors.append("请在性别输入G或B")
        if not stu_age:
            errors.append("请输入年龄")
        elif not stu_age.isdigit():
            errors.append("请在年龄输入正整数")
        if not errors:
            stu_objs = Student.objects.filter(grade=int(stu_grade), age=int(stu_age), gender=stu_gender)
            return render(request, 'test11.html', locals())
        else:
            return render(request, 'test11.html', locals())
```

## 编写Form类

* 在上例中，从GET参数获取的有三个字段需要进行校验，但如果校验字段有特别多，甚至上百个，if else判断就非常麻烦

* Form类可以方便的校验字段

* ```python
  django.forms.Form
  ```

* 示例：在myjango目录下，新建forms.py

  ```python
  from django import forms
  
  
  class myjangoForm(forms.Form):
      name = forms.CharField(
          required=False,
      )
      age = forms.IntegerField(
          required=True,
          min_value=1,
          error_messages = {
              'required': "请输入年龄",
              'min_value': "输入的年龄大于0"
          }
      )
      gender = forms.CharField(
          required=True,
          error_messages={
              'required': "请输入性别",
          }
      )
      grade = forms.IntegerField(
          required=True,
          min_value=1,
          max_value=4,
          error_messages={
              'required': "请输入年级",
              'min_value': "输入的年级大于0",
              'max_value': "输入的年级小于4"
          }
      )
  ```

  console 中对my对象进行输出：

  ```python
  from mydjango import forms
  my = forms.myjiangoForm()
  # 默认输出为表格形式
  print(my)
  <tr><th><label for="id_name">Name:</label></th><td><input type="text" name="name" id="id_name"></td></tr>
  <tr><th><label for="id_age">Age:</label></th><td><input type="number" name="age" min="1" required id="id_age"></td></tr>
  <tr><th><label for="id_gender">Gender:</label></th><td><input type="text" name="gender" required id="id_gender"></td></tr>
  <tr><th><label for="id_grade">Grade:</label></th><td><input type="number" name="grade" min="1" max="4" required id="id_grade"></td></tr>
  # 输出为列表形式
  print(my.as_ul())
  <li><label for="id_name">Name:</label> <input type="text" name="name" id="id_name"></li>
  <li><label for="id_age">Age:</label> <input type="number" name="age" min="1" required id="id_age"></li>
  <li><label for="id_gender">Gender:</label> <input type="text" name="gender" required id="id_gender"></li>
  <li><label for="id_grade">Grade:</label> <input type="number" name="grade" min="1" max="4" required id="id_grade"></li>
  # 输出为段落形式
  print(my.as_p())
  <p><label for="id_name">Name:</label> <input type="text" name="name" id="id_name"></p>
  <p><label for="id_age">Age:</label> <input type="number" name="age" min="1" required id="id_age"></p>
  <p><label for="id_gender">Gender:</label> <input type="text" name="gender" required id="id_gender"></p>
  <p><label for="id_grade">Grade:</label> <input type="number" name="grade" min="1" max="4" required id="id_grade"></p>
  # 只输出某个字段
  print(my['name'])
  <input type="text" name="name" id="id_name">
  print(my['age'])
  <input type="number" name="age" min="1" required id="id_age">
  my1 = forms.myjiangoForm({'name': 'cxy', 'age': 18, 'gender': 'G', 'grade': 4})
  # 校验是否正确
  my1.is_valid()
  Out[14]: True
  my2 = forms.myjiangoForm({'age': 18, 'gender': 'G', 'grade': 6})
  my2.is_valid()
  Out[16]: False
  # 查看某字段的错误信息
  my2['name'].errors
  Out[18]: []
  my2['grade'].errors
  Out[19]: ['输入的年级小于4']
  # 查看所有字段的错误信息，以字典形式表示
  my2.errors
  Out[20]: {'grade': ['输入的年级小于4']}
  
  ```

## 在视图中使用Form对象

* Form是一个表单类，它的主要作用：

  * 用于校验字段
  * 用于生成表单对应的html代码

* 示例：test12.html

  ```python
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>form</title>
  </head>
  <body>
      <form action="" method="post">
          <table>
              {{ form.as_table }}
          </table>
          <input type="submit" value="Search">
      </form>
  </body>
  </html>
  ```

  ```python
  from mydjango.forms import myjangoForm
  from django.views.decorators.csrf import csrf_exempt
  
  @csrf_exempt
  def formForm(request):
      if request.method == 'POST':
          form = myjangoForm(request.POST)
          if form.is_valid():
              print("完成后续业务工作")
              return HttpResponse("Success")
      else:
          form = myjangoForm()
          return render(request, 'test12.html', {'form': form})
  ```

## 改变字段显示风格

* forms中可以指定字段显示成不同的风格，使用widget参数传入，如：TextInput（单行），Textarea（多行）

* 示例

  ```python
  gender = forms.CharField(
          required=True,
          error_messages={
              'required': "请输入性别",
          },
          widget=forms.Textarea
      )
  ```

## 设置最小和最大长度

* forms中可以设置指定字段的长度范围，使用min_value和max_value参数传入

* 示例

  ```python
  grade = forms.IntegerField(
          required=True,
          min_value=1,
          max_value=4,
          error_messages={
              'required': "请输入年级",
              'min_value': "输入的年级大于0",
              'max_value': "输入的年级小于4"
          }
      )
  ```

## 设置表单默认值

* 设置表单各个字段初始默认值，在对forms对象实例化时进行，使用initial参数

* 示例

  ```python
  from mydjango.forms import myjangoForm
  from django.views.decorators.csrf import csrf_exempt
  
  @csrf_exempt
  def formForm(request):
      if request.method == 'POST':
          form = myjangoForm(request.POST)
          if form.is_valid():
              print("完成后续业务工作")
              return HttpResponse("Success")
          else:
              
      else:
          form = myjangoForm(initial={'name': 'cxy', 'age': 18, 'gender': 'G', 'grade': 1})
          return render(request, 'test12.html', {'form': form})
  ```

## 自定义校验规则

* form校验顺序：先使用系统校验规则，若通过，则调用自定义校验规则

* 自定义校验规则的方法必须以“clean_”为前缀，后跟字段名字

* 示例：

  ```python
  from django import forms
  
  
  class myjangoForm(forms.Form):
      name = forms.CharField(
          required=False,
      )
      age = forms.IntegerField(
          required=True,
          min_value=1,
          error_messages = {
              'required': "请输入年龄",
              'min_value': "输入的年龄大于0"
          },
      )
      gender = forms.CharField(
          required=True,
          error_messages={
              'required': "请输入性别",
          },
      )
      grade = forms.IntegerField(
          required=True,
          min_value=1,
          max_value=4,
          error_messages={
              'required': "请输入年级",
              'min_value': "输入的年级大于0",
              'max_value': "输入的年级小于4"
          }
      )
  
      def clean_gender(self):
          gender = self.cleaned_data['gender']   # 读取表单返回的值，返回类型为字典dict型
          if not (gender == 'G' or gender == 'B'):
              raise forms.ValidationError("只能填写‘G’或‘B’")
          return gender
  ```

  ```python
  from mydjango.forms import myjangoForm
  from django.views.decorators.csrf import csrf_exempt
  
  @csrf_exempt
  def formForm(request):
      if request.method == 'POST':
          form = myjangoForm(request.POST)
          if form.is_valid():
              print("完成后续业务工作")
              return HttpResponse("Success")
          else:
              return render(request, 'test12.html', {'form': form})
      else:
          form = myjangoForm(initial={'name': 'cxy', 'age': 18, 'gender': 'G', 'grade': 1})
          return render(request, 'test12.html', {'form': form})
  ```

## 为字段指定标签

* 设置表单各个字段的标签，默认的标签是字段名首字母大写的格式，使用label参数进行设置

* 示例

  ```python
  name = forms.CharField(
          required=False,
          label='姓名',
      )
  ```

  

