# JavaSpring2--IoC容器

## 容器

* 容器是一种为某种特定组件的运行提供必要支持的一个软件环境。

  例如，Tomcat就是一个Servlet容器，它可以为Servlet的运行提供运行环境。

  类似Docker这样的软件也是一个容器，它提供了必要的Linux环境以便运行一个特定的Linux进程。

* 通常来说，使用容器运行组件，除了提供一个组件运行环境之外，容器还提供了许多底层服务。

  例如，Servlet容器底层实现了TCP连接，解析HTTP协议等非常复杂的服务，如果没有容器来提供这些服务，我们就无法编写像Servlet这样代码简单，功能强大的组件。

  早期的JavaEE服务器提供的EJB容器最重要的功能就是通过声明式事务服务，使得EJB组件的开发人员不必自己编写冗长的事务处理代码，所以极大地简化了事务处理。

* **Spring的核心就是提供了一个IoC容器**，它可以管理所有轻量级的JavaBean组件，提供的底层服务包括组件的生命周期管理、配置和组装服务、AOP支持，以及建立在AOP基础上的声明式事务服务等。

## IoC原理

* IoC全称Inversion of Control，直译为控制反转。

### Java组件协作方式

* 我们假定一个在线书店，通过`BookService`获取书籍：

  ```java
  public class BookService {
      private HikariConfig config = new HikariConfig();
      private DataSource dataSource = new HikariDataSource(config);
  
      public Book getBook(long bookId) {
          try (Connection conn = dataSource.getConnection()) {
              ...
              return book;
          }
      }
  }
  ```

* 为了从数据库查询书籍，`BookService`持有一个`DataSource`。为了实例化一个`HikariDataSource`，又不得不实例化一个`HikariConfig`。

