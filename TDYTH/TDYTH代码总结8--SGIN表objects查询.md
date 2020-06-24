# TDYTH代码总结8--SGIN表objects查询

+ 测试代码

  ```python
  import MySQLdb
  
  def test3():
      db = MySQLdb.connect(host='192.168.1.211',
                           user='root',
                           passwd='123456',
                           db='SGIN',
                           charset='utf8')
      sql = "select router_network_name,router_network_id,router_ip_list,router_mac_list from objects where router_name=\'%s\'" % (str('WGS_geo_01_01'))
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          res = cursor.fetchone()
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          res = ['']
      cursor.close()
      db.close()
      print res
      res = str(res)
      print 'str(res)=' + res
      router_network_name = res.split("'")[1]
      router_network_id = res.split("'")[3]
      router_ip_list = res.split("'")[5]
      router_mac_list = res.split("'")[7]
      print 'net_list = ' + router_network_name
      print 'router_network_id = ' + router_network_id
      print 'router_ip_list = ' + router_ip_list
      print 'router_mac_list=' + router_mac_list
  
      for i in range(0, res.count("'") + 1):
          print res.split("'")[i]
  
      net_name_list = []
      for i in range(0, router_network_name.count(',') + 1):
          print router_network_name.split(',')[i]
          net_name_list.append(router_network_name.split(',')[i])
      print 'net_name_list:'
      print net_name_list
  
      net_id_list = []
      for i in range(0, router_network_id.count(',') + 1):
          print router_network_id.split(',')[i]
          net_id_list.append(router_network_id.split(',')[i])
      print 'net_id_list:'
      print net_id_list
  
      ip_list = []
      for i in range(0, router_ip_list.count(',') + 1):
          print router_ip_list.split(',')[i]
          ip_list.append(router_ip_list.split(',')[i])
      print 'ip_list:'
      print ip_list
  
      mac_list = []
      for i in range(0, router_mac_list.count(',') + 1):
          print router_mac_list.split(',')[i]
          mac_list.append(router_mac_list.split(',')[i])
      print 'mac_list:'
      print mac_list
      
  if __name__ =='__main__':
      test3()
  ```

+ 输出

  ```
  (u'm_net1,m_net3,m_net11,m_net12,m_net23', u'8dc67f97-ed83-4677-bacf-3ed52b8c6f18,6ab8964c-f98f-4914-b66c-d436b4a4370a,83625e93-b390-4093-a7ed-7d337287dd92,5387bffd-97c8-4dd1-8fb2-9f05c3954ac6,ed143226-7898-46de-aef8-a9f18df71bd5', u'60.60.1.11,60.60.3.11,60.60.11.11,60.60.12.11,60.60.23.11', u'fa:16:3e:73:55:da,fa:16:3e:49:6c:61,fa:16:3e:9f:6f:1f,fa:16:3e:f9:da:f4,fa:16:3e:3e:6a:43')
  str(res)=(u'm_net1,m_net3,m_net11,m_net12,m_net23', u'8dc67f97-ed83-4677-bacf-3ed52b8c6f18,6ab8964c-f98f-4914-b66c-d436b4a4370a,83625e93-b390-4093-a7ed-7d337287dd92,5387bffd-97c8-4dd1-8fb2-9f05c3954ac6,ed143226-7898-46de-aef8-a9f18df71bd5', u'60.60.1.11,60.60.3.11,60.60.11.11,60.60.12.11,60.60.23.11', u'fa:16:3e:73:55:da,fa:16:3e:49:6c:61,fa:16:3e:9f:6f:1f,fa:16:3e:f9:da:f4,fa:16:3e:3e:6a:43')
  net_list = m_net1,m_net3,m_net11,m_net12,m_net23
  router_network_id = 8dc67f97-ed83-4677-bacf-3ed52b8c6f18,6ab8964c-f98f-4914-b66c-d436b4a4370a,83625e93-b390-4093-a7ed-7d337287dd92,5387bffd-97c8-4dd1-8fb2-9f05c3954ac6,ed143226-7898-46de-aef8-a9f18df71bd5
  router_ip_list = 60.60.1.11,60.60.3.11,60.60.11.11,60.60.12.11,60.60.23.11
  router_mac_list=fa:16:3e:73:55:da,fa:16:3e:49:6c:61,fa:16:3e:9f:6f:1f,fa:16:3e:f9:da:f4,fa:16:3e:3e:6a:43
  (u
  m_net1,m_net3,m_net11,m_net12,m_net23
  , u
  8dc67f97-ed83-4677-bacf-3ed52b8c6f18,6ab8964c-f98f-4914-b66c-d436b4a4370a,83625e93-b390-4093-a7ed-7d337287dd92,5387bffd-97c8-4dd1-8fb2-9f05c3954ac6,ed143226-7898-46de-aef8-a9f18df71bd5
  , u
  60.60.1.11,60.60.3.11,60.60.11.11,60.60.12.11,60.60.23.11
  , u
  fa:16:3e:73:55:da,fa:16:3e:49:6c:61,fa:16:3e:9f:6f:1f,fa:16:3e:f9:da:f4,fa:16:3e:3e:6a:43
  )
  m_net1
  m_net3
  m_net11
  m_net12
  m_net23
  net_name_list:
  ['m_net1', 'm_net3', 'm_net11', 'm_net12', 'm_net23']
  8dc67f97-ed83-4677-bacf-3ed52b8c6f18
  6ab8964c-f98f-4914-b66c-d436b4a4370a
  83625e93-b390-4093-a7ed-7d337287dd92
  5387bffd-97c8-4dd1-8fb2-9f05c3954ac6
  ed143226-7898-46de-aef8-a9f18df71bd5
  net_id_list:
  ['8dc67f97-ed83-4677-bacf-3ed52b8c6f18', '6ab8964c-f98f-4914-b66c-d436b4a4370a', '83625e93-b390-4093-a7ed-7d337287dd92', '5387bffd-97c8-4dd1-8fb2-9f05c3954ac6', 'ed143226-7898-46de-aef8-a9f18df71bd5']
  60.60.1.11
  60.60.3.11
  60.60.11.11
  60.60.12.11
  60.60.23.11
  ip_list:
  ['60.60.1.11', '60.60.3.11', '60.60.11.11', '60.60.12.11', '60.60.23.11']
  fa:16:3e:73:55:da
  fa:16:3e:49:6c:61
  fa:16:3e:9f:6f:1f
  fa:16:3e:f9:da:f4
  fa:16:3e:3e:6a:43
  mac_list:
  ['fa:16:3e:73:55:da', 'fa:16:3e:49:6c:61', 'fa:16:3e:9f:6f:1f', 'fa:16:3e:f9:da:f4', 'fa:16:3e:3e:6a:43']
  ```

  