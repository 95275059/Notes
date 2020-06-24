# TDYTH代码总结7--获取某条链路的源（目的）实例的device tap

+ 测试代码

  + 注：相关实例的mac地址已经预存在数据库SGIN里的表objects中了
  
  ```python
  import MySQLdb
  import os
  import libvirt
  import sys
  
  def get_dst_nameAndmac(link_src_name, link_dst_name):
      '''
      get name and mac of link_dst instance
      :param link_src_name:
      :param link_dst_name:
      :return: instance_name, mac or None, None
      '''
      db = MySQLdb.connect(host = '192.168.1.11',
                           user = 'root',
                           passwd = '123456',
                           db = 'SGIN',
                           charset = 'utf8')
      sql1 = "select router_network_name from objects where router_name=\'%s\'"%(str(link_src_name))
      sql2 = "select router_network_name,instance_name,router_mac_list from objects where router_name=\'%s\'"%(str(link_dst_name))
      cursor = db.cursor()
    try:
          cursor.execute(sql1)
          net_list1 = str(cursor.fetchone()).split("'")[1]
          cursor.execute(sql2)
          res2 = str(cursor.fetchone())
          net_list2 = res2.split("'")[1]
          instance_name = res2.split("'")[3]
          router_mac_list = res2.split("'")[5]
          db.commit()
      except Exception, e:
          db.rollback()
          print e
      cursor.close()
      db.close()
  
      for i in range(0, net_list1.count(',')+1):
          for j in range(0,net_list2.count(',')+1):
              if str(net_list1.split(',')[i]) == str(net_list2.split(',')[j]):
                  return instance_name, router_mac_list.split(',')[j]
              else:
                  pass
      return None, None
  	
  def get_device_tap(instance_name, mac):
      '''
      Find name of device tap on OVS according to mac and instance_name
      :param instance_name:
      :param mac:
      :return: Name of device tap or None
      '''
      instance_xml = str(instance_name)+'.xml'
      list1 = os.listdir('/etc/libvirt/qemu')
      if instance_xml in list1:
          conn = libvirt.open(None)
          dom = conn.lookupByName(instance_name)
          xml = dom.XMLDesc()
          macIndex = xml.find(mac)
          device_tap_name = xml[xml.find('tap', macIndex):xml.find('tap', macIndex)+14]
          conn.close()
          return device_tap_name
      else:
          #raise Exception, ValueError
          return None
  
  if __name__ == '__main__':
      src_name = sys.argv[1]
      dst_name = sys.argv[2]
      instance_name, mac = get_dst_nameAndmac(dst_name, src_name)
      device_tap_name = get_device_tap(instance_name, mac)
      print '%s - %s link : %s device_tap_name = %s'%(str(src_name), str(dst_name), str(src_name), str(device_tap_name))
      instance_name, mac = get_dst_nameAndmac(src_name, dst_name)
      device_tap_name = get_device_tap(instance_name, mac)
      print '%s - %s link : %s device_tap_name = %s' % (str(src_name), str(dst_name), str(dst_name), str(device_tap_name))
  ```

+ 输出

  ```bash
  [root@compute16 compute_node]# python get_device_tap.py MILSTAR_geo_01 MILSTAR_geo_02
  MILSTAR_geo_01 - MILSTAR_geo_02 link : MILSTAR_geo_01 device_tap_name = tapdcfa6f5b-21
  MILSTAR_geo_01 - MILSTAR_geo_02 link : MILSTAR_geo_02 device_tap_name = tapdaa343ed-05
  ```

