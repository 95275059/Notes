# Algorithm9--反转问题

## 反转字符串

### 力扣344.反转字符串

```python
"""
344.反转字符串
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        时间击败12.78%，内存击败15.17%
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
```

### 力扣541.反转字符串 II

```python
"""
541.反转字符串 II
给定一个字符串 s 和一个整数 k，从字符串开头算起，每 2k 个字符反转前 k 个字符。
如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        时间击败90.24%，内存击败57.80%
        """
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i: i + k] = reversed(t[i: i + k])
        return "".join(t)
```

## 反转链表

### 力扣206.翻转链表

```python
"""
206.翻转链表
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
解题思路：栈；双链表
"""
import ListNode
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        栈
        时间击败43.69%，内存击败71.38%
        """
        if not head:
            return head
        stack = list()
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next
        newhead = stack.pop()
        cur = newhead
        while stack:
            cur.next = stack.pop()
            cur = cur.next
        cur.next = None
        return newhead

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        迭代，双链表
        双链表求解是把原链表的结点一个个摘掉，每次摘掉的链表都让他成为新的链表的头结点，然后更新新链表。
        时间击败96.12%，内存击败63.76%
        """
        if not head or not head.next:
            return head
        newhead = None
        while head:
            curnode = head
            head = head.next
            curnode.next = newhead
            newhead = curnode
        return newhead

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        递归
        递归版本稍微复杂一些，其关键在于反向工作。假设链表的其余部分已经被反转，现在应该如何反转它前面的部分？
        若从节点 n_k+1到 n_m已经被反转，而我们正处于 n_k我们希望 n_{k+1}的下一个节点指向 n_kn
        所以，n_k.next.next=n_k
        时间击败96.12%，内存击败63.76%
        """
        if not head or not head.next:
            return head
        newhead = self.reversList2(head.next)
        head.next.next = head
        head.next = None
        return newhead
```

### 力扣92. 反转链表 II

```python
"""
92. 反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
"""
import ListNode


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        迭代，双链表
        时间击败80.68%，内存击败43.03%
        """
        if not head or not head.next or left == right:
            return head
        index = 1
        newhead, curnode, pre = head, head, None
        while curnode:
            if index < left:
                pre = curnode
                curnode = curnode.next
                index += 1
            if index == left:
                if pre:
                    pre.next = self.reverse(curnode, right-left+1)
                else:
                    newhead = self.reverse(curnode, right-left+1)
                break
        return newhead

    def reverse(self, head, length):
        if not head or not head.next:
            return head
        index = 0
        newhead, endnode = None, head
        while index < length:
            curnode = head
            head = head.next
            curnode.next = newhead
            newhead = curnode
            index += 1
        endnode.next = head
        return newhead
```

