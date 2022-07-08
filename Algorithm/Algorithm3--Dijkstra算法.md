# Algorithm3--Dijkstra算法

## 介绍

* Dijkstra是用来求单源最短路径的
  * 单源：从一个顶点出发，Dijkstra算法只能求一个顶点到其他点的最短距离而不是任意两点

## 原理

* 前提条件和环境

  一个连通图，若干节点，节点可能有数值，但是`路径`一定有`权值`。

  并且路径**不能为负**。否则Dijkstra就不适用。

* 核心思想：贪心

  在对问题求解时，总是做出在当前看来是最好的选择。

  也就是说，不从整体最优上加以考虑，他所做出的是在某种意义上的局部最优解。

  贪心算法不是对所有问题都能得到整体最优解，关键是贪心策略的选择，选择的贪心策略必须具备无后效性，即某个状态以前的过程不会影响以后的状态，只与当前状态有关。

* 过程

  涉及的变量：

  * 首先，Dijkstra处理的是带正权值的`有权图`，那么，就需要一个**二维数组**（如果空间大用list数组）存储各个点到达(`边`)的权值大小。**(邻接矩阵或者邻接表存储)**
  * 其次，还需要一个**boolean数组**判断那些点已经确定最短长度，那些点没有确定。**int数组**记录距离(**在算法执行过程可能被多次更新**)。
  * 需要**优先队列**加入**已经确定点的周围点**。每次抛出确定最短路径的那个并且确定最短，直到所有点路径确定最短为止。

  过程

  * 一般从选定点开始抛入优先队列。（路径一般为0），`boolean数组`标记0的位置(最短为0) , 然后0`周围连通的点`抛入优先队列中（可能是node类），并把各个点的距离记录到对应数组内(**如果小于就更新，大于就不动，初始第一次是无穷肯定会更新**)，第一次就结束了
  * 从队列中抛出`距离最近`的那个点`B`（**第一次就是0周围邻居**）。这个点距离一定是最近的（所有权值都是正的，点的距离只能越来越长。）标记这个点为`true`，**并且将这个点的邻居加入队列**(下一次确定的最短点在前面未确定和这个点邻居中产生),并更新通过`B`点计算各个位置的长度，如果小于则更新！

## 力扣：743.网络延迟时间

### 题目

有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

### Python

```python
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        g = [[float('inf')] * n for _ in range(n)]
        for x, y, time in times:
            g[x-1][y-1] = time
        dist = [float('inf')] * n
        dist[k - 1] = 0
        used = [False] * n
        for _ in range(n):
            x = -1
            for y, u in enumerate(used):
                if not u and (x == -1 or dist[y] < dist[x]):
                    x = y
            used[x] = True
            for y, time in enumerate(g[x]):
                dist[y] = min(dist[y], dist[x] + time)

        ans = max(dist)
        return ans if ans < float('inf') else -1
```

### Java

```java
import java.util.Arrays;

public class NetworkDelayTime743 {
	public int networkDelayTime(int[][] times, int n, int k) {
		// Dijkstra
		// 时间击败97.16%，内存击败11.64%
		// 就是一个比较大的数代表距离无限大不存在通路，同时不会因为做加法运算导致越界变成负数
		final int INF = Integer.MAX_VALUE / 2;
		int[][] g = new int[n][n];
		for (int i=0; i<n; i++) Arrays.fill(g[i], INF);
		for (int[] t: times) {
			int x = t[0] - 1, y = t[1] - 1;
			g[x][y] = t[2];
		}
		int[] dist = new int[n];
		Arrays.fill(dist, INF);
		dist[k-1] = 0;
		boolean[] used = new boolean[n];
		for (int i=0; i<n; i++) {
			int x = -1;
			for (int y=0; y<n; y++) {
				if (!used[y] && (x == -1 || dist[y] < dist[x])) x = y;
			}
			used[x] = true;
			for (int y=0; y<n; y++) dist[y] = Math.min(dist[y], dist[x]+g[x][y]);
		}
		int ans = Arrays.stream(dist).max().getAsInt();
		return ans == INF ? -1 : ans;
    }
}
```







