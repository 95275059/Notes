# -*-coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl

myfont = matplotlib.font_manager.FontProperties(fname='simsun.ttf')
mpl.rcParams['axes.unicode_minus'] = False

concurrent_number = [1, 2, 3, 4, 5, 6, 7]
tcp_nova_docker = [2.48, 1.79292969, 1.828125, 1.77539063, 1.57128906, 1.46875, 1.40527344]
tcp_yun = [31.3, 41.6, 35.28, 31.66, 30.13, 21, 20.53]
udp_nova_docker = [7.76, 9.76, 16.11, 21.17, 24.05, 26.07, 27.56]
udp_yun = [11.8, 22.5, 33.27, 39.38, 46.03, 48.81, 47.28]

plt.figure(figsize=(13, 5))
# -----------------------   tcp test   -----------------------------
plt.subplot(121)
# nova-docker
plt.plot(concurrent_number, tcp_nova_docker, color="red", label="Nova-docker", linewidth=1.5, marker="s", markersize=4)

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
# nova-docker
plt.plot(concurrent_number, udp_nova_docker, color="red", label="Nova-docker", linewidth=1.5, marker="s", markersize=4)

# yun
plt.plot(concurrent_number, udp_yun, color="blue", label="Yun", linewidth=1.5, marker="o", markersize=4)

# 设置图例
plt.legend(fontsize=8)

# 网格线
plt.grid(linestyle='--', linewidth=0.5)

plt.xlabel(u'并发数', fontproperties=myfont, fontsize=14)
plt.ylabel(u'UDP吞吐量（Gbits/s）', fontproperties=myfont, fontsize=14)

# plt.savefig("4-11 并发情况下Nova-docker与Yun吞吐量对比.pdf", format="pdf", bbox_inches='tight', pad_inches=0.05)
plt.savefig("4-11 并发情况下Nova-docker与Yun吞吐量对比.svg", format="svg", bbox_inches='tight', pad_inches=0.05)

plt.show()
