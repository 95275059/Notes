# -*-coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl

myfont = matplotlib.font_manager.FontProperties(fname='simsun.ttf')
mpl.rcParams['axes.unicode_minus'] = False

label_list = [u'无限制', 'Nova-docker', 'Zun', 'Yun']
cpu_list = [800, 800, 100, 100]
memory_list = [8, 1, 1, 1]
disk_list = [50, 50, 4.6, 4.6]
color_list = ['c', 'red', 'green', 'blue']
hatch_list = ['o', '/', '+', '*']

label_list.reverse()
cpu_list.reverse()
memory_list.reverse()
disk_list.reverse()
color_list.reverse()
hatch_list.reverse()

plt.figure(figsize=(20, 5))
# ---------------------------- cpu ---------------------------
plt.subplot(131)
cpu_rects = plt.barh(range(4), cpu_list, alpha=0.8, color=color_list, hatch=hatch_list,
                     edgecolor='black')
plt.yticks(range(4), label_list, fontproperties=myfont)
plt.xlabel(u'CPU利用率（%）', fontproperties=myfont, fontsize=14)
plt.title('CPU', fontsize=14)

# --------------------------- memory -------------------------
plt.subplot(132)
memory_rects = plt.barh(range(4), memory_list, alpha=0.8, color=color_list, hatch=hatch_list,
                        edgecolor='black')
plt.yticks(range(4), label_list, fontproperties=myfont)
plt.xlabel(u'内存大小（GB）', fontproperties=myfont, fontsize=14)
plt.title('Memory', fontsize=14)

# --------------------------- disk ----------------------------
plt.subplot(133)
disk_rects = plt.barh(range(4), disk_list, alpha=0.8, color=color_list, hatch=hatch_list,
                      edgecolor='black')
plt.yticks(range(4), label_list, fontproperties=myfont)
plt.xlabel(u'文件大小（GB）', fontproperties=myfont, fontsize=14)
plt.title('Disk', fontsize=14)

# 输出图片
plt.savefig("4-13 资源限制对比.pdf", format="pdf", bbox_inches='tight', pad_inches=0.05)

plt.show()
