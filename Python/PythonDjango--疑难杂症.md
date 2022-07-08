# PythonDjango--疑难杂症

## 403 Forbidden

```
CSRF verification failed. Request aborted.
```

### 解决方案

* 方法一：我们可以在settings.py中注释掉一行即可。这一行大概在46行左右。

  ```
  'django.middleware.csrf.CsrfViewMiddleware'
  ```

* 方法二：在html页面的form标签下加上

  ```
  {%csrf_token%}
  ```

* 方法三：views.py上导入

  ```
  from django.views.decorators.csrf import csrf_exempt
  ```

  然后在自己写的函数上面加上

  ```
  @csrf_exempt
  ```

