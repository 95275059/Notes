# TDYTH代码总结10--获取实例在计算节点下的instance_name

+ 测试代码

  ```python
  # -*- coding:utf-8 -*-
  import MySQLdb
  import sys
  
  def get_instance_name(host_name):
  	host_name = host_name.replace('_','-')
  	db = MySQLdb.connect(host = '192.168.1.11',
                               user = 'root',
                               passwd = '123456',
                               db = 'nova',
                               charset = 'utf8')
          sql = "SELECT id FROM `instances` WHERE hostname=\'%s\' AND vm_state=\'active\'" % (str(host_name))
          cursor = db.cursor()
          try:
              cursor.execute(sql)
              instance_id=cursor.fetchone()
              instance_id=str(instance_id[0])
              print 'instance_id:'
              print instance_id
              hex_id='%x' % (int(instance_id))
              print 'hex_id：'
              print hex_id
              instance_name='instance-'+str(hex_id).rjust(8,'0')
              print 'instance_name：'
              print instance_name
              db.commit()
          except Exception,e:
              db.rollback()
              print e
              instance_name=None
          cursor.close()
          db.close()
          return instance_name
  
  if __name__=='__main__':
      instance = sys.argv[1]
      get_instance_name(instance)
  ```

+ 输出

  ```python
  [root@controller test]# python get_instance_name.py WGS_geo_02_01
  instance_id:
  48625
  hex_id：
  bdf1
  instance_name：
  instance-0000bdf1
  ```

+ 实用代码

  ```python
  # -*- coding:utf-8 -*-
  import MySQLdb
  import sys
  
  def get_instance_name(host_name):
  	host_name = host_name.replace('_','-')
  	db = MySQLdb.connect(host = '192.168.1.11',
                               user = 'root',
                               passwd = '123456',
                               db = 'nova',
                               charset = 'utf8')
          sql = "SELECT id FROM `instances` WHERE hostname=\'%s\' AND vm_state=\'active\'" % (str(host_name))
          cursor = db.cursor()
          try:
              cursor.execute(sql)
              instance_id=cursor.fetchone()
              instance_id=str(instance_id[0])
              hex_id='%x' % (int(instance_id))
              instance_name='instance-'+str(hex_id).rjust(8,'0')
              db.commit()
          except Exception,e:
              db.rollback()
              print e
              instance_name=None
          cursor.close()
          db.close()
          return instance_name
  ```

  