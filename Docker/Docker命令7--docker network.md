# Docker命令7--docker network

### docker network 

```bash
root@ubuntu16:~# docker network --help

Usage:	docker network COMMAND

Manage networks

Commands:
  connect     Connect a container to a network
  create      Create a network
  disconnect  Disconnect a container from a network
  inspect     Display detailed information on one or more networks
  ls          List networks
  prune       Remove all unused networks
  rm          Remove one or more networks

Run 'docker network COMMAND --help' for more information on a command.
```

---

### docker network ls

+ 列出网络

+ 语法

  ```
  docker network ls [OPTIONS]
  ```

  + [OPTIONS]
  
    | 选项                | 说明                                         |
    | ------------------- | -------------------------------------------- |
    | -f, --filter filter | Provide filter values (e.g. 'driver=bridge') |
    | --format string     | Pretty-print networks using a Go template    |
    | --no-trunc          | Do not truncate the output                   |
    | -q, --quiet         | Only display network IDs                     |

+ 实例

  ```bash
  root@ubuntu16:~# docker network ls
  NETWORK ID          NAME                DRIVER              SCOPE
  2f6b6558e61e        bridge              bridge              local
  88452592372f        host                host                local
  ce7832aa6ff1        my_net              bridge              local
  a1bdf3fabe87        my_net2             bridge              local
  cddb7d14b045        none                null                local
  ```

  ```bash
  root@ubuntu16:~# docker network ls --no-trunc
  NETWORK ID                                                         NAME                DRIVER              SCOPE
  2f6b6558e61ed980b5a8e2930f0e9546ba197251aae663f0aceee7d1822666cc   bridge              bridge              local
  88452592372fad71b1dcc9dcbb0430453f806b070205c85cd738354863bafcc3   host                host                local
  ce7832aa6ff125169b5b38ea43cf7410d14f116dc42841a3411c0f374f9eabc1   my_net              bridge              local
  a1bdf3fabe871bb7e9ab4e25c2a0d1dbb11f0f44c3d1328d4e447a862cd6c408   my_net2             bridge              local
  cddb7d14b045a18e9e8595331c7b383fb6c73721c38eee3d89fd3fdc2deeb62a   none                null                local
  ```

---

### docker network inspect

+ 显示一个或多个网络的详细信息

+ 语法

  ```bash
  docker network inspect [OPTIONS] NETWORK [NETWORK...]
  ```

  + [OPTIONS]

    | 选项                | 说明                                          |
    | ------------------- | --------------------------------------------- |
    | -f, --format string | Format the output using the given Go template |
    | -v, --verbose       | Verbose output for diagnostics （详细输出）   |

  + NETWORK

    可以是NETWORK ID或者是NAME

+ 实例

  ```bash
  root@ubuntu16:~# docker network inspect bridge
  [
      {
          "Name": "bridge",
          "Id": "2f6b6558e61ed980b5a8e2930f0e9546ba197251aae663f0aceee7d1822666cc",
          "Created": "2020-11-25T10:08:39.373817354+08:00",
          "Scope": "local",
          "Driver": "bridge",
          "EnableIPv6": false,
          "IPAM": {
              "Driver": "default",
              "Options": null,
              "Config": [
                  {
                      "Subnet": "172.17.0.0/16",
                      "Gateway": "172.17.0.1"
                  }
              ]
          },
          "Internal": false,
          "Attachable": false,
          "Ingress": false,
          "ConfigFrom": {
              "Network": ""
          },
          "ConfigOnly": false,
          "Containers": {
              "548af276a749ce10fe3d10eecdffce033f00fb4c0f93271a59d12f22eed80c60": {
                  "Name": "docker-registry",
                  "EndpointID": "27b97462473f7f051aace968dc7a42f095980679e8f1b8ee054060bfaeb55cf4",
                  "MacAddress": "02:42:ac:11:00:02",
                  "IPv4Address": "172.17.0.2/16",
                  "IPv6Address": ""
              },
              "a8eab09f590341645f5c3b9d6c4e67d448dbd0e3f549db684dbbc372a5fde84c": {
                  "Name": "relaxed_curran",
                  "EndpointID": "69ecab133375792097e52b3a68f5627015bdbf43d09c91a5016dcf933613d2cc",
                  "MacAddress": "02:42:ac:11:00:04",
                  "IPv4Address": "172.17.0.4/16",
                  "IPv6Address": ""
              }
          },
          "Options": {
              "com.docker.network.bridge.default_bridge": "true",
              "com.docker.network.bridge.enable_icc": "true",
              "com.docker.network.bridge.enable_ip_masquerade": "true",
              "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
              "com.docker.network.bridge.name": "docker0",
              "com.docker.network.driver.mtu": "1500"
          },
          "Labels": {}
      }
  ]
  ```

