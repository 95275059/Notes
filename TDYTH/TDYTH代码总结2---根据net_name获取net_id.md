# TDYTH代码总结2---根据net_name获取net_id

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
          net_id = ''
      cursor.close()
      db.close()
      return net_id
  
  if __name__=='__main__':
      net_id = get_net_id('net_cxy_test')
      print net_id
      print list(net_id)
      print list(net_id)[0]
  ```

+ 输出

  ```bash
  [root@controller test]# python get_net_id.py 
  (u'ed2029be-1b33-41ae-8651-31416353e85d',)
  [u'ed2029be-1b33-41ae-8651-31416353e85d']
  ed2029be-1b33-41ae-8651-31416353e85d
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
  ```

  



