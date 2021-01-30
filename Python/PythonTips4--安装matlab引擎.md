# PythonTips4--安装matlab引擎

## 参考网址

https://ww2.mathworks.cn/help/matlab/matlab_external/install-the-matlab-engine-for-python.html

https://ww2.mathworks.cn/help/matlab/matlab_external/get-started-with-matlab-engine-for-python.html

https://zhuanlan.zhihu.com/p/94377688

## 版本匹配需求

https://www.mathworks.com/content/dam/mathworks/mathworks-dot-com/support/sysreq/files/python-compatibility.pdf

## 安装步骤

### 安装环境

+ Python3.6 in Anaconda3
+ Matlab2018b

### 以管理员身份打开Anaconda Prompt并切换到python3.6

```bash
conda activate python36
```

+ 注意：必须以管理员身份打开Anaconda Prompt，否则会出现如下错误

  ```bash
  (python36) C:\Program Files\MATLAB\R2018b\extern\engines\python>python setup.py install
  running install
  running build
  running build_py
  error: You do not have write permission in build\lib\matlab\engine\
  ```

  或者

  ```bash
  (python36) C:\Program Files\MATLAB\R2018b\extern\engines\python>python setup.py install
  running install
  running build
  running build_py
  error: could not create 'build': 拒绝访问。
  ```

### 获取matlab安装文件夹的完整路径

在matlab命令行窗口输入`matlabroot`

### 在Anaconda Prompt中切换路径

```bash
cd matlabroot\extern\engines\python
```

### 执行setup.py脚本

```bash
python setup.py install
```

