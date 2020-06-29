# TDYTH代码总结11--根据port_id获取端口状态status

+ 实用代码

  ```python
  #!/usr/bin/python
  #coding:utf-8
  import sys
  import MySQLdb
  
  def get_port_status(port_id):
      '''
      Check if the port exits
      :param port_id:
      :return: return 1 if exists, otherwise 0
      '''
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='neutron',
                           charset='utf8')
      sql = "select status from ports where id=\'%s\'"%str(port_id)
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
      return res
  
  if __name__ =='__main__':
      port_id = sys.argv[1]
      print 'port status:'
      port_status = get_port_status(port_id)
      print port_status
      print list(port_status)
      print list(port_status)[0]
  ```

+ 输出

  ```python
  [root@controller test]# python get_port_status.py d5258faf-5fa7-4347-a338-b8e7579e15b5
  port status:
  (u'ACTIVE',)
  [u'ACTIVE']
  ACTIVE
  ```

+ 实用代码

  ```python
  #!/usr/bin/python
  #coding:utf-8
  import sys
  import MySQLdb
  
  def get_port_status(port_id):
      '''
      Check if the port exits
      :param port_id:
      :return: return 1 if exists, otherwise 0
      '''
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='neutron',
                           charset='utf8')
      sql = "select status from ports where id=\'%s\'"%str(port_id)
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
      return list(res)[0]
  
  if __name__ =='__main__':
      port_id = sys.argv[1]
      print 'port status:'
      print get_port_status(port_id)
  ```

  