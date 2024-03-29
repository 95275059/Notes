# LinuxTips65--modprobe

### 功能

用于自动处理可载入模块

可载入指定的个别模块或是载入一组相依的模块

### 语法

```bash
modprobe [-acdlrtvV][--help][模块文件][符号名称 = 符号值]
```

| 选项              | 说明                           |
| ----------------- | ------------------------------ |
| -a 或 --all       | 载入全部的模块                 |
| -c 或 --show-conf | 显示所有模块的设置信息         |
| -d 或 --debug     | 使用排错模式                   |
| -l 或 --list      | 显示可用的模块                 |
| -r 或 --remove    | 模块闲置不用时，即自动卸载模块 |
| -t 或 --type      | 指定模块类型                   |
| -V 或 --version   | 执行时显示详细的信息           |
| -help             | 显示帮助                       |
| -v 或 --verbose   | 执行时显示详细的信息           |

### 实例

```bash
modporbe tun
```

