# -*-coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from pylab import mpl

myfont = matplotlib.font_manager.FontProperties(fname='simsun.ttf')
mpl.rcParams['axes.unicode_minus'] = False

label_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
x = range(len(label_list))

plt.figure(figsize=(20, 12))
# ----------------------------------- 1 process --------------------------------------
plt.subplot(231)
process_1_zun = [2352, 730.8, 380.3, 1374, 872.1, 2316.7, 674.7, 269.7, 296.2, 960, 3129.2, 466.2]
process_1_yun = [3144.7, 833.8, 951.8, 1990.6, 1259.8, 3355.1, 975.7, 344.2, 669.4, 1882, 5604.7, 716.9]
process_1_zun_rect = plt.bar(x, height=process_1_zun, width=0.4, alpha=0.8, color='green',
                             edgecolor='black', label='Zun', hatch='xx')
process_1_yun_rect = plt.bar([i + 0.4 for i in x], height=process_1_yun, width=0.4, alpha=0.8, color='blue',
                             edgecolor='black',
                             label='Yun')
plt.xticks([i + 0.2 for i in x], label_list, fontproperties=myfont, fontsize=14)
plt.xlabel(u'测试项', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'（1）1个进程', fontproperties=myfont, fontsize=14)
plt.legend()

# ----------------------------------- 4 process --------------------------------------
plt.subplot(232)
process_4_zun = [8991.4, 2745.3, 2090.6, 1438.3, 983.5, 2486.9, 2656.2, 1088.3, 1330.7, 3842, 7807.7, 1573.1]
process_4_yun = [10995.5, 2954.9, 3399.2, 2655.4, 1690.5, 4733.6, 3453, 1339.9, 2595.8, 5580.5, 8631.2, 2238.7]
process_4_zun_rect = plt.bar(x, height=process_4_zun, width=0.4, alpha=0.8, color='green',
                             edgecolor='black', label='Zun', hatch='xx')
process_4_yun_rect = plt.bar([i + 0.4 for i in x], height=process_4_yun, width=0.4, alpha=0.8, color='blue',
                             edgecolor='black',
                             label='Yun')
plt.xticks([i + 0.2 for i in x], label_list, fontproperties=myfont, fontsize=14)
plt.xlabel(u'测试项', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'（2）4个进程', fontproperties=myfont, fontsize=14)

plt.legend()

# ----------------------------------- 6 process --------------------------------------
plt.subplot(233)
process_6_zun = [12110.4, 3962.9, 2332.2, 1339, 875.6, 2572.5, 3509.9, 1460.1, 1496.8, 4589.6, 8310, 1968.9]
process_6_yun = [15690.8, 4191.3, 4440.7, 2652.9, 1671.6, 5069.7, 4878.4, 2045, 3661.9, 7726.5, 9583.4, 3225.6]
process_6_zun_rect = plt.bar(x, height=process_6_zun, width=0.4, alpha=0.8, color='green',
                             edgecolor='black', label='Zun', hatch='xx')
process_6_yun_rect = plt.bar([i + 0.4 for i in x], height=process_6_yun, width=0.4, alpha=0.8, color='blue',
                             edgecolor='black',
                             label='Yun')
plt.xticks([i + 0.2 for i in x], label_list, fontproperties=myfont, fontsize=14)
plt.xlabel(u'测试项', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'（3）6个进程', fontproperties=myfont, fontsize=14)
plt.legend()

# ----------------------------------- 9 process --------------------------------------
plt.subplot(234)
process_9_zun = [16395.3, 5681.4, 3947.1, 1277.3, 849.4, 2429.9, 4924.4, 2223.5, 2631.6, 6832.4, 8521.7, 2285.6]
process_9_yun = [16979.9, 5726.9, 5863.7, 2288, 1452.6, 4432.4, 5918, 2661.7, 4569.7, 9521.9, 9325.9, 4265.7]
process_9_zun_rect = plt.bar(x, height=process_9_zun, width=0.4, alpha=0.8, color='green',
                             edgecolor='black', label='Zun', hatch='xx')
