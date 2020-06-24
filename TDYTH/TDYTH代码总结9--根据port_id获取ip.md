# TDYTH代码总结9--根据port_id获取ip

+ 测试代码

  ```python
  import MySQLdb
  
  def get_ip_by_port(port_id):
      '''
      get the IP bound to the port
      :param port_id:
      :return:
      '''
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='neutron',
                           charset='utf8')
      sql = "select ip_address from ipallocations where port_id=\'%s\'"%str(port_id)
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          ip = cursor.fetchone()
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          ip = ''
      cursor.close()
      db.close()
      return ip
  
  if __name__=="__main__":
      ip = get_ip_by_port('6d8470a1-58c9-4759-b213-84de4e646050')
      print ip
      print list(ip)
      print list(ip)[0]
  ```

+ 输出

  ```bash
  [root@controller test]# python get_ip_by_port.py 
  (u'223.223.223.3',)
  [u'223.223.223.3']
  223.223.223.3
  ```

+ 实用代码

  ```python
  import MySQLdb
  
  def get_ip_by_port(port_id):
      '''
      get the IP bound to the port
      :param port_id:
      :return:
      '''
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='neutron',
                           charset='utf8')
      sql = "select ip_address from ipallocations where port_id=\'%s\'"%str(port_id)
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          ip = cursor.fetchone()
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          ip = ['']
      cursor.close()
      db.close()
      return list(ip)[0]
  ```

  

