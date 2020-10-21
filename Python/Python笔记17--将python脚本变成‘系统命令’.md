# Python笔记17--将python脚本变成‘系统命令’

### 适用场景

使用argparse模块写出来的python脚本，希望像系统命令一样可以在任意目录下直接执行

如使用argparse模块写出VMC.py脚本，希望能在任意目录下直接执行类似 `VMC status SBIRS_geo_01`的命令

### 操作

+ 重命名VMC.py为VMC

+ 从`python VMC status SBIRS_geo_01`变成 `VMC status SBIRS_geo_01`

  + 修改VMC脚本运行权限

    + chmod 755 VMC

  + 在VMC脚本的开头加入注释

    ```bash
    #!/usr/bin/env python
    ```

    或者

    ```bash
    #!/usr/bin/python
    ```

+ 保证文件格式为unix格式

  + vim打开VMC文件

  + ```bash
    :set ff
    ```

    查看文件格式，如果显示fileformat=dos，则需要重新设置文件格式

  + ```bash
    :set ff=unix
    ```

  + ```bash
    :wq
    ```

+ 能使VMC脚本在任意目录下执行

  将脚本放入/usr/bin目录下