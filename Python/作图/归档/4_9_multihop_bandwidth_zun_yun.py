# -*-coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl

myfont = matplotlib.font_manager.FontProperties(fname='simsun.ttf')
mpl.rcParams['axes.unicode_minus'] = False

hop_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tcp_zun = [10.1, 6.73, 4.66, 3.91, 2.95, 2.62, 2.15, 2.03, 1.84, 1.68, 1.63]
tcp_yun = [31.6, 24, 20, 17.6, 15.4, 9.52, 9.25, 8.51, 8.48, 7.83, 6.72]
udp_zun = [3.25, 2.06, 1.33, 1.02, 0.77734375, 0.676757813, 0.619140625, 0.5234375, 0.489257813, 0.395507813,
           0.360351563]
udp_yun = [10.6, 8.28, 6.85, 5.64, 4.81, 3.5, 3.49, 3.1, 3.08, 2.8, 2.4]

plt.figure(figsize=(13, 5))
# -----------------------   tcp test   -----------------------------
plt.subplot(121)
# zun
plt.plot(hop_number, tcp_zun, color="green", label="Zun", linewidth=1.5, marker="v", markersize=4)

# yun
plt.plot(hop_number, tcp_yun, color="blue", label="Yun", linewidth=1.5, marker="D", markersize=4)

# 设置图例
plt.legend(fontsize=8)

# 网格线
plt.grid(linestyle='--', linewidth=0.5)

# plt.xlabel(u'跳数', fontproperties=myfont, fontsize=14)
plt.ylabel(u'TCP吞吐量（Gbits/s）', fontproperties=myfont, fontsize=14)

# -----------------------   udp test   -----------------------------
plt.subplot(122)
# nova-docker
plt.plot(hop_number, udp_zun, color="green", label="Zun", linewidth=1.5, marker="v", markersize=4)

# yun
plt.plot(hop_number, udp_yun, color="blue", label="Yun", linewidth=1.5, marker="D", markersize=4)

# 设置图例
plt.legend(fontsize=8)

# 网格线
plt.grid(linestyle='--', linewidth=0.5)

plt.xlabel(u'跳数', fontproperties=myfont, fontsize=14)
plt.ylabel(u'UDP吞吐量（Gbits/s）', fontproperties=myfont, fontsize=14)

# plt.savefig("4-9 多跳情况下Zun与Yun吞吐量对比.pdf", format="pdf", bbox_inches='tight', pad_inches=0.05)
plt.savefig("4-9 多跳情况下Zun与Yun吞吐量对比.svg", format="svg", bbox_inches='tight', pad_inches=0.05)

plt.show()
