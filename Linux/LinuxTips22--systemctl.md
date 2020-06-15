# LinuxTips22--systemctl

1. 通过systemctl管理单一服务

   systemctl [command] [unit]

   + command

     | command   | 说明                                               |
     | --------- | -------------------------------------------------- |
     | start     | 启动                                               |
     | stop      | 关闭                                               |
     | restart   | 重启                                               |
     | reload    | 在不关闭服务的情况下，重新载入配置文件，让设置生效 |
     | enable    | 开机自启动                                         |
     | disable   | 开机不启动                                         |
     | status    | 查看服务状态                                       |
     | is-active | 查看服务是否正在运行中                             |
     | is-enable | 查看是否开机自启动                                 |

2. 常见状态

   + active(running)

     正有一只或多只程序正在系统中执行

   + active(exited)

     仅执行一次就正常结束的服务，目前没有任何程序在系统中执行

   + active(waiting)

     正在执行当中，不过还在等待其他的事件才能继续处理。

   + inactive

     服务目前没有运行

   