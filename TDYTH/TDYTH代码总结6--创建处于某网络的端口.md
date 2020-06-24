# TDYTH代码总结6--创建处于某网络的端口

+ 测试代码

  ```python
  import sys
  import MySQLdb
  sys.path.append('/home/cxy_tdyt/tdyt_openstack')
  import credentials
  print 'Initializing...'
  neutron_client = credentials.get_neutron_client(credentials.get_nova_creds())
  
  def get_net_id(net):
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='neutron',
                           charset='utf8')
      sql = "select id from networks where name=\'%s\'"%(str(net))
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          net_id = cursor.fetchone()
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          net_id = ['']
      cursor.close()
      db.close()
      return list(net_id)[0]
  
  def set_body_value(net_id):
      body_value = {
          "port": {
              "admin_state_up": True,
              "network_id": net_id
          }
      }
      return body_value
  
  def create_port(net_name):
      net_id = get_net_id(net_name)
      body_value = set_body_value(net_id)
      res = neutron_client.create_port(body=body_value)
      return res
  
  if __name__=='__main__':
      res = create_port('net_cxy_test2')
      print 'res:'
      print res
      res_port = res['port']
      print 'res_port:'
      print res_port
      print 'port_id:'
      port_id_new = res_port['id']
      print port_id_new
      print 'mac_address:'
      mac_address = res_port['mac_address']
      print mac_address
      print 'network_id:'
      network_id = res_port['network_id']
      print network_id
      print 'fixed_ips:'
      fixed_ips = res_port['fixed_ips'][0]
      print fixed_ips
      print 'subnet_id:'
      subnet_id = fixed_ips['subnet_id']
      print subnet_id
      print 'ip_address:'
      ip_address = fixed_ips['ip_address']
      print ip_address
  ```

+ 输出

  ```bash
  [root@controller test]# python port_create.py 
  Initializing...
  res:
  {u'port': {u'allowed_address_pairs': [], u'extra_dhcp_opts': [], u'updated_at': u'2020-06-23T12:08:06', u'device_owner': u'', u'binding:profile': {}, u'port_security_enabled': True, u'fixed_ips': [{u'subnet_id': u'19290ef3-3757-40aa-9ce3-b825ab35b134', u'ip_address': u'223.223.222.20'}], u'id': u'0f4e5275-3a60-49f0-a4b0-c978b4035128', u'security_groups': [u'82accba2-c713-4b41-84d7-bd1832c632c2'], u'binding:vif_details': {}, u'binding:vif_type': u'unbound', u'mac_address': u'fa:16:3e:66:76:18', u'status': u'DOWN', u'binding:host_id': u'', u'description': u'', u'device_id': u'', u'name': u'', u'admin_state_up': True, u'network_id': u'ce59735e-69a2-4568-a9d0-491cb1bc976d', u'dns_name': None, u'created_at': u'2020-06-23T12:08:06', u'binding:vnic_type': u'normal', u'tenant_id': u'f2e64bde168f41358b47ca3f1e1caea1'}}
  res_port:
  {u'allowed_address_pairs': [], u'extra_dhcp_opts': [], u'updated_at': u'2020-06-23T12:08:06', u'device_owner': u'', u'binding:profile': {}, u'port_security_enabled': True, u'fixed_ips': [{u'subnet_id': u'19290ef3-3757-40aa-9ce3-b825ab35b134', u'ip_address': u'223.223.222.20'}], u'id': u'0f4e5275-3a60-49f0-a4b0-c978b4035128', u'security_groups': [u'82accba2-c713-4b41-84d7-bd1832c632c2'], u'binding:vif_details': {}, u'binding:vif_type': u'unbound', u'mac_address': u'fa:16:3e:66:76:18', u'status': u'DOWN', u'binding:host_id': u'', u'description': u'', u'device_id': u'', u'name': u'', u'admin_state_up': True, u'network_id': u'ce59735e-69a2-4568-a9d0-491cb1bc976d', u'dns_name': None, u'created_at': u'2020-06-23T12:08:06', u'binding:vnic_type': u'normal', u'tenant_id': u'f2e64bde168f41358b47ca3f1e1caea1'}
  port_id:
  0f4e5275-3a60-49f0-a4b0-c978b4035128
  mac_address:
  fa:16:3e:66:76:18
  network_id:
  ce59735e-69a2-4568-a9d0-491cb1bc976d
  fixed_ips:
  {u'subnet_id': u'19290ef3-3757-40aa-9ce3-b825ab35b134', u'ip_address': u'223.223.222.20'}
  subnet_id:
  19290ef3-3757-40aa-9ce3-b825ab35b134
  ip_address:
  223.223.222.20
  ```

  

