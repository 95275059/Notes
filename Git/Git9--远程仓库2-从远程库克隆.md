# Git9--远程仓库2-从远程库克隆及上传代码

1. 创建远程仓库

   Name : Git_Study

   Description : A repository for private Git Study

   Initialize this repository with a README

2. 从远程库中克隆

   + **git clone git@github.com:95275059/Git_Study.git**

   + **git clone https://github.com/95275059/Git_Study.git**

     https除了速度慢以外，还有一个麻烦就是每次推送都必须输入口令

   + 操作

     ```bash
     $ git clone git@github.com:95275059/Git_Study.git
     Cloning into 'Git_Study'...
     The authenticity of host 'github.com (13.229.188.59)' can't be established.
     RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
     Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
     Warning: Permanently added 'github.com,13.229.188.59' (RSA) to the list of known hosts.
     remote: Enumerating objects: 3, done.
     remote: Counting objects: 100% (3/3), done.
     remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
     Receiving objects: 100% (3/3), done.
     ```

   + **注：新生成秘钥的时候。第一次git clone 或者git push会出现以下错误**

     The authenticity of host 'github.com (13.229.188.59)' can't be established.

     这个时候在Are you sure you want to continue connecting输入yes即可

     不要直接回车

     原因是，少了一个known_hosts文件

3. 上传代码

   + 将需要上传的代码提交到本地版本库

     ```bash
     $ git add readme.txt
     ```

     ```bash
     $ git commit -m "commit readme.txt"
     [master f6a477b] commit readme.txt
      1 file changed, 4 insertions(+)
      create mode 100644 readme.txt
     ```

   + 将本地版本库内容提交到远程GitHub中

     **git push origin master**

     ```bash
     $ git push origin master
     Enumerating objects: 4, done.
     Counting objects: 100% (4/4), done.
     Delta compression using up to 8 threads
     Compressing objects: 100% (3/3), done.
     Writing objects: 100% (3/3), 379 bytes | 379.00 KiB/s, done.
     Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
     To https://github.com/95275059/Git_Study.git
        fb98a1f..f6a477b  master -> master
     ```

4. 拉取代码

   ```bash
   $ git pull
   ```

   









