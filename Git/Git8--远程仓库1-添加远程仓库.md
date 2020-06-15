# Git8--远程仓库1-添加远程仓库

1. 创建SSH KEY

   + 由于本地Git仓库和Github仓库之间的传输是通过SSH加密的，因此需要设置SSH KEY

   + GitHub需要识别出你推送的提交确实是本人推送的，而不是别人冒充的，而Git支持SSH 协议，所以，GitHub只要知道了你的公钥，就可以确认只有你自己才能推送

   + GitHub允许添加多个Key

     如果有多台电脑，把每台电脑的Key都添加到GitHub上，就可以在每台电脑上往GitHub推送了

   + 在用户主目录（C:\Users\CXY）下，如果没有.ssh目录，或者.ssh目录下没有id_rsa和id_rsa.pub这两个文件，则需要先创建SSH KEY

   + 方法

     + ssh-keygen -t rsa -C "1227837302@qq.com"

     + 操作

       ```bash
       $ ssh-keygen -t rsa -C "1227837302@qq.com"
       Generating public/private rsa key pair.
       Enter file in which to save the key (/c/Users/CXY/.ssh/id_rsa):
       Created directory '/c/Users/CXY/.ssh'.
       Enter passphrase (empty for no passphrase):
       Enter same passphrase again:
       Your identification has been saved in /c/Users/CXY/.ssh/id_rsa.
       Your public key has been saved in /c/Users/CXY/.ssh/id_rsa.pub.
       The key fingerprint is:
       SHA256:GynDdzZ7dsKvb1iEzjWGVr6YrcgBlsENopyux96TqH0 1227837302@qq.com
       The key's randomart image is:
       +---[RSA 3072]----+
       |      ...o       |
       |   . o .o .   .  |
       |    +    o   =   |
       |   . .  +.  + *  |
       |    . +.S.++ B o |
       |   o   + =.+= +  |
       |  . o. ....o=+.  |
       |   +..E   ooo+.  |
       |  ..o...    .+o  |
       +----[SHA256]-----+
       ```

       一路回车，使用默认值就可以了

       由于这个KEY也不是用于私密性的工作，所以也不用设置密码

   + id_rsa和id_rsa.pub

     id_rsa是私钥，不能泄露出去

     id_rsa.pub是公钥，可以给别人

2. 登录GitHub,新建SSH Key

   + Settings--SSH and GPG keys--New SSH key

   + Title

     任意填

   + Key

     把id_rsa.pub文件中的内容贴进去

