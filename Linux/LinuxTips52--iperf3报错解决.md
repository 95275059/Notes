# LinuxTips52--iperf3报错解决

### 报错：iperf3: error while loading shared libraries: libiperf.so.0: cannot open shared object file: No such file or directory

+ 原因：这个问题容易发生在centos6 和Ubuntu较老版本上

+ 解决：在正常编译后运行

  ```bash
  ldconfig
  ```

  