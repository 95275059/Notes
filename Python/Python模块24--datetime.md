# Python模块24--datetime

## 将时间转换为毫秒级时间戳

```python
import datetime
a = '26 Apr 2021 14:15:42.692'
time_a = datetime.datetime.strptime(a, '%d %b %Y %H:%M:%S.%f')
print(time_a.timestamp())
```

