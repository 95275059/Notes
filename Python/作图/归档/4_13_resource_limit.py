# -*-coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from pylab import mpl

myfont = matplotlib.font_manager.FontProperties(fname='simsun.ttf')
mpl.rcParams['axes.unicode_minus'] = False

label_list = [u'无限制', 'Nova-docker', 'Zun', 'Yun']
cpu_list = [800, 800, 100, 100]
memory_list = [8, 1, 1, 1]
disk_list = [50, 50, 4.6, 4.6]
hatch_list = {'o', '/', '+', '*'}

legend_elements = [Patch(facecolor='orange', edgecolor='black', label=u'无限制'),
                   Patch(facecolor='red', edgecolor='black', label='Nova-docker'),
                   Patch(facecolor='green', edgecolor='black', label='Zun'),
                   Patch(facecolor='blue', edgecolor='black', label='Yun')]

plt.figure(figsize=(19, 5))
# ---------------------------- cpu ---------------------------
plt.subplot(131)
cpu_rects = plt.bar(range(4), height=cpu_list, width=0.4, alpha=0.8, color=['orange', 'red', 'green', 'blue'],
                    edgecolor='black')
plt.xticks(range(4), label_list, fontproperties=myfont, fontsize=14)
plt.ylabel(u'CPU利用率（%）', fontproperties=myfont, fontsize=14)
plt.title('CPU', fontproperties=myfont, fontsize=14)
# 设置标注
for rect in cpu_rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height + 1, str(height), ha="center", va="bottom")
plt.legend(handles=legend_elements, loc=1, prop=myfont)

# --------------------------- memory -------------------------
plt.subplot(132)
memory_rects = plt.bar(range(4), height=memory_list, width=0.4, alpha=0.8, color=['orange', 'red', 'green', 'blue'],
                       edgecolor='black')
plt.xticks(range(4), label_list, fontproperties=myfont, fontsize=14)
plt.ylabel(u'内存大小（GB）', fontproperties=myfont, fontsize=14)
plt.title('Memory', fontproperties=myfont, fontsize=14)
# 设置标注
for rect2 in memory_rects:
    height = rect2.get_height()
    plt.text(rect2.get_x() + rect2.get_width() / 2, height + 0.01, str(height), ha="center", va="bottom")
plt.legend(handles=legend_elements, loc=1, prop=myfont)

# --------------------------- disk ----------------------------
plt.subplot(133)
disk_rects = plt.bar(range(4), height=disk_list, width=0.4, alpha=0.8, color=['orange', 'red', 'green', 'blue'],
                     edgecolor='black')
plt.xticks(range(4), label_list, fontproperties=myfont, fontsize=14)
plt.ylabel(u'文件大小（GB）', fontproperties=myfont, fontsize=14)
plt.title('Disk', fontproperties=myfont, fontsize=14)
# 设置标注
for rect3 in disk_rects:
    height = rect3.get_height()
    plt.text(rect3.get_x() + rect3.get_width() / 2, height + 0.0625, str(height), ha="center", va="bottom")
plt.legend(handles=legend_elements, loc=1, prop=myfont)

# ---------------------------------------------------------------

# 输出图片
plt.savefig("4-13 资源限制对比.pdf", format="pdf", bbox_inches='tight', pad_inches=0.05)
# plt.savefig("4-13 资源限制对比.svg", format="svg", bbox_inches='tight', pad_inches=0.05)

plt.show()
