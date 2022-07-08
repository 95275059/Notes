# Algorithm17--第K大、小问题

## Leetcode703.数据流中的第K大元素

```python
"""
703.数据流中的第K大元素
设计一个找到数据流中第 k 大元素的类（class）。
注意是排序后的第 k 大元素，不是第 k 个不同的元素。
请实现 KthLargest 类：
KthLargest(int k, int[] nums) 使用整数 k 和整数流 nums 初始化对象。
int add(int val) 将 val 插入数据流 nums 后，返回当前数据流中第 k 大的元素。
解题思路：优先队列
我们可以使用一个大小为 k 的优先队列来存储前 k 大的元素，其中优先队列的队头为队列中最小的元素，也就是第 k 大的元素。
在单次插入的操作中，我们首先将元素 val 加入到优先队列中。
如果此时优先队列的大小大于 k，我们需要将优先队列的队头元素弹出，以保证优先队列的大小为 k。
"""
import heapq
class KthLargest(object):
    # 时间击败30.00%，内存击败58.18%
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = list()
        self.k = k
        i = 0
        while i < len(nums):
            heapq.heappush(self.heap, nums[i])
            if i >= self.k:
                heapq.heappop(self.heap)
            i += 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.heap, val)
        n = len(self.heap)
        if n > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]



# Your KthLargest object will be instantiated and called as such:
obj = KthLargest(3, [4, 5, 8, 2])
param_1 = obj.add(3)
print(param_1)
```

## JZOffer40.最小的K个数

```python
"""
JZOffer40.最小的K个数
输入整数数组 arr ，找出其中最小的 k 个数。
例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
解题思路：堆
我们用一个大根堆实时维护数组的前 k 小值。
首先将前 k 个数插入大根堆中，
随后从第 k+1 个数开始遍历，如果当前遍历到的数比大根堆的堆顶的数要小，就把堆顶的数弹出，再插入当前遍历到的数。
最后将大根堆里的数存入数组返回即可。
在下面的代码中，由于 C++ 语言中的堆（即优先队列）为大根堆，我们可以这么做。
而 Python 语言中的堆为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前 k 小值。
"""
import heapq


class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        时间击败74.71%，内存击败26.07%
        """
        if k == 0:
            return list()
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -hp[0] > arr[i]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        ans = [-x for x in hp]
        return ans
```

