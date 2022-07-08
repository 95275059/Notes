# Linux笔记11--文件搜索命令1-find

## 文件搜索命令 find

命令所在路径：/bin/find

执行权限：所有用户

语法：find [搜索范围] [匹配条件]

功能：文件搜索

## 实例

### 例1：根据文件名进行搜索 

+ find /etc ==-name== init 

+ 若不区分文件名大小写 

  find /etc ==-iname== init

+ 若查找文件名中带init的文件

  find /etc -name \*init

+ 若查找以init开头的文件

  find /etc -name init*

+ 若查找文件名以init开头后面还有三位字母的文件

  find /etc -name init???

注：和Windows 中根据文件名搜索不一样，Windows中会搜索所有带init的文件，而Linux中只会搜索文件名为Init的文件，相当于精准搜索。

### Error：路径必须在表达式之前(大多出现在用*的情况下)

+ 解决方法一：用双引号引号将要匹配的字段引起来

  find /etc -name "init*"

+ 解决方法二：使用转义符把*转义

  find /etc -name init\\*

---

### 例2：根据文件大小进行搜索

+ 查找/目录下文件大小大于100MB的文件

  find  ==-size== +204800 

  注：number单位是一个数据块，一个数据块大小为512字节(0.5KB)

  +number : 大于 ； -number : 小于 ；n : 等于

### 例3：根据所有者进行搜索 

find /home ==-user== cxy1

### 例4：根据所属组进行搜索 

find /home ==-group== cxy1

### 例5：根据访问时间进行搜素

+ 在/etc下查找5分钟内被修改过属性的文件和目录

  find /etc -cmin -5 

+ ==-amin== 访问时间 access
+ ==-cmin== 文件属性 change
+ ==-mmin== 文件内容 modify

注：避免在服务器访问高峰期进行find查找，搜索范围越小越好，搜索条件越精准越好

### 例6：搜索条件有多个

+ 选项==-a== : 两个条件同时满足

  在/etc下查找大于80MB小于100MB的文件：find /etc -size +163840 -a -size -204800

+ 选项==-o== : 两个条件满足任意一个即可

  在/etc下查找文件名为init或者以init开头后面有三个字母的文件：find /etc -name init -o -name init???

### 例7：对搜索结果进行操作

==-exec/-ok 命令 {} \;==

-ok:对每个查找结果会一个一个询问要不要查看 (在进行删除操作时比较常用)

+ 在/etc下查找inittab文件并显示其详细信息 

  /etc -name inittab -exec ls -l {} \;

  注：{}与\之间有一个空格；

### 例8：根据文件类型查找

f : 文件 ；d : 目录 ；l : 软链接文件

+ 在/etc 下查找以init开头的目录

  find /etc -name init* -a ==-type== f

### 例9：根据i节点查找

在tmp目录下通过i节点查找test文件并删除

==-inum==![](https://img-blog.csdnimg.cn/2019041916281816.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3poYWFuZHpoYQ==,size_16,color_FFFFFF,t_70) 注：有时通过文件名删除文件时会莫名其妙删除不了，可以通过i节点进行删除

通过i节点查找某文件的硬链接文件

 

 

   
