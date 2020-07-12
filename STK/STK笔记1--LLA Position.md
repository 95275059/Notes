# STK笔记1--LLA Position

### 表格输出格式

![笔记1-1](E:\Notes\STK\笔记1-1.png)

### MATLAB数据提取

```matlab
>> [secData,secNames] = stkReport('*/Missile/Missile1', 'LLA Position',0,0,1)
Warning: ConnectHost:  setting default connection to localhost:5001 
Warning: mexConnect:  Connecting to localhost:5001
 

secData = 

    [1x7 struct]


secNames = 

    'Section_1'

>> secNames

secNames = 

    'Section_1'

>> secData

secData = 

    [1x7 struct]

>> secData{1}

ans = 

1x7 struct array with fields:

    name
    data
    type

>> secData{1}(1)

ans = 

    name: 'Time'
    data: 0
    type: 'Double'

>> secData{1}(2)

ans = 

    name: 'Lat'
    data: 0.2635
    type: 'Double'

>> secData{1}(3)

ans = 

    name: 'Lon'
    data: 2.4435
    type: 'Double'

>> secData{1}(4)

ans = 

    name: 'Alt'
    data: 1.4392e+03
    type: 'Double'

>> secData{1}(5)

ans = 

    name: 'Lat Rate'
    data: 7.0563e-04
    type: 'Double'

>> secData{1}(6)

ans = 

    name: 'Lon Rate'
    data: 5.3275e-04
    type: 'Double'

>> secData{1}(7)

ans = 

    name: 'Alt Rate'
    data: 5.4860e+03
    type: 'Double'

>> stkFindData(secData{1}, 'Lat')

ans =

    0.2635

>> stkFindData(secData{1}, 'Lon')

ans =

    2.4435

>> stkFindData(secData{1}, 'Alt')

ans =

   1.4392e+03
   
>> stkFindData(secData{1}, 'Lat Rate')

ans =

   7.0563e-04

>> stkFindData(secData{1}, 'Lon Rate')

ans =

   5.3275e-04

>> stkFindData(secData{1}, 'Alt Rate')

ans =

   5.4860e+03
```

### MATLAB数据换算

+ Lat/Lon/Lat_Rate/Lon_Rate

  m1 = STK report中的数据

  m2 = matlab提取出来的数据

  **m1 = m2*57.295**

  



