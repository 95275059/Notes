# MATLABTips14--矩阵函数

### magic

+ 语法

  ```matlab
  M = magic（n）
  ```

  返回由整数1到n ^ 2构成的n乘n矩阵，行和列的和相等。 

  顺序n必须是大于或等于3的标量。

  因为是nXn矩阵，所以矩阵元素从1……n^2全排列。

+ 示例

  ```matlab
  >> magic(3)
  
  ans =
  
       8     1     6
       3     5     7
       4     9     2
  ```

  ```matlab
  >> sum(magic(3))
  
  ans =
  
      15    15    15
  ```

  ```matlab
  >> sum(magic(3),2)
  
  ans =
  
      15
      15
      15
  ```

  