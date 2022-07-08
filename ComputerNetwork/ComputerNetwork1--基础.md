# ComputerNetwork1--基础

### 二层网络、三层网络

https://blog.csdn.net/cj2580/article/details/80107037

### 集线器、网桥、交换机

https://blog.csdn.net/dataiyangu/article/details/82496340

+ 集线器(HUB) -- 物理层
+ 网桥(Network Bridge) -- 链路层
+ 交换机(Switch) -- 链路层

### VLAN(Virtual Local Area Network)

+ 参考网站

  **https://blog.csdn.net/liufuchun111/article/details/90710838**

  https://blog.csdn.net/qq_38265137/article/details/80390759

* 用于在二层交换机上分割广播域的技术
* 可以直观的描述为：Vlan将一台交换机在逻辑上分割成了数台交换机
* 设置vlan后不同VLANID的广播域被隔离，要实现不同VLANID广播域通信，需要用到VLAN间路由服务
  * VLAN间路由可以使用普通的路由器，也可以使用三层交换机

### Vxlan（Virtual **eXtensible** Local Area Network）

+ https://blog.csdn.net/tony_vip/article/details/100097245
  + 虚拟机迁移

    + 将虚拟机从一个物理机迁移到另一个物理机

    + 在迁移过程中，业务不能中断

      + 虚拟机迁移前后，IP地址，MAC地址等参数位置不变

        + 即，迁移必须发生在同一个二层域中

### 关于发送数据包时，如何获取目的MAC地址

TCP/IP里面是用的ARP协议。比如新建了一个内网，如果一台机器A找机器B，封装FRAME时（OSI的第二层用的数据格式），要封装对方的MAC，开始时A不知道B的MAC，只知道IP，它就发一个ARP包，源IP是自己的，目的IP是B的，源MAC是自己的，目的MAC是广播的。然后这个请求包在内网内被广播，当其他机器接到这个包时，用目的IP和自己的IP比较，不是的话就丢弃。B接到时，发现IP与自己的一样，就答应这个包的请求，把自己的MAC送给A。如果B是其他子网的机器，那么路由器会判断出B是其他子网，然后路由器把自己的MAC返回给A，A以后再给B发包时，目的MAC封装的是路由器的。



