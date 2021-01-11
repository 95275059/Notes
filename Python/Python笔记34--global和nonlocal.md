# Python笔记34--global和nonlocal

### global

+ 在函数内部使用函数外的变量进行操作

+ 实例

  ```python
  x = 1
  y = 1
  def test():
      x=2
      global y
      y = 2
  test()
  print(x)
  print(y)
  ```

  ```python
  1
  2
  ```

---

### nonlocal

+ 在函数或其他作用域中使用**外层（非全局变量）变量**

+ 实例

  ```python
  def createCounter():
      count = 0
      def counter():
          nonlocal count
          count += 1
          return count
      return counter
  counterA = createCounter()
  print(counterA(), counterA(), counterA(), counterA(), counterA())
  ```

  ```
  1 2 3 4 5
  ```

  