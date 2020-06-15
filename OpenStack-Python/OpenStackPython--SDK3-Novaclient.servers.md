# OpenStackPython--SDK3-Novaclient.servers

1. 路径

   ```shell
   /usr/lib/python2.7/site-packages/novaclient/v2/servers.py
   ```

2. python调用

   参考网址：https://docs.openstack.org/python-novaclient/latest/reference/api/novaclient.v2.servers.html

   *class* novaclient.v2.servers.ServerManager(*api*)

   Bases: novaclient.base.BootingManagerWithFind

   + nova_client.servers.interface_attach(server, port_id, net_id, fixed_ip) 

     将一个网络接口绑定到一个实例上

     + server : 实例的server或者ID
     + port_id : 端口id
     + net_id : 实例所在网络
     + fixed_ip : ip地址

     **==这个SDK没有运行成功，提示参数报错，或者不能同时出现net_id和port_id啥的==**

     **替换实现方案**

     ```python
     通过直接执行命令 nova interface-attach 实现
     import os
     
     def get_instance(instance_name):
         ''' 获取云主机
         :param instance_name:云主机名称
         :return:云主机实例
         '''
         instance_list = nova_client.servers.list()  # 要获取nova客户端
         instance = ""
         for ins in instance_list:
             if ins.name == instance_name:
                 instance = ins
                 break
         return instance
     
     def interface_attach_by_name(instance_name,port_id):
         ''' 连接接口
         :param instance_name:云主机的名称
         :param net_name:网络名称
         :return:
         '''
         instance = get_instance(instance_name)
         instance_id = instance.id
         os.system('source /root/admin-openrc;nova interface-attach --port-id ' + port_id + ' ' + instance_id)
     ```

     **注意：接口绑定或者断开后，需要等待少量时间，instance.networks调用获取network和ip才是更新后的**

     ---

   + nova_client.servers.interface_detach(server, port_id)

     将端口从实例上分离

     + server : 实例的server或者ID
     + port_id : 端口id

     **注意：要注意端口绑定在实例上还是网络上**

     + 如果端口绑定在实例上（创建虚拟机时直接指定network和ip）

       detach后端口被删除

     + 如果端口绑定在网络上

       detach后端口仍然存在

     ---

   + nova_client.servers.add_fixed_ip(server, network_id)

     向一个实例添加一个ip(即，为实例添加端口，放入一个网络中)

     + server : 实例的server或者ID
     + network_id : ip所在的网络的ID

     ---

   + nova_client.servers.add_floating_ip(server, address, fixed_address=None)

     向实例添加一个浮动ip

     + server : 实例的server或者ID
     + address : 要添加的浮动ip(FloatIP)或者浮动地址字符串(stirng floating address)
     + fixed_address : The FixedIP the floatingIP should be associated witch(optional)

     ---

   + nova_client.servers.add_security_group(server, security_group)

     向实例添加一个安全组

     + server : 实例的server或者ID
     + security_group : 要添加的安全组的名称

     ---

   + nova_client.servers.backup(server, backup_name, backup_type, rotation)

     备份一个实例

     + server : 实例的server或者ID
     + backup_name : 备份镜像的名称
     + backup_type : 备份类型，like 'daily' or 'weekly'
     + rotation : 表示要保留多少备份的int类型参数

     ---

   + nova_client.servers.add_tag(server, tag)

     Add single tag to an instance

     ---

   + nova_client.servers.change_password(server, password)

     更新实例的密码

     + server : 实例的server或者ID

     ---

   + nova_client.servers.clear_password(server)

     删除一个实例的管理员密码

     + server : 实例的server或者ID

     ---

   + nova_client.servers.confirm_resize(server)

     Confirm that the resize worked, thus removing the original server.

     确认调整大小有效，从而删除原始服务器

     + server : The server to share onto.

     ---

   + nova_client.servers.create(***name***, ***image***, ***flavor***,*meta=None*,*files=None*,*reservation_id=False*,*min_count=None*,*max_count=None*,*security_groups=None*, *userdata=None*,*key_name=None*,***availability_zone=None***,*block_device_mapping=None*,*block_device_mapping_v2=None*, ***nics=None***, *scheduler_hints=None*, *config_drive=None*, *disk_config=None*, *admin_pass=None*, *access_ip_v4=None*, *access_ip_v6=None*, *trusted_image_certificates=None*, *host=None*, *hypervisor_hostname=None*,***kwargs*)

     + name : 实例名称

     + image

       ```python
       image = nova_client.glance.find_image(image_name)
       ```

     + flavor 

       ```python
       flavor = nova_client.flavors.find(flavor_name)
       ```

     + availability_zone : 可用域

       ```python
       for ava in nova.availability_zones.list():
           if ava.hosts is not None and ava.hosts.keys()[0] == availability_zone:
               az_zoneName = ava.zoneName
           elif ava.hosts is None:
               print('one of availability zones may be done.')
               continue
       ```

     + nics : 包函所在网络ID、IP和Port的列表

       列表元素为字典类型

       网络ID获取：nova_client.neutron.find_network(network_name).id

       字典中关于port的键的名字还不知道

       ```python
       nic = [{'net-id' : str(net_id) , 'v4-fixed-ip' : str(instance_ip)},{},...]
       ```

       ```python
       #计算服务为server自动分配一个网络
       nic = 'auto'
       ```

       ```python
       #计算服务不为server分配任何网络
       nic = 'none'
       ```

     **注：执行后，不会马上就创建好，要监控实例的状态，等到状态变为为‘ACTIVE’才算创建成功**

     + 获取实例状态

       ```python
       nova_client.servers.get(server).status
       ```

     + 创建后检测状态代码

       ```python
       status = 'BUILD'
       while status == 'BUILD':
           print (name + ' is building...')
           time.sleep(3)
           status = nova.servers.get(server).status
           if status == 'ACTIVE':
               print (name + ' has been created.')
           elif status == 'ERROR':
               print (name + ' build failed.')
               continue
       ```

     ---

   + nova_client.servers.create_image(server, image_name, metadata=None)

     快照服务器

     + server : The server(or its ID) to share onto.
     + image_name : 快照镜像的名称
     + metadata : metadata to give newly-created image entity

     ---

   + nova_client.servers.delete(server)

     删除实例(i.e. shut down and delete the image)

     + server : 实例的server或者ID

     ---

   + nova_client.servers.delete_all_tags(server)

     Remove all tags from an instance

     ---

   + nova_client.servers.delete_meta(server, keys)

     Delete metadata from a server

     + server : 实例的server或者ID
     + keys : A list of metadata keys to delete from the server

     ---

   + 

   

   

   

   

