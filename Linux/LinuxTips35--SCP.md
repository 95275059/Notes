# LinuxTips35--SCP

1. 功能

   + 用于linux之间复制文件和目录
   + Secure Copy
   + 是linux系统下基于ssh登录进行安全的远程文件拷贝命令
   + scp是加密的，rcp是不加密的，scp是rcp的加强版

2. 语法

   ```shell
   scp [选项] file_source file_target
   ```

   ```shell
   scp [-1246BCpqrv] [-c cipher] [-F ssh_config] [-i identity_file] [-l limit] [-o ssh_option] [-P port] [-S program] [[user@]host1:]file1 [...] [[user@]host2:]file2
   ```

   | 选项             | 说明                                                         |
   | ---------------- | ------------------------------------------------------------ |
   | -1               | 强制scp使用协议ssh1                                          |
   | -2               | 强制scp使用协议ssh2                                          |
   | -4               | 强制scp命令只是用IPv4寻址                                    |
   | -6               | 强制scp命令只是用IPv6寻址                                    |
   | -B               | 使用批处理模式（传输过程中不询问传输口令或短语）             |
   | -C               | 允许压缩（将-C标志传递给ssh，从而打开压缩功能）              |
   | **-p**           | **保留源文件的修改时间，访问时间和访问权限**                 |
   | **-q**           | **不显示传输进度条**                                         |
   | **-r**           | **递归复制整个目录 **                                        |
   | **-v**           | **详细方式显示输出。**scp和ssh(1)会显示出整个过程的调试信息。这些信息用于调试连接，验证和配置问题 |
   | -c cipher        | 以cipher将数据传输进行加密，这个选项将直接传递给ssh          |
   | -F ssh_config    | 指定一个替代的ssh配置文件，这个参数直接传递给ssh             |
   | -i identity_file | 从指定文件中读取传输时使用的秘钥文件，此参数直接传递给ssh    |
   | -l limit         | 限定用户所能使用的带宽，以Kbit/s为单位                       |
   | -o ssh_option    |                                                              |
   | -P port          | port指定数据传输用到的端口号                                 |
   | -S program       | 指定加密传输时使用的程序。此程序必须能够理解ssh(1)的选项     |

3. 实例

   + 本地复制到远程

     + 复制文件

       ```shell
       scp local_file remote_username@remote_ip:remote_folder
       #指定了用户名，命令执行后需要输入密码；指定了远程目录，文件名不变
       scp local_file remote_username@remote_ip:remote_file
       #指定了用户名，命令执行后需要输入密码；指定了文件名
       scp local_file remote_ip:remote_folder
       #没有指定用户名，命令执行后需要输入用户名和密码；指定了远程目录，文件名不变
       scp local_file remote_ip:remote_file
       #没有指定用户名，命令执行后需要输入用户名和密码；指定了文件名
       ```

     + 复制目录

       ```shell
       scp -r local_folder remote_username@remote_ip:remote_folder
       #指定了用户名，命令执行后需要输入密码
       scp -r local_folder remote_ip:remote_folder
       #没有指定用户名，命令执行后需要输入用户名和密码
       ```

   + 远程复制到本地
     + 只需要将从本地复制到远程的命令的后两个参数调换顺序即可

4. 说明

   + 如果远程服务器防火墙有为scp命令设置了指定的端口，需要使用选项-P来设置命令的端口号
   + 使用scp命令要确保使用的用户具有可读取远程服务器响应文件的权限，否则scp无法起作用