# OpenStack命令4--glance命令

## 查看目前已经存在的image

```shell
[root@controller cxy_tdyt]# glance image-list
+--------------------------------------+-------------------------------------+
| ID                                   | Name                                |
+--------------------------------------+-------------------------------------+
| 7a8c99ab-deb2-44d9-b25a-8e228fbb9648 |  ldw_kvm_router                     |
| 20179345-4f28-43ab-9b68-9a0aebb780c4 |  ldw_kvm_router_v1                  |
| 7b179f91-b236-46b1-86ac-0cbb1be4644a | 1                                   |
| d13d1802-8e54-48f3-a75a-cf1a49cbe706 | 1u_1g_200g_300mb                    |
| 877deaac-c90c-4d5c-9fe9-63ac4d43bee7 | 1u_6g_100g_500mb                    |
| f306f75d-bbe3-4f94-9f27-25c0d7c4f2d6 | 2u_4g_10g_50mb                      |
| f05d9960-bdb0-4790-a494-d890de9d984c | 4u_1g_250g_50mb                     |
| fb9f98ad-0349-4069-aa3b-13a98bc31fbb | 4u_1g_25g_50mb                      |
| 1dbd9f38-1a8c-49ab-824a-01d5dbc2b162 | 4u_2g_50g_100mb                     |
| f54be00c-9fb3-4ff7-ba3b-40471a347553 | 4u_3g_10g_100m                      |
| 237f2596-8dd2-417a-92b9-7630b697f25c | 6u_1g_20g_10mb                      |
| 05474d51-0317-485d-8dbd-19d49cedac08 | 8u_8g_50g_limit                     |
...
```

---

## 镜像上传（创建镜像）

```shell
[root@controller cxy_tdyt]# glance image-create --name cirros \
> --file /tmp/cirros-0.3.4-x86_64-disk.img \
> --disk-format qcow2 \
> --container-format bare \
> --public
```

```shell
[root@controller cxy_tdyt]# openstack image create --name cirros \
> --file /tmp/cirros-0.3.4-x86_64-disk.img \
> --disk-format qcow2 \
> --container-format bare \
> --public
```

```shell
[root@controller images]# glance image-create --name cxy --file cxy.qcow2 --disk-format qcow2 --container-format bare --visibility public
```

+ 其他参数

  + --progress

    显示文件上传百分比%

---

## 镜像删除

```
[root@controller cxy_tdyt]# glance image-delete *image_id*
```

---

## 显示镜像详细信息

```bash
[root@controller cxy_tdyt]# glance image-show *image_id*
```

```bash
[root@controller cxy_tdyt]# glance image-show 41acd03c-cd7b-4252-a39c-e7751bd0f1c4
+------------------+--------------------------------------+
| Property         | Value                                |
+------------------+--------------------------------------+
| checksum         | bddaa64b03fdbd88297955d664a52a09     |
| container_format | docker                               |
| created_at       | 2019-12-19T03:07:36Z                 |
| disk_format      | raw                                  |
| id               | 41acd03c-cd7b-4252-a39c-e7751bd0f1c4 |
| min_disk         | 0                                    |
| min_ram          | 0                                    |
| name             | ubuntu                               |
| owner            | f2e64bde168f41358b47ca3f1e1caea1     |
| protected        | False                                |
| size             | 66600960                             |
| status           | active                               |
| tags             | []                                   |
| updated_at       | 2019-12-19T03:07:36Z                 |
| virtual_size     | None                                 |
| visibility       | private                              |
+------------------+--------------------------------------+
```

---

## 镜像下载

```bash
[root@controller images]# glance image-download --file *directory and file name of the downloaded image* *image_id*
```

```bash
[root@controller images]# glance image-download --file /home/cxy_tdyt/images/cirros.img cb135ef3-140c-46d8-9f61-51a036f534dd
```

---

