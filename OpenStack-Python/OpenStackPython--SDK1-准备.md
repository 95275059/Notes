# OpenStackPython--SDK1-准备

1. 安装OpenStack相关服务调用的python库

   ```linux
   pip install python-openstackclient
   ```

   ```linux
   pip install python-keystoneclient
   ```

   ```linux
   pip install python-heatclient
   ```

   ```linux
   pip install python-glanceclient
   ```

   ```linux
   pip install python-novaclient
   ```

   ```linux
   pip install pythuon-neutronclient
   ```

2. 若安装的OpenStack的所有入口IP都映射为controller，则需要在本机的/etc/hosts中也加入一条映射

   ```shell
   <ip> controller
   ```

   

