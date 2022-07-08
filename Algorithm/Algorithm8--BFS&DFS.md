# Algorithm8--BFS&DFS

## BFS

* 广度优先搜索，从根节点开始，辐射状搜索节点，一层一层的探索。
* DFS：递归+回溯实现，数据结构是栈；

### 二叉树的层序遍历

```python
"""
使用队列十分重要，如果使用 Listc的话，我们删除元素需要 O(n) 的时间复杂度。而队列删除元素只需要 O(1) 的时间。
"""
import TreeNode
import collections



class Solution(object):
    def levelOrderTraversal(self, root):
        result= list()
        if not root:
            return result
        toVisit = collections.deque([root])
        while toVisit:
            size = len(toVisit)
            curline = list()
            for _ in range(size):
                curnode = toVisit.popleft()
                curline.append(curnode.val)
                if curnode.left:
                    toVisit.append(curnode.left)
                if curnode.right:
                    toVisit.append(curnode.right)
            result.append(curline)
        return result
```

### 力扣102.二叉树的层序遍历

```python
"""
102.二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
解题思路：广度优先搜索
"""
import TreeNode
import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        广度优先搜索
        时间击败68.98%，内存击败45.80%
        """
        if not root:
            return []
        result = list()
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            curline = list()
            for i in range(size):
                curnode = queue.popleft()
                curline.append(curnode.val)
                if curnode.left:
                    queue.append(curnode.left)
                if curnode.right:
                    queue.append(curnode.right)
            result.append(curline)
        return result
```

### 力扣429.N叉树的层序遍历

```python
"""
429.ncha-shu-de-ceng-xu-bian-li-by-leetcode
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
"""
import Node
import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        时间击败85.17%，内存击败99.04%
        """
        result = list()
        if not root:
            return result
        toVisit = collections.deque([root])
        while toVisit:
            size = len(toVisit)
            curline = list()
            for _ in range(size):
                curnode = toVisit.popleft()
                curline.append(curnode.val)
                toVisit.extend(curnode.children)
            result.append(curline)
        return result
```

### 力扣107. 二叉树的层序遍历 II

```python
"""
107. 二叉树的层序遍历 II
给定一个二叉树，返回其节点值自底向上的层序遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
"""
import TreeNode
import collections


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        时间击败37.72%，内存击败66.67%
        """
        result = list()
        if not root:
            return result
        toVisit = collections.deque([root])
        while toVisit:
            size = len(toVisit)
            curline = list()
            for _ in range(size):
                curnode = toVisit.popleft()
                curline.append(curnode.val)
                if curnode.left:
                    toVisit.append(curnode.left)
                if curnode.right:
                    toVisit.append(curnode.right)
            result.append(curline)
        return result[::-1]
```

## DFS

* 深度优先搜索，从根节点开始，探索整个图，走到底然后再回溯；
* 以树的遍历为例，前序/中序/后序搜索都是深度优先，层序遍历时广度优先搜索。
* 但是DFS和BFS都是搜索树和图的算法。
* DFS：递归+回溯实现，数据结构是栈；
* 剪枝
  * 最优化剪枝：如果当前步骤已经可以确定不是最优结果（与已有结果比较），则可以直接剪掉
  * 可行性剪枝：如果当前结果已经可以确定不符合要求，则可以直接剪掉

### 前序遍历

* https://segmentfault.com/a/1190000016674584
* 前序遍历是三种遍历顺序中最简单的一种，因为`根`节点是最先访问的，而我们在访问一个树的时候最先遇到的就是根节点。
* 对应力扣144.binary-tree-preorder-traversal
* N叉树前序遍历：力扣589.ncha-shu-de-qian-xu-bian-li-by-leetcode
* 应用场景：
  * 实现目录结构的显示。

```python
import TreeNode


class Solution(object):

    def preorderTraversal(self, root):
        # 递归实现
        result = list()
        self.preOrderHelper(root, result)
        return result

    def preOrderHelper(self, root, result):
        if not root:
            return
        result.append(root.val)
        self.preOrderHelper(root.left, result)
        self.preOrderHelper(root.right, result)

    def preorderTraversal1(self, root):
        # 迭代实现
        # 使用栈来实现。
        # 由于出栈顺序和入栈顺序相反，所以每次添加节点的时候先添加右节点，再添加左节点。
        # 这样在下一轮访问子树的时候，就会先访问左子树，再访问右子树
        result = list()
        if not root:
            return result
        toVisit = list()
        toVisit.append(root)
        while toVisit:
            curnode = toVisit.pop()
            result.append(curnode.val)
            if curnode.right:
                toVisit.append(curnode.right)
            if curnode.left:
                toVisit.append(curnode.left)
        return result

```

### 中序遍历

* 中序遍历相对前序遍历要复杂一点，因为我们说过，在二叉树的访问中，最先遇到的是根节点，但是在中序遍历中，最先访问的不是根节点，而是左节点。（当然，这里说复杂是针对非递归方法而言的，递归方法都是很简单的。）
* 对应力扣94.binary-tree-inorder-traversal
* 应用场景
  * 做表达式树，在编译器底层实现的时候用户可以实现基本的加减乘除，比如 a*b+c。

