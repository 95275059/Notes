# GitTips4--gitpush文件过大报错

## 报错:remote: error: GH001: Large files detected

```bash
$ git push origin master
Logon failed, use ctrl+c to cancel basic credential prompt.
Enumerating objects: 140, done.
Counting objects: 100% (140/140), done.
Delta compression using up to 12 threads
Compressing objects: 100% (97/97), done.
Writing objects: 100% (97/97), 13.13 MiB | 279.00 KiB/s, done.
Total 97 (delta 64), reused 0 (delta 0)
remote: Resolving deltas: 100% (64/64), completed with 37 local objects.
remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com.
remote: error: Trace: 9c0f8df8de413eccb40fe25cc2959f57dfd1ce075c8ae3e563c3b44521396a55
remote: error: See http://git.io/iEPt8g for more information.
remote: error: File log/link_generator.log is 101.12 MB; this exceeds GitHub's file size limit of 100.00 MB
To https://github.com/95275059/CMD-SGIN-EP.git
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'https://github.com/95275059/CMD-SGIN-EP.git'
```

## 解决

回退到没添加大文件的那次commit记录

## 操作

+ ```
  git log
  ```

  查看提交记录

+ ```
  git reset ***
  ```

  回退