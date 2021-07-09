# PythonDjango1--基础

## 简介

### 介绍

* Django是一个基于Python的Web应用框架

* 和Flask的区别：

  奉行“包含一切”的哲学

  Django包含了几乎所有的Web开发功能

  例如：身份验证、URL路由、ORM、数据库迁移等功能

* Django看上去失去了一些弹性，但是在某种程度上开发网站会更有效率

### Django工作方式

* Django是MTV框架，和MVC类似

  * MVC框架 : 业务模型（model）、用户界面（view）、控制器（controller）

    使用*MVC*的目的是将M和V的实现代码分离，从而使同一个程序可以使用不同的表现形式。

    比如一批统计数据可以分别用柱状图、饼图来表示。

    C存在的目的则是确保M和V的同步，一旦M改变，V应该同步更新。

  * MTV框架 : 模型（model）、模板（template）、视图（view）

    * Model(模型)： 负责业务对象与数据库的对象(ORM)。
    * Template(模板)：负责如何把页面展示给用户。
    * View(视图)：负责业务逻辑，并在适当的时候调用Model和Template。

    Django还有一个urls分发器，它的作用是将一个个URL的页面请求分发给不同的View处理，view再调用相应的Model和Templage。

  * Django将MVC中的视图进一步分解为Django视图和Django模板两部分。分别决定“展示哪些数据”和“如何展现”

    使得Django模板根据需要随时替换，而不仅仅限于内置的模板

    MVC中的Controller控制器部分，由Django框架的URL conf来实现的

  * 工作流程

    ![Django1-1](E:\Notes\Python\Django1-1.png)

### Django框架的组成部分

* ORM（面向对象的映射器，用于数据模型和关系型数据库间的媒介）
* 一个基于正则表达式的URL分发器
* 一个视图系统，用于处理请求
* 一个模板系统
* 除此之外，还包含一些组件
  * 一个轻量级的、独立的Web服务器，用于开发和测试
  * 一个表单序列化及验证系统
  * 一个缓存框架
  * 中间件支持
  * 内置的分发系统
  * 序列化系统
  * 自动化管理界面
  * 。。。

### Django框架的优缺点

* 优点

  * 文档非常齐全

  * 全套的解决方案

    例如，cache，session，orm

  * 强大的URL路由配置

* 缺点

  * 系统解耦合

    例如ORM，Template、SQLAlchemy

  * 自带的ORM远不如SQLAlchemy
  * Template功能比较弱，不能插入Python代码
  * URL配置虽然强大，但全部要手写

## 安装Django开发环境

```shell
pip install Django
```

## 使用startproject命令创建Django Web工程

* 安装完Django后，会有一个全局的脚本文件django-admin.py，该文件提供了一个命令startproject，后跟工程名字

  ```
  django-admin startproject hello
  ```

* 











