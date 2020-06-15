# Python笔记8--python字符串前u,r,b

1. 字符串前加u

   + 字符串以Unicode格式进行编码，一般用在中文字符串前，防止因为源码存储格式问题，导致再次使用时出现乱码

2. 字符串前加r

   + 去掉反斜杠的转义机制

   + 例

     ```python
     print(r'\n\t')
     #\n\t
     ```

3. 字符串前加b

   + b""代表后面字符串是bytes类型

   + 网络编程中，**服务器和浏览器**只认bytes类型数据

   + python3中bytes和str的相互转换方式是

     ```python
     str.encode('utf-8')
     bytes.decode('utf-8')
     ```

     

