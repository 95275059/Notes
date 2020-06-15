# LinuxTips12--curl命令

1. 简介

   curl是一个利用URL规则在命令行下工作的文件传输工具，支持文件的上传和下载。

   语法：curl [option] [url]

2. 常见参数

   | 选项                            | 说明                                         |
   | ------------------------------- | -------------------------------------------- |
   | -A(--user-agent <string>)       | 设置用户代理发送给服务器                     |
   | -b(--cookie <name=string/file>) | cookie字符串或文件读取位置                   |
   | -c(--cookie-jar <file>)         | 操作结束后把cookie写入到这个文件中           |
   | -C(--continue-at <offset>)      | 断点续传                                     |
   | -D(--dump-header <file>)        | 把header信息写入到该文件中                   |
   | -e(--referer)                   | 来源网址                                     |
   | -f(--fail)                      | 连接失败时不显示http错误                     |
   | -o(--output <file>)             | 把输出写到该文件中                           |
   | -O(--remote-name)               | 把输出写到该文件中，保留使用远程文件的文件名 |
   | -r(--range <range>)             | 检索来自HTTP/1.1或FTP服务器字节范围          |
   | -s(--silent)                    | 静音模式，不输出任何东西                     |
   | -T(--upload-file <file>)        | 上传文件                                     |
   | -u(--user <user[:password]>)    | 设置服务器的用户和密码                       |
   | -w(--write-out [format])        | 设置输出格式                                 |
   | -x(--proxy <host[:port]>)       | 在指定的端口上使用HTTP代理                   |
   | -#(--progress-bar)              | 进度条显示当前的传送状态                     |

3. 基本用法

   + 抓取网页

     curl http://www.baidu.com

   + 保存网页

     + curl -o baidu.html www.baidu.com 

     + curl http://www.baidu.com > baidu.html

   + 保存网页中的文件
   
     curl -O http://www.baidu.com/hello.sh
   
   + cookie
   
     + 保存http的response里面的cookie信息
   
       curl -c cookie_baidu.txt www.baidu.com
   
     + 保存http的response里面的header信息
   
       curl -D cookie_header_baidu.txt www.baidu.com
   
     + 发送cookie
   
       curl -b cookie_baidu.txt www.baidu.com    #从文件中读取cookie
   
       curl -b "key1=val1;key2=val2;" www.baidu.com   #发送cookie文本

　