# PythonDjango6--通用视图类

## 简单的通用视图类

* 基类： django.views.generic.view

* 示例

  在views目录下新建CommonViewClass.py

  ```python
  from django.http import HttpResponse
  from django.views.generic import View  # 所有视图类的基类
  
  class MyView(View):
      def get(self, request, **kwargs):
          return HttpResponse('Hello World!')
  ```

  ```python
  re_path(r'^CommonView/$', CommonViewClass.MyView.as_view()),
  ```

## 可以向模板中传递变量值的通用视图类

* 基类： django.views.generic.base.TemplateView

* 示例

  ```python
  from django.views.generic.base import TemplateView  # 可以使用模板的类
  
  class HomePageView(TemplateView):
      template_name = 'test8_product1.html'    # TemplateView的成员变量
      def get_context_data(self, **kwargs):
          context = super(HomePageView, self).get_context_data(**kwargs)   # 固定格式
          context['phone_product1'] = 'Iphone'   # 传入参数
          context['phone_product2'] = 'Huawei'
          return context   # 注意返回
  ```

  ```python
  re_path(r'^TemplateView/$', CommonViewClass.HomePageView.as_view()),
  ```

## 用于页面跳转的通用视图类

* 基类：django.views.generic.base.RedirectView

* 示例：

  ```python
  from django.views.generic.base import RedirectView
  
  ...
  re_path(r'^RedirectView/$', RedirectView.as_view(url='http://baidu.com')),
  ...
  ```

## 列表视图（ListView）

* 基类：django.views.generic.ListView

* 示例：test13.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>ListView</title>
  </head>
  <body>
      <ul>
      {% for stu in students %}
          <li>{{ stu.name }} - {{ stu.age }} - {{ stu.gender }} - {{ stu.grade }}</li>
      {% endfor %}
      </ul>
  </body>
  </html>
  ```

  输出所有数据：

  ```python
  from django.views.generic import ListView
  from mydjango.models import Student
  
  class MyListView(ListView):
      model = Student   # ListView成员变量，指定模型类
      template_name = 'test13.html'   # ListView成员变量，指定模板
      context_object_name = 'students'   # ListView成员变量，重新指定返回给模板的变量名
  ```

  输出过滤后的部分数据：

  ```python
  class MyListView(ListView):
      model = Student   # ListView成员变量，指定模型类
      template_name = 'test13.html'   # ListView成员变量，指定模板
      context_object_name = 'students'   # ListView成员变量，重新指定返回给模板的变量名
      def get_queryset(self):   # ListView成员方法，默认返回所有数据，通过重写该方法实现数据过滤
          return super(MyListView, self).get_queryset().filter(grade = 4)
  ```

  * 这个示例过滤出年级为4的数据，但是是自己制定的过滤方案，并没有什么通用性，希望通过表单传入过滤方案提高通用性

  ```python
  from django.views.generic import ListView
  from mydjango.models import Student
  
  class MyListView(ListView):
      model = Student   # ListView成员变量，指定模型类
      template_name = 'test13.html'   # ListView成员变量，指定模板
      context_object_name = 'students'   # ListView成员变量，重新指定返回给模板的变量名
      def get_queryset(self):   # ListView成员方法，默认返回所有数据，通过重写该方法实现数据过滤
          grade = self.request.GET.get('grade')
          return super(MyListView, self).get_queryset().filter(grade=grade)
  ```

## 细节视图（DetailView）

* DetailView和ListView经常一起使用，使用ListView列出信息， 使用DetailView显示详细信息

* 基类：django.views.generic.DetailView

* 示例：test14.html

  ```python
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Student_detail</title>
  </head>
  <body>
      <h1>学生</h1>
      <p>姓名：{{ student.name }}</p>
      <p>年龄：{{ student.age }}</p>
      <p>性别：{{ student.gender }}</p>
      <p>年级：{{ student.grade }}</p>
  </body>
  </html>
  ```

  ```python
  from django.views.generic import DetailView
  
  
  class MyDetailView(DetailView):
      queryset = Student.objects.all()
      template_name = 'test14.html'
      context_object_name = 'student'
      def get_object(self, queryset=None):   # DetailView成员函数，用于获取对象，需要传入一个数据集
          obj = super(MyDetailView, self).get_object(queryset=queryset)
          return obj
  ```

  ```python
  re_path(r'^DetailView/(?P<pk>\d+)$', CommonViewClass.MyDetailView.as_view()),
  ```

