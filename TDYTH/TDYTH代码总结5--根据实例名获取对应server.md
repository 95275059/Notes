# TDYTH代码总结5--根据实例名获取对应server

+ 测试代码

  ```python
  #coding:utf-8
  import sys
  sys.path.append('/home/cxy_tdyt/tdyt_openstack')
  import credentials
  print 'Initializing...'
  nova_client = credentials.get_nova_client(credentials.get_nova_creds())
  
  def get_instance(instance_name):
      ''' 获取云主机
      :param instance_name:云主机名称
      :return:云主机实例
      '''
      # 通过虚拟机名称获取云主机server(单个)
      instance_list = nova_client.servers.list()
      instance = ""
      for ins in instance_list:
          if ins.name == instance_name:
              instance = ins
              break
      return instance
  
  if __name__=='__main__':
      server = get_instance('test_cxy2')
      print 'server:'
      print server
      print 'server.id:'
      print server.id
      print 'server.name:'
      print server.name
      print 'server.status:'
      print server.status
      print 'server.networks:'
      print server.networks
      print 'server.networks.keys():'
      print server.networks.keys()
      print 'list(server.networks.keys()):'
      print list(server.networks.keys())
      print 'server.networks.values():'
      print server.networks.values()
      print 'list(server.networks.values()):'
      print list(server.networks.values())
  
      net_list = []
      ip_list = []
      for net,ip in server.networks.items():
          net_list.append(net)
          ip_list.append(ip[0])
      print 'net_list:'
      print net_list
      print 'ip_list:'
      print ip_list
  ```

+ 输出

  ```bash
  [root@controller test]# python get_instance.py 
  Initializing...
  server:
  <Server: test_cxy2>
  server.id:
  ceaeb58e-c67a-4595-b15f-c0835f800433
  server.name:
  test_cxy2
  server.status:
  ACTIVE
  server.networks:
  {u'net_cxy_test2': [u'223.223.222.4'], u'net_cxy_test': [u'223.223.223.13']}
  server.networks.keys():
  [u'net_cxy_test2', u'net_cxy_test']
  list(server.networks.keys()):
  [u'net_cxy_test2', u'net_cxy_test']
  server.networks.values():
  [[u'223.223.222.4'], [u'223.223.223.13']]
  list(server.networks.values()):
  [[u'223.223.222.4'], [u'223.223.223.13']]
  net_list:
  [u'net_cxy_test2', u'net_cxy_test']
  ip_list:
  [u'223.223.222.4', u'223.223.223.13']
  ```



