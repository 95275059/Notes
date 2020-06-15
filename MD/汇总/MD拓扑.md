# M拓扑

1. Facility

   + WGS（白色）

     | 地面站                                       | 经纬度                 | Model_Facility.sc名称 |
     | -------------------------------------------- | ---------------------- | --------------------- |
     | 科罗拉多州施里弗（Schiriever）空军基地       | 38.798111, -104.517833 | Facility_WGS_01       |
     | 夏威夷瓦希阿瓦（Wahiawa）宽带控制中心        | 21.501018, -158.019448 | Facility_WGS_02       |
     | 马里兰州米德堡（Fort Meade）宽带卫星控制中心 | 39.105062, -76.734219  | Facility_WGS_03       |

   + 预警卫星系统

     + SBIRS（黄色）

       | 地面站                             | 经纬度                 | Model_Facility.sc名称 |
       | ---------------------------------- | ---------------------- | --------------------- |
       | 伯克利空军基地                     | 39.724222, -104.783561 | Facility_SBIRS_01     |
       | 澳大利亚Nurrungar海外地面站        | -31.323767, 136.776947 | Facility_SBIRS_02     |
       | 莱根赫斯空军基地（RAF Lakenheath） | 52.390672, 0.537485    | Facility_SBIRS_03     |

     + TDRS（红色）

       | 地面站                           | 经纬度               | Model_Facility.sc名称 |
       | -------------------------------- | -------------------- | --------------------- |
       | 白沙接地端子（WSGT）**TDRS**     | 32.5007°N 106.6086°W | Facility_TDRS_01      |
       | 关岛的远程接地端子(GRGT)**TDRS** | 13.6148°N 144.8565°E | Facillity_TDRS_02     |

   + MILSTAR（天蓝）

     | 地面站                                   | 经纬度                 | Model_Facility.sc名称 |
     | ---------------------------------------- | ---------------------- | --------------------- |
     | 科罗拉多州科罗拉多斯普林斯的猎鹰空军基地 | 38.823927, -104.700061 | Facility_MILSTAR_01   |

2. WGS 卫星（10颗）（白色）

   参考Scenario_2

   | 卫星名称        | Model_WGS.sc名称 |
   | --------------- | ---------------- |
   | WGS F1(USA 195) | WGS_geo_01       |
   | WGS F2(USA 204) | WGS_geo_02       |
   | WGS F3(USA 211) | WGS_geo_03       |
   | WGS F4(USA 233) | WGS_geo_04       |
   | WGS F5(USA 243) | WGS_geo_05       |
   | WGS F6(USA 244) | WGS_geo_06       |
   | WGS F7(USA 263) | WGS_geo_07       |
   | WGS F8(USA 272) | WGS_geo_08       |
   | WGS F9(USA 275) | WGS_geo_09       |
   | WGS 10(USA 291) | WGS_geo_10       |

   卫星位置排序：343

   | 排序前     | 排序后     |
   | ---------- | ---------- |
   | WGS_geo_03 | WGS_geo_01 |
   | WGS_geo_01 | WGS_geo_02 |
   | WGS_geo_10 | WGS_geo_03 |
   | WGS_geo_09 | WGS_geo_04 |
   | WGS_geo_02 | WGS_geo_05 |
   | WGS_geo_04 | WGS_geo_06 |
   | WGS_geo_06 | WGS_geo_07 |
   | WGS_geo_08 | WGS_geo_08 |
   | WGS_geo_07 | WGS_geo_09 |
   | WGS_geo_05 | WGS_geo_10 |

   卫星分组排序：343

   | 排序前     | 排序后Model_WGS_V2.sc/Model_WGS_V3.sc |
   | ---------- | ------------------------------------- |
   | WGS_geo_01 | WGS_geo_01_01                         |
   | WGS_geo_02 | WGS_geo_02_01                         |
   | WGS_geo_03 | WGS_geo_03_01                         |
   | WGS_geo_04 | WGS_geo_01_02                         |
   | WGS_geo_05 | WGS_geo_02_02                         |
   | WGS_geo_06 | WGS_geo_03_02                         |
   | WGS_geo_07 | WGS_geo_01_03                         |
   | WGS_geo_08 | WGS_geo_02_03                         |
   | WGS_geo_09 | WGS_geo_03_03                         |
   | WGS_geo_10 | WGS_geo_02_04                         |

   + Access of Facility

     | Facility        | Satellite                    |
     | --------------- | ---------------------------- |
     | Facility_WGS_01 | WGS_geo_02_04                |
     | Facility_WGS_02 | WGS_geo_02_03；WGS_geo_03_03 |
     | Facility_WGS_03 | WGS_geo_01_01；WGS_geo_02_04 |

