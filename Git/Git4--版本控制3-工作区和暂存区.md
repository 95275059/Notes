# Git4--版本控制3-工作区和暂存区

1. 工作区（Working Directiory）

   电脑里能看到的目录(E:/Git)

2. 版本库（Repository）

   工作区的隐藏目录：E:/Git/.git

   + stage(index)：暂存区
   + master：Git自动创建的第一个分支
   + HEAD：指向master的一个指针

   ![4.3-1](E:\Notes\Git\4.3-1.png)

3. 修改readme.txt文件并新增LICENSE

   + readme.txt

     ```
     Git is a distributed version control system.
     Git is free software distributed under the GPL.
     Git has a mutable index called stage.
     ```

   + LICENSE

     ```
     LICENSE FILE
     ```

4. 查看仓库状态

   ```bash
   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   readme.txt
   
   Untracked files:
     (use "git add <file>..." to include in what will be committed)
           LICENSE
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```

   可以看到，readme.txt被修改了，LICENSE没有被添加过（状态为Untracked）

   此时， LICENSE 为红色

5. 将readme.txt和LICENSE添加到暂存区

   ```bash
   CXY@MSI MINGW64 /e/Git (master)
   $ git add readme.txt
   
   CXY@MSI MINGW64 /e/Git (master)
   $ git add LICENSE
   ```

6. 查看仓库状态

   ```bash
   $ git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           new file:   LICENSE
           modified:   readme.txt
   ```

   此时暂存区状态：

   ![4.3-2](E:\Notes\Git\4.3-2.png)

   **即：git add命令实际上就是把要提交的所有修改放到暂存区（stage），然后执行git commit命令就可以一次性把暂存区的所有修改提交到分支**

   此时 new file:   LICENSE 和 modified:   readme.txt 为绿色

7. 提交修改

   ```
   $ git commit -m "understand how stage works"
   [master cdf591e] understand how stage works
    2 files changed, 2 insertions(+)
    create mode 100644 LICENSE
   ```

8. 查看仓库状态

   ```bash
   $ git status
   On branch master
   nothing to commit, working tree clean
   ```

   此时工作区（working tree）是干净的了

   此时版本库的状态为：

   ![4.3-3](.\4.3-3.png)