process_9_yun_rect = plt.bar([i + 0.4 for i in x], height=process_9_yun, width=0.4, alpha=0.8, color='blue',
                             edgecolor='black',
                             label='Yun')
plt.xticks([i + 0.2 for i in x], label_list, fontproperties=myfont, fontsize=14)
plt.xlabel(u'测试项', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'（4）9个进程', fontproperties=myfont, fontsize=14)
plt.legend()

# ----------------------------------- 12 process --------------------------------------
plt.subplot(235)
process_12_zun = [17985.9, 7469.2, 3997.1, 1210.4, 829.3, 2387.6, 5424.7, 2660.5, 2939.5, 7296.9, 8489.7, 2069.5]
process_12_yun = [18164.4, 7155.2, 6592.7, 2195.1, 1366.1, 4486, 6902.4, 3219.9, 4999.7, 9837.3, 9482.4, 5133.7]
process_12_zun_rect = plt.bar(x, height=process_12_zun, width=0.4, alpha=0.8, color='green',
                              edgecolor='black', label='Zun', hatch='xx')
process_12_yun_rect = plt.bar([i + 0.4 for i in x], height=process_12_yun, width=0.4, alpha=0.8, color='blue',
                              edgecolor='black',
                              label='Yun')
plt.xticks([i + 0.2 for i in x], label_list, fontproperties=myfont, fontsize=14)
plt.xlabel(u'测试项', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'（5）12个进程', fontproperties=myfont, fontsize=14)

height = process_12_zun_rect[1].get_height()
plt.text(process_12_zun_rect[1].get_x() + process_12_zun_rect[1].get_width() / 2, height + 1,
         process_12_zun[1], ha="right", va="bottom")
height = process_12_yun_rect[1].get_height()
plt.text(process_12_yun_rect[1].get_x() + process_12_yun_rect[1].get_width() / 2, height + 1,
         process_12_yun[1], ha="left", va="bottom")

plt.legend()

# ----------------------------------- 16 process --------------------------------------
plt.subplot(236)
process_16_zun = [19030.1, 9648.4, 4558.8, 1189.6, 793.2, 2271.8, 5955.5, 3011.8, 3515.4, 8185.5, 8379.8, 2178.5]
process_16_yun = [18144.5, 9568, 7105.3, 2260.4, 1417.8, 4507.4, 6909.6, 3323.9, 5330.6, 9867.1, 9452, 5140.9]
process_16_zun_rect = plt.bar(x, height=process_16_zun, width=0.4, alpha=0.8, color='green',
                              edgecolor='black', label='Zun', hatch='xx')
process_16_yun_rect = plt.bar([i + 0.4 for i in x], height=process_16_yun, width=0.4, alpha=0.8, color='blue',
                              edgecolor='black',
                              label='Yun')
plt.xticks([i + 0.2 for i in x], label_list, fontproperties=myfont, fontsize=14)
plt.xlabel(u'测试项', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'（6）16个进程', fontproperties=myfont, fontsize=14)

height = process_16_zun_rect[0].get_height()
plt.text(process_16_zun_rect[0].get_x() + process_16_zun_rect[0].get_width() / 2, height + 1,
         process_16_zun[0], ha="right", va="bottom")
height = process_16_yun_rect[0].get_height()
plt.text(process_16_yun_rect[0].get_x() + process_16_yun_rect[0].get_width() / 2, height + 1,
         process_16_yun[0], ha="left", va="bottom")

height = process_16_zun_rect[1].get_height()
plt.text(process_16_zun_rect[1].get_x() + process_16_zun_rect[1].get_width() / 2, height + 1,
         process_16_zun[1], ha="right", va="bottom")
height = process_16_yun_rect[1].get_height()
plt.text(process_16_yun_rect[1].get_x() + process_16_yun_rect[1].get_width() / 2, height + 1,
         process_16_yun[1], ha="left", va="bottom")

plt.legend()

# 输出图片
# plt.savefig("5-9 环境2中单独测试项对比结果.pdf", format="pdf", bbox_inches='tight', pad_inches=0.05)
plt.savefig("5-9 环境2中单独测试项对比结果.svg", format="svg", bbox_inches='tight', pad_inches=0.05)

plt.show()
