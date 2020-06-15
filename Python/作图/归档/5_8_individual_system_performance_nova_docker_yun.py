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
process_1_nova_docker = [2004.8, 622.4, 353.5, 1146.6, 895.9, 1957.7, 634.4, 364.7, 466.4, 564.2, 2520.6, 280.8]
process_1_yun = [3086, 833.9, 552.1, 3132.7, 2007.1, 4443.2, 1532.5, 391, 991.7, 1099.5, 3944.5, 1982.3]
process_1_nova_docker_rect = plt.bar(x, height=process_1_nova_docker, width=0.4, alpha=0.8, color='red',
                                     edgecolor='black', label='Nova-docker', hatch='//')
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
process_4_nova_docker = [8392.8, 2462.7, 1460.9, 2232.6, 1494.5, 3013.3, 2264.1, 1433.4, 2071.7, 2663.8, 5925.4, 914.7]
process_4_yun = [11011.5, 2935.7, 2243.2, 3532.5, 2294.5, 6431.8, 5353.9, 1569.8, 3278.9, 4029.1, 5665.7, 4804.5]
process_4_nova_docker_rect = plt.bar(x, height=process_4_nova_docker, width=0.4, alpha=0.8, color='red',
                                     edgecolor='black', label='Nova-docker', hatch='//')
process_4_yun_rect = plt.bar([i + 0.4 for i in x], height=process_4_yun, width=0.4, alpha=0.8, color='blue',
                             edgecolor='black',
                             label='Yun')
plt.xticks([i + 0.2 for i in x], label_list, fontproperties=myfont, fontsize=14)
plt.xlabel(u'测试项', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'（2）4个进程', fontproperties=myfont, fontsize=14)

height = process_4_nova_docker_rect[-2].get_height()
plt.text(process_4_nova_docker_rect[-2].get_x() + process_4_nova_docker_rect[-2].get_width() / 2, height + 1,
         process_4_nova_docker[-2], ha="right", va="bottom")
height = process_4_yun_rect[-2].get_height()
plt.text(process_4_yun_rect[-2].get_x() + process_4_yun_rect[-2].get_width() / 2, height + 1,
         process_4_yun[-2], ha="left", va="bottom")

plt.legend()

# ----------------------------------- 6 process --------------------------------------
plt.subplot(233)
process_6_nova_docker = [10212.6, 3620.7, 1926.6, 1613.2, 1215, 1975.5, 3228.5, 2046.5, 2800.7, 3690.9, 5914.4, 1362.2]
process_6_yun = [15592, 4176, 3065.8, 3489.2, 2239, 6447.5, 7578.4, 2444.3, 4699.6, 6233.9, 6096.4, 4605.2]
process_6_nova_docker_rect = plt.bar(x, height=process_6_nova_docker, width=0.4, alpha=0.8, color='red',
                                     edgecolor='black', label='Nova-docker', hatch='//')
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
process_9_nova_docker = [14781, 5436.4, 2491.7, 1651.4, 1214.2, 2664.3, 4628.1, 2992.5, 4103.8, 4795.6, 6262.9, 1831]
process_9_yun = [16892.6, 5700.7, 3787.8, 3294.1, 2104.4, 6156.4, 8337.6, 3443.7, 6137.5, 6509.3, 6368.7, 4554.6]
process_9_nova_docker_rect = plt.bar(x, height=process_9_nova_docker, width=0.4, alpha=0.8, color='red',
                                     edgecolor='black', label='Nova-docker', hatch='//')
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
process_12_nova_docker = [17994.7, 7192, 2828.7, 1618.9, 1053.4, 2823.5, 5818.1, 3649.8, 5014.7, 4884.1, 6229.2, 2267.3]
process_12_yun = [17967.4, 7168.7, 4023.7, 3176.2, 2042.9, 5988.1, 8955.8, 4486.7, 6842, 5013.1, 5454, 4560]
process_12_nova_docker_rect = plt.bar(x, height=process_12_nova_docker, width=0.4, alpha=0.8, color='red',
                                      edgecolor='black', label='Nova-docker', hatch='//')
