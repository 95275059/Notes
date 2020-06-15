

# Linux笔记61--系统管理5-系统定时任务

1. crond服务管理与访问控制

   默认情况下开机自启动

   systemctl status crond查看状态

2. 用户的crontab设置

   crontab [选项]

   | 选项 | 说明                          |
   | ---- | ----------------------------- |
   | -e   | 编辑crontab定时任务           |
   | -l   | 查询crontab任务               |
   | -r   | 删除当前用户所有的crontab任务 |

   ---

   ---

   crontab -e

   进入crontab编辑界面。打开vim编辑工作

   [] [] [] [] [] 执行的任务

   ---

   | 项目     | 含义                 | 范围                    |
   | -------- | -------------------- | ----------------------- |
   | 第一个[] | 一小时当中的第几分钟 | 0-59                    |
   | 第二个[] | 一天当中的第几小时   | 0-23                    |
   | 第三个[] | 一个月当中的第几天   | 1-31                    |
   | 第四个[] | 一年当中的第几个月   | 1-12                    |
   | 第五个[] | 一周当中的星期几     | 0-7（0和7都代表星期日） |

   | 特殊符号 | 含义                 |
   | -------- | -------------------- |
   | *        | 代表任意时间         |
   | ,        | 代表不连续的时间     |
   | -        | 代表连续的时间范围   |
   | */n      | 代表每隔多久执行一次 |

   ---

   | 时间              | 含义                                                    |
   | ----------------- | ------------------------------------------------------- |
   | 45 22 * * * 命令  | 在22点55分执行命令                                      |
   | 0 17 * * 1 命令   | 每周一17点整执行命令                                    |
   | 0 5 1,15 * * 命令 | 每月一号和十五号的凌晨五点整执行命令                    |
   | 40 4 * * 1-5 命令 | 每周一到周五的凌晨4点40分 执行命令                      |
   | */10 4 * * * 命令 | 每天凌晨4点每隔10分钟执行一次命令                       |
   | 0 0 1,15 * 1 命令 | 每月一号和十五号以及每月的每周一 这些天的零点整执行命令 |

   ==注：星期几和几号最好不要同时出现，他们定义的都是天，非常容易让管理员混乱==

   ==注：定时任务识别的最小时间单位是分钟，只要分钟变了，就认为过了一分钟==

3. 例子：autobak.sh

   ```
   #!/bin/bash
   
   date=$(date +\%y\%m\%d)    
   #在定时任务中，%有特殊含义，因此必须在%前加上\来取消这种特殊含义
   size=$(du -sh /etc)
   
   echo "Date : $date!" > /home/cxy/sh/dbinfo.txt
   echo "Data size : $size" >> /home/cxy/sh/dbinfo.txt
   cd /home/cxy/sh
   tar -zcf etc_$date.tar.gz /etc /home/cxy/sh/dbinfo.txt &>/dev/null
   rm -rf /home/cxy/sh/dbinfo.txt
   ```

   + crontab -e

     0 5 * * * /home/cxy/sh/autobak.sh

     ==注：手动修改时间（date -s 04:59:30）会出现错误，不要自己修改时间==

   + 查看结果

4. 无法定时可能的原因

   + 环境变量

     解决方法：

     ```
     source /etc/profile
     . ~/.bash_profile
     #!/bin/bash
     ...
     ```

   + PATH

     + cat /etc/crontab

       SHELL=/bin/bash
       PATH=/sbin:/bin:/usr/sbin:/usr/bin
       MAILTO=root

     + echo $PATH

       /usr/lib64/qt-3.3/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin

     在脚本中加入一行：

     export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/root/bin