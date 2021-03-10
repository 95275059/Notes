# Python模块13--subprocess

### 介绍

+ 运行python的时候，我们都是在创建并运行一个进程。
+ 像Linux进程那样，一个进程可以fork一个子进程，并让这个子进程exec另外一个程序。
+ 在Python中，我们通过标准库中的subprocess 模块启动一个新进程，并连接到它们的输入/输出/错误管道，从而获取返回值。
+ subprocess包中定义有数个创建子进程的函数，这些函数分别以不同的方式创建子进程，所以我们可以根据需要来从中选取一个使用。
+ 另外subprocess还提供了一些管理标准流(standard stream)和管道(pipe)的工具，从而在进程间使用文本通信。
+ **subprocess模块打算来替代几个过时的模块和函数，比如：os.system, os.spawn, os.popen**,

---

### 使用run方法(Python3)

+ 语法

  ```python
  subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
  ```

  - args：表示要执行的命令。

    必须是一个字符串，字符串参数列表。

  - stdin、stdout 和 stderr：子进程的标准输入、输出和错误。

    其值可以是 subprocess.PIPE、subprocess.DEVNULL、一个已经存在的文件描述符、已经打开的文件对象或者 None。

    subprocess.PIPE 表示为子进程创建新的管道。

    subprocess.DEVNULL 表示使用 os.devnull。

    默认使用的是 None，表示什么都不做。

    另外，stderr 可以合并到 stdout 里一起输出。

  - timeout：设置命令超时时间。

    如果命令执行时间超时，子进程将被杀死，并弹出 TimeoutExpired 异常。

  - check：如果该参数设置为 True，并且进程退出状态码不是 0，则弹 出 CalledProcessError 异常。

  - encoding: 如果指定了该参数，则 stdin、stdout 和 stderr 可以接收字符串数据，并以该编码方式编码。否则只接收 bytes 类型的数据。

  - shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。

  - 返回值

    run 方法调用方式返回 CompletedProcess 实例，和直接 Popen 差不多，实现是一样的，实际也是调用 Popen，与 Popen 构造函数大致相同，

    **returncode**: 执行完子进程状态，通常返回状态为0则表明它已经运行完毕，若值为负值 "-N",表明子进程被终。

+ 实例

  ```python
  #执行ls -l /dev/null 命令
  >>> subprocess.run(["ls", "-l", "/dev/null"])
  crw-rw-rw-  1 root  wheel    3,   2  5  4 13:34 /dev/null
  CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0)
  ```

  ```python
  import subprocess
  
  def runcmd(command):
      ret = subprocess.run(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8",timeout=1)
      if ret.returncode == 0:
          print("success:",ret)
      else:
          print("error:",ret)
  
  runcmd(["dir","/b"])#序列参数
  runcmd("exit 1")#字符串参数
  ```

  ```python
  success: CompletedProcess(args=['dir', '/b'], returncode=0, stdout='.idea\n.vs\nargs_Study.py\nargs_Study2.py\nclient.py\ncount_study.py\ndictionary_test.py\nencode_decode_study.py\nfind_study.py\nintersection_study.py\nIOselect_client.py\nIOselect_server.py\niscapitalize.py\nisupper.py\njoin_test.py\nkwargs_study.py\nlist_test.py\nlocals_test.py\nmain.py\nmaketrans.py\npool_study.py\nprint_format.py\nprocess_study.py\nreload_study.py\nremove_test.py\nres_test.py\nre_Study.py\nselect_client1.py\nselect_client2.py\nselect_client3.py\nselect_server.py\nserver.py\nset_study.py\nsplit_study.py\nstring_study.py\nstrip_test.py\nstr_to_list.py\ntest.py\ntime_test.py\ntranslate_study.py\nupper.py\nvenv\nzip_test.py\n__pycache__\n', stderr='')
  error: CompletedProcess(args='exit 1', returncode=1, stdout='', stderr='')
  ```

---

### 使用Popen()方法

Popen 是 subprocess的核心，子进程的创建和管理都靠它处理。

subprocess.Popen()是用来代替os.popen()的

