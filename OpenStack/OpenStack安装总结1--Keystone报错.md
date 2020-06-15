# OpenStack安装总结1--Keystone报错

1. 创建服务实体和身份认证服务步骤出错

   ```shell
   # openstack service create --name keystone --description "OpenStack Identity" identity 
   An unexpected error prevented the server from fulfilling your request. (HTTP 500) (Request-ID: req-d1a3d033-ff54-433d-8f73-9f664b0bc8ce)
   ```

   查看日志 tail -f /var/log/keystone/keystone.log

   ```shell
   [root@controller ~]# tail -f /var/log/keystone/keystone.log 
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi     self._start()
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi   File "/usr/lib/python2.7/site-packages/oslo_db/sqlalchemy/enginefacade.py", line 338, in _start
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi     engine_args, maker_args)
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi   File "/usr/lib/python2.7/site-packages/oslo_db/sqlalchemy/enginefacade.py", line 362, in _setup_for_connection
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi     sql_connection=sql_connection, **engine_kwargs)
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi   File "/usr/lib/python2.7/site-packages/oslo_db/sqlalchemy/engines.py", line 152, in create_engine
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi     test_conn = _test_connection(engine, max_retries, retry_interval)
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi   File "/usr/lib/python2.7/site-packages/oslo_db/sqlalchemy/engines.py", line 334, in _test_connection
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi     six.reraise(type(de_ref), de_ref)
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi   File "<string>", line 2, in reraise
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi DBConnectionError: (pymysql.err.OperationalError) (2003, "Can't connect to MySQL server on 'controller' ([Errno 111] Connection refused)")
   2020-06-08 10:03:43.115 11199 ERROR keystone.common.wsgi
   ```

   **错误：DBConnectionError: (pymysql.err.OperationalError) (2003, "Can't connect to MySQL server on 'controller' ([Errno 111] Connection refused)")**

   **解决**：mariadb配置文件/etc/my.cnf.d/openstack.cnf中，bind-address值改错了，应该为控制节点的管理网络IP地址，以使得其他节点可以通过管理网络访问数据库

   ---

2. 创建服务实体和身份认证服务步骤出错

   ```shell
   # openstack service create --name keystone --description "OpenStack Identity" identity 
   An unexpected error prevented the server from fulfilling your request. (HTTP 500) (Request-ID: req-d1a3d033-ff54-433d-8f73-9f664b0bc8ce)
   ```

   查看日志 tail -f /var/log/keystone/keystone.log

   ```shell
   [root@controller ~]# tail -f /var/log/keystone/keystone.log 
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi   File "/usr/lib/python2.7/site-packages/pymysql/connections.py", line 906, in _read_packet
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi     packet.check_error()
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi   File "/usr/lib/python2.7/site-packages/pymysql/connections.py", line 367, in check_error
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi     err.raise_mysql_exception(self._data)
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi   File "/usr/lib/python2.7/site-packages/pymysql/err.py", line 120, in raise_mysql_exception
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi     _check_mysql_exception(errinfo)
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi   File "/usr/lib/python2.7/site-packages/pymysql/err.py", line 112, in _check_mysql_exception
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi     raise errorclass(errno, errorvalue)
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi ProgrammingError: (pymysql.err.ProgrammingError) (1146, u"Table 'keystone.service' doesn't exist") [SQL: u'INSERT INTO service (id, type, enabled, extra) VALUES (%s, %s, %s, %s)'] [parameters: ('481ac2a624584ea2ae972314c8ff10a6', u'identity', 1, '{"description": "OpenStack Identity", "name": "keystone"}')]
   2020-06-08 10:11:08.364 11200 ERROR keystone.common.wsgi
   ```

   **错误：ProgrammingError: (pymysql.err.ProgrammingError) (1146, u"Table 'keystone.service' doesn't exist") [SQL: u'INSERT INTO service (id, type, enabled, extra) VALUES (%s, %s, %s, %s)'] [parameters: ('481ac2a624584ea2ae972314c8ff10a6', u'identity', 1, '{"description": "OpenStack Identity", "name": "keystone"}')]**

   **原因：**创建域失败，keystone日志报错无数据表。

   **解决：**重新初始化数据库。su -s /bin/sh -c "keystone-manage db_sync" keystone