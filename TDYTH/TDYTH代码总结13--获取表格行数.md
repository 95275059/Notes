# TDYTH代码总结13--获取表格行数

+ 测试代码

  ```python
  import MySQLdb
  import sys
  def get_table_raws(table_name):
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='SGIN',
                           charset='utf8')
      sql = "SELECT COUNT(*) FROM %s"%(str(table_name))
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          res = cursor.fetchone()
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          res = ['0']
      cursor.close()
      db.close()
      return res
  
  if __name__ == '__main__':
      table_name = sys.argv[1]
      raws = get_table_raws(table_name)
      print raws
      raws = list(raws)[0]
      print raws
  ```

+ 输出

  ```bash
  [root@controller test]# python get_table_raws.py objects
  (34L,)
  34
  ```

  ```bash
  [root@controller test]# python get_table_raws.py obje
  (1146, "Table 'SGIN.obje' doesn't exist")
  ['0']
  0
  ```

+ 实用代码

  ```python
  import MySQLdb
  import sys
  def get_table_raws(table_name):
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='SGIN',
                           charset='utf8')
      sql = "SELECT COUNT(*) FROM %s"%(str(table_name))
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          res = cursor.fetchone()
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          res = '0'
      cursor.close()
      db.close()
      return list(res)[0]
  
  if __name__ == '__main__':
      table_name = sys.argv[1]
      print  get_table_raws(table_name)
  ```

  