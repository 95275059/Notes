# Algorithm11--拓扑排序

https://blog.csdn.net/lisonglisonglisong/article/details/45543451

### 有向无环图

给定一个包含 n 个节点的有向图 G，我们给出它的节点编号的一种排列，如果满足：

对于图 G 中的任意一条有向边 (u,v)，u 在排列中都出现在 v 的前面。

那么称该排列是图 G 的「拓扑排序」。根据上述的定义，我们可以得出两个结论：

* 如果图 *G* 中存在环（即图 G 不是「有向无环图」），那么图 G* 不存在拓扑排序。

* 如果图 *G* 是有向无环图，那么它的拓扑排序可能不止一种。

  举一个最极端的例子，如果图 G*G* 值包含 n*n* 个节点却没有任何边，那么任意一种编号的排列都可以作为拓扑排序。

## 力扣210课程表II

```python
"""
210.课程表II
现在你总共有 n 门课需要选，记为 0 到 n-1。
在选修某些课程之前需要一些先修课程。
例如，想要学习课程 0 ，你需要先完成课程 1 ，我们用一个匹配来表示他们: [0,1]
给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。
可能会有多个正确的顺序，你只要返回一种就可以了。
如果不可能完成所有课程，返回一个空数组。
解题思路：拓扑排序：深度，广度优先
深度优先遍历：
    思路：
        我们可以将深度优先搜索的流程与拓扑排序的求解联系起来，用一个栈来存储所有已经搜索完成的节点。
        对于一个节点 u，如果它的所有相邻节点都已经搜索完成，那么在搜索回溯到 u 的时候，u 本身也会变成一个已经搜索完成的节点。
        这里的「相邻节点」指的是从 u 出发通过一条有向边可以到达的所有节点。
        假设我们当前搜索到了节点 u，如果它的所有相邻节点都已经搜索完成，那么这些节点都已经在栈中了，此时我们就可以把 u 入栈。
        可以发现，如果我们从栈顶往栈底的顺序看，由于 u 处于栈顶的位置，那么 u 出现在所有 u 的相邻节点的前面。
        因此对于 u 这个节点而言，它是满足拓扑排序的要求的。
        这样以来，我们对图进行一遍深度优先搜索。
        当每个节点进行回溯的时候，我们把该节点放入栈中。
        最终从栈顶到栈底的序列就是一种拓扑排序。
    算法：
        对于图中的任意一个节点，它在搜索的过程中有三种状态，即：
            「未搜索」：我们还没有搜索到这个节点；
            「搜索中」：我们搜索过这个节点，但还没有回溯到该节点，即该节点还没有入栈，还有相邻的节点没有搜索完成）；
            「已完成」：我们搜索过并且回溯过这个节点，即该节点已经入栈，并且所有该节点的相邻节点都出现在栈的更底部的位置，满足拓扑排序的要求。
        通过上述的三种状态，我们就可以给出使用深度优先搜索得到拓扑排序的算法流程，在每一轮的搜索搜索开始时，我们任取一个「未搜索」的节点开始进行深度优先搜索。
        我们将当前搜索的节点 u 标记为「搜索中」，遍历该节点的每一个相邻节点 v：
        如果 v 为「未搜索」，那么我们开始搜索 v，待搜索完成回溯到 u；
        如果 v 为「搜索中」，那么我们就找到了图中的一个环，因此是不存在拓扑排序的；
        如果 v 为「已完成」，那么说明 v 已经在栈中了，而 u 还不在栈中，因此 u 无论何时入栈都不会影响到 (u,v) 之前的拓扑关系，以及不用进行任何操作。
        当 u 的所有相邻节点都为「已完成」时，我们将 u 放入栈中，并将其标记为「已完成」。
        在整个深度优先搜索的过程结束后，如果我们没有找到图中的环，那么栈中存储这所有的 n 个节点，从栈顶到栈底的顺序即为一种拓扑排序。
广度优先遍历：
    思路：
        方法一的深度优先搜索是一种「逆向思维」：最先被放入栈中的节点是在拓扑排序中最后面的节点。
        我们也可以使用正向思维，顺序地生成拓扑排序，这种方法也更加直观。
        我们考虑拓扑排序中最前面的节点，该节点一定不会有任何入边，也就是它没有任何的先修课程要求。
        当我们将一个节点加入答案中后，我们就可以移除它的所有出边，代表着它的相邻节点少了一门先修课程的要求。
        如果某个相邻节点变成了「没有任何入边的节点」，那么就代表着这门课可以开始学习了。
        按照这样的流程，我们不断地将没有入边的节点加入答案，直到答案中包含所有的节点（得到了一种拓扑排序）或者不存在没有入边的节点（图中包含环）。
        上面的想法类似于广度优先搜索，因此我们可以将广度优先搜索的流程与拓扑排序的求解联系起来。
    算法：
        我们使用一个队列来进行广度优先搜索。
        开始时，所有入度为 0 的节点都被放入队列中，它们就是可以作为拓扑排序最前面的节点，并且它们之间的相对顺序是无关紧要的。
        在广度优先搜索的每一步中，我们取出队首的节点 u：
        我们将 u 放入答案中；
        我们移除 u 的所有出边，也就是将 u 的所有相邻节点的入度减少 1。
        如果某个相邻节点 v 的入度变为 0，那么我们就将 v 放入队列中。
        在广度优先搜索的过程结束后。
        如果答案中包含了这 n 个节点，那么我们就找到了一种拓扑排序，否则说明图中存在环，也就不存在拓扑排序了。
"""
import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        深度优先遍历
        """
        # 存储有向图
        edges = collections.defaultdict(list)
        # 标记每个节点的状态：0=未搜索，1=搜索中，2=已搜索
        visited = [0]*numCourses
        # 用数组来模拟栈，下标0为栈底，n-1为栈顶
        result = list()
        # 判断有向图是否有环
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            # 将节点标记为搜索中
            visited[u] = 1
            # 搜索其相邻节点
            # 只要发现有环，立刻停止搜索
            for v in edges[u]:
                # 如果未搜索，那么搜索相邻节点
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                # 如果搜索中，说明有环
                elif visited[v] == 1:
                    valid = False
                    return
            # 将节点标记为已完成
            visited[u] = 2
            # 将节点入栈
            result.append(u)

        # 每次挑选一个未搜索的节点，开始进行深度优先搜索
        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)
        if not valid:
            return list()
        # 如果没有环，那么就有拓扑排序
        # 注意下标0为栈底，因此需要将数组反向输出
        return result[::-1]

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        广度优先遍历
        时间击败65.48%，内存击败40.48%
        """
        # 存储有向图
        edges = collections.defaultdict(list)
        # 存储每个节点的入度
        indeg = [0] * numCourses
        # 存储答案
        result = list()

        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1

        # 将所有入度为0的节点放入队列中
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])

        while q:
            # 从队首取出一个节点
            u = q.popleft()
            # 放入答案中
            result.append(u)
            for v in edges[u]:
                indeg[v] -= 1
                # 如果相邻节点v的入度为0，就可以选v对应的课程了
                if indeg[v] == 0:
                    q.append(v)

        if len(result) != numCourses:
            result = ()
        return result
```

## 力扣207课程表

```python
"""
207.课程表
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。
先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
"""
import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        广度优先遍历
        时间击败95.21%，内存击败95.21%
        """
        edges = collections.defaultdict(list)
        indeg = [0]*numCourses
        visited = 0
        for cur, pre in prerequisites:
            edges[pre].append(cur)
            indeg[cur] += 1

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        while q:
            cur = q.popleft()
            visited += 1
            for node in edges[cur]:
                indeg[node] -= 1
                if indeg[node] == 0:
                    q.append(node)
        return visited == numCourses
```

