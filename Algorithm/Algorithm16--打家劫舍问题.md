# Algorithm16--打家劫舍问题

## Leetcode198.打家劫舍

```python
"""
198.打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
解题思路：动态规划
    首先考虑最简单的情况。如果只有一间房屋，则偷窃该房屋，可以偷窃到最高总金额。
    如果只有两间房屋，则由于两间房屋相邻，不能同时偷窃，只能偷窃其中的一间房屋，因此选择其中金额较高的房屋进行偷窃，可以偷窃到最高总金额。
    如果房屋数量大于两间，应该如何计算能够偷窃到的最高总金额呢？
        对于第 k~(k>2)间房屋，有两个选项：
            偷窃第 k 间房屋，那么就不能偷窃第 k−1 间房屋，偷窃总金额为前 k−2 间房屋的最高总金额与第 k 间房屋的金额之和。
            不偷窃第 k 间房屋，偷窃总金额为前 k−1 间房屋的最高总金额。
        在两个选项中选择偷窃总金额较大的选项，该选项对应的偷窃总金额即为前 k 间房屋能偷窃到的最高总金额。
    用 dp[i] 表示前 i 间房屋能偷窃到的最高总金额，那么就有如下的状态转移方程：
    dp[i]=max(dp[i−2]+nums[i],dp[i−1])
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        时间击败94.51%，内存击败81.26%
        """
        if not nums or not len(nums):
            return 0
        length = len(nums)
        if length == 1:
            return nums[0]
        p1, p2 = max(nums[0], nums[1]), nums[0]
        for k in range(2, length):
            fn = max(p2 + nums[k], p1)
            p2 = p1
            p1 = fn
        return p1
```

## Leetcode213.打家劫舍II

```python
"""
213.打家劫舍II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
解题思路：
    首先考虑最简单的情况。
    如果只有一间房屋，则偷窃该房屋，可以偷窃到最高总金额。
    如果只有两间房屋，则由于两间房屋相邻，不能同时偷窃，只能偷窃其中的一间房屋，因此选择其中金额较高的房屋进行偷窃，可以偷窃到最高总金额。
    注意到当房屋数量不超过两间时，最多只能偷窃一间房屋，因此不需要考虑首尾相连的问题。
    如果房屋数量大于两间，就必须考虑首尾相连的问题，第一间房屋和最后一间房屋不能同时偷窃。
    如何才能保证第一间房屋和最后一间房屋不同时偷窃呢？
        如果偷窃了第一间房屋，则不能偷窃最后一间房屋，因此偷窃房屋的范围是第一间房屋到最后第二间房屋；
        如果偷窃了最后一间房屋，则不能偷窃第一间房屋，因此偷窃房屋的范围是第二间房屋到最后一间房屋。
    假设数组 nums 的长度为 n。
    如果不偷窃最后一间房屋，则偷窃房屋的下标范围是 [0,n−2]；
    如果不偷窃第一间房屋，则偷窃房屋的下标范围是 [1,n−1]。
    在确定偷窃房屋的下标范围之后，即可用第 198 题的方法解决。
    对于两段下标范围分别计算可以偷窃到的最高总金额，其中的最大值即为在 n 间房屋中可以偷窃到的最高总金额。
    假设偷窃房屋的下标范围是 [start,end]，用 dp[i] 表示在下标范围 [start,i] 内可以偷窃到的最高总金额，那么就有如下的状态转移方程：
    dp[i]=max(dp[i−2]+nums[i],dp[i−1])
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        时间击败39.10%，内存击败14.05%
        """
        def robrange(start, end):
            first, second = nums[start], max(nums[start], nums[start+1])
            for i in range(start+2, end+1):
                first, second = second, max(first + nums[i], second)
            return second

        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        else:
            return max(robrange(0, n-2), robrange(1, n-1))
```

## Leetcode337.打家劫舍III

```python
"""
337.打家劫舍III
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。
这个地区只有一个入口，我们称之为“根”。
除了“根”之外，每栋房子有且只有一个“父“房子与之相连。
一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。
如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。
计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
解题思路：动态规划
    简化一下这个问题：一棵二叉树，树上的每个点都有对应的权值，每个点有两种状态（选中和不选中），问在不能同时选中有父子关系的点的情况下，能选中的点的最大权值和是多少。
    我们可以用 f(o) 表示选择 o 节点的情况下，o 节点的子树上被选择的节点的最大权值和；
    g(o) 表示不选择 o 节点的情况下，o 节点的子树上被选择的节点的最大权值和；
    l 和 r 代表 o 的左右孩子。
    当 o 被选中时，o 的左右孩子都不能被选中，故 o 被选中情况下子树上被选中点的最大权值和为 l 和 r 不被选中的最大权值和相加，
        即 f(o)=g(l)+g(r)。
    当 o 不被选中时，o 的左右孩子可以被选中，也可以不被选中。
        对于 o 的某个具体的孩子 x，它对 o 的贡献是 x 被选中和不被选中情况下权值和的较大值。
            故 g(o)=max{f(l),g(l)}+max{f(r),g(r)}。
    至此，我们可以用哈希表来存 f 和 g 的函数值，用深度优先搜索的办法后序遍历这棵二叉树，我们就可以得到每一个节点的 f 和 g。
    根节点的 f 和 g 的最大值就是我们要找的答案。
"""
class Solution(object):
    f = dict()
    g = dict()

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        时间击败6.71%，内存击败5.13%
        """
        self.dfs(root)
        f_root = self.f[root] if root in self.f else 0
        g_root = self.g[root] if root in self.g else 0
        return max(f_root, g_root)


    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.dfs(node.right)
        g_left = self.g[node.left] if node.left in self.g else 0
        f_left = self.f[node.left] if node.left in self.f else 0
        g_right = self.g[node.right] if node.right in self.g else 0
        f_right = self.f[node.right] if node.right in self.f else 0
        self.f[node] = node.val + g_left + g_right
        self.g[node] = max(g_left, f_left) + max(g_right, f_right)

    def rob1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        时间击败70.81%，内存击败83.43%
        假设二叉树的节点个数为 n。
        我们可以看出，以上的算法对二叉树做了一次后序遍历，时间复杂度是 O(n)；
        由于递归会使用到栈空间，空间代价是 O(n)，哈希表的空间代价也是 O(n)，故空间复杂度也是 O(n)。
        我们可以做一个小小的优化，我们发现无论是 f(o) 还是 g(o)，他们最终的值只和 f(l)、g(l)、f(r)、g(r) 有关，
        所以对于每个节点，我们只关心它的孩子节点们的 f 和 g 是多少。
        我们可以设计一个结构，表示某个节点的 f 和 g 值，在每次递归返回的时候，都把这个点对应的 f 和 g 返回给上一级调用，这样可以省去哈希表的空间。
        """
        rootstatus = self.dfs1(root)
        return max(rootstatus)

    def dfs1(self, node):
        if not node:
            return [0, 0]
        l = self.dfs1(node.left)
        r = self.dfs1(node.right)
        selected = node.val + l[1] + r[1]
        notselected = max(l) + max(r)
        return [selected, notselected]
```

