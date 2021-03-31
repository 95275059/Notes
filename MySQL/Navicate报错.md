# Navicate报错

## 内存越界

![Navicate报错-1](Navicate报错-1.png)

### 原因

这是**内存越界**的问题，需要**重新注册Windows的动态链接库**。

### 解决

**运行 -> cmd**，然后在命令行中输入：**for %1 in (%windir%\system32\*.dll) do regsvr32.exe /s %1** ，最后**回车运行**