# MySQL笔记1--常用语句

1. 创建表

   ```mysql
   CREATE TABLE GWL_Switch_MD(
       sate_name varchar(20),
       tag char(1),
       fac_name varchar(20),
       port_id char(36)
   );
   ```

   ```mysql
   CREATE TABLE GWL_Switch_MD(sate_name varchar(20),tag char(1),fac_name varchar(20),port_id varchar(36));
   ```

2. 删除表

   ```mysql
   DROP TABLE GWL_Switch_MD;
   ```

3. 清空表内容

   ```mysql
   delete from GWL_Switch_MD;
   ```

4. 查看表内容

   ```mysql
   select * from GWL_Switch_MD;
   ```

5. 插入表

   ```mysql
   insert into GWL_Switch_MD(sate_name,tag,fac_name,port_id) values('SBIRS_geo_01','1','Facility_SBIRS_02','00000000-0000-0000-0000-000000000000');
   ```

6. 返回表行数

   ```mysql
   SELECT count(*) FROM objects
   ```

7. 返回表列数

   ```mysql
   SELECT count(*) FROM information_schema.COLUMNS WHERE table_name='objects'
   ```

   

   

