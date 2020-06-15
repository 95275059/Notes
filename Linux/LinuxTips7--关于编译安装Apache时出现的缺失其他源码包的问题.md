# LinuxTips7--关于编译安装Apache时出现的缺失其他源码包的问题

错误：configure:error:APR not found.Please read the documentation

解决方法：需要下载apr apr-util pcre三个源码包并完成编译安装

1. 下载软件包

   apr：http://archive.apache.org/dist/apr

   apr-util：http://archive.apache.org/dist/apr

   pcre：http://jaist.dl.sourceforge.net/project/pcre/pcre

   ---

2. 安装所需的几个rpm包

   yum install -y expat-devel

   yum install -y gcc

   yum install -y gcc-c++

   yum install -y libxml2-devel

   **==开始前必须先安装这几个，否则会出现下面标黄的错误，尤其最后一个错误巨坑==**

3. 解决apr not found 问题

   + 进入目录/usr/local/src  并将apr源码包放入

   + tar -xzvf apr-1.7.0.tar.gz
   + cd apr-1.4.5
   + ./configure --prefix=/usr/local/apr1
   + make
   + make install

3. 解决apr-util not found问题

   + 进入目录/usr/local/src  并将apr-util源码包放入

   + tar -xzvf apr-util-1.6.1.tar.gz

   + cd apr-util-1.6.1

   + ./configure --prefix=usr/local/apr-util1 --with-apr=usr/local/apr1

   + make

     ==**致命错误**==：这里在编译后出现一个致命错误：expat.h：没有那个文件或目录

     **原因：**缺少expat库

     **解决方法：**yum install -y expat-devel   ;   然后make clean   ;   最后再次编译

4. 解决pcre问题

   + 进入目录/usr/local/src   并将pcre源码包放入

   + tar -xzvf pcre-8.43.tar.gz

   + cd pcre-8.43

   + ./configure --prefix=/usr/local/pcre8

     ==**错误：**==Invalid C++ compiler or C++ compiler flags

     **原因：**没有安装gcc-c++或者gcc-c++安装失败导致，需要重新安装gcc-c++

     **解决方法：**yum install -y gcc-c++

5. 编译Apache

   + 进入目录/usr/local/src   并将httpd源码包放入

   + tar -xzvf httpd-2.4.41.tar.gz

   + cd httpd-2.4.41

   + ./configure --prefix=/usr/local/apache2 --with-apr=/usr/local/apr1 --with-apr-util=/usr/local/apr-util1 --with-pcre=/usr/local/pcre8

   + make

     ==**错误：**==

     ```
     collect2: error: ld returned 1 exit status
     make[2]: *** [htpasswd] 错误 1
     make[2]: 离开目录“/usr/local/src/httpd-2.4.41/support”
     make[1]: *** [all-recursive] 错误 1
     make[1]: 离开目录“/usr/local/src/httpd-2.4.41/support”
     make: *** [all-recursive] 错误 1
     ```

     **原因：**缺少xml相关的库，需要安装libxml2-devel包。但直接安装不能解决问题，因为httpd调用的apr-util已经安装好了，但是apr-utilb并没有libxml2-devel包支持

     **解决方法：**

     + 安装libxmol2-devel包

       yum install -y libxml2-devel

     + 删除apr-util安装目录，并重新编译安装

       + rm -rf /usr/local/apr-util

       + cd /usr/local/src/apr-util-1.6.1

       + make clean     **#必须清楚之前配置时的缓存**

       + ./configure --prefix=/usr/local/apr-util1 --with-apr=/usr/local/apr1

       + make

       + make install

     + 重新编译安装httpd

       + cd /usr/local/src/httpd-2.4.41

       + make clean     **#必须清楚之前配置时的缓存**

       + ./configure --prefix=/usr/local/apache2 --with-apr=/usr/local/apr1 --with-apr-util=/usr/local/apr-util1 --with-pcre=/usr/local/pcre8
       + make
       + make install