```python
import TreeNode


class Solution(object):
    def inOrderTraversal(self, root):
        # 递归实现
        result = list()
        self.inOrderHelper(root, result)
        return result

    def inOrderHelper(self, root, result):
        if not root:
            return
        self.inOrderHelper(root.left, result)
        result.append(root.val)
        self.inOrderHelper(root.right, result)

    def inOrderTraversal1(self, root):
        # 迭代实现
        # 中序遍历的迭代法要稍微复杂一点，因为最先遇到的根节点不是最先访问的
        # 我们需要先访问左子树，再回退到根节点，再访问根节点的右子树
        # 这里的一个难点是从左子树回退到根节点的操作
        # 虽然可以用栈来实现回退，但是要注意在出栈时保存根节点的引用，因为我们还需要通过根节点来访问右子树
        result = list()
        toVisit = list()
        curnode = root
        while curnode or toVisit:
            while curnode:
                toVisit.append(curnode)
                curnode = curnode.left
            curnode = toVisit.pop()
            result.append(curnode.val)
            curnode = curnode.right
        return result
```

### 后序遍历

* 后序遍历是三种遍历方法中最难的
* 与中序遍历相比，虽然都是先访问左子树，但是在回退到根节点的时候，后序遍历不会立即访问根节点，而是先访问根节点的右子树，这里要小心的处理入栈出栈的顺序。（当然，这里说复杂是针对非递归方法而言的，递归方法都是很简单的。
* 对应力扣145.binary-tree-postorder-traversal
* N叉树中序遍历：力扣590.n-ary-tree-postorder-traversal
* 应用场景
  * 实现计算目录内的文件占用的数据大小
  * 对节点操作时必访问过其子节点
  * 适合进行破坏性操作（删除节点）

```python
class Solution:
    def postOrderTraversal(self, root):
        result = list()
        self.postOrderHelper(root, result)
        return result

    def postOrderHelper(self, root, result):
        if not root:
            return
        self.postOrderHelper(root.left, result)
        self.postOrderHelper(root.right, result)
        result.append(root.val)

    def postOrderTraversal1(self, root):
        # 迭代实现
        result, toVisit = list(), list()
        curnode = root
        pre = None
        while curnode or toVisit:
            while curnode:
                toVisit.append(curnode) # 添加根节点
                curnode = curnode.left # 递归添加左节点
            curnode = toVisit[-1] # 已经访问到最左的节点
            # 在不存在右节点或者右节点已经访问过的情况下，访问根节点
            if not curnode.right or curnode.right == pre:
                toVisit.pop()
                result.append(curnode.val)
                pre = curnode
                curnode = None
            # 右节点还没有访问过
            else:
                curnode = curnode.right
        return result
```

### 模板

```python
int MAXN=0;
int dx[4]={1,-1,0,0};
int dy[4]={0,0,1,-1};
bool can_move(int x,int y)
{
    if(...)       //越界情况
      return false;
    if(...)       //非法情况
      return false;
    return true;
}
 
 void dfs(int x,int y,int ans)
 {
     if(x==ex&&y=ey)
     {
         MAXN=max(MAXN,ans);
     }
     visit[x][y]=1;
     for(int i=0;i<4;i++)
     {
        int tx=x+dx[i];
        int ty=y+dy[i];
        if(can_move(tx,ty))
            dfs(tx,ty,ans+1);
     }
     visit[x][y]=0;
     return;
 }
```

### 单词搜索

```python
"""
79.单词搜索
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
进阶：你可以使用搜索剪枝的技术来优化解决方案，使其在 board 更大的情况下可以更快解决问题？
解题思路：回溯
设函数 check(i,j,k) 表示判断以网格的 (i,j) 位置出发，能否搜索到单词 word[k..]，
其中 word[k..] 表示字符串 word 从第 k 个字符开始的后缀子串。
如果能搜索到，则返回 true，反之返回 false。
函数 check(i,j,k) 的执行步骤如下：
    如果 board[i][j]!=s[k]，当前字符不匹配，直接返回 false。
    如果当前已经访问到字符串的末尾，且对应字符依然匹配，此时直接返回 true。
    否则，遍历当前位置的所有相邻位置。
        如果从某个相邻位置出发，能够搜索到子串 word[k+1..]，则返回 true，否则返回 false。
这样，我们对每一个位置 (i,j) 都调用函数 check(i,j,0) 进行检查：
    只要有一处返回 true，就说明网格中能够找到相应的单词，否则说明不能找到。
为了防止重复遍历相同的位置，需要额外维护一个与 board 等大的 visited 数组，用于标识每个位置是否被访问过。
每次遍历相邻位置时，需要跳过已经被访问的位置。
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        时间击败43.66%，内存击败12.89%
        """
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        def check(i, j, k):
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i,j))
            result = False
            for di, dj in directions:
                newi, newj = i+di, j+dj
                if 0 <= newi < h and 0 <= newj < w:
                    if (newi, newj) not in visited:
                        if check(newi, newj, k+1):
                            result = True
                            break
            visited.remove((i,j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True
        return False
```

### 分割回文串

### 硬币兑换

### 100 Same Tree

### 98 Validate Binary Search Tree

### 114 Flatten Binary Tree to Linked List

### 113 Path Sum II

### 473 Matchsticks to Square

### 200 Number Of Islands

### 472 Concatenated Words
