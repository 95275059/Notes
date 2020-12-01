# MySQLTips1--(1054, "Unknown column ' ' in 'field list'")

### 错误情况

```mysql
CREATE TABLE monitor_radar_dane_01(Objects char(20),Start_Time char(10),Stop_Time char(10));
```

```mysql
INSERT INTO monitor_radar_dane_01 VALUES (Missile1,478,1630);
```

### 原因

missile1缺少引号

### 解决

```mysql
INSERT INTO monitor_radar_dane_01 VALUES ('Missile1',478,1630);
```



