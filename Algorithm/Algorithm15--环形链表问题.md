# Algorithm15--环形链表问题

## 问题大概

判断一个链表是否有环，

进阶：要求空间复杂度在O(1)

变形：返回入环的第一个节点

## 力扣141：环形链表

```python
"""
141.环形链表
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。
进阶：你能用 O(1)（即，常量）内存解决此问题吗？
"""
import ListNode

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        哈希表
        时间击败78.12%，内存击败12.87%
        """
        map = set()
        while head:
            if head in map:
                return True
            else:
                map.add(head)
            head = head.next
        return False

    def hasCycle1(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        快慢指针
        利用了Floyd 判圈算法，又称龟兔赛跑算法
            假想「乌龟」和「兔子」在链表上移动，「兔子」跑得快，「乌龟」跑得慢。
            当「乌龟」和「兔子」从链表上的同一个节点开始移动时，如果该链表中没有环，那么「兔子」将一直处于「乌龟」的前方；
            如果该链表中有环，那么「兔子」会先于「乌龟」进入环，并且一直在环内移动。
            等到「乌龟」进入环时，由于「兔子」的速度快，它一定会在某个时刻与乌龟相遇，即套了「乌龟」若干圈。
        具体地，我们定义两个指针，一快一慢。
        慢指针每次只移动一步，而快指针每次移动两步。
        初始时，慢指针在位置 head，而快指针在位置 head.next。
        这样一来，如果在移动的过程中，快指针反过来追上慢指针，就说明该链表为环形链表。否则快指针将到达链表尾部，该链表不为环形链表。
        为什么我们要规定初始时慢指针在位置 head，快指针在位置 head.next，而不是两个指针都在位置 head（即与「乌龟」和「兔子」中的叙述相同）？
            1.观察下面的代码，我们使用的是 while 循环，循环条件先于循环体。
            由于循环条件一定是判断快慢指针是否重合，如果我们将两个指针初始都置于 head，那么 while 循环就不会执行。
            2.当然，我们也可以使用 do-while 循环。
            此时，我们就可以把快慢指针的初始值都置为 head。
        时间击败60.77%，内存击败42.25%
        """
        if not head or not head.next:
            return False
        fast, slow = head.next, head
        while fast != slow:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
```

## 力扣142：环形链表II

```python
"""
142.环形链表II
给定一个链表，返回链表开始入环的第一个节点。 
如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。
进阶：你是否可以使用 O(1) 空间解决此题？
解题思路：快慢指针
我们使用两个指针，fast 与 slow。它们起始都位于链表的头部。
随后，slow 指针每次向后移动一个位置，而 fast 指针向后移动两个位置。
如果链表中存在环，则 fast 指针最终将再次与 slow 指针在环中相遇。
设链表中环外部分的长度为 a。slow 指针进入环后，又走了 b 的距离与 fast 相遇。slow没有走过的环的长度为c,即环长为b+c
此时，fast 指针已经走完了环的 n 圈，因此它走过的总距离为 a+n(b+c)+b=a+(n+1)b+nc。
根据题意，任意时刻，fast 指针走过的距离都为 slow 指针的 2 倍。
因此，我们有a+(n+1)b+nc=2(a+b)
a+(n+1)b+nc=2(a+b)⟹a=c+(n−1)(b+c)
有了 a=c+(n-1)(b+c)a=c+(n−1)(b+c) 的等量关系，我们会发现：从相遇点到入环点的距离加上 n−1 圈的环长，恰好等于从链表头部到入环点的距离。
因此，当发现 slow 与 fast 相遇时，我们再额外使用一个指针 ptr。起始，它指向链表头部；随后，它和 slow 每次向后移动一个位置。最终，它们会在入环点相遇。
"""
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        哈希表，无法满足进阶要求
        时间击败67.57%，内存击败13.55%
        """
        map = set()
        while head:
            if head not in map:
                map.add(head)
                head = head.next
            else:
                return head
        return None

    def detectCycle2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        快慢指针
        时间击败67.57%，内存击败66.39%
        """
        if not head:
            return None
        slow, fast = head, head
        while fast != None:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return None
            if fast == slow:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None
```