+ 语法

  ```python
  class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, 
  preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, 
  startupinfo=None, creationflags=0,restore_signals=True, start_new_session=False, pass_fds=(),
  *, encoding=None, errors=None)
  ```

  - args：shell命令，可以是字符串或者序列类型（如：list，元组）
  - bufsize：缓冲区大小。当创建标准流的管道对象时使用，默认-1。
    0：不使用缓冲区
    1：表示行缓冲，仅当universal_newlines=True时可用，也就是文本模式
    正数：表示缓冲区大小
    负数：表示使用系统默认的缓冲区大小。
  - stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
  - preexec_fn：只在 Unix 平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
  - shell：如果该参数为 True，将通过操作系统的 shell 执行指定的命令。
  - cwd：用于设置子进程的当前目录。
  - env：用于指定子进程的环境变量。如果 env = None，子进程的环境变量将从父进程中继承。

+ Popen对象方法

  - poll(): 检查进程是否终止，如果终止返回 returncode，否则返回 None。

  - wait(timeout): 等待子进程终止。

  - communicate(input,timeout): 和子进程交互，发送和读取数据。

    向stdin发送数据，或从stdout和stderr中读取数据。

    可选参数input指定发送到子进程的参数

    Communicate()返回一个元组：(stdoutdata, stderrdata)。

    注意：如果希望通过进程的stdin向其发送数据，在创建Popen对象的时候，参数stdin必须被设置为PIPE。同样，如果希望从stdout和stderr获取数据，必须将stdout和stderr设置为PIPE

    `Popen.communicate() `和进程沟通:发送数据到标准输入.从标准输出和错误读取数据直到遇到结束符.等待进程结束.

    输入参数应该是一个字符串,以传递给子进程,如果没有数据的话应该是`None`.

    基本上,当你用` communicate()`函数的时候意味着你要执行命令了.

  - send_signal(singnal): 发送信号到子进程 。

  - terminate(): 停止子进程,也就是发送SIGTERM信号到子进程。

  - kill(): 杀死子进程。发送 SIGKILL 信号到子进程。

+ 实例1

  ```python
  [root@cxy-centos7-1 home]# python
  Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
  [GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux2
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import subprocess
  >>> p = subprocess.Popen('ls -l', shell=True)
  total 0
  drwxr-xr-x. 2 root root 6 Jan 15  2020 cxy
  >>> p.returncode
  >>> p.wait()
  0
  >>> p.returncode
  0
  ```

  ```python
  import time
  import subprocess
  
  def cmd(command):
      subp = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding="utf-8")
      subp.wait(2)
      if subp.poll() == 0:
          print(subp.communicate()[1])
      else:
          print("失败")
  
  
  
  cmd("java -version")
  cmd("exit 1")
  ```

  ```python
  openjdk version "11.0.3" 2019-04-16
  OpenJDK Runtime Environment (build 11.0.3+12-b304.10)
  OpenJDK 64-Bit Server VM (build 11.0.3+12-b304.10, mixed mode, sharing)
  
  失败
  ```

+ 实例2

  `subprocess.Popen`需要一个数组作为参数:

  ```python
  >>> p = subprocess.Popen(["echo", "hello world"], stdout = subprocess.PIPE)
  >>> print(p.communicate())
  ('hello world\n', None)
  >>> p = subprocess.Popen(["ls", "-l"], stdout = subprocess.PIPE)
  >>> print(p.communicate())
  ('total 0\ndrwxr-xr-x. 2 root root 6 Jan 15  2020 cxy\n', None)
  ```

  当然你可以使用 "shell=True",但并不推荐这样的方式.

+ 实例3：用subprocess写ping程序

  ```python
  # Import the module
  import subprocess
  
  # Ask the user for input
  host = raw_input("Enter a host to ping: ")    
  
  # Set up the echo command and direct the output to a pipe
  p1 = subprocess.Popen(['ping', '-c 2', host], stdout=subprocess.PIPE)
  
  # Run the command
  output = p1.communicate()[0]
  
  print output
  ```

  ```shell
  [root@cxy-centos7-1 home]# python test.py 
  Enter a host to ping: 192.168.200.4
  PING 192.168.200.4 (192.168.200.4) 56(84) bytes of data.
  64 bytes from 192.168.200.4: icmp_seq=1 ttl=64 time=0.387 ms
  64 bytes from 192.168.200.4: icmp_seq=2 ttl=64 time=0.398 ms
  
  --- 192.168.200.4 ping statistics ---
  2 packets transmitted, 2 received, 0% packet loss, time 1000ms
  rtt min/avg/max/mdev = 0.387/0.392/0.398/0.020 ms
  ```

  

