# LinuxTips23--chrony

1. chrony

   chrony有两个核心组件

   + chronyd:守护进程

     主要用于调整内核中运行的系统时间和时间服务器同步

     它确定计算机增加时间的比率，并对此进行调整补偿

   + chronyc:用户界面

     用于监控性能并进行多样化的；配置

     可以在chronyd实例控制的计算机上工作，也可以在一台不同的远程计算机上工作

2. chrony配置文件

   /etc/chrony.conf

   ```
   # Use public servers from the pool.ntp.org project.
   # Please consider joining the pool (http://www.pool.ntp.org/join.html).
   #使用pool.ntp.org项目中的公共服务器。以server开，理论上添加多少时间服务器都可以
   server 0.centos.pool.ntp.org iburst
   server 1.centos.pool.ntp.org iburst
   server 2.centos.pool.ntp.org iburst
   server 3.centos.pool.ntp.org iburst
   
   # Record the rate at which the system clock gains/losses time.
   # 根据实际时间计算出服务器增减时间的比率，然后记录到这个文件中，在系统重启后为系统做出最佳时间补偿调整
   driftfile /var/lib/chrony/drift
   
   # chronyd根据需求减慢或加速时间调整，
   # 在某些情况下系统时钟可能漂移过快，导致时间调整用时过长。
   # 该指令强制chronyd调整时期，大于某个阀值时步就调整系统时钟。
   # 只有在因chronyd启动时间超过指定的限制时（可使用负值来禁用限制）没有更多时钟更新时才生效。
   # Allow the system clock to be stepped in the first three updates
   # if its offset is larger than 1 second.
   makestep 1.0 3
   
   # Enable kernel synchronization of the real-time clock (RTC).
   # 将启用一个内核模式，在该模式中，系统时间每11分钟会拷贝到实时时钟（RTC）。
   rtcsync
   
   # Enable hardware timestamping on all interfaces that support it.
   # 通过使用hwtimestamp指令启用硬件时间戳
   #hwtimestamp *
   
   # Increase the minimum number of selectable sources required to adjust
   # the system clock.
   #minsources 2
   
   # Allow NTP client access from local network.
   # 指定一台主机、子网，或者网络以允许或拒绝NTP连接到扮演时钟服务器的机器
   #allow 192.168.0.0/16
   #deny 192.168/16
   
   # Serve time even if not synchronized to a time source.
   #local stratum 10
   
   # Specify file containing keys for NTP authentication.
   # 指定包含NTP验证密钥的文件。
   #keyfile /etc/chrony.keys
   
   # Specify directory for log files.
   # 指定日志文件的目录。
   logdir /var/log/chrony
   
   # Select which information is logged.
   #log measurements statistics tracking
   
   ```

3. 实例测试

   服务端：192.168.92.70

   客户端：192.168.92.71

   + 安装chrony

     yum install -y chrony

   + firewalld设置

     #由于NTP使用123/UDP端口，所以需要firewalld允许NTP服务

     firewall-cmd --add-service=ntp --permanent

     firewall-cmd --reload

   + 设置时区

     + 查看系统时区

       + timedatectl

         ```
               Local time: 四 2019-10-10 15:21:38 CST
           Universal time: 四 2019-10-10 07:21:38 UTC
                 RTC time: 四 2019-10-10 07:21:37
                Time zone: Asia/Shanghai (CST, +0800)
              NTP enabled: yes
         NTP synchronized: yes
          RTC in local TZ: no
               DST active: n/a
         
         ```

         如果当前时区不正确，按下面步骤设置

         + 查看所有可用的时区

           timedatectl list-timezones

         + 筛选查看在亚洲并且S开头的时区

           timedatectl list-timezones | grep -E "Asia/S.*"

         + 设置当前系统为Asia/Shanghai时区

           timedatectl set-timezone Asia/Shanghai

         + 强制同步系统时钟

           chronyc -a makestep

   + 服务端

     + 编辑服务端配置文件/etc/chrony.conf

       + 注释掉默认时间同步服务器

         ```
         #server 0.centos.pool.ntp.org iburst
         #server 1.centos.pool.ntp.org iburst
         #server 2.centos.pool.ntp.org iburst
         #server 3.centos.pool.ntp.org iburst
         ```

       + 添加时间的同步源time5.aliyun.com

         ```
         server time5.aliyun.com iburst
         ```

       + 去掉 allow 192.168.0.0/16 的注释

         允许其他节点网段同步时间，配置为对应网段

     + 重启服务并加入开机启动项

       systemctl enable chronyd.service && systemctl restart chronyd.service

     + 查看时间同步状态

       + chronyc sources

         ```
         210 Number of sources = 4
         MS Name/IP address         Stratum Poll Reach LastRx Last sample               
         ===============================================================================
         ^+ amy.chl.la                    2   6    17     5  -1429us[-2305us] +/-  188ms
         ^* sv1.ggsrv.de                  2   6    17     4  +4525us[+3649us] +/-  160ms
         ^? a.chl.la                      0   6     0     -     +0ns[   +0ns] +/-    0ns
         ^+ ntp5.flashdance.cx            2   6    17     4  +6134us[+5258us] +/-  215ms
         ```

         注：^*代表NTP服务当前同步的服务器

     + 查看当前时间是否准确

       timedatectl

       ```
             Local time: 四 2019-10-10 16:11:15 CST
         Universal time: 四 2019-10-10 08:11:15 UTC
               RTC time: 四 2019-10-10 08:11:15
              Time zone: Asia/Shanghai (CST, +0800)
            NTP enabled: yes
       NTP synchronized: yes
        RTC in local TZ: no
             DST active: n/a
       ```

       注：NTP synchronized: yes代表同步成功

   + 客户端

     + 修改配置文件，使客户端与服务端同步时间

       vim /etc/chrony.conf

       ```
       #server 0.centos.pool.ntp.org iburst
       #server 1.centos.pool.ntp.org iburst
       #server 2.centos.pool.ntp.org iburst
       #server 3.centos.pool.ntp.org iburst
       server 192.168.92.70 iburst
       ```

     + 重启服务并设置开机启动

       systemctl enable chronyd.service && systemctl restart chronyd.service

     + 查看时间同步状态

       chronyc source

       ```
       210 Number of sources = 1
       MS Name/IP address         Stratum Poll Reach LastRx Last sample               
       ===============================================================================
       ^* 192.168.92.70            3   6   377   112  -3560ns[ -180us] +/-   26ms
       ```

     + 查看时间是否与服务端一致

       timedatectl

4. NTP其他操作命令
   + timedatectl set-ntp yes   #启动ntp同步服务
   + timedatectl set-timezone Asia/Shanghai   #设置时区
   + yum install -y ntpdate   #安装时间同步工具
   + ntpdate 0.centos.pool.ntp.org   #强制与网络NTP服务器同步时间
   + ntpdate 192.168.92.70   #强制与192.168.92.70同步时间





