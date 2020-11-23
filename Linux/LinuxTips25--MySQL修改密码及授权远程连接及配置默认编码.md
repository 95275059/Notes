# LinuxTips25--MySQL修改密码及授权远程连接及配置默认编码

### 修改密码

+ 查看当前（临时）密码

  cat /var/log/mysqld.log | grep password

+ 登录MySQL

  mysql -u root -p

+ 修改密码

  + 修改密码策略

    set global validate_password.policy=0    #密码强度设置为最低等级

    set global validate_password.length=6  #密码允许的最小长度为6

    flush privileges                                           #更新授权表

    ---

    MySQL密码策略相关参数

    | 参数                                 | 含义                                    |
    | ------------------------------------ | --------------------------------------- |
    | validate_password.length             | 密码最小长度                            |
    | validate_password.dictionary_file    | 指定密码验证的文件路径                  |
    | validate_password.mixed_case_count   | 整个密码中至少要包含大/小写字母的总个数 |
    | validate_password.number_count       | 整个密码中至少要包含阿拉伯数字的个数    |
    | validate_password.policy             | 指定密码的强度验证等级，默认为 MEDIUM   |
    | validate_password_special_char_count | 整个密码中至少要包含特殊字符的个数      |

    ---

    validate_password.policy的取值：

    | 取值     | 含义                                       |
    | -------- | ------------------------------------------ |
    | 0/LOW    | 只验证长度                                 |
    | 1/MEDIUM | 验证长度、数字、大小写、特殊字符           |
    | 2/STRONG | 验证长度、数字、大小写、特殊字符、字典文件 |

  + 修改密码

    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '123456';

### 设置允许远程登录及开启防火墙

MySQL默认不允许远程登录，需要开启远程访问权限

允许远程登录

+ 法一：

  + 查看user表

    select user,authentication_string,host from user;

 可以看到，host默认都是localhost

  + update user set host='%' where user='root';
    
   + flush privileges;
   
   + 法二：
   
     grant all privileges on \*.* to 'root'@'%' with grant option;

   开启防火墙

   + firewall-cmd --zone=public --add-port=3306/tcp --permanent
   + firewall-cmd --reload

### 配置默认编码为UTF-8

+ 修改/etc/my.cnf配置文件

  在[mysqld]下添加编码配置

  character_set_server=utf8

  init_connect='SET NAMES utf8'

+ 重启mysql服务

  systemctl restart mysqld