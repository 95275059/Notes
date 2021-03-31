# LinuxTips30--TC5-Netem

## Netem概念

+ Netem是Linux2.6及以上内核版本提供的一个**网络模拟功能模块**
+ 该功能模块可以用来在性能良好的局域网中，模拟出复杂的互联网传输性能，诸如低带宽、传输延迟、丢包等等情况。
+ 使用Linux2.6或以上版本内核的很多发行版Linux都开启了该内核功能，比如Fedora、Ubuntu、Redhat、OpenSuse、CentOS、Debian等等。
+ **而TC可以用来控制netem的工作模式**
+ **总之，如果想使用netem，需要至少两个条件，一个是内核中的netem功能被包含，另一个是要有TC**

## Netem原理

+ TC用于Linux内核的流量控制，主要是通过在输出端口处建立一个队列来实现流量控制。
  + 接收包从**输入接口（Input Interface）**进来后，经过**流量限制（Ingress Policing）**丢弃不符合规定的数据包
  + 由**输入多路分配器（Input De-Multiplexing）**进行判断选择：如果接受包的目的是本主机，name将该包送给上层处理；否则需要进行转发，将接收包交到**转发块（Forwarding Block）**处理。转发块同时也接收本主机上层（TCP,UDP等）产生的包。
  + 转发块通过查看路由表，决定所处理包的下一跳
  + 然后，对包进行排列以便将它们传送到**输出接口（Output Interface）**
+ 一般我们只能限制网卡发送的数据包，不能限制网卡接收的数据包，所以我们可以通过改变发送次序来控制传输速录。
+ Linux流量控制主要是在输出接口排列时进行处理和实现的

## Netem命令

+ Netem可以完成如下功能：（故障）模拟时延，丢包，重复包，乱序

+ 模拟延时传输

  ```shell
  #tc qdisc add dev eth0 root netem delay 100ms
  ```

  + 该命令将eth0网卡的传输设置为延迟100毫秒发送

  ```shell
  #tc qdisc add dev eth0 root netem delay 100ms 10ms
  ```

  + 更真实的情况下，延迟值不会这么精确，会有一定的波动
  + 该命令将eth0网卡的传输设置为延迟90~110ms之间的任意值发送

  ```shell
  #tc qdisc add dev eth0 root netem delay 100ms 10ms 30%
  ```

  + 该命令将eth0网卡的传输设置为100ms，同时，大约有30%的包的延迟会在90~110ms之间

+ 模拟网络丢包

  ```shell
  #tc qdisc add dev eth0 root netem loss 1%
  ```

  + 该命令将eth0网卡的传输设置为随机丢掉1%的数据包

  ```shell
  #tc qdisc add dev eth0 root netem loss 1% 30%
  ```

  + 该命令将eth0网卡的传输设置为随机丢掉1%的数据包，丢包成功率为30%

+ 模拟包重复

  ```shell
  #tc qdisc add dev eth0 root netem duplicate 1%
  ```

  + 该命令将eth0网卡的传输设置为随机产生1%的重复数据包

+ 模拟包损坏

  ```shell
  #tc qdisc add dev eth0 root netem corrupt 0.2%
  ```

  + 该命令将eth0网卡的传输设置为随机产生0.2%的损坏的数据包
  + 注：内核版本需在2.6.16以上

+ 模拟包乱序

  ```shell
  #tc qdisc add dev eth0 root netem delay 10ms reorder 25% 50%
  ```

  + 该命令将eth0网卡的传输设置为：有25%的数据包（50%相关）会被立即发送，其他的延迟10ms

  ```shell
  #tc qdisc add dev eth0 root netem delay 100ms 10ms
  ```

  + 新版本中，上面这条命令也会在一定程度上打乱发包的次序

+ 删除配置

  ```shell
  #tc qdisc del dev eth0 XXXXXXXXXX(自己加的配置)
  ```

  + 该命令将删除eth0网卡的相关传输配置

  + ```shell
    tc qdisc del dev eth0 root
    ```

    这条命令会把网卡所有的tc配置全部清除掉（包括子类下的netem啥的），因为清除的是根，根下的子分类（class）也会被清除

+ 查看已经配置的网络条件

  ```shell
  #tc qdisc show dev eth0
  ```

  + 该命令将查看并显示eth0网卡的相关传输配置