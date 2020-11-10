# GitTips4--远程分支创建与同步

### 创建本地分支

```bash
git checkout -b monitor
```

直接创建monitor分支并转到该monitor分支

```bash
CXY@DESKTOP-FU9B4Q1 MINGW64 /e/Gitlab/md (master)
$ git checkout -b monitor
Switched to a new branch 'monitor'
```

### 在当前分支提交

```bash
git add --all
git commit -m "remarks"
```

### 创建远程分支

在远程仓库下新建同名monitor分支

### 将本地分支push到远程分支

```bash
git push origin monitor:monitor
```

b



