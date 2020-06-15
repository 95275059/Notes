# -*-coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
from pylab import mpl

myfont = matplotlib.font_manager.FontProperties(fname='simsun.ttf')
mpl.rcParams['axes.unicode_minus'] = False

hop_number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tcp_nova_docker = [5.16, 2.62, 1.76, 1.47, 1.18, 0.942382813, 0.844726563, 0.602539063, 0.546875, 0.481445313,
                   0.248046875]
tcp_yun = [42.6, 33.5, 28.3, 25.6, 22.6, 13.8, 12.6, 10.9, 10.5, 10.5, 9.49]
udp_nova_docker = [10.8, 7.99, 5.54, 4.69, 3.99, 3.26, 2.98, 2.48, 2.3, 2.09, 1.89]
udp_yun = [18, 12.5, 10.6, 9.33, 8.21, 6.09, 5.53, 5.13, 4.66, 4.4, 3.96]

plt.figure(figsize=(13, 5))
# -----------------------   tcp test   -----------------------------
plt.subplot(121)
# nova-docker
plt.plot(hop_number, tcp_nova_docker, color="red", label="Nova-docker", linewidth=1.5, marker="x", markersize=4)

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
plt.plot(hop_number, udp_nova_docker, color="red", label="Nova-docker", linewidth=1.5, marker="x", markersize=4)

# yun
plt.plot(hop_number, udp_yun, color="blue", label="Yun", linewidth=1.5, marker="D", markersize=4)

# 设置图例
plt.legend(fontsize=8)

# 网格线
plt.grid(linestyle='--', linewidth=0.5)

plt.xlabel(u'跳数', fontproperties=myfont, fontsize=14)
plt.ylabel(u'UDP吞吐量（Gbits/s）', fontproperties=myfont, fontsize=14)

# plt.savefig("4-8 多跳情况下Nova-docker与Yun吞吐量对比.pdf", format="pdf", bbox_inches='tight', pad_inches=0.05)
plt.savefig("4-8 多跳情况下Nova-docker与Yun吞吐量对比.svg", format="svg", bbox_inches='tight', pad_inches=0.05)

plt.show()
