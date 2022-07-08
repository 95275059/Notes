# PythonDjango4--数据库模型

## 传统的数据库访问方式

* 常用的数据库 SQLite MySQL
* 常用的数据库模块：pymysql

* 示例：

  ```python
  from pymysql import *
  import json
  from django.http import HttpResponse
  
  
  def processDB(request):
      # 连接数据库
      db = connect(host='127.0.0.1', user='root', passwd='123456', database='mydjango', charset='utf8')
      cursor = db.cursor()
      sql = 'SELECT name, age FROM Student;'
      cursor.execute(sql)
      results = cursor.fetchall()
      print(results)
      fields = ['name', 'age']
      records = []
      for row in results:
          print(zip(fields, row))
          records.append(dict(zip(fields, row)))
      print(records)
      return HttpResponse(json.dumps(records))
  ```

* 优点：直白
* 缺点：
  * 尽管比较直白，但是要将参数以及SQL语句硬编码在源代码中，可以通过将这些数据保存到文件中解决
  * 存在大量的重复代码，可以通过编写额外的代码（类封装）来尽可能解决代码重复的问题
  * 如果使用python模块访问数据库，就会将整个项目绑死在一种数据库上，这个缺点很难弥补
* 解决方案：ORM

## Django中的MTV模式

### MVC模式（Model View Controller）

* 一种Web架构模式，

* 将业务逻辑、模型数据和用户界面分开

* 将前后端分开，前端和后端无必然联系

* 三要素

  * Model（数据模型）：将数据库与数据操作解耦；只需要该数据模型的配置设置，即可切换数据库

  * View（视图）：呈现给用户的效果；接收来自Model的数据并进行展现

  * Controller（控制器）：Model和View之间的沟通桥梁。

    数据发生变化，Model发送至Controller，Controller发送至View

    View中进行数据操作，View将数据操作通过Controller发送至Model

### MTV模式（Model Template View）

* 三要素

  * Model（数据模型）：和MVC的model一致

  * Template（模板）：把页面如何展示给用户

  * View（视图）：实际上就是映射函数（将一个url映射到一个函数上）

    和MVC的Controller有些像，但是有所不同，可以认为MTV的controller是django中urls.py中设置的url映射

## 使用Django ORM操作数据库

### ORM

* ORM（Object Relational Mapping，面向对象的映射器，用于数据模型和关系型数据库间的媒介）
* 可以将数据库的表映射到Python中的对象，表中的字段映射为Python对象的属性
* 一个Python对象代表表中的一条记录，即表是Python对象的集合（一般是列表）
* ORM是通过mysqlclient模块来访问MySQL

### 安装mysqlclient模块

* 如果使用了多版本的Python环境，安装了Anaconda，注意要通过Anaconda的pip进行安装

* 查看Anaconda环境

  ```shell
  (python36) C:\WINDOWS\system32>conda info --env
  # conda environments:
  #
  base                     C:\Users\CXY\Anaconda3
  python36              *  C:\Users\CXY\Anaconda3\envs\python36
  ```

* 进入C:\Users\CXY\Anaconda3\envs\python36\Scripts

  ```shell
  (python36) C:\Users\CXY\Anaconda3\envs\python36\Scripts>pip3 install mysqlclient
  Collecting mysqlclient
    Downloading mysqlclient-2.0.3-cp36-cp36m-win_amd64.whl (178 kB)
       |████████████████████████████████| 178 kB 285 kB/s
  Installing collected packages: mysqlclient
  Successfully installed mysqlclient-2.0.3
  ```

### 创建ORM初始目录

* 实际上可以理解为创建一个映射数据库

* 通过命令行创建

  ```
  (python36) E:\Python\MyDjango36>python manage.py startapp mydjango
  ```

  后跟数据库名

### 配置settings.py中的INSTALLED_APPS

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mydjango'
]
```

加入'mydjango'

### 检查配置

```shell
(python36) E:\Python\MyDjango36>python manage.py check
System check identified no issues (0 silenced).
```

### 配置settings.py中的DATABASES

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydjango',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '123456'
    }
}
```

### 在models.py中建立数据模型

将表映射成对象

```python
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField(max_length=2)
    gender = models.CharField(max_length=1)
    grade = models.IntegerField(max_length=1)
```

### 创建表

```shell
python manage.py makemigrations mydjango   #建立建表文件

python manage.py migrate 
```

```shell
(python36) E:\Python\MyDjango36>python manage.py makemigrations
Migrations for 'mydjango':
  mydjango\migrations\0001_initial.py
    - Create model Student

(python36) E:\Python\MyDjango36>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, mydjango, sessions
Running migrations:
  Applying mydjango.0001_initial... OK
```

操作完成之后，在数据库中出现表：mydjango_student

### 实例：插入表

```python
from mydjango.models import Student
from django.http import HttpResponse

def insertDB(request):
    m1 = Student(name='b', age=19, gender='B', grade=2)
    m1.save()
    return HttpResponse(m1)  # Student object (1)
```

### 实例：查找所有行

```python
def selectallDB(request):
    result = Student.objects.all()
    name = []
    for x in result:
        name.append(x.name)
    return HttpResponse(name)
```

## 对数据表的查询、insert、update和delete

已知表student包含三种字段：name, age, gender, grade

### 查询

* 示例：查询几条

  ```python
  def selectDB(request):
      stu = Student.objects.get(name='a')
      print(stu)
      print(stu.name)
      print(stu.age)
      print(stu.gender)
      print(stu.grade)
      return HttpResponse(stu)
  ```

  ```python
  Student object (1)
  a
  18
  G
  1
  ```

