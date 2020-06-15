# -*-coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl

myfont = matplotlib.font_manager.FontProperties(fname='simsun.ttf')
mpl.rcParams['axes.unicode_minus'] = False

number_of_parallel_processes = [1, 4, 6, 9, 12, 16]
score_env1_nova_docker = [761.8, 2357.5, 2702.5, 3496.9, 3914.6, 4230.6]
score_env1_yun = [1556.9, 3874, 4809.5, 5323.4, 5452.3, 5708.1]
score_env2_zun = [847.3, 2379.5, 2758.9, 3527.9, 3719, 4002.6]
score_env2_yun = [1347.1, 3469.2, 4431, 4973.4, 5398.9, 5644.5]

plt.figure(figsize=(13, 5))
# -----------------------   env1 test   -----------------------------
plt.subplot(121)
# nova-docker
plt.plot(number_of_parallel_processes, score_env1_nova_docker, color="red", label="Nova-docker", linewidth=1.5,
         marker="s", markersize=4)

# yun
plt.plot(number_of_parallel_processes, score_env1_yun, color="blue", label="Yun", linewidth=1.5, marker="o",
         markersize=4)

# 设置图例
plt.legend(fontsize=8)

# 网格线
plt.grid(linestyle='--', linewidth=0.5)

plt.xlabel(u'Unixbench进程数', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'(1) Nova-docker vs Yun', fontproperties=myfont, fontsize=14)

# -----------------------   env2 test   -----------------------------
plt.subplot(122)
# zun
plt.plot(number_of_parallel_processes, score_env2_zun, color="green", label="Zun", linewidth=1.5, marker="^", markersize=4)

# yun
plt.plot(number_of_parallel_processes, score_env2_yun, color="blue", label="Yun", linewidth=1.5, marker="o",
         markersize=4)

# 设置图例
plt.legend(fontsize=8)

# 网格线
plt.grid(linestyle='--', linewidth=0.5)

plt.xlabel(u'Unixbench进程数', fontproperties=myfont, fontsize=14)
plt.ylabel(u'得分', fontproperties=myfont, fontsize=14)
plt.title(u'(2) Zun vs Yun', fontproperties=myfont, fontsize=14)


# plt.savefig("5-7 环境1和环境2中容器系统性能测试对比.pdf", format="pdf", bbox_inches='tight', pad_inches=0.05)
plt.savefig("5-7 环境1和环境2中容器系统性能测试对比.svg", format="svg", bbox_inches='tight', pad_inches=0.05)

plt.show()
