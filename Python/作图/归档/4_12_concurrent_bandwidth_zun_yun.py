# -*-coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl

myfont = matplotlib.font_manager.FontProperties(fname='simsun.ttf')
mpl.rcParams['axes.unicode_minus'] = False

concurrent_number = [1, 2, 3, 4, 5, 6, 7]
tcp_zun = [7.14, 5.74, 4.91, 4.63, 4.19042969, 3.48535156, 3.54589844]
tcp_yun = [23.2, 36.9, 39, 37.22, 33.88, 24.42, 24.41]
udp_zun = [2.18, 4.1, 5.85, 7.9, 9.81, 11.08, 11.92]
udp_yun = [8.28, 17.26, 28.66, 38.33, 45.9, 54.38, 56.87]

plt.figure(figsize=(13, 5))
# -----------------------   tcp test   -----------------------------
plt.subplot(121)
# zun
plt.plot(concurrent_number, tcp_zun, color="green", label="Zun", linewidth=1.5, marker="^", markersize=4)

# yun
plt.plot(concurrent_number, tcp_yun, color="blue", label="Yun", linewidth=1.5, marker="o", markersize=4)

# 设置图例
plt.legend(fontsize=8)

# 网格线
plt.grid(linestyle='--', linewidth=0.5)

# plt.xlabel(u'跳数', fontproperties=myfont, fontsize=14)
plt.ylabel(u'TCP吞吐量（Gbits/s）', fontproperties=myfont, fontsize=14)

# -----------------------   udp test   -----------------------------
plt.subplot(122)
# zun
plt.plot(concurrent_number, udp_zun, color="green", label="Zun", linewidth=1.5, marker="^", markersize=4)

# yun
plt.plot(concurrent_number, udp_yun, color="blue", label="Yun", linewidth=1.5, marker="o", markersize=4)

# 设置图例
plt.legend(fontsize=8)

# 网格线
plt.grid(linestyle='--', linewidth=0.5)

plt.xlabel(u'并发数', fontproperties=myfont, fontsize=14)
plt.ylabel(u'UDP吞吐量（Gbits/s）', fontproperties=myfont, fontsize=14)

# plt.savefig("4-12 并发情况下Zun与Yun吞吐量对比.pdf", format="pdf", bbox_inches='tight', pad_inches=0.05)
plt.savefig("4-12 并发情况下Zun与Yun吞吐量对比.svg", format="svg", bbox_inches='tight', pad_inches=0.05)

plt.show()
