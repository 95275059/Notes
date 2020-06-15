# LinuxTips37--su命令

1. 功能

   用于变更为其他使用者的身份

   除了root外，需要键入该使用者的密码

   使用权限：所有使用者

2. 语法

   ```shell
   su [-fmp] [-c command] [-s shell] [--help] [version] [-] [--l] [USER [ARG]]
   ```

   | 参数                             | 说明                                                         |
   | -------------------------------- | ------------------------------------------------------------ |
   | -f (或--fast)                    | 不必读启动档（如 csh.cshrc等），仅用于csh或tcsh              |
   | -m -p (或--preserve-environment) | 执行时不改变环境变量                                         |
   | -c command (或--command=command) | 变更为账号为USER的使用者并执行命令（command）后再变回原来的使用者 |
   | -s shell (或--shell=shell)       | 指定要执行的shell(bash csh tcsh等)，预设值为/etc/passwd内的该使用者（USER）shell |
   | --help                           | 显示说明文件                                                 |
   | --versin                         | 显示版本咨询                                                 |
   | --l (或--login)                  | 增加该参数以后，就像是重新login为该使用者（USER）一样，大部分环境变量（HOME SHELL USER等等）都是以该使用者为主，并且工作目录也会改变；如果没有指定USER，内定是root |
   | USER                             | 欲变更的使用者账号                                           |
   | ARG                              | 传入新的shell参数                                            |

3. 实例

   + 变更账号为root并在执行ls指令后退出变回原使用者

     ```shell
     su -c ls root
     ```

   + 变更账号为root并传入-f参数给新执行的shell

     ```shell
     su root -f
     ```

   + 变更账号为clsung并改变工作目录至clsung的家目录（home dir）

     ```shell
     su - clsung
     ```

   + 切换用户

     ```shell
     hnlinux@runoob.com:~$ whoami //显示当前用户
     hnlinux
     hnlinux@runoob.com:~$ pwd //显示当前目录
     /home/hnlinux
     hnlinux@runoob.com:~$ su root //切换到root用户
     密码： 
     root@runoob.com:/home/hnlinux# whoami 
     root
     root@runoob.com:/home/hnlinux# pwd
     /home/hnlinux
     ```

   + 切换用户并切换到root的家目录

     ```shell
     hnlinux@runoob.com:~$ whoami //显示当前用户
     hnlinux
     hnlinux@runoob.com:~$ pwd //显示当前目录
     /home/hnlinux
     hnlinux@runoob.com:~$ su - root //切换到root用户
     密码： 
     root@runoob.com:/home/hnlinux# whoami 
     root
     root@runoob.com:/home/hnlinux# pwd //显示当前目录
     /root
     ```

     