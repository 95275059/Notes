# LinuxTips20--wget工具

1. wget简介

   + wget是一个下载文件的工具

   + 支持HTTP,HTTPS,FTP协议，可以使用HTTP代理。

   + 能够自动下载

     wget可以在用户退出系统之后继续在后台执行。

     即用户在登录系统后，启动一个wget下载任务，然后退出系统，wget将在后台执行直到任务完成。

   + 递归下载

     wget可以跟踪HTML页面上的链接依次下载来创建远程服务器的本地版本，完全重建原始站点的目录结构

   + 稳定

     在带宽很窄的情况下和不稳定网络中有很强的适应性。

     如果是由于网络的原因下载失败，wget会不断尝试的，直到整个文件下载完毕。

     如果是服务器打断下载进程，wget会再次联到服务器上从挺值得地方继续下载。--对从限定了链接时间的服务器上下载大文件非常有用

2. wget命令

   wget [选项] [URL]

   | 选项                      | 说明                                                 |
   | ------------------------- | ---------------------------------------------------- |
   | -P                        | 指定下载到哪个目录                                   |
   | -r                        | 递归下载                                             |
   | -np                       | 不追溯到父目录                                       |
   | -c                        | 断点续传                                             |
   | -nd                       | 递归下载时不创建一层层目录，把所有文件下载到当前目录 |
   | -o                        | 将log指定保存到文件（新建一个文件）                  |
   | -a,--append-output=FILE   | 把记录追加到FILE文件中                               |
   | -A                        | 只下载指定文件类型                                   |
   | -N                        | 不要重新下载文件除非比本地文件新                     |
   | -O,--output-document=FILE | 下载并以不同的文件名保存                             |
   | -nc                       | 不要覆盖存在的文件或使用.#前缀                       |
   | -q                        | 安静模式（无信息输出）                               |
   | -v                        | 详尽的输出（此为默认值）                             |
   | -b                        | 启动后转入后台                                       |
   | -i                        | 下载本地或外部FILE中的URLs                           |

3. 实例

   + 下载单个文件

     wget http://www.baidu.com

     wget -q http://www.baidu.com    #安静模式下载

     直接在当前目录下载一个index.html文件。如果当前目录已经有同名文件，会在后面加数字

   + 下载到指定目录

     wget -P /home/cxy/ http://www.baidu.com

   + 将下载的文件存放到指定的文件夹下，同时重命名下载的文件

     wget -O /home/cxy/baidu.index http://www.baidu.com

   + 下载多个文件

     + 法一：直接带多个URL

       wget -P /home/cxy/ http://www.baidu.com  http://www.taobao.com

     + f法二：将多个URL写入文件

       + 将多个URL写入文件file.txt

         ```
         vim file.txt
         
         http://www.baidu.com
         http://www.taobao.com
         ```

       + wget -i file.txt