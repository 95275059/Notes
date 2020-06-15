# MATLABTips5--tcpip及文件读取相关命令和实例

1. tcpip

   + 创建tcpip对象

     前提是主机和从机要在同一网络下

   + 语法

     + t = tcpip(RemoteHost)

       + 创建与远程主机和默认远程端口为80的关联的TCPIP对象

       + ==当TCPIP对象被创建，它的Status属性值为closed==

       + ==当对象通过fopen函数连接到主机时，该Status属性被配置为open==

     + t = tcpip(RemoteHost,RemotePort)

       + 创建具有指定远程端口值的TCPIP对象

     + t = tcpip(__,Name,Value)

       + 使用指定的可选名称/值对，创建一个TCPIP对象
       + 如果指定了无效的属性名称或属性值，则不会创建该对象

2. fopen

   + 打开文件或获得有关打开文件的信息

   + 语法

     + **fileID = fopen(filename)**

       打开文件filename，以二进制读取形式进行访问，并返回等于或大于三的整数文件标识符

       + 文件标识符

         | 文件标识符 | 含义             |
         | ---------- | ---------------- |
         | 0          | 标准输入         |
         | 1          | 标准输出（屏幕） |
         | 2          | 标准错误         |

     + **fileID = fopen(filename,permission)**

       将打开由permission指定访问类型的文件

     + fileID = fopen(filename,permission,machinefmt,encodingIn)

       + 使用machinefmt参数另外指定在文件中读写字节或位时的顺序
       + 可选的encodingIn参数指定与文件相关联的字符编码方案

     + [fileID , errmsg] = fopen(__)

       如果fopen打开文件失败，则还将返还一条因系统而异的错误消息

       否则，errmsg是一个空字符向量

       可以将这个语法与前面的语法结合使用

     + fIDs = fopen('all')

       返回包含所有打开文件的文件标识符的行向量

       为标准输入，输出以及错误而保留的标识符不包括在内

       向量中元素的数量等于打开文件的数量

     + filename = fopen(fileID)

       返回上一次调用fopen在打开fileID指定的文件时所用的文件名

       输出文件名将解析到完整路径

       fopen函数不会从文件读取信息来确定输出值

     + [filename,permission,machinefmt,encodingOut] = fopen(fileID)

       返回上一次调用 `fopen` 在打开指定文件时所使用的权限、计算机格式以及编码

       如果是以二进制模式打开的文件，则 permission 会包含字母‘b’

       encodingOut输出是一个标准编码方案名称

       fopen不会从文件读取信息来确定这些输出值

       fileID会为所有输出参数返回空字符向量

   ---

3. fwrite

   + 将数据写入二进制文件

   + 语法

     + fwrite(fileID,A)

       将数组A中的元素按列顺序以8位无符号整数的形式写入一个二进制文件

       该二进制文件由文件标识符fileID指示

       使用fopen可以打开文件并获取fileID值

       读取文件后，调用fclose(fileID)来关闭文件

     + fwrite(fileID,A,precision)

       按照 `precision` 说明的形式和大小写入 `A` 中的值

     + fwrite(fileID,A,precision,skip)

       在写入每个值之前跳过 `skip` 指定的字节数或位数

       `skip` 参数为可选参数

     + fwrite(fileID,A,precision,skip,machinefmt)

       另外还指定将字节或位写入文件的顺序

     + count = fwrite(__)

       返回 `A` 中 `fwrite` 已成功写入到文件的元素数

       可以将此语法与前面语法中的任何输入参数结合使用

   ---

4. fread

   + 读取二进制文件中的数据

   + 语法

     + A = fread(fileID)

       将打开的二进制文件中的数据读取到列向量 `A` 中，并将文件指针定位在文件结尾标记处

       该二进制文件由文件标识符 `fileID` 指示

       使用 `fopen` 可打开文件并获取 `fileID` 值

       读取文件后，请调用 `fclose(fileID)` 来关闭文件

     + A = fread(fileID,sizeA)

       将文件数据读取到维度为 `sizeA` 的数组 `A` 中，并将文件指针定位到最后读取的值之后

       `fread` 按列顺序填充 `A`

       `sizeA` 参数为可选参数

     + A = fread(fileID,sizeA,precision)

       根据 `precision` 描述的格式和大小解释文件中的值

     + A = fread(fileID,sizeA,precision,skip)

       在读取文件中的每个值之后将跳过 `skip` 指定的字节或位数

        `skip` 参数是可选的

     + A = fread(fileID,sizeA,precision,skip,machinefmt)

       另外指定在文件中读取字节或位时的顺序

     + [A,count] = fread(__)

       还将返回 `fread` 读取到 `A` 中的字符数

       可以将此语法与前面语法中的任何输入参数结合使用

   ---

5. fclose

   + 关闭一个或所有打开的文件

   + 语法

     + fclose(flieID)

       关闭打开的文件

     + fclose('all')

       关闭所有打开的文件

     + status = flcose(__)

       当关闭操作成功时，返回status 0

       否则返回-1

       可以将此语法与前面语法中的任何输入参数结合使用

   ---

6. echotcpip

   + 启动或停止TCPIP回显服务器

   + 语法

     + echotcpip('state',port)

       启动端口号为TCPIP服务器的port

       state只能是on

       | 参数  | 说明             |
       | ----- | ---------------- |
       | state | 打开或关闭服务器 |
       | port  | 服务器的端口号   |

     + echotcpip('state')

       停止回显服务器

       state只能是off

   ---

7. 实例

   ```matlab
   %Start a TCP/IP echo server and create a TCPIP object.
   echotcpip('on',4012)
   t = tcpip('localhost',4012); %实际换成host的ip地址和端口
   
   %Connect the TCPIP object to the host.
   fopen(t)
   
   %Write to the host and read from the host.
   fwrite(t,65:74) %注意，这里是ASCII码
   A = fread(t, 10);
   
   % Disconnect the TCPIP object from the host and stop the echo server.
   fclose(t)
   echotcpip('off')
   ```

   ```matlab
   	st = whos('s');
       %创建一个tcpip对象t
       t = tcpip('192.168.1.213',50000,'Timeout',60,'InputBufferSize',st.bytes,'OutputBufferSize',st.bytes);
       %将tcpip对象t连接到远程主机（‘192.168.1.213’）
       fopen(t);
       %写入主机
       fwrite(t,s)
       %断开tcpip对象t和远程主机的连接
       fclose(t);
   ```

   

   