---

### docker network create

+ 创建网络

+ 语法

  ```bash
  docker network create [OPTIONS] NETWORK
  ```

  + [OPTIONS]

    ```bash
    Options:
          --attachable           Enable manual container attachment
          --aux-address map      Auxiliary IPv4 or IPv6 addresses used by Network driver (default map[])
          --config-from string   The network from which copying the configuration
          --config-only          Create a configuration only network
      -d, --driver string        Driver to manage the Network (default "bridge")
          --gateway strings      IPv4 or IPv6 Gateway for the master subnet
          --ingress              Create swarm routing-mesh network
          --internal             Restrict external access to the network
          --ip-range strings     Allocate container ip from a sub-range
          --ipam-driver string   IP Address Management Driver (default "default")
          --ipam-opt map         Set IPAM driver specific options (default map[])
          --ipv6                 Enable IPv6 networking
          --label list           Set metadata on a network
      -o, --opt map              Set driver specific options (default map[])
          --scope string         Control the network's scope
          --subnet strings       Subnet in CIDR format that represents a network segment
    ```

+ 实例1：创建172.22.16.0/24 网关为172.22.16.1的网络，网络名为my_net2

  ```bash
  root@ubuntu16:~# docker network create --driver bridge --subnet 172.22.16.0/24 --gateway 172.22.16.1 my_net2
  a1bdf3fabe871bb7e9ab4e25c2a0d1dbb11f0f44c3d1328d4e447a862cd6c408
  root@ubuntu16:~# brctl show
  bridge name	bridge id		STP enabled	interfaces
  br-a1bdf3fabe87		8000.024295f95abc	no		
  br-ce7832aa6ff1		8000.0242e5520021	no		
  docker0		8000.0242cf9b5495	no		veth40556dc
  							veth71385a4
  root@ubuntu16:~# docker network inspect my_net2
  [
      {
          "Name": "my_net2",
          "Id": "a1bdf3fabe871bb7e9ab4e25c2a0d1dbb11f0f44c3d1328d4e447a862cd6c408",
          "Created": "2020-11-25T16:10:52.935030606+08:00",
          "Scope": "local",
          "Driver": "bridge",
          "EnableIPv6": false,
          "IPAM": {
              "Driver": "default",
              "Options": {},
              "Config": [
                  {
                      "Subnet": "172.22.16.0/24",
                      "Gateway": "172.22.16.1"
                  }
              ]
          },
          "Internal": false,
          "Attachable": false,
          "Ingress": false,
          "ConfigFrom": {
              "Network": ""
          },
          "ConfigOnly": false,
          "Containers": {},
          "Options": {},
          "Labels": {}
      }
  ]
  root@ubuntu16:~# ip a show br-a1bdf3fabe87
  13: br-a1bdf3fabe87: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
      link/ether 02:42:95:f9:5a:bc brd ff:ff:ff:ff:ff:ff
      inet 172.22.16.1/24 brd 172.22.16.255 scope global br-a1bdf3fabe87
         valid_lft forever preferred_lft forever
  ```

---

### docker network connect

+ 将一个容器连接到一个网络(给容器加一块对应网络的网卡)

+ 语法

  ```bash
  docker network connect [OPTIONS] NETWORK CONTAINER
  ```

  + [OPTIONS]

    ```bash
    Options:
          --alias strings           Add network-scoped alias for the container
          --driver-opt strings      driver options for the network
          --ip string               IPv4 address (e.g., 172.30.100.104)
          --ip6 string              IPv6 address (e.g., 2001:db8::33)
          --link list               Add link to another container
          --link-local-ip strings   Add a link-local address for the container
    ```

+ 实例：为容器httpd添加一块my_net2的网卡

  ```bash
  root@ubuntu16:~# docker ps
  CONTAINER ID        IMAGE               COMMAND              CREATED              STATUS              PORTS               NAMES
  223b2da7533e        httpd               "httpd-foreground"   About a minute ago   Up 59 seconds       80/tcp              intelligent_moore
  02b576084372        ubuntu:latest       "/bin/bash"          32 minutes ago       Up 32 minutes                           elegant_moore
  50a31b176289        ubuntu:latest       "/bin/bash"          35 minutes ago       Up 35 minutes                           modest_sinoussi
  root@ubuntu16:~# docker network connect my_net2 223b2da7533e
  ```

  

