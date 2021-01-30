# Anaconda笔记3--命令

## help

```bash
(python36) C:\Users\CXY>conda --help
usage: conda [-h] [-V] command ...

conda is a tool for managing and deploying applications, environments and packages.

Options:

positional arguments:
  command
    clean        Remove unused packages and caches.
    config       Modify configuration values in .condarc. This is modeled
                 after the git config command. Writes to the user .condarc
                 file (C:\Users\CXY\.condarc) by default.
    create       Create a new conda environment from a list of specified
                 packages.
    help         Displays a list of available conda commands and their help
                 strings.
    info         Display information about current conda install.
    install      Installs a list of packages into a specified conda
                 environment.
    list         List linked packages in a conda environment.
    package      Low-level conda package utility. (EXPERIMENTAL)
    remove       Remove a list of packages from a specified conda environment.
    uninstall    Alias for conda remove. See conda remove --help.
    search       Search for packages and display associated information. The
                 input is a MatchSpec, a query language for conda packages.
                 See examples below.
    update       Updates conda packages to the latest compatible version. This
                 command accepts a list of package names and updates them to
                 the latest versions that are compatible with all other
                 packages in the environment. Conda attempts to install the
                 newest versions of the requested packages. To accomplish
                 this, it may update some packages that are already installed,
                 or install additional packages. To prevent existing packages
                 from updating, use the --no-update-deps option. This may
                 force conda to install older versions of the requested
                 packages, and it does not prevent additional dependency
                 packages from being installed. If you wish to skip dependency
                 checking altogether, use the '--force' option. This may
                 result in an environment with incompatible packages, so this
                 option must be used with great caution.
    upgrade      Alias for conda update. See conda update --help.

optional arguments:
  -h, --help     Show this help message and exit.
  -V, --version  Show the conda version number and exit.

conda commands available from other packages:
  build
  convert
  develop
  env
  index
  inspect
  metapackage
  render
  server
  skeleton

(python36) C:\Users\CXY>
```

## conda install

Installs a list of packages into a specified conda environment.

```bash
conda install matplotlib
```

## conda remove

Remove a list of packages from a specified conda environment.

```bash
conda remove matplotlib
```

## conda update

Updates conda packages to the latest compatible version.

```bash
conda update matplotlib 
```

## conda list

List linked packages in a conda environment.

```bash
conda list
```

## conda create

Create a new conda environment from a list of specified packages.

```bash
conda create --name python36 python=3.6
```

## conda activate

进入环境

```bash
conda activate python36
```

离开环境

```bash
deactivate
```

## conda env

+ 列出所有已创建的环境

  ```bash
  conda env list
  ```

  当前安静旁边会有一个星号

  默认环境（即在不选定环境时使用的环境）名为base

+ 删除环境

  ```bash
  conda env remove --name python36
  ```

## conda config

+ 显示通道地址

  ```bash
  conda config --show channels
  ```

+ 添加通道

  ```bash
  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  ```

+ 删除通道

  ```bash
  conda config --remove channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  ```

+ 清除索引缓存

  ```bash
  conda clean -i
  ```

+ 设置从channels中安装包时显示channel的url

  ```bash
  conda config --set show_channel_urls yes
  ```

  

