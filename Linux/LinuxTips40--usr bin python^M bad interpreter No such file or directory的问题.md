# LinuxTips40--/usr/bin/python^M: bad interpreter: No such file or directory的问题

+ 原因

  ^M是Windows下的断元字符

  在多个环境上编写，可能会因为字符（win/unix换行符不一样）、缩进（两个编辑环境的缩进tab/space不一致）均易导致这种错误

+ 解决方法

  vim 打开文件，进入命令模式

  ```bash
  :set ff=unix
  ```

  或
  
  ```bash
  :set fileformat=unix
  ```
  
  

