# GitTips1--add报错

1. **报错​ : warning:LF will be replaced by CRLF in ...**

   ```bash
   $ git add .
   warning: LF will be replaced by CRLF in Linux/Linux绗旇10--鏉冮檺绠＄悊鍛戒护2.md.
   The file will have its original line endings in your working directory
   ```

   + 原因

     Windows中的换行符为CRLF，而在Linux下的换行符为LF

     工作区的文件都应该用CRLF来换行

     如果改动文件时引入了LF，提交改动时，Git会警告哪些不是纯CRLF文件，但Git不会擅自修改工作区的那些文件，而是对暂存区进行修改。

     因此，当进行git add操作时，只要Git发现改动的内容里有LF换行符，就会出现这个警告

   + 解决：不进行自动转换

     ```bash
     $ git config --global core.autocrlf false
     ```

   