# NET3--REST与RESTful

1. REST

   REST(Representational State Transfer)：表征性状态转移

   REST指的是一组架构约束条件和原则，如果一个架构符合REST的约束条件和原则，就称它为RESTful架构

   REST本身并没有创造新的技术、组件或服务，而隐藏在RESTful背后的理念就是使用Web的现有特征和能力， 更好地使用现有Web标准中的一些准则和约束。

2. REST的约束条件和原则

   + REST面向资源，资源通过URI进行暴露

   + 客户-服务器（cs）

   + 无状态：服务器不会保存有关客户的任何状态，来自客户的每个请求必须包含服务器处理该请求所需的所有信息

   + 可缓存

     例如：服务器通过token缓存已登录过的用户信息，客户端请求会带一个token过来，后台服务通过带过来的token在缓存中取出用户信息，提高效率

   + 分层系统

   + 统一接口

     | 操作           | 非REST                           | REST                          |
     | -------------- | -------------------------------- | ----------------------------- |
     | 获取所有小狗狗 | GET /rest/api/getDogs            | GET /rest/api/dogs            |
     | 添加一个小狗狗 | GET /rest/api/addDogs            | POST /rest/api/dogs           |
     | 修改一个小狗狗 | GET /rest/api/editDogs/:dog_id   | PUT /rest/api/dogs/:dog_id    |
     | 删除一个小狗狗 | GET /rest/api/deleteDogs/:dog_id | DELETE /rest/api/dogs/:dog_id |

     REST很好地利用了HTTP的动词，状态码，报头等。

3. REST优缺点
   + 优点：是因为他对URI进行了限制，只用于定义资源。这样看起来比较容易理解。尤其是对简单的对象的增删改查，很好理解。
   + 缺点：是因为这种限制，导致设计URI变得复杂了。尤其是复杂的关系，操作，资源集合，硬性套用REST原则设计非常困难