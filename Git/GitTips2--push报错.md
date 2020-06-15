# GitTips2--push报错

1. **报错 : fatal: The remote end hung up unexpectedly**

   + 原因：推送文件过大或者网不好

   + 解决

     + 方法一：修改提交缓存大小为500M，或者更大

       + 方法一

         ```bash
         $ git config --global http.postBuffer 524288000
         ```

         ```bash
         $ git config --global http.postBuffer 1048576000 
         ```

       + 方法二

         在克隆/创建版本库生成的.git目录下面修改生成的config文件，增加

         ```
         [http]  
         postBuffer = 524288000
         ```

         然后重新推送

     + 方法二：配置git的最低速度和最低速度时间(单位 秒)

       ```bash
       git config --global http.lowSpeedLimit 0
       git config --global http.lowSpeedTime 999999  
       ```

     + 方法三：网速太慢，换网

     

