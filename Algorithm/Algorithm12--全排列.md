# Algorithm12--全排列

## 力扣46.全排列

```python
"""
46.全排列
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
解题思路：回溯
回溯法：一种通过探索所有可能的候选解来找出所有的解的算法。
    如果候选解被确认不是一个解（或者至少不是最后一个解），回溯算法会通过在上一步进行一些变化抛弃该解，即回溯并且再次尝试。
这个问题可以看作有 n 个排列成一行的空格，我们需要从左往右依此填入题目给定的 n 个数，每个数只能使用一次。
那么很直接的可以想到一种穷举的算法，即从左往右每一个位置都依此尝试填入一个数，看能不能填完这 n 个空格，在程序中我们可以用「回溯法」来模拟这个过程。
我们定义递归函数 backtrack(first, output) 表示从左往右填到第 first 个位置，当前排列为 output。
那么整个递归函数分为两个情况：
    如果 first==n，说明我们已经填完了 n 个位置（注意下标从 0 开始），找到了一个可行的解，我们将 output 放入答案数组中，递归结束。
    如果 first<n，我们要考虑这第 first 个位置我们要填哪个数。
        根据题目要求我们肯定不能填已经填过的数，因此很容易想到的一个处理手段是我们定义一个标记数组 vis[] 来标记已经填过的数，
        那么在填第 first 个数的时候我们遍历题目给定的 n 个数，如果这个数没有被标记过，我们就尝试填入，并将其标记，继续尝试填下一个位置，即调用函数 backtrack(first + 1, output)。
        回溯的时候要撤销这一个位置填的数以及标记，并继续尝试其他没被标记过的数。
使用标记数组来处理填过的数是一个很直观的思路，但是可不可以去掉这个标记数组呢？
毕竟标记数组也增加了我们算法的空间复杂度。
答案是可以的，我们可以将题目给定的 n 个数的数组 nums 划分成左右两个部分，左边的表示已经填过的数，右边表示待填的数，我们在回溯的时候只要动态维护这个数组即可
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        时间击败45.86%，内存击败24.29%
        """
        def backtrack(first=0):
            if first == n:
                ans.append(nums[:])
            for i in range(first,n):
                # 动态维护数组
                nums[i], nums[first] = nums[first], nums[i]
                # 继续递归填下一个数
                backtrack(first+1)
                # 撤销操作
                nums[i], nums[first] = nums[first], nums[i]
        n = len(nums)
        ans = []
        backtrack()
        return ans
```

## 力扣47.全排列II

```python
"""
47.全排列II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
此题是「46. 全排列」的进阶，序列中包含了重复的数字，要求我们返回不重复的全排列，那么我们依然可以选择使用搜索回溯的方法来做。
我们将这个问题看作有 nn 个排列成一行的空格，我们需要从左往右依次填入题目给定的 n 个数，每个数只能使用一次。
那么很直接的可以想到一种穷举的算法，即从左往右每一个位置都依此尝试填入一个数，看能不能填完这 n 个空格，在程序中我们可以用「回溯法」来模拟这个过程。
我们定义递归函数 backtrack(idx, perm) 表示当前排列为 perm，下一个待填入的位置是第 idx 个位置（下标从 0 开始）。
那么整个递归函数分为两个情况：
    如果 idx==n，说明我们已经填完了 n 个位置，找到了一个可行的解，我们将 perm 放入答案数组中，递归结束。
    如果 idx<n，我们要考虑第 idx 个位置填哪个数。
    根据题目要求我们肯定不能填已经填过的数，因此很容易想到的一个处理手段是我们定义一个标记数组 vis 来标记已经填过的数，
    那么在填第 idx 个数的时候我们遍历题目给定的 n 个数，如果这个数没有被标记过，我们就尝试填入，并将其标记，继续尝试填下一个位置，即调用函数 backtrack(idx + 1, perm)。
    搜索回溯的时候要撤销该个位置填的数以及标记，并继续尝试其他没被标记过的数。
但题目解到这里并没有满足「全排列不重复」 的要求，在上述的递归函数中我们会生成大量重复的排列，因为对于第 idx 的位置，如果存在重复的数字 i，我们每次会将重复的数字都重新填上去并继续尝试导致最后答案的重复，因此我们需要处理这个情况。
要解决重复问题，我们只要设定一个规则，保证在填第 idx 个数的时候重复数字只会被填入一次即可。
而在本题解中，我们选择对原数组排序，保证相同的数字都相邻，然后每次填入的数一定是这个数所在重复数集合中「从左往右第一个未被填过的数字」，即如下的判断条件：
if (i > 0 && nums[i] == nums[i - 1] && !vis[i - 1]) {
    continue;
}
假设我们有 3 个重复数排完序后相邻，那么我们一定保证每次都是拿从左往右第一个未被填过的数字，
即整个数组的状态其实是保证了 [未填入，未填入，未填入] 到 [填入，未填入，未填入]，再到 [填入，填入，未填入]，最后到 [填入，填入，填入] 的过程的，因此可以达到去重的目标。
"""

class Solution(object):
    visited = None
    def permuteUnique(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        时间击败66.63%，内存击败84.50%
        """
        result = list()
        perm = list()
        self.visited = [False] * len(nums)
        nums.sort()
        self.backtrack(nums, result, 0, perm)
        return result

    def backtrack(self, nums, result, index, perm):
        if index == len(nums):
            result.append(perm[:])
        for i in range(0, len(nums)):
            if self.visited[i] or (i > 0 and nums[i] == nums[i-1] and not self.visited[i-1]):
                continue
            perm.append(nums[i])
            self.visited[i] = True
            self.backtrack(nums, result, index+1, perm)
            self.visited[i] = False
            perm.pop()


if __name__ == '__main__':
    nums = [1, 1, 2]
    solution = Solution()
    print(solution.permuteUnique(nums))
```

