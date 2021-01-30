# Anaconda笔记1--安装使用

## 安装

### 参考网址

https://blog.csdn.net/weixin_43715458/article/details/100096496

### 清华源

https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/

## 更换镜像源

### 参考网址

https://blog.csdn.net/ada0915/article/details/78529877

https://cloud.tencent.com/developer/article/1572996

### 清华镜像源

https://mirror.tuna.tsinghua.edu.cn/help/anaconda/

### 具体步骤

+ 根据清华镜像源网址提供的default_channels网址，添加镜像源

  ```shell
  (base) C:\Users\CXY>conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  (base) C:\Users\CXY>conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  (base) C:\Users\CXY>conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
  (base) C:\Users\CXY>conda config --set show_channel_urls yes
  (base) C:\Users\CXY>conda config --show channels
  channels:
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
    - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    - defaults
  ```

+ 删除defaults

  + 进入目录C:\Users\CXY

  + 备份.andarc为.andarc.bak

    ```shell
    ssl_verify: true
    channels:
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
      - defaults
    show_channel_urls: true
    ```

  + 创建新的.andarc文件，删掉defaults

    ```shell
    ssl_verify: true
    channels:
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    show_channel_urls: true
    ```

  + 确认

    ```shell
    (base) C:\Users\CXY>conda config --show channels
    channels:
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
      - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
    ```

  + 清楚索引缓存

    ```shell
    (base) C:\Users\CXY>conda clean -i
    ```

## 使用

### 基础使用

https://www.jianshu.com/p/62f155eb6ac5

https://www.jianshu.com/p/026a2c43b081

https://www.cnblogs.com/WangYiqiang/p/12257671.html



### 

