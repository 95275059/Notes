# STKTips2--地球同步轨道

1. 英文

   + Geosynchronous orbit
   + Geostationary orbit

2. 基本参数

   | 参数                                     | 数值          |
   | ---------------------------------------- | ------------- |
   | 轨道周期                                 | 23小时56分4秒 |
   | 轨道偏心率（Eccentricity）e=√(1-(b/a)^2) | 0             |
   | 轨道半径                                 | 42164km       |
   | 轨道高度                                 | 35786km       |
   | 近地点幅角（argument of the perigee）    | 0             |

   注：轨道偏心率为0，就表示**轨道是圆形的**

3. 基本介绍

   + 轨道周期等于地球在惯性空间中的自转周期（23小时56分4秒），且方向亦与之一致
   + 卫星在每天同一时间的星下点轨迹相同

4. 分类

   + 同步轨道静止卫星

     + 特征
       + 轨道面的倾角为零
       + 卫星始终位于赤道某地的上空，相对于地球表面是静止的
       + 地面高度约为3.6km
       + 利用均布在地球赤道上的 3颗这样的卫星就可以实现除南北极很小一部分地区外的全球通信

     + 轨道六参数

       | 参数                                   | 数值       |
       | -------------------------------------- | ---------- |
       | 轨道偏心率（Eccentricity）             | 0          |
       | 轨道倾角（Inclination）                | 0          |
       | 近地点幅角（argument of perigee）      | 0          |
       | Lon.Ascn.Node                          | 相应径度   |
    | 半长轴（Semimajor Axis）               | 42164.31km |
       | 平近点角/真近点角（True/Mean Anomaly） | 相应值     |

   + 倾斜轨道同步卫星

   + 极地轨道同步卫星
   
     + 轨道面的倾角为90°
     + 每一圈内都可以经过任何纬度和南北两极的上空
     + 由于卫星在任何位置上都可以覆盖一定的区域，因此，为覆盖南北极，轨道倾角并不需要严格的90°，只需在90°附近就行。在工程上常把倾角在90°左右，但仍能覆盖全球的轨道也称为极轨道