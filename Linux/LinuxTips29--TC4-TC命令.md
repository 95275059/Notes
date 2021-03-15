# LinuxTips29--TC4-TC命令

## Linux流量控制具体流程

- 基本步骤
  - 针对网络物理设备（如以太网卡eth0）绑定一个队列QDisc；
  - 在该队列上建立分类class；
  - 为每一分类建立一个基于路由的过滤器filter；
  - 最后与过滤器相配合，建立特定的路由表。

---

## TC中队列和类别的标识

+ 使用“major:minor”这样的句柄来标识队列和类别，其中major和minor为数字

+ 队列

  + minor总是为0，即“major:0”，也可以简写为“major:”

  + major在同一个网卡的所有队列中必须是唯一的

+ 类别

  + 类别的major必须和它的父类别或父队列的major相同
  + minor在同一个队列内部则必须是唯一的

---

## TC命令

### 基本操作

+ add

  在一个节点里加入一个QDisc、类或者过滤器。添加时，需要传递一个祖先作为参数，传递参数时既可以使用ID也可以直接传递设备的根。如果要建立一个QDisc或者过滤器，可以使用**句柄(handle)**来命名；如果要建立一个类，可以使用**类识别符(classid)**来命名。

- remove

  删除有某个句柄(handle)指定的QDisc，根QDisc(root)也可以删除。被删除QDisc上的所有子类以及附属于各个类的过滤器都会被自动删除。

- change

  以替代的方式修改某些条目。除了句柄(handle)和祖先不能修改以外，change命令的语法和add命令相同。换句话说，change命令不能一定（移动==？==）节点的位置。

- replace

  对一个现有节点进行近于原子操作的删除／添加。如果节点不存在，这个命令就会建立节点。

- link

  只适用于DQisc，替代一个现有的节点。

### 流量监视

+ 显示队列的状况

  ```shell
  #tc qdisc ls dev eth0
  ```

  + 简单显示指定设备的队列状况

  ```shell
  #tc -s qdisc ls dev eth0
  ```

  + 详细显示指定设备的队列状况

+ 显示分类状况

  ```shell
  #tc class ls dev eth0
  ```

  + 简单显示指定设备的分类状况

  ```shell
  #tc -s class ls dev eth0
  ```

  + 详细显示指定设备的分类状况

+ 显示过滤器状况

  ```shell
  #tc -s filter ls dev eth0
  ```

---

## 示例1

> 假设eth0出口有100mbit/s的带宽， 分配给WWW 、E-mail和Telnet三种数据流量， 其中分配给WWW的带宽为40Mbit/s，分配给Email的带宽为40Mbit/s， 分配给Telnet的带宽为20Mbit/S。

### 创建HTB队列

```shell
#tc qdisc [add|change|replace|link] dev DEV [parent qdisk-id|root][handle qdisc-id] qdisc[qdisc specific parameters]
```

+ 为网卡eth0配置一个HTB队列

  ```shell
  #tc qdisc add dev eth0 root handle 1: htb default 1 r2q 0
  ```

  + ”add 表示要添加
  
  + ”dev eth0 表示要操作的网卡为eth0
  
  + ”root 表示为网卡eth0添加的是一个根队列
  
  + ”handle 1: 表示队列的句柄为1:
  
  + ”htb 表示要添加的队列为HTB队列。
  
  + ”default 1" 是htb特有的队列参数，意思是所有未分类的流量都将分配给类别1:11。
  
  + "r2q 0" 是针对quantum的设置
  
    根据HTB的官方文档显示，quantum是在可以“借”的情况下，一次可以“借”多少，并且说这个值最好尽量的小，但要大于MTU
  
    而且这个值是不用手动设置，它会根据r2q的值计算出来。
  
    quantum = rate / r2q
  
    **1500 < quantum < 60000**
  
    r2q 0 可能就是不借

### 为本队列创建相应的类别

```shell
#tc class [add|change|replace] dev DEV parent qdisc-id [classid class-id] qdisc [qdisc specific parameters]
```

+ 可以利用下面这三个命令为根队列1创建三个类别，分别是1:11,1:12和1:13，它们分别占用40、40和20mbit的带宽。

  ```shell
  #tc class add dev eth0 parent 1: classid 1:11 htb rate 40mbit ceil 40mbit
  ```

  ```shell
  #tc class add dev eth0 parent 1: classid 1:12 htb rate 40mbit ceil 40mbit
  ```

  ```shell
  #tc class add dev eth0 parent 1: cllassid 1:13 htb rate 20mbit ceil 20mbit
  ```

  + ”parent 1:”表示类别的父亲为根队列1:
  + ”classid1:11″表示创建一个标识为1:11的类别
  + ”rate 40mbit”表示系统将为该类别确保带宽40mbit，”ceil 40mbit”，表示该类别的最高可占用带宽为40mbit。