* 示例：查询所有

  ```python
  def selectallDB(request):
      result = Student.objects.all()
      name = []
      for x in result:
          name.append(x.name)
      return HttpResponse(name)
  ```

### insert

* 插入数据其实就是创建模型类的过程

* 示例

  ```python
  from mydjango.models import Student
  m1 = Student(name='b', age=19, gender='B', grade=2)
  m1.save()
  ```

* 注：需要save

### update

* 先查询后修改

* 示例

  ```python
  def updateDB(request):
      stu = Student.objects.get(name='a')
      stu.name = 'aa'
      stu.save()
      return HttpResponse('Success')
  ```

* 注：需要save

### delete

* 先查询后删除

* 示例：删除一条

  ```python
  def deleteDB(request):
      stu = Student.objects.get(name='c')
      stu.delete()
      return HttpResponse('Success')
  ```

* 示例：删除所有，即清空表

  ```python
  Student.objects.all().delete()
  ```

* 注：不需要save

## 数据过滤

* 过滤所有数据

  ```python
  def filterDB(request):
      # 过滤所有数据
      all = Student.objects.all()
      stu_names = []
      for stu in all:
          stu_names.append(stu.name)
      return HttpResponse(",".join(stu_names))
  ```

* 过滤指定的数据

  * 方法一：Model_object.objects.get() ：返回一个模型对象

    ```python
    stu = Student.objects.get(name='c') 
    ```

  * 方法二：Model_object.objects.filter()  ：返回一个QuerySet

    ```python
    def filterDB(request):
    # 过滤指定数据
        stu_girls = Student.objects.filter(gender='G')
        stugirl_names = []
        for sg in stu_girls:
            stugirl_names.append(sg.name)
        return HttpResponse(",".join(stugirl_names))
    ```

* 多种筛选条件

  * and

    ```python
    stu_girls = Student.objects.filter(gender='G', grade=3)
    ```

  * like

    
    
    ```python
    def filterDB(request):
    # like
        stus = Student.objects.filter(name__icontains='b')
        stugirl_names = []
        for sg in stus:
            stugirl_names.append(sg.name)
        return HttpResponse(",".join(stugirl_names))
    ```
    
    name__icontains : 忽略大小写
    
    name__contains : 大小写敏感

## 获得单个模型对象

* Model_object.objects.get() ：返回一个模型对象

  注 : 如果查询到多条记录或者没有查询到任何记录，get会抛出异常，类似：

  ```python
  mydjango.models.Student.MultipleObjectsReturned: get() returned more than one Student -- it returned 2!
  ```

  ```python
  mydjango.models.Student.DoesNotExist: Student matching query does not exist.
  ```

* 示例：

  ```python
  stu_girls = Student.objects.get(name='b')
  print(type(stu_girls))
  stu_girls = Student.objects.filter(name='b')
  print(type(stu_girls))
  ```

  ```python
  <class 'mydjango.models.Student'>
  <class 'django.db.models.query.QuerySet'>
  ```

* 改进：

  ```python
  try:
      stu_girls = Student.objects.get(gender='G')
      print(type(stu_girls))
  except Student.DoesNotExist:
      return HttpResponse("未查到任何信息")
  except Student.MultipleObjectsReturned:
      return HttpResponse("查询结果多余一条")
  return HttpResponse("查询成功")
  ```

## 数据排序

* 使用Model_object.objects.order_by() ：默认是升序

  Student.objects.order_by('grade') : 默认按照年级升序排列

  Student.objects.order_by('-grade') : 按照年级逆序（降序）排列

  按多个字段查找的时候，先按第一个字段排序，然后按第二个字段排序。。。

* 示例

  ```python
  def orderDB(request):
      dateSet = Student.objects.order_by('grade', 'age')
      result = []
      for stu in dateSet:
          result.append(stu.name)
      return HttpResponse(",".join(result))
  ```

## 连锁查询

* filter相当于SQL中的WHERE，order_by 相当于SQL中的ORDER BY

* 可以组合连锁查询

* 示例

  ```python
  def multiDB(request):
      dataSet = Student.objects.filter(grade='4').order_by('age')
      result = []
      for stu in dataSet:
          result.append(stu.name)
      return HttpResponse(",".join(result))
  ```

## 限制返回的数据

* 限制返回的数据个数，即返回查询结果集的子集

*  SQL：对应limit

  ```sql
  SELECT * FROM table1 WHERE name like 'a%' limit 1,10
  ```

  返回从第二条记录开始的10条记录，即2-11条记录

* 通过切片实现：[a:b] 和python切片意义一致，代表[a,b)，但不支持负索引

* 示例：

  ```python
  def limitDB(request):
      dataSet = Student.objects.order_by('grade')[1:3]
      result = []
      for stu in dataSet:
          result.append(stu.name)
      return HttpResponse(",".join(result))
  ```

## 更新指定列

* update底层过程

  ```python
  def updateDB(request):
      stu = Student.objects.get(name='a')
      stu.name = 'aa'
      stu.save()
      return HttpResponse('Success')
  ```

  实际上底层生成的sql语句是 :

  ```sql
  UPDATE mydjango_student SET name='aa',age=18,gender='G',grade=1 WHERE name='a';
  ```

  其他未修改字段的依旧重新设置了一遍

* 示例

  ```python
  def updateDB(request):
      stu = Student.objects.filter(name='a').update(name='aa')
      return HttpResponse('Success')
  ```

  

