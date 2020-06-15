# Git5--版本控制4-管理修改

1. **Git跟踪并管理的是修改，而不是文件**

2. 实例验证

   + 为readme.txt添加一行

     ```
     Git is a distributed version control system.
     Git is free software distributed under the GPL.
     Git has a mutable index called stage.
     Git tracks changes.
     ```

   + 添加

     ```bash
     $ git add readme.txt
     
     $ git status
     On branch master
     Changes to be committed:
       (use "git restore --staged <file>..." to unstage)
             modified:   readme.txt
     
     ```

   + 再修改readme.txt

     ```
     Git is a distributed version control system.
     Git is free software distributed under the GPL.
     Git has a mutable index called stage.
     Git tracks changes of files.
     ```

   + 提交

     ```bash
     $ git commit -m "git tracks changes"
     [master 9101989] git tracks changes
      1 file changed, 2 insertions(+), 1 deletion(-)
     ```

     ```bash
     $ git status
     On branch master
     Changes not staged for commit:
       (use "git add <file>..." to update what will be committed)
       (use "git restore <file>..." to discard changes in working directory)
             modified:   readme.txt
     ```

     可以看到，第二次的修改并没有被提交

     也就是说，Git跟踪管理的是修改，而不是文件

   + 查看工作区中的文件和版本库中最新版本的区别

     **git diff HEAD -- readme.txt**

     ```bash
     $ git diff HEAD -- readme.txt
     diff --git a/readme.txt b/readme.txt
     index db28b2c..9a8b341 100644
     --- a/readme.txt
     +++ b/readme.txt
     @@ -1,4 +1,4 @@
      Git is a distributed version control system.
      Git is free software distributed under the GPL.
      Git has a mutable index called stage.
     -Git tracks changes.
     \ No newline at end of file
     +Git tracks changes of files.
     \ No newline at end of file
     ```

     

   

   

   