3. MILSTAR 卫星（9颗）（天蓝）

   | 卫星名称                                     | Model_MILSTAR.sc名称 |
   | -------------------------------------------- | -------------------- |
   | MILSTAR-1 1(USA 99 / Milstar-DFS 1)          | MILSTAR_geo_01       |
   | MILSTAR-1 2(USA 115 / Milstar-DFS 2)         | MILSTAR_geo_02       |
   | MILSTAR-2 3(USA 164 / Milstar 5)             | MILSTAR_geo_03       |
   | MILSTAR-2 4(USA 169 / Milstar 6)             | MILSTAR_geo_04       |
   | AEHF 1(USA 214)                              | MILSTAR_geo_05       |
   | AEHF 2(USA 235)                              | MILSTAR_geo_06       |
   | AEHF 3(USA 246)                              | MILSTAR_geo_07       |
   | AEHF 4(USA 288)                              | MILSTAR_geo_08       |
   | MILSTAR-2 2(USA 157 / Milstar 4)（参数缺失） | MILSTAR_geo_09       |
   | AEHF 5(USA 292)（参数缺失）（AEHF 1的替代）  | MILSTAR_geo_10       |
   | AEHF 6(USA 298)（参数缺失）（AEHF 2的替代）  |                      |

   | 卫星名称                                     | Model_MILSTAR_V2.sc名称 |
   | -------------------------------------------- | ----------------------- |
   | MILSTAR-1 1(USA 99 / Milstar-DFS 1)          | MILSTAR_geo_01          |
   | MILSTAR-1 2(USA 115 / Milstar-DFS 2)         | MILSTAR_geo_02          |
   | MILSTAR-2 2(USA 157 / Milstar 4)（参数缺失） | MILSTAR_geo_03          |
   | MILSTAR-2 3(USA 164 / Milstar 5)             | MILSTAR_geo_04          |
   | MILSTAR-2 4(USA 169 / Milstar 6)             | MILSTAR_geo_05          |
   | AEHF 1(USA 214)                              | MILSTAR_geo_06          |
   | AEHF 2(USA 235)                              | MILSTAR_geo_07          |
   | AEHF 3(USA 246)                              | MILSTAR_geo_08          |
   | AEHF 4(USA 288)                              | MILSTAR_geo_09          |
   | AEHF 5(USA 292)（参数缺失）（AEHF 1的替代）  |                         |
   | AEHF 6(USA 298)（参数缺失）（AEHF 2的替代）  |                         |

   排序后：

   | 排序前         | 排序后         |
   | -------------- | -------------- |
   | MILSTAR_geo_08 | MILSTAR_geo_01 |
   | MILSTAR_geo_04 | MILSTAR_geo_02 |
   | MILSTAR_geo_02 | MILSTAR_geo_03 |
   | MILSTAR_geo_06 | MILSTAR_geo_04 |
   | MILSTAR_geo_05 | MILSTAR_geo_05 |
   | MILSTAR_geo_03 | MILSTAR_geo_06 |
   | MILSTAR_geo_01 | MILSTAR_geo_07 |
   | MILSTAR_geo_09 | MILSTAR_geo_08 |
   | MILSTAR_geo_07 | MILSTAR_geo_09 |

4. SBIRS 卫星 （8颗）（黄色）

   | 卫星名称       | Model_SBIRS.sc名称 |
   | -------------- | ------------------ |
   | GEO-1(USA 230) | SBIRS_geo_01       |
   | GEO-2(USA 241) | SBIRS_geo_02       |
   | GEO-3(USA 273) | SBIRS_geo_03       |
   | GEO-4(USA 282) | SBIRS_geo_04       |
   | HEO-1(USA 184) | SBIRS_heo_01       |
   | HEO-2(USA 200) | SBIRS_heo_02       |
   | HEO-3(USA 259) | SBIRS_heo_03       |
   | HEO-4(USA 278) | SBIRS_heo_04       |

5. TDRS 卫星（3颗）（红色）**==（不搭）==**

   | 卫星名称                                                     | Model_TDRS.sc名称 | Model_TDRS_V2.sc |
   | ------------------------------------------------------------ | ----------------- | ---------------- |
   | TDRS 3（第一代）（备用星；62W）                              | TDRS_geo_01       |                  |
   | TDRS 5（参数缺失）（第一代）（备用星;167W）                  | TDRS_geo_02       |                  |
   | TDRS 6（参数缺失）（第一代）（备用星;46W）                   | TDRS_geo_03       |                  |
   | TDRS 7（参数缺失）（第一代）==（作为TDRS-Z ，填补TDRS东和TDRS西之间的空白区域，275W）== | TDRS_geo_04       | TDRS_geo_01      |
   | TDRS 8（参数缺失）（第二代TDRS-H）（备用星;271W）            | TDRS_geo_05       |                  |
   | TDRS 9（第二代TDRS-I）==（TDRS东，62W）==                    | TDRS_geo_06       | TDRS_geo_02      |
   | TDRS 10（第二代TDRS-J）==（TDRS西，171W）==                  | TDRS_geo_07       | TDRS_geo_03      |
   | TDRS 11（第三代TDRS-K）（171W）（参数缺失）                  | TDRS_geo_08       |                  |
   | TDRS 12（第三代TDRS-L）（41W）（参数缺失）                   | TDRS_geo_09       |                  |
   | TDRS 13（第三代TDRS-M）                                      | 没有参数，未搭    |                  |

   ![TDRS](.\TDRS.png)

   + 第三代用于替代第一代及第二代，第一代马上退役，只部署TDRS-7,TDRS-9,TDRS-10即可

6. 预警雷达（8个）（紫色）

   | 地面站                                  | 经纬度                 | Model_Radar.sc名称 |
   | --------------------------------------- | ---------------------- | ------------------ |
   | 比耳空军基地(Beale AFB)                 | 39.111545, -121.361287 | Radar_UEWR_01      |
   | 科利尔空军基地(Clear AFB)               | 64.303823, -149.148919 | Radar_UEWR_02      |
   | 图勒空军基地(Thule AB)                  | 76.533373, -68.699921  | Radar_UEWR_03      |
   | 菲林代尔斯皇家空军基地(RAF Fylingdales) | 54.361929, -0.670116   | Radar_UEWR_04      |
   | 科德角空军基地(Cap cod AFS)             | 41.766004, -70.538747  | Radar_UEWR_05      |
   | 新竹县五峰乡乐山                        | 24.496971, 121.070496  | Radar_UEWR_06      |
   | 卡塔尔                                  | 25.263007, 51.200628   | Radar_UEWR_07      |
   | 艾瑞克森（Eareckson）空军基地           | 52.724916, 174.112407  | Radar_Dane_01      |

7. 跟踪识别雷达（9个）（粉色）

   | 地面站                           | 经纬度                 | Model_Radar.sc名称 |
   | -------------------------------- | ---------------------- | ------------------ |
   | 太平洋威克岛                     | 19.336598, 166.639795  | Radar_XGround_01   |
   | 阿拉斯加州的朱诺                 | 58.420487, -134.440302 | Radar_XGround_02   |
   | 日本北部青森县车力村三泽基地     | 40.686367, 141.366115  | Radar_XGround_03   |
   | 以色列内盖夫沙漠凯伦山           | 30.714786, 34.875705   | Radar_XGround_04   |
   | 土耳其马拉蒂亚省                 | 38.435548, 38.320586   | Radar_XGround_05   |
   | 日本南部京都京丹后市经岬分屯基地 | 35.766502, 135.193218  | Radar_XGround_06   |
   | 海基X波段雷达（位置不定）        | 44.733396, -175.612852 | Radar_XSea_01      |
   | 宙斯盾舰（位置不定）             | 44.422031, -147.609885 | Radar_AEGIS_01     |
   | 宙斯盾舰（位置不定）             | 33.933237, -138.005052 | Radar_AEGIS_02     |

   Radar Access
   
   | Model_Radar.sc   | Access                                                       |
   | ---------------- | ------------------------------------------------------------ |
   | Radar_XGround_01 | MILSTAR_geo_01;MILSTAR_geo_02;MILSTAR_geo_08;MILSTAR_geo_09; |
   | Radar_XGround_02 | MILSTAR_geo_01;MILSTAR_geo_02;MILSTAR_geo_03;MILSTAR_geo_04; |
   | Radar_XGround_03 | MILSTAR_geo_01;MILSTAR_geo_08;MILSTAR_geo_09;                |
   | Radar_XGround_04 | MILSTAR_geo_05;MILSTAR_geo_06;MILSTAR_geo_07;MILSTAR_geo_09; |
   | Radar_XGround_05 | MILSTAR_geo_05;MILSTAR_geo_06;MILSTAR_geo_07;MILSTAR_geo_09; |
   | Radar_XGround_06 | MILSTAR_geo_01;MILSTAR_geo_08;MILSTAR_geo_09;                |
   | Radar_XSea_01    | MILSTAR_geo_01;MILSTAR_geo_02;MILSTAR_geo_09;                |
| Radar_AEGIS_01   | MILSTAR_geo_01;MILSTAR_geo_02;MILSTAR_geo_03;                |
   | Radar_AEGIS_02   | MILSTAR_geo_01;MILSTAR_geo_02;MILSTAR_geo_03;MILSTAR_geo_04; |

8. 指挥中心（3个）（墨绿）

   | 指挥中心                       | 经纬度                 | Model_Facility.sc |
   | ------------------------------ | ---------------------- | ----------------- |
   | 美国华盛顿五角大楼             | 38.872082, -77.056299  | CC_01             |
   | 美国内布拉斯加州奥法特空军基地 | 41.971633, -95.883277  | CC_02             |
   | 夏威夷霍蘭·史密斯營            | 21.386613, -157.908402 | CC_03             |



