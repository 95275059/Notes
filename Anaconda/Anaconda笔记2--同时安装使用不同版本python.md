# Anaconda笔记2--同时安装使用不同版本python

## 需求

已安装python 3.7.0,anaconda 3.5.3.1,conda 4.5.11

需要安装python 3.6环境

## 具体步骤

### 创建python3.6环境

```sh
(base) C:\Users\CXY>conda create --name python36 python=3.6
```

### 激活python3.6环境

```shell
(base) C:\Users\CXY>conda activate python36

(python36) C:\Users\CXY>
```

### 安装并打开Spyder IDE(如果需要的话)

```sh
conda install spyder
```

```shell
spyder
```

### 退出python3.6

```shell
deactivate
```

### 创建项目

https://www.pianshen.com/article/5112941084/