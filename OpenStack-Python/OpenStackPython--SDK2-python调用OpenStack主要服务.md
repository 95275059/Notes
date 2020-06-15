# OpenStackPython--SDK2-python调用OpenStack主要服务

+ 创建keystone session

  ```python
  #方法一：实验室
  from keystoneauth1 import loading
  from keystoneauth1 import session
  
  loader = loading.get_plugin_loader('password')
  auth = loader.load_from_options(auth_url="http://controller:35357/v3", username="admin",
                                      password="123456", project_name="admin",
                                      user_domain_name="default",
                                      project_domain_name="default", )
  sess = session.Session(auth=auth)
  ```

  ```python
  #方法二：
  from keystoneauth1.identity import v3
  from keystoneauth1 import session
  
  def get_keystone_session():
      # auth_url为keystone的endpoint入口，新版本openstack中(Tenant租户改名为project）
      auth = v3.Password(auth_url="http://<ip>:5000/v3", username="",password="", project_name="",user_domain_id="", project_domain_id="")
      sess = session.Session(auth=auth)
      return sess
  ```

+ 获取keystone客户端

  ```python
  from keystoneclient.v3 import client as keyclient
  
  def get_keystone_client():
      sess = get_keystone_session()
      keystone = keyclient.Client(session=sess)
      return keystone
  ```

+ 获取nova客户端

  ```python
  from novaclient import client as noclient
  
  def get_nova_client():
      sess = get_keystone_session()
      nova = noclient.Client(2, session=sess)
      return nova
  ```

+ 获取neutron客户端

  ```python
  from neutronclient.v2_0 import client as ntclient
  
  def get_neutron_client():
      sess = get_keystone_session()
      neutron = ntclient.Client(session=sess)
      return neutron
  ```

+ 获取glance客户端

  ```python
  from glanceclient import glclient
  
  def get_glance_client():
      sess = get_keystone_session()
      glance = glclient('2', session=sess)
      return glance
  ```

+ 获取heat客户端

  heat客户端的获取比较复杂，只能通过keystone客户端返回的token的认证

  ```python
  from heatclient import client as hclient
  
  def get_heat_client():
      creds = {}
      creds['username'] = ''
      creds['password'] = ''
      creds['auth_url'] = 'http://<ip>:5000/v3'
      creds['project_name'] = ''
      ks_client = keyclient.Client(**creds)
      heat_endpoint = ks_client.service_catalog.url_for(service_type='orchestration', endpoint_type='publicURL')
      # 后来需求Heat服务单独改为HTTPS，可以在以下参数中加入 insecure=True
      heat = hclient.Client('1', heat_endpoint, token=ks_client.auth_token)
      return heat
  ```

  