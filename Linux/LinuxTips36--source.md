# LinuxTips36--source

+ 也称为“点命令”，也就是一个点符号（.），是bash的内部命令

+ ```shell
  source filename
  . filename
  ```

1. 功能

   + 使shell读入指定的shell程序文件并依次执行文件中的语句
   + source命令通常用于执行刚修改的初始化文件，使之立即生效，而不必注销并重新登陆

2. 使用

   如果常常要反复输入一长串命令，可以把这些命令做成一个文件，让它自动按顺序执行，会很方便。

3. source filename 与 sh filename 及./filename执行脚本的区别

   + .当shell脚本具有可执行权限时，用sh filename与./filename执行脚本是没有区别的。./filename是因为当前目录没有在PATH中，所有"."是用来表示当前目录的。
   + sh filename 重新建立一个子shell，在子shell中执行脚本里面的语句，该子shell继承父shell的环境变量，但子shell新建的、改变的变量不会被带回父shell，除非使用export。
   + source filename：这个命令其实只是简单地读取脚本里面的语句依次在当前shell里面执行，没有建立新的子shell。那么脚本里面所有新建、改变变量的语句都会保存在当前shell里面。
   + 举例
     + 新建一个test.sh脚本，内容为:A=1
     + 然后使其可执行chmod +x test.sh
     + 运行sh test.sh后，echo $A，显示为空，因为A=1并未传回给当前shell
     + 运行./test.sh后，也是一样的效果
     + 运行source test.sh 或者 . test.sh，然后echo $A，则会显示1，说明A=1的变量在当前shell中