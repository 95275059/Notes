# TDYTH代码总结1--根据IP获取mac地址

+ 测试代码

  ```python
  import MySQLdb
  
  def get_port_mac(ip):
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='neutron',
                           charset='utf8')
      sql = "select mac_address from ipallocations,ports where port_id=ports.id and ip_address=\'%s\'"%(str(ip))
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          mac=cursor.fetchone()
          db.commit()
      except Exception,e:
          db.rollback()
          print e
          mac = ''
      cursor.close()
      db.close()
      return mac
  
  if __name__=='__main__':
      port = get_port_mac('60.60.42.13')
      print list(port)
      print list(port)[0]
  ```

+ 输出

  ```bash
  [root@controller test]# python get_port_mac.py 
  fa:16:3e:a4:40:a1
  fa:16:3e:c1:18:30
  ```

+ 实用代码

  ```pythn
  import MySQLdb
  
  def get_port_mac(ip):
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='neutron',
                           charset='utf8')
      sql = "select mac_address from ipallocations,ports where port_id=ports.id and ip_address=\'%s\'"%(str(ip))
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          mac=cursor.fetchone()
          db.commit()
      except Exception,e:
          db.rollback()
          print e
          mac = ['']
      cursor.close()
      db.close()
      return list(mac)[0]
  ```

  

