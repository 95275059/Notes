# TDYTH代码总结4--判断表是否空

+ 测试代码

  ```python
  import MySQLdb
  
  def judge_table():
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='SGIN',
                           charset='utf8')
      sql = "select * from GWL_Switch_MD"
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          count = cursor.fetchone()
          if count !=None:
              flag = 1
          else:
              flag = 0
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          flag = -1
      cursor.close()
      db.close()
      return flag
  
  
  if __name__=='__main__':
      print judge_table()
  ```

  + 表空返回0，否则返回1；查找过程出错返回-1

+ 输出

  ```python
  [root@controller test]# python judge_table.py 
  1
  ```

+ 实用代码

  ```python
  import MySQLdb
  
  def judge_table():
      db = MySQLdb.connect(host='192.168.1.11',
                           user='root',
                           passwd='123456',
                           db='SGIN',
                           charset='utf8')
      sql = "select * from GWL_Switch_MD"
      cursor = db.cursor()
      try:
          cursor.execute(sql)
          count = cursor.fetchone()
          if count !=None:
              flag = 1
          else:
              flag = 0
          db.commit()
      except Exception, e:
          db.rollback()
          print e
          flag = -1
      cursor.close()
      db.close()
      return flag
  ```

  

