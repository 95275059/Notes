# Linux笔记10--权限管理命令2

### 权限管理命令 chown(change file ownership)--对文件或目录都可以

+ 命令所在路径：/bin/chown

+ 执行权限：root

+ 语法：chown [用户] [文件或目录] (用户:新的所有者)

+ 功能：改变文件或目录的所有者

+ chown 需要超级用户 **root** 的权限才能执行此命令

+ 语法

  ```bash
  chown [-cfhvR] [--help] [--version] user[:group] file...
  ```

  | 选项      | 说明                                 |
  | --------- | ------------------------------------ |
  | user      | 新的文件拥有者的使用者 ID            |
  | group     | 新的文件拥有者的使用者组(group)      |
  | -c        | 显示更改的部分的信息                 |
  | -f        | 忽略错误信息                         |
  | -h        | 修复符号链接                         |
  | -v        | 显示详细的处理信息                   |
  | -R        | 处理指定目录以及其子目录下的所有文件 |
  | --help    | 显示辅助说明                         |
  | --version | 显示版本                             |

+ 示例

  + 把 /var/run/httpd.pid 的所有者设置 root

    ```bash
    chown root /var/run/httpd.pid
    ```

  + 将当前前目录下的所有文件与子目录的拥有者皆设为 runoob，群体的使用者 runoobgroup

    ```bash
    chown -R runoob:runoobgroup *
    ```

  + 把 /home/runoob 的关联组设置为 512 （关联组ID），不改变所有者

    ```bash
    chown :512 /home/runoob
    ```

 2.权限管理命令 chgrp(change file group ownership)

 命令所在路径：/bin/chgrp

 执行权限：root

 语法：chgrp [用户组] [文件或目录]

 功能：改变文件或目录的所属组

 ![](https://img-blog.csdnimg.cn/20190419134004786.PNG)

 注：groupadd命令为添加组，只能由root创建

 3.权限管理命令 umask(the user file-creation mask)

 命令所在路径：Shell内置命令

 执行权限：所有用户

 语法：umask [-S]

 -S 以rwx形式显示新建文件缺省权限

 功能：显示，设置文件的缺省权限 

 例1：

 ![](https://img-blog.csdnimg.cn/20190419140240555.PNG)

 在创建文件或目录时，所有者是创建该文件/目录的用户，所属组是缺省权限

 注意到，目录China(rwxrx-r-x)和文件test(rw-r--r--)的权限不一样，这是因为在Linux中权限管理有一个基本定义：缺省创建 的文件不能具有可执行权限(x)，这是基于安全性考虑(对于一些病毒木马文件，使其没有执行权限)

 例2：

 ![](https://img-blog.csdnimg.cn/20190419140947883.PNG)

 0：一种特殊权限 ；

 022：代表三种用户(UGO)的权限

 如果是目录：将777(rwx rwx rwx)与022(--- -w- -w-)做异或运算求得755(rwx r-x r-x)

 如果是文件：默认缺省权限为 : rw- r-- r--

 注：如果希望目录的缺省权限为700(rwx --- ---)(此时文件的缺省权限为600 : rw- --- ---) 则需要修改umask 

 将运算过程逆过来，得到umask应该改为077(--- rwx rwx) **[不推荐更改umask]**

 ![](https://img-blog.csdnimg.cn/20190419143529294.PNG)

 

   
