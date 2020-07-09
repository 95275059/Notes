# Python12--文件

1. 文件类型

   + 文本文件

     可以处理各种语言所需的字符，只包含基本文本字符，不包括诸如字体，字号，颜色等信息。

     可以在文本编辑器和浏览器中显示，即在任何情况下，文本文件都是可读的

   + 二进制文件

     每一种二进制文件都需要自己的处理程序才能打开并操作。

     如：Word文档，PDF，图像，可执行程序等

2. 文件的访问
   + 使用open()打开（建立）文件，返回一个file图像
   + 使用file对象的读/写方法对文件进行读/写操作
     + 读操作：将数据从外存传输到内存的过程
     + 写操作：将数据从内存传输到外存的过程
   + 使用file对象的close()方法关闭文件

3. 打开（建立）文件

   使用open()函数打开（建立）文件时，会建立文件和使用它的程序之间的连接，并返回代表连接的文件对象。

   文件对象也称为文件描述符或文件流。

   当建立了Python程序和文件之间的连接后，就创建了‘流数据’。通常程序使用**输入流**读出数据，使用**输出流**写入数据。

   ```python
   fileobj=open(filename[,mode[,buffering]])
   ```

   + filename:文件名，可以是绝对路径，也可以是相对路径

   + mode:指明文件类型和操作的字符串

     + 'r':读模式

       若文件不存在，发生FileNotFoundError异常；默认值

     + 'w':写模式

       若文件不存在，则创建文件再打开；若文件存在，则清空文件内容再打开

     + 'a':追加模式

       若文件不存在，则创建文件再打开；若文件存在，打开文件后将新内容追加至原内容之后

     + 'x':创建写模式

       如果文件不存在，则创建文件；若果文件存在，返回FileExitError异常

     + 't':文本文件模式

       默认值

     + 'b':二进制模式

       可添加到其他模式中使用

     + '+':读/写模式

       可添加到其他模式中使用

   + buffering:控制缓冲

   ```python
   print(fileobj)
   ```

   + 打印文件对象可以看到文件名，读/写模式和编码格式

4. 读文本文件
   + read()方法
     + 无参数read():一次性读取文件全部内容为一个字符串
     + 有参数read(a):设置最大读入字符数a来限制read()一次返回的大小
   + readline()方法
     + 一次获取文件的一行为一个字符串返回
   + readlines()方法
     + 返回一个字符串列表，每一项是文件中每一行的字符串

5. 写文本文件

   + 以w/a模式打开文件时，不能进行读操作，否则会报错

   + write()方法

     ```python
     filename.write(字符串)
     ```

     注：write()方法不能自动在字符串末尾添加换行符，需要自己添加’\n‘

   + writelines()方法

      向文件写入一个序列字符串列表

      ```python
     filename.writelines(list)
      ```

      注：list元素必须全部为字符串，不能为整数序列等

   + 例：自定义函数copy_file函数，实现文件内容的复制

     ```python
     def copy_file(oldfile,newfile):
         oldFile=open(oldfile,"r")
         newFile=open(newfile,"w")
         strr=oldFile.read()
         print("oldfile:")
         print(strr)
         newFile.write(strr)
         return
     
     copy_file("D:\\Python\\Hello.txt","D:\\Python\\Hello2.txt")          #传递文件路径
     ```

6. 文件内移动

   当使用open()函数打开文件时，该函数在内存中创建缓冲区，将磁盘上的文件内容复制到缓冲区。

   文件对象将缓冲区视为一个大的列表，列表中的每一个元素都有自己的索引，文件对象按字节对缓冲区索引计数。

   文件对象会对文件当前位置（当前读/写操作发生的位置）进行维护。

   + ```python
     filename.tell()
     ```

     可以计算文件当前位置和开始位置之间的字节偏移量。

   + filename.seek(offset[,whence]):设置新的文件当前位置，允许在文件中跳转，实现对文件的随机访问

   + 将文件当前指针由引用点(whence)移动指定的字节数(offset)到指定的位置

   + offset:字节数，表示偏移量

   + whence:引用点，有三个取值

   + 文件开始处为0，默认值；以文件的开始处作为基准位置，此时offset非负

   + 当前位置为1，以文件当前位置为基准位置，此时offset可以为负

   + 文件结尾处为2，以文件末尾作为基准位置

   + 注：当文件以文本文件方式打开时，只能默认从文件头计算偏移量。即：whence为1或者2时，offset只能取0。

   + ```python
     exampleFile=open("D:\\Python\\example.txt","w+")
     exampleFile.write("123456789")
     exampleFile.seek(3)
     exampleFile.write("ZUT")
     exampleFile.seek(0)
     s=exampleFile.read()
     exampleFile.close()
     print(s)
     #123ZUT789
     exlFile=open("D:\\Python\\example.txt","r+b")
     exlFile.seek(3)
     exlFile.seek(-1,1)
     s=exlFile.read(3)
     print(s)
     #b'3ZU'
     ```

7. 文件的关闭

   关闭文件是取消程序和文件之间连接的过程，内存缓冲区的所有内容将写入磁盘，因此必须在使用文件后关闭文件确保信息不会丢失

   + try/finally语句

     ```python
     helloFile=open("D:\\Python\\hello.txt","w")
     try:
         helloFile.write("Hello,Sunny Day!")
     finally:
         helloFile.close()
     ```

   + with语句

     with语句可以打开文件并赋值给对象，文件会在语句结束后自动关闭，即使是由于异常引起的结束也是如此

     ```python
      with open("D:\\Python\\hello.txt") as helloFile:
         s=helloFile.read()
     print(s)
     ```

8. 二进制文件读/写

 

 

 

   
