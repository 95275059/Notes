# TDYTH代码总结3--根据net_name及IP获取port_id

+ 测试代码

  ```python
  import MySQLdb
  
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
  
  def get_port_id(ip,net_name):
      net_id = get_net_id(net_name)
      print 'net_id:'+net_id
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='neutron',
                           charset='utf8')
      sql = "select port_id from ipallocations where ip_address=\'%s\' and network_id =\'%s\'" % (str(ip),str(net_id))
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          port_id = cursor.fetchone()
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          port_id = ''
      cursor.close()
      db.close()
      return port_id
  
  if __name__=='__main__':
      port_id = get_port_id('223.223.223.3','net_cxy_test')
      print port_id
      print list(port_id)
      print list(port_id)[0]
  ```

+ 输出

  ```bash
  [root@controller test]# python get_port_id.py 
  net_id:ed2029be-1b33-41ae-8651-31416353e85d
  (u'6d8470a1-58c9-4759-b213-84de4e646050',)
  [u'6d8470a1-58c9-4759-b213-84de4e646050']
  6d8470a1-58c9-4759-b213-84de4e646050
  ```

+ 实用代码

  ```python
  import MySQLdb
  
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
  
  def get_port_id(ip,net_name):
      net_id = get_net_id(net_name)
      db = MySQLdb.connect(host='192.168.1.11',
                         user='root',
                           passwd='123456',
                           db='neutron',
                           charset='utf8')
      sql = "select port_id from ipallocations where ip_address=\'%s\' and network_id =\'%s\'" % (str(ip),str(net_id))
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          port_id = cursor.fetchone()
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          port_id = ['']
      cursor.close()
      db.close()
      return list(port_id)[0]
  ```
  
  