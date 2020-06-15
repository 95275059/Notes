# Git3--版本控制2-版本回退

1. 再修改一次readme.txt

   ```
   Git is a distributed version control system.
   Git is free software distributed under the GPL.
   ```

2. 提交readme.txt

   ```bash
   CXY@MSI MINGW64 /e/Git (master)
   $ git add readme.txt
   
   CXY@MSI MINGW64 /e/Git (master)
   $ git commit -m "appen GPL to readme.txt"
   [master 0e39e83] appen GPL to readme.txt
    1 file changed, 1 insertion(+), 1 deletion(-)
   
   ```

3. ==到目前为止，readme.txt共有3个版本==

   + wrote a readme file 

     ```
     Git is a version control system.
     Git is free software
     ```

   + add distributed to readme.txt

     ```
     Git is a distributed version control system.
     Git is free software
     ```

   + append GPL to readme.txt

     ```
     Git is a distributed version control system.
     Git is free software distributed under the GPL.
     ```

4. git log 命令

   + 可以查看历史**提交记录**

     该命令显示从最近到最远的提交日志

   ```bash
   $ git log
   commit 0e39e8398d29b12ea0ee0a3039a59ec597a4b60a (HEAD -> master)
   Author: 95275059 <1227837302@qq.com>
   Date:   Tue Dec 17 20:08:45 2019 +0800
   
       appen GPL to readme.txt
   
   commit 29b3de8ce1cdf287fe46d1c9b4b7412188e9aa33
   Author: 95275059 <1227837302@qq.com>
   Date:   Tue Dec 17 19:56:16 2019 +0800
   
       add distributed to readme.txt
   
   commit 4a23546dd154bceae3a63a75065b42c3313e2719
   Author: 95275059 <1227837302@qq.com>
   Date:   Tue Dec 17 14:58:14 2019 +0800
   
       wrote a readme file
   ```

   + git log --pretty=oneline

     只显示版本号和提交说明

     ```bash
     $ git log --pretty=oneline
     0e39e8398d29b12ea0ee0a3039a59ec597a4b60a (HEAD -> master) appen GPL to readme.txt
     29b3de8ce1cdf287fe46d1c9b4b7412188e9aa33 add distributed to readme.txt
     4a23546dd154bceae3a63a75065b42c3313e2719 wrote a readme file
     ```

     + HEAD代表当前版本，即最新提交的版本

       上一个版本是HEAD^

       上上个版本是HEAD^^

       往上100个版本是HEAD~100

     + 版本号(commit id)

       + 就是上面的：

         0e39e8398d29b12ea0ee0a3039a59ec597a4b60a

         29b3de8ce1cdf287fe46d1c9b4b7412188e9aa33

         4a23546dd154bceae3a63a75065b42c3313e2719

       + 命名规则

         SHA1计算出来的非常大的数字，用十六进制表示

         ==避免版本冲突，后面 会详细解释==

     + 每提交一个版本，Git会把它们自动串成一条时间线。

5. 版本回退

   + 把当前版本（append GPL to readme.txt）回退到上一个版本（add distributed to readme.txt）

     **git reset --hard commit_id** 

     ```bash
     git reset --soft 19462f6f46cf4cbc211d366359afac0c17a7c190
     // 注意 --hard 参数会抛弃当前工作区的修改
     // 使用 --soft 参数的话会回退到之前的版本，但是保留当前工作区的修改，可以重新提交
     ```

     ```bash
     $ git reset --hard HEAD^
     HEAD is now at 29b3de8 add distributed to readme.txt
     ```

     此时打开readme.txt已经是上一个版本了

   + 查看版本库状态

     ```bash
     $ git log
     commit 29b3de8ce1cdf287fe46d1c9b4b7412188e9aa33 (HEAD -> master)
     Author: 95275059 <1227837302@qq.com>
     Date:   Tue Dec 17 19:56:16 2019 +0800
     
         add distributed to readme.txt
     
     commit 4a23546dd154bceae3a63a75065b42c3313e2719
     Author: 95275059 <1227837302@qq.com>
     Date:   Tue Dec 17 14:58:14 2019 +0800
     
         wrote a readme file
     ```

     第三个版本（append GPL to readme.txt）已经看不到了

     + 但是如果想要还原第三个版本，只要命令行窗口还没有被关掉，可以往回翻命令行，找到第三个版本的commit id，然后制定回到这（未来的）第三个版本

       ```bash
       $ git reset --hard 0e39e8398
       HEAD is now at 0e39e83 appen GPL to readme.txt
       ```

       + 版本号没必要写全，写前几位就可以了，Git会自动去找。

       + 但是也不能只写前一两位，因为Git可能会找到多个版本号，就没有办法确定是哪个了。

       此时打开readme.txt，已经变成第三个版本了

     + 如果想要还原第三个版本，但是命令行窗口已经关闭甚至电脑关过机了，还是可以补救的

       + git reflog

         查看命令历史

         ```bash
         $ git reflog
         0e39e83 (HEAD -> master) HEAD@{0}: reset: moving to 0e39e8398
         29b3de8 HEAD@{1}: reset: moving to HEAD^
         0e39e83 (HEAD -> master) HEAD@{2}: commit: appen GPL to readme.txt
         29b3de8 HEAD@{3}: commit: add distributed to readme.txt
         4a23546 HEAD@{4}: commit (initial): wrote a readme file
         ```

6. 版本回退原理

   在Git内部有一个指向当前版本的HEAD指针

   当回退版本的时候，Git仅仅把HEAD从指向append GPL

   ![3.2-1](.\3.2-1.png)

   改为指向add distributed:

   ![3.2-2](.\3.2-2.png)

   顺便更新工作区的文件

   