### 为各个类别设置过滤器

```shell
#tc filter [add|change|replace] dev DEV [parent qdisc-id|root] protocol protocol prio priority filtertype [filtertype specific parameters] flowid flow-id
```

+ 由于需要将WWW、E-mail、Telnet、三种流量分配到三个类别，即上述1:11,1:12,1:13。因此，需要创建三个过滤器

  ```shell
  #tc filter add dev eth0 protocol ip parent 1:0 prio 1 u32 match ip dport 80 0xffff flowid 1:11
  ```

  ```shell
  #tc filter add dev eth0 protocol ip parent 1:0 prio 1 u32 match ip dport 25 0xffff flowid 1:12
  ```

  ```shell
  #tc filter add dev eth0 protocol ip parent 1:0 prio 1 u32 match ip dport 23 oxffff flowid 1:13
  ```

  + "protocol ip" : 表示该过滤器应该检查报文分组的协议字段

  + “prio 1” : 表示它们对报文处理的优先级别是相同的

    ==注：对于不同优先级的过滤器，系统将按照从小到大的优先级顺序来执行过滤器；对于相同的优先级，系统将按照命令的先后顺序执行==

  + u32选择器

    用于匹配不同的数据流

    + 以第一个命令为例
    + 判断的是dport字段
    + 如果该字段与0xffff进行与操作的结果是80，则“flowid 1:11”表示将把数据流分配给类别1:11

### 带宽共享

+ 上面的例子中，三种数据流（www、Email、Telnet）之间是互相排斥的

+ 当某个数据流的流量没有达到配额时，其剩余的带宽并不能被其他两个数据流所借用。即不同的数据流无法==共享（一定的）带宽==

+ 带宽共享

  + HTB带宽共享原理
    + 对于一个类别中的所有子类别，它们将共享该父类别所拥有的带宽，同时，又可以使得各个子类别申请的各自带宽得到保证
    + 当某个数据流的实际使用带宽没有达到其配额时，其剩余的带宽可以借给其他的数据流。
    + 而在借出的过程中，如果本数据流的数据量增大，则借出的带宽部分将收回，以保证本数据流的带宽配额


## 示例2

> 同样是三个数据流WWW、E-mail和Telnet。其中的Telnet独立分配20Mbit/s的带宽；WWW和E-mail各自分配40Mbit/s的带宽，同时它们又是共享的关系，即它们可以互相借用带宽

![](.\tips29-1.jpg)

### TC命令

+ 创建HTB队列

  ```shell
  #tc qdisc add dev eth0 root handle 1: htb default 21
  ```

+ 创建20M的独立分类（for Telnet）

  ```shell
  #tc class add dev eth0 parent 1: classid 1:1 htb rate 20mbit ceil 20mbit
  ```

+ 创建80M的共享分类

  ```shell
  #tc class add dev eth0 parent 1: classid 1:2 htb rate 80mbit ceil 80mbit
  ```

+ 创建40M子分类（for WWW）

  ```shell
  #tc class add dev eth0 parent 1:2 classid 1:21 htb rate 40mbit ceil 40 mbit
  ```

+ 创建40M子分类（for E-mail）

  ```shell
  #tc class add dev eth0 parent 1:2 classid 1:22 htb rate 40mbit ceil 40mbit
  ```

+ 为20M的独立分类（Telnet）设置过滤器

  ```shell
  #tc filter add dev eth0 protocol ip parent 1: prio 1 u32 match ip dport 23 0xffff flowid 1:1
  ```

+ 为40M的子分类（WWW）设置过滤器

  ```shell
  #tc filter add dev eth0 protocol ip parent 1: prio 1 u32 match ip dport 80 0xffff flowid 1:21
  ```

+ 为40M的子分类（E-mail）设置过滤器

  ```shell
  #tc filter add dev eth0 protocol ip parent 1: prio 1 u32 match ip dport 25 0xffff flowid 1:22
  ```

+ **HTB队列中类别和子类别的包含关系，可以构建更复杂的多层次类别树，从而实现更加灵活地带宽共享和独占模式，达到企业级的带宽管理目的**

  









