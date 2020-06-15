# Python模块4--multiprocessing

1. 相关基础

   + Unix/Linux实现多进程

     + Unix/Linux操作系统提供了一个fork()系统调用。

     + 普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为**父进程**）复制了一份（称为**子进程**），然后，分别在父进程和子进程内返回。

     + 子进程永远返回0，而父进程返回子进程的ID。这样，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。

     + Python的os模块封装了常见的系统调用，其中就包括fork

     + python创建子进程实例

       ```python
       import os
       
       print('Process (%s) start...' % os.getpid())
       # Only works on Unix/Linux/Mac:
       pid = os.fork()
       if pid == 0:
           print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
       else:
           print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
       ```

       ```python
       output:
       Process (876) start...
       I (876) just created a child process (877).
       I am child process (877) and my parent is 876.
       ```

   + Windows的多进程

     由于Windows没有fork调用，而如果我们需要在Windows上用Python编写多进程的程序，就需要使用到multiprocessing模块

   ---

2. multiprocessing概述

   + multiprocessing模块是跨平台和版本的多进程模块
   + multiprocessing是一个用与 threading 模块相似API的支持产生进程的包。 
   + multiprocessing 包同时提供本地和远程并发，**使用子进程代替线程**，有效避免Global Interpreter Lock带来的影响。因此， multiprocessing模块允许程序员充分利用机器上的多个核心。
   + Unix 和 Windows 上都可以运行。
   + multiprocessing模块还引入了在 threading模块中没有类似物的API。例如Pool对象
   + **window下，想要使用进程模块，就必须把有关进程的代码写入if __name__ == '\__main__':语句的下面，才能正常使用windows下的进程模块。Unix/Linux下则不需要**

   ---

3. Process对象

   + 利用multiprocessing.Process对象来创建一个进程。该进程可以允许放在Python程序内部编写的函数中。

   + 该Process对象与Thread对象的用法相同，拥有is_alive()、join([timeout])、run()、start()、terminate()等方法。

   + 语法
   
     ```python
     p = Process([group [, target [, name [, args [, kwargs]]]]])
     ```
   
     + target : 传递一个函数的引用，可以认为这个子进程就是执行这个函数的代码，这里传的是函数的引用，后面不能有小括号
     + args : 给target指定的函数传递的参数，以**元组**的 方式传递，
       + p = Process(target=run_proc, args=('test',))
       + 注意只有一个参数时，不可省略最后的逗号
     + kwargs : 给garget指定的函数传递关键字参数，以**字典**的方式传递
     + name : 给进程设定一个名字，可以不设定
     + group : 指定进程组，大多数情况下用不到
   
   + Process常用方法
   
     + p.start() : 启动子进程实例（创建子进程）
     + p.is_alive() : 判断子进程是否还活着
     + p.join([timeout]) : 等待子进程p结束后或者等待多少秒后继续往下运行，通常用于进程间的同步
     + p.terminate() : 不管任务是否完成，立即终止子进程
   
   + Process的常用属性
   
     + name : 当前进程的别名，默认为Process-N,N为从1开始递增的证书
     + pid : 当前进程的pid(进程号)
       + 获取当前进程的id和当前进程的父进程的id
         + import os
         + os.getpid() : 获取当前进程的id
         + os.getppid() : 获取当前进程的父进程的id
   
   + 实例
   
     ```python
     from multiprocessing import Process
     import os
     
     # 子进程要执行的代码
     def run_proc(name):
         print('Run child process %s (%s)...' % (name, os.getpid()))
     
     if __name__=='__main__':
         print('Parent process %s.' % os.getpid())
         p = Process(target=run_proc, args=('test',))
         print('Child process will start.')
         p.start()
         p.join()
         print('Child process end.')
     ```
     
     ```python
     output:
     Parent process 10288.
     Child process will start.
     Run child process test (15592)...
     Child process end.
     ```
   
   ---

4. Pool对象

   + Pool类可以提供指定数量的进程供用户调用，当有新的请求提交到Pool中时，如果池还没有满，就会创建一个新的进程来执行请求。如果池满，请求就会告知先等待，直到池中有进程结束，才会创建新的进程来执行这些请求。 

   + 若需要启动大量的子进程，可以用进程池的方式批量创建子进程

   + Pool提供了一种方便的方法，可以跨多个输入值并行化函数的执行，跨进程分配输入数据（数据并行）。

   + Pool类表示一个**工作进程池**。它具有允许以几种不同方式将任务分配到工作进程的方法。

   + 语法

     ```python
     from multiprocessing.pool import Pool
     p = Pool(processes = 2)
     ```

     + processes : 设置进程数。这个参数可以不设置，如果不设置，函数会根据计算机的实际情况来决定要运行多少个进程
     + **Pool的默认大小是CPU的核数**

   + 方法

     + apply()（==不建议使用，并且python3以后不再出现==）

       ```python
       result = p.apply(func[,args=()[,kwds={}]])
       ```

       + 该函数用于传递不定参数，同python中的apply函数一致，主进程会被阻塞知道函数执行结束

     + apply_async

       ```python
       result = p.apply_async(func[,args=()[,kwds={}[,callback=None]]])
       ```

       + 与apply用法一直，但是它是非阻塞的，且支持结果返回后进行回调

     + map()

       ```python
       result = p.map(func,iterable[,chunksize=None])
       ```

       + 与内置的map函数用法行为基本一直，它会使进程阻塞直到结果返回
       + 虽然第二个参数时一个迭代器，但在实际使用中，必须在整个队列都就绪后， 程序才会运行子进程

     + map_async()

       ```python
       result = p.map(func,iterable[,chunksize=None[,callback=None]])
       ```

       + 与map用法一致，但是它是非阻塞的

     + close()

       ```python
       p.close()
       ```

       + 关闭进程池，使其不再接受新的任务
       + **调用close()之后就不能继续添加新的Process了**

     + terminal()

       ```python
       p.terminal()
       ```

       + 结束工作进程，不再处理未处理的任务

     + join()

       ```python
       p.join()
       ```

       + 主进程阻塞等待子进程的退出
       + **join方法要在close或terminal之后使用**

   + 实例

     ```python
     from multiprocessing import Pool
     import os, time, random
     
     def long_time_task(name):
         print('Run task %s (%s)...' % (name, os.getpid()))
         start = time.time()
         time.sleep(random.random() * 3)
         end = time.time()
         print('Task %s runs %0.2f seconds.' % (name, (end - start)))
     
     if __name__=='__main__':
         print('Parent process %s.' % os.getpid())
         p = Pool(4)
         for i in range(5):
             p.apply_async(long_time_task, args=(i,))
         print('Waiting for all subprocesses done...')
         p.close()
         p.join()
         print('All subprocesses done.')
     ```

     ```python
     output:
     #task0,1,2,3立刻执行，task4要等待前面某个task完成后才能执行，因为pool的大小是4
     Parent process 6312.
     Waiting for all subprocesses done...
     Run task 0 (17932)...
     Run task 1 (1888)...
     Run task 2 (17896)...
     Run task 3 (16132)...
     Task 2 runs 0.43 seconds.
     Run task 4 (17896)...
     Task 3 runs 1.73 seconds.
     Task 0 runs 1.78 seconds.
     Task 1 runs 2.14 seconds.
     Task 4 runs 2.30 seconds.
     All subprocesses done.
     ```

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

     

   

