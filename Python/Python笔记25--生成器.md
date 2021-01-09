# Python笔记25--生成器

### 描述

+ 通过列表生成式，可以直接创建一个列表。
+ 但是，受到内存限制，列表容量肯定是有限的。
+ 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
+ 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
+ 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

### 创建Generator

+ 方法一：只要把一个列表生成式的`[]`改成`()`，就创建了一个generator

  ```python
  L = [x*x for x in range(0,10)]
  print(L)
G = (x*x for x in range(10))
  print(G)
  print(next(G))
  print(next(G))
  print('#'*10)
  for n in G:
      print(n)
  ```
  
  ```python
  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  <generator object <genexpr> at 0x00000192F25A6948>
  0
  1
  ##########
  4
  9
  16
  25
  36
  49
  64
  81
  ```
  
  + 获取生成器的元素：使用next()函数
  + generator保存的是算法，每次调用`next(G)`，就计算出`G`的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出`StopIteration`的错误。
  + 获取生成器的元素一般用for循环，因为生成器也是可迭代对象，同时并且不需要关心`StopIteration`的错误。
  
+ 方法二：使用函数实现

  如果推算的算法比较复杂，用类似列表生成式的`for`循环无法实现的时候，还可以用函数来实现。

  + 斐波拉契函数

    ```python
    def fib(max):
        n, a, b = 0, 0, 1
        while n<max:
            print(b)
            a ,b = b, a + b
            n = n + 1
        return 'Done'
    print(fib(6))
    ```

    ```
    1
    1
    2
    3
    5
    8
    Done
    ```
    + 注意赋值语句：

      ```python
      a, b = b, a + b
      ```

      相当于

      ```python
      t = (b, a + b)
      a = t[0]
      b = t[1]
      ```

      但不必显式写出临时变量t就可以赋值。

  + 仔细观察，可以看出，`fib`函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

  + 也就是说，上面的函数和generator仅一步之遥。

  + **要把`fib`函数变成generator，只需要把`print(b)`改为`yield b`就可以了**：

    ```python
    def fib(max):
        n, a, b = 0, 0, 1
        while n<max:
            yield b
            a ,b = b, a + b
            n = n + 1
        return 'Done'
    
    print(fib)
    t = fib(6)
    print(t)
    print(next(t))
    print(next(t))
    print("#"*10)
    for i in t:
        print(i)
    ```

    ```python
    <function fib at 0x000001B091DC4B88>
    <generator object fib at 0x000001B091D46A48>
    1
    1
    ##########
    2
    3
    5
    8
    ```

    如果一个函数定义中包含`yield`关键字，那么这个函数就不再是一个普通函数，而是一个generator：

  + 这里，最难理解的就是generator和函数的执行流程不一样。

    函数是顺序执行，遇到`return`语句或者最后一行函数语句就返回。

    **而变成generator的函数，在每次调用`next()`的时候执行，遇到`yield`语句返回，再次执行时从上次返回的`yield`语句处继续执行。**

  + 但是用`for`循环调用generator时，发现拿不到generator的`return`语句的返回值。

  + 如果想要拿到返回值，必须捕获`StopIteration`错误，返回值包含在`StopIteration`的`value`中：

    ```python
    def fib(max):
        n, a, b = 0, 0, 1
        while n<max:
            yield b
            a ,b = b, a + b
            n = n + 1
        return 'Done'
    
    print(fib)
    t = fib(6)
    print(t)
    while True:
        try:
            x = next(t)
            print('G:', x)
        except StopIteration as e:
            print('Generator return value:', e.value)
            break
    ```

    ```python
    <function fib at 0x000001F54FCA4B88>
    <generator object fib at 0x000001F54FC26A48>
    G: 1
    G: 1
    G: 2
    G: 3
    G: 5
    G: 8
    Generator return value: Done
    ```

    + 使用for循环，并不会捕捉到StopIteration异常

### 生成杨辉三角

+ 杨辉三角

  ```python
            1
           / \
          1   1
         / \ / \
        1   2   1
       / \ / \ / \
      1   3   3   1
     / \ / \ / \ / \
    1   4   6   4   1
   / \ / \ / \ / \ / \
  1   5   10  10  5   1
  ```

+ 输出格式

  ```
  # 期待输出:
  # [1]
  # [1, 1]
  # [1, 2, 1]
  # [1, 3, 3, 1]
  # [1, 4, 6, 4, 1]
  # [1, 5, 10, 10, 5, 1]
  # [1, 6, 15, 20, 15, 6, 1]
  # [1, 7, 21, 35, 35, 21, 7, 1]
  # [1, 8, 28, 56, 70, 56, 28, 8, 1]
  # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
  ```

+ 思路：把每一行看做一个list，试写一个generator，不断输出下一行的list

+ 实现（自己）

  ```python
  def yh(max):
      num = 1
      last_li = []
      while num <= max:
          if num == 1:
              li = [1]
              last_li = li
              yield li
          else:
              li = [last_li[0]]
              for i in range(1,num-1):
                  li.append(last_li[i-1] + last_li[i])
              li.append(last_li[num-2])
              last_li = li
              yield li
          num += 1
      return 'Done'
  t = yh(10)
  for i in t:
      print(i)
  ```

+ 实现（其他）

  ```python
  def yh(max):
      l = [1]
      while:
          yield l
          l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
  ```

+ 实现（其他）

  ```python
  def triangles():
      n = 1
      a = []
      while True:
          a2 = [1 if x==0 or x == n-1 else a[x-1]+a[x] for x in range(0,n) ]
          n += 1
          a = a2
          yield a
  ```













