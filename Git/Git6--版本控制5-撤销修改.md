# Git6--版本控制5-撤销修改

==修改后未添加到暂存区==

1. 在readme.txt中添加一行

   ```
   Git is a distributed version control system.
   Git is free software distributed under the GPL.
   Git has a mutable index called stage.
   Git tracks changes of files.
   My stupid boss still prefers SVN.
   ```

2. 查看仓库状态

   ```bash
   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   readme.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   ```

3. **丢弃工作区的修改**

   **git checkout -- file**

   ```bash
   $ git checkout -- readme.txt
   ```

   + 该命令把readme.txt文件在工作区的修改全部撤销，这里有两种情况

     + readme.txt自修改后还没有被放到暂存区，现在，撤销修改就回到和版本库一模一样的状态
     + reame.txt已经添加到暂存区，又作了修改，现在，撤销修改就是回到添加到暂存区后的状态

     总之，就是让这个文件回到最近一次git commit或git add时的状态

4. 查看readme.txt内容

   ```
   Git is a distributed version control system.
   Git is free software distributed under the GPL.
   Git has a mutable index called stage.
   Git tracks changes.
   ```

---

---

---

==修改后已经添加到暂存区==

1. 修改readme.txt文件

   ```
   Git is a distributed version control system.
   Git is free software distributed under the GPL.
   Git has a mutable index called stage.
   Git tracks changes.
   My stupid boss still prefers SVN.
   ```

2. 将readme.txt添加到暂存区

   ```bash
   git add readme.txt
   ```

3. 查看仓库状态

   ```bash
   $ git status
   On branch master
   Changes to be committed:
     (use "git restore --staged <file>..." to unstage)
           modified:   readme.txt
   ```

   可以看到，修改只是添加到了暂存区，但是还没有被提交

4. **把暂存区的修改撤销掉，重新放回工作区**

   + **git reset HEAD filename**

     该命令可以把暂存区的修改撤销掉（unstage），重新放回工作区

   + 撤销暂存区的对readme.txt的修改

     ```bash
     $ git reset HEAD readme.txt
     Unstaged changes after reset:
     M       readme.txt
     ```

   + 查看仓库状态

     ```bash
     $ git status
     On branch master
     Changes not staged for commit:
       (use "git add <file>..." to update what will be committed)
       (use "git restore <file>..." to discard changes in working directory)
             modified:   readme.txt
     
     no changes added to commit (use "git add" and/or "git commit -a")
     ```

     可以看到，现在暂存区是干净的，而工作区有修改

5. 丢弃工作区的修改

   ```bash
   $ git checkout -- readme.txt
   ```

   

