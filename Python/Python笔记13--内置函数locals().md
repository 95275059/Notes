# Python笔记13--内置函数locals()

1. 描述

   + 会以**字典类型**返回当前位置的全部局部变量

   + 对于函数，方法，lambda函式，类，以及实现了\_\_call\_\_方法的类实例，它都返回True

2. 语法

   ```python
   locals()
   ```

   + 返回值：返回字典类型的局部变量

3. 实例

   ```python
   def test():
       username = 'admin'
       password = '123456'
       auth_url = 'http://controller:5000/v3'
       project_name = 'admin'
       project_domain_name = 'default'
       user_domain_name = 'default'
       print(locals())
   
   if __name__ == '__main__':
       test()
   ```

   output:

   ```python
   {'username': 'admin', 'password': '123456', 'auth_url': 'http://controller:5000/v3', 'project_name': 'admin', 'project_domain_name': 'default', 'user_domain_name': 'default'}
   ```

   

   

   

