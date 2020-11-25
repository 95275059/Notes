# LinuxTips59--ssh连接报错

### **IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!**

+ 报错信息

  ```bash
  root@controller:/home# scp -r cxy_tdyt/ root@192.168.1.111:/211cxy_tdyt/
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  @    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
  Someone could be eavesdropping on you right now (man-in-the-middle attack)!
  It is also possible that a host key has just been changed.
  The fingerprint for the ECDSA key sent by the remote host is
  SHA256:vKMCqhFco0dx6R082cFcw5JhlHvM+/U+EDIn0jxli+Y.
  Please contact your system administrator.
  Add correct host key in /root/.ssh/known_hosts to get rid of this message.
  Offending ECDSA key in /root/.ssh/known_hosts:28
    remove with:
    ssh-keygen -f "/root/.ssh/known_hosts" -R 192.168.1.111
  ECDSA host key for 192.168.1.111 has changed and you have requested strict checking.
  Host key verification failed.
  lost connection
  ```

+ 原因

  ssh会把每个你访问过计算机的公钥(public key)都记录在本地~/.ssh/known_hosts

  当下次访问相同计算机时，OpenSSH会核对公钥。如果公钥不同，OpenSSH会发出警告， 避免你受到DNS Hijack之类的攻击。

+ 解决方案

  + 方案一：手动删除修改known_hsots里面的内容；【建议这个】

    ```bash
    rm -rf ~/.ssh/known_hosts
    ```

  + 方案二：SSH登陆时忽略known_hsots的访问，但是安全性低

    修改配置文件“~/.ssh/config”，加上这两行，重启服务器

    ```bash
    StrictHostKeyChecking no
    UserKnownHostsFile /dev/null
    ```

    