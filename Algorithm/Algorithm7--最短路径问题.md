# Algorithm7--最短路径问题

## floyd算法

## dijkstra算法

### 算法原理：贪心

### 743.网络延迟时间

* 准备
  * 一个临街矩阵，存储有向图的拓扑
  * 一个距离数组，存储到各个节点的最短距离
  * 一个状态数组，存储各个节点是否已经找到最短距离
* 思路
  * N个节点，循环N次
  * 每次循环找到未确定最短距离节点集合中距离最短的一个节点，并将该节点放入确定组
  * 然后更新距离数组

```python
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        g = [[float('inf')*n for _ in range(n)]]
        for src, dst, value in times:
            g[src-1][dst-1] = value
        dst = [float('inf')] * n
        used = [False] * n
        dst[k-1] = 0
        for _ in range(n):
            x = -1
            for index, state in enumerate(used):
                if not state and (x==-1 or dst[y] < dst[x]):
                    x = y
            used[x] = True
            for index, value in g[x]:
                dst[index] = min(dst[index], dst[x]+value)
        result = max(dst)
        return result if result < float('inf') else -1
```

## bellman ford算法

