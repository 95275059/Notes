## LaTexTips1--度数

1. 方法一

   ```
   ^{\circ}
   ```

2. 方法二

   + 添加定义

     ```
     \def\degree{${}^{\circ}$}
     ```

   + 使用

     ```
     45\degree
     ```

3. 方法三

   + 添加包

     ```
     \usepackage{gensymb}
     ```

   + 使用

     ```
     45\degree
     ```

4. 方法四

   + 添加包

     ```
     \usepackage{textcomp}
     ```

   + 使用

     ```
     45\textdegree
     ```

---

+ 度数后每空格

  添加空格"\ "

  ```
  45\degree\ in turn
  ```

  