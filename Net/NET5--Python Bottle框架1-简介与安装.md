# NET5--Python Bottle框架1-简介与安装

1. Bottle简介

   Bottle 是一个快速，简单，轻量级的 Python WSGI Web 框架。单一文件，只依赖 Python 标准库 。

   [Bootle](http://bottlepy.org/docs/dev-cn/) 是一个非常精致的WSGI框架，它提供了 Python Web开发中需要的基本支持：URL路由，Request/Response对象封装，模板支持，与WSGI服务器集成支持。整个框架的全部代码约有 2000行，它的核心部分没有其他任何依赖，只要有Python环境就可以运行。

   Bottle适用于**小型的Web开发**，在应用程序规模比较小的情况下可以实现快速开发。但是由于自身功能所限，对于大型的Web程序，Bottle的功能略显不足，程序员需要手动管理模块、数据库、配置等等，与Pylons等框架相比Bottle的优势就难以体现出来了。

   + URL映射（Routing）：将URL请求映射到Python函数，使URL更简洁。
   + 模板（Templates）：快速且pythonic的内置模板引擎，同时支持mako，jinja2和cheetah等模板。
   + 基础功能（Utilities）：方便地访问表单数据，上传文件，使用cookie，查看HTTP元数据。
   + 开发服务器（Server）：内置了开发服务器，且支持paste，fapw3，bjoern，Google App Engine，cherrypy 等符合 WSGI 标准的 HTTP 服务器。

2. 安装

   Bootle并不基于任何扩展的类库。只需要下载bootle.py文件到项目目录就可以使用

   + 在pycharm项目的terminal下直接 pip install bottle