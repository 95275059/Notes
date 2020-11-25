# LinuxTips61--Ubuntu开启root账户远程登录

### 设置root账户密码

Ubuntu默认是没有开启root账户登录选项的，想要在启动系统时用root账户登录系统，需要自己进行额外的设置。

+ 设置root账户密码

  ```bash
  cxy@ubuntu16:~$ sudo passwd
  Enter new UNIX password: 
  Retype new UNIX password: 
  passwd: password updated successfully
  ```

  执行命令后，首先输入当前账户密码，确认无误后，系统会提示`Enter new UNIX password`，这是root密码，自行设置。注意在Ubuntu的命令行中，输入的密码是不可见的，只需要输入之后回车即可。

+ 允许root用户ssh远程登录

  + 修改配置文件

    ```bash
    sudo vim /etc/ssh/sshd_config
    ```

    ```bash
    PermitRootLogin yes
    ```

    允许root登录

  + 注：

    ```bash
    PermitRootLogin prohibit-password 
    ```

    允许root登录，但是禁止root用密码登录

  + 重启服务

    ```bash
    sudo service ssh restart
    ```

    

  