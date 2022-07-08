# PythonDjango2--视图与Url

## 在视图中显示动态内容

* 新建ServerTime.py

  ```python
  from django.http import HttpResponse
  import datetime
  
  def currentDateTime(request):
      now = datetime.datetime.now()
      html = "<html><body>It is now %s.</body></html>" % now
      return HttpResponse(html)
  ```

* url.py 加入对应路由

## URL配置与松耦合

* 松耦合原则：是一种重要的保证互换性的软件开发方法

  例如：修改ServerTime.py 但不会影响url.py

  同时，一个view可能映射到多个url中

## 动态Url

* DynamicUrl.py

  ```python
  from django.http import HttpResponse
  from django.http import Http404
  
  def fun(request, value):
      try:
          value = int(value)
      except ValueError:
          raise Http404()
      result = 'fun%s' % value
      return HttpResponse(result)
  ```

* urls.py

  ```python
  re_path(r'^fun/(\d{1,3})/$', DynamicUrl.fun)
  ```

  