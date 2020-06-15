# Git2--版本控制1-版本更新

1. 修改readme.txt文件

   ```
   Git is a distributed version control system.
   Git is free software
   ```

2. git status 命令

   + 查看仓库当前的状态

   ```bash
   $ git status
   On branch master
   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   readme.txt
   
   no changes added to commit (use "git add" and/or "git commit -a")
   
   ```

   可以看到readme.txt已经被修改了，但是没有准备提交的修改

   此时，modified:   readme.txt 为红色

3. git diff 命令

   + git diff 即为 git difference，显示的格式是Unix通用的diff格式
   + 可以查看工作区的文本具体的变化内容

   ```bash
   $ git diff readme.txt
   diff --git a/readme.txt b/readme.txt
   index f0ec47f..ee2c1ea 100644
   --- a/readme.txt
   +++ b/readme.txt
   @@ -1,2 +1,2 @@
   -Git is a version control system.
   +Git is a distributed version control system.
    Git is free software
   \ No newline at end of file
   ```

4. 提交修改

   和提交新文件是一样的步骤

   + 将文件添加到仓库

     ```bash
     $ git add readme.txt
     ```

     ```bash
     $ git status
     On branch master
     Changes to be committed:
       (use "git restore --staged <file>..." to unstage)
             modified:   readme.txt
     ```

     可以看到，将要被提交的修改包括readme.txt

     此时，modified:   readme.txt 为绿色

   + 将文件提交到仓库
   
     ```bash
     $ git commit -m "add distributed to readme.txt"
     [master 29b3de8] add distributed to readme.txt
   1 file changed, 1 insertion(+), 1 deletion(-)
     ```
   
     ```bash
     $ git status
     On branch master
  nothing to commit, working tree clean
     ```

     可以看到当前没有需要提交的修改，工作目录（working tree）是干净的
   
     