# Algorithm6--爬楼梯

## 70.爬楼梯

### 题目

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。

### 解题思路：动态规划，可以通过递归和迭代的方式实现

* 我们用 f(x)表示爬到第 x 级台阶的方案数，考虑最后一步可能跨了一级台阶，也可能跨了两级台阶，所以我们可以列出如下式子：

  f(x) = f(x - 1) + f(x - 2)

* 它意味着爬到第 x 级台阶的方案数是爬到第 x−1 级台阶的方案数和爬到第 x−2 级台阶的方案数的和。
* 很好理解，因为每次只能爬 1 级或 2 级，所以 f(x) 只能从 f(x−1) 和 f(x−2) 转移过来，而这里要统计方案总数，我们就需要对这两项的贡献求和。

### 代码

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        超出时间限制2333，从后往前看
        """
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs1(self, n):
        """
        从前往后看
        """
        if n <= 2:
            return n
        point1 = 1
        point2 = 2
        for i in range(3, n+1):
            temp = point1 + point2
            point1 = point2
            point2 = temp
        return point2
```

## 746.使用最小花费爬楼梯

### 题目

数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。

### 解题思路：动态规划

* 假设数组 cost 的长度为 n，则 n 个阶梯分别对应下标 0 到 n−1，楼层顶部对应下标 n，问题等价于计算达到下标 n 的最小花费。
* 可以通过动态规划求解。
* 创建长度为 n+1 的数组 dp，其中 dp[i] 表示达到下标 i 的最小花费。
* 由于可以选择下标 0 或 1 作为初始阶梯，因此有 dp[0]=dp[1]=0。
* 当 2≤i≤n 时，可以从下标 i−1 使用 cost[i−1] 的花费达到下标 i，或者从下标 i−2 使用 cost[i−2] 的花费达到下标 i。
* 为了使总花费最小，dp[i] 应取上述两项的最小值，因此状态转移方程如下：
* dp[i]=min(dp[i−1]+cost[i−1],dp[i−2]+cost[i−2])
* 依次计算 dp 中的每一项的值，最终得到的 dp[n] 即为达到楼层顶部的最小花费

### 代码

```python
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        上述代码的时间复杂度和空间复杂度都是 O(n)。
        注意到当 i≥2 时，dp[i] 只和 dp[i−1] 与 dp[i−2] 有关，因此可以使用滚动数组的思想，将空间复杂度优化到 O(1)。
        """
        length = len(cost)
        dp = [0]*(length+1)
        for i in range(2, length+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[length]
    def minCostClimbingStairs1(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        时间击败32.45%，内存击败87.52%
        """
        length = len(cost)
        pre, cur = 0, 0
        for i in range(2, length+1):
            next = min(cur+cost[i-1], pre+cost[i-2])
            pre = cur
            cur = next
        return cur
```