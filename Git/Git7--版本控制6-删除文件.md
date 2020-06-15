# Git7--版本控制6-删除文件

1. 在Git中，删除也是一个修改操作

2. 实例

   + 新建文件test.txt

     查看仓库状态

     ```bash
     $ git status
     On branch master
     Untracked files:
       (use "git add <file>..." to include in what will be committed)
             test.txt
     
     nothing added to commit but untracked files present (use "git add" to track)
     ```

   + 将test.txt提交

     ```bash
     $ git add test.txt
     
     CXY@MSI MINGW64 /e/Git (master)
     $ git commit -m "add test.txt"
     [master d5fe048] add test.txt
      1 file changed, 0 insertions(+), 0 deletions(-)
      create mode 100644 test.txt
     ```

   + 删除工作区中的test.txt文件

   + 查看仓库状态

     ```bash
     $ git status
     On branch master
     Changes not staged for commit:
       (use "git add/rm <file>..." to update what will be committed)
       (use "git restore <file>..." to discard changes in working directory)
             deleted:    test.txt
     
     no changes added to commit (use "git add" and/or "git commit -a")
     ```

   + **从版本库中删除test.txt文件**

     + 方法

       用**git rm**删掉，并且用**git commit**提交

     + 操作

       ```bash
       $ git rm test.txt
       rm 'test.txt'
       
       CXY@MSI MINGW64 /e/Git (master)
       $ git commit -m "remove test.txt"
       [master ac1a81d] remove test.txt
        1 file changed, 0 insertions(+), 0 deletions(-)
        delete mode 100644 test.txt
       ```

       ==先手动删除文件，然后使用git rm和git add效果是一样的==

       ==但是用git rm更符合逻辑，但其实效果一样==

3. 如果手动在工作区中删错了，该怎么办

   版本库中该文件还存在

   + 撤销工作区的修改

     ```bash
     $ git checkout -- test.txt
     ```

   注：从来没有被添加到版本库就被删除的文件，是无法恢复的

4. 注

   如果一个文件已经被提交到版本库，那么永远不用担心误删，但是要小心，你只能恢复文件到最新版本，你会丢失**最近一次提交后你修改的内容**。