process_12_yun_rect = plt.bar([i + 0.4 for i in x], height=process_12_yun, width=0.4, alpha=0.8, color='blue',
                              edgecolor='black',
                              label='Yun')
plt.xticks([i + 0.2 for i in x], label_list, fontproperties=myfont, fontsize=14)
plt.xlabel(u'测试项', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'（5）12个进程', fontproperties=myfont, fontsize=14)

height = process_12_nova_docker_rect[0].get_height()
plt.text(process_12_nova_docker_rect[0].get_x() + process_12_nova_docker_rect[0].get_width() / 2, height + 1,
         process_12_nova_docker[0], ha="right", va="bottom")
height = process_12_yun_rect[0].get_height()
plt.text(process_12_yun_rect[0].get_x() + process_12_yun_rect[0].get_width() / 2, height + 1,
         process_12_yun[0], ha="left", va="bottom")

height = process_12_nova_docker_rect[1].get_height()
plt.text(process_12_nova_docker_rect[1].get_x() + process_12_nova_docker_rect[1].get_width() / 2, height + 1,
         process_12_nova_docker[1], ha="right", va="bottom")
height = process_12_yun_rect[1].get_height()
plt.text(process_12_yun_rect[1].get_x() + process_12_yun_rect[1].get_width() / 2, height + 1,
         process_12_yun[1], ha="left", va="bottom")

height = process_12_nova_docker_rect[-2].get_height()
plt.text(process_12_nova_docker_rect[-2].get_x() + process_12_nova_docker_rect[-2].get_width() / 2, height + 1,
         process_12_nova_docker[-2], ha="right", va="bottom")
height = process_12_yun_rect[-2].get_height()
plt.text(process_12_yun_rect[-2].get_x() + process_12_yun_rect[-2].get_width() / 2, height + 1,
         process_12_yun[-2], ha="left", va="bottom")

plt.legend()

# ----------------------------------- 16 process --------------------------------------
plt.subplot(236)
process_16_nova_docker = [19219.4, 9571.8, 3005.1, 1743.4, 1174.7, 2715, 6233.6, 3952.2, 5952.9, 5092.9, 6429.8, 2226.5]
process_16_yun = [17957.1, 9576.8, 3991.6, 3313.1, 2162.9, 6133.8, 8935.5, 4483.2, 7113.9, 5195.6, 5853.5, 4575.2]
process_16_nova_docker_rect = plt.bar(x, height=process_16_nova_docker, width=0.4, alpha=0.8, color='red',
                                      edgecolor='black', label='Nova-docker', hatch='//')
process_16_yun_rect = plt.bar([i + 0.4 for i in x], height=process_16_yun, width=0.4, alpha=0.8, color='blue',
                              edgecolor='black',
                              label='Yun')
plt.xticks([i + 0.2 for i in x], label_list, fontproperties=myfont, fontsize=14)
plt.xlabel(u'测试项', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'（6）16个进程', fontproperties=myfont, fontsize=14)

height = process_16_nova_docker_rect[0].get_height()
plt.text(process_16_nova_docker_rect[0].get_x() + process_16_nova_docker_rect[0].get_width() / 2, height + 1,
         process_16_nova_docker[0], ha="right", va="bottom")
height = process_16_yun_rect[0].get_height()
plt.text(process_16_yun_rect[0].get_x() + process_16_yun_rect[0].get_width() / 2, height + 1,
         process_16_yun[0], ha="left", va="bottom")

height = process_16_nova_docker_rect[-2].get_height()
plt.text(process_16_nova_docker_rect[-2].get_x() + process_16_nova_docker_rect[-2].get_width() / 2, height + 1,
         process_16_nova_docker[-2], ha="right", va="bottom")
height = process_16_yun_rect[-2].get_height()
plt.text(process_16_yun_rect[-2].get_x() + process_16_yun_rect[-2].get_width() / 2, height + 1,
         process_16_yun[-2], ha="left", va="bottom")

plt.legend()

# 输出图片
# plt.savefig("5-8 环境1中单独测试项对比结果.pdf", format="pdf", bbox_inches='tight', pad_inches=0.05)
plt.savefig("5-8 环境1中单独测试项对比结果.svg", format="svg", bbox_inches='tight', pad_inches=0.05)

plt.show()
