# DockerTips2--ubuntu镜像更换apt-get源

### 参考网址

https://zhuanlan.zhihu.com/p/86371599

https://www.cnblogs.com/wangyao2174/p/7174863.html

### 通过Dockerfile添加

```bash
RUN  sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
RUN  apt-get clean
```

+ 实操

  + vim /root/Dockerfile/Dockerfile

    ```bash
    FROM ubuntu
    RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
    RUN apt-get clean
    RUN apt-get update
    RUN apt-get install -y vim
    ```

  + 构建镜像

    ```bash
    root@ubuntu16:~/Dockerfile# docker build -t ubuntu-with-vim-dockerfile .
    Sending build context to Docker daemon  2.048kB
    Step 1/5 : FROM ubuntu
     ---> d70eaf7277ea
    Step 2/5 : RUN sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
     ---> Running in 4269bb30a305
    Removing intermediate container 4269bb30a305
     ---> c62c71526782
    Step 3/5 : RUN apt-get clean
     ---> Running in d2d175effe11
    Removing intermediate container d2d175effe11
     ---> 2488a8b485f6
    Step 4/5 : RUN apt-get update
     ---> Running in 172438e34cec
    Get:1 http://mirrors.aliyun.com/ubuntu focal InRelease [265 kB]
    Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [107 kB]
    Get:3 http://mirrors.aliyun.com/ubuntu focal-updates InRelease [111 kB]
    Get:4 http://mirrors.aliyun.com/ubuntu focal-backports InRelease [98.3 kB]
    Get:5 http://mirrors.aliyun.com/ubuntu focal/restricted amd64 Packages [33.4 kB]
    Get:6 http://mirrors.aliyun.com/ubuntu focal/main amd64 Packages [1275 kB]
    Get:7 http://mirrors.aliyun.com/ubuntu focal/multiverse amd64 Packages [177 kB]
    Get:8 http://mirrors.aliyun.com/ubuntu focal/universe amd64 Packages [11.3 MB]
    Get:9 http://mirrors.aliyun.com/ubuntu focal-updates/restricted amd64 Packages [126 kB]
    Get:10 http://mirrors.aliyun.com/ubuntu focal-updates/main amd64 Packages [849 kB]
    Get:11 http://mirrors.aliyun.com/ubuntu focal-updates/multiverse amd64 Packages [30.5 kB]
    Get:12 http://mirrors.aliyun.com/ubuntu focal-updates/universe amd64 Packages [865 kB]
    Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [107 kB]
    Get:13 http://mirrors.aliyun.com/ubuntu focal-backports/universe amd64 Packages [4277 B]
    Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [107 kB]
    Get:14 http://security.ubuntu.com/ubuntu focal-security/multiverse amd64 Packages [1165 B]
    Get:15 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [89.4 kB]
    Get:15 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [89.4 kB]
    Get:15 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [89.4 kB]
    Get:15 http://security.ubuntu.com/ubuntu focal-security/restricted amd64 Packages [89.4 kB]
    Get:16 http://security.ubuntu.com/ubuntu focal-security/universe amd64 Packages [643 kB]
    Get:17 http://security.ubuntu.com/ubuntu focal-security/main amd64 Packages [465 kB]
    Fetched 16.3 MB in 5min 14s (52.0 kB/s)
    Reading package lists...
    Removing intermediate container 172438e34cec
     ---> 80a0540d7c67
    Step 5/5 : RUN apt-get install -y vim
     ---> Running in 48b3c3d7d863
    Reading package lists...
    Building dependency tree...
    Reading state information...
    The following additional packages will be installed:
      alsa-topology-conf alsa-ucm-conf file libasound2 libasound2-data
      libcanberra0 libexpat1 libgpm2 libltdl7 libmagic-mgc libmagic1 libmpdec2
      libogg0 libpython3.8 libpython3.8-minimal libpython3.8-stdlib libreadline8
      libsqlite3-0 libssl1.1 libtdb1 libvorbis0a libvorbisfile3 mime-support
      readline-common sound-theme-freedesktop vim-common vim-runtime xxd xz-utils
    Suggested packages:
      libasound2-plugins alsa-utils libcanberra-gtk0 libcanberra-pulse gpm
      readline-doc ctags vim-doc vim-scripts
    The following NEW packages will be installed:
      alsa-topology-conf alsa-ucm-conf file libasound2 libasound2-data
      libcanberra0 libexpat1 libgpm2 libltdl7 libmagic-mgc libmagic1 libmpdec2
      libogg0 libpython3.8 libpython3.8-minimal libpython3.8-stdlib libreadline8
      libsqlite3-0 libssl1.1 libtdb1 libvorbis0a libvorbisfile3 mime-support
      readline-common sound-theme-freedesktop vim vim-common vim-runtime xxd
      xz-utils
    0 upgraded, 30 newly installed, 0 to remove and 4 not upgraded.
    Need to get 14.9 MB of archives.
    After this operation, 70.5 MB of additional disk space will be used.
    Get:1 http://mirrors.aliyun.com/ubuntu focal/main amd64 libmagic-mgc amd64 1:5.38-4 [218 kB]
    Get:2 http://mirrors.aliyun.com/ubuntu focal/main amd64 libmagic1 amd64 1:5.38-4 [75.9 kB]
    Get:3 http://mirrors.aliyun.com/ubuntu focal/main amd64 file amd64 1:5.38-4 [23.3 kB]
    Get:4 http://mirrors.aliyun.com/ubuntu focal/main amd64 libexpat1 amd64 2.2.9-1build1 [73.3 kB]
    Get:5 http://mirrors.aliyun.com/ubuntu focal/main amd64 libmpdec2 amd64 2.4.2-3 [81.1 kB]
    Get:6 http://mirrors.aliyun.com/ubuntu focal/main amd64 libssl1.1 amd64 1.1.1f-1ubuntu2 [1318 kB]
    Get:7 http://mirrors.aliyun.com/ubuntu focal-updates/main amd64 libpython3.8-minimal amd64 3.8.5-1~20.04 [714 kB]
    Get:8 http://mirrors.aliyun.com/ubuntu focal/main amd64 mime-support all 3.64ubuntu1 [30.6 kB]
    Get:9 http://mirrors.aliyun.com/ubuntu focal/main amd64 readline-common all 8.0-4 [53.5 kB]
    Get:10 http://mirrors.aliyun.com/ubuntu focal/main amd64 libreadline8 amd64 8.0-4 [131 kB]
    Get:11 http://mirrors.aliyun.com/ubuntu focal-updates/main amd64 libsqlite3-0 amd64 3.31.1-4ubuntu0.2 [549 kB]
    Get:12 http://mirrors.aliyun.com/ubuntu focal-updates/main amd64 libpython3.8-stdlib amd64 3.8.5-1~20.04 [1671 kB]
    Get:13 http://mirrors.aliyun.com/ubuntu focal/main amd64 xxd amd64 2:8.1.2269-1ubuntu5 [50.1 kB]
    Get:14 http://mirrors.aliyun.com/ubuntu focal/main amd64 vim-common all 2:8.1.2269-1ubuntu5 [85.1 kB]
    Get:15 http://mirrors.aliyun.com/ubuntu focal-updates/main amd64 xz-utils amd64 5.2.4-1ubuntu1 [82.5 kB]
    Get:16 http://mirrors.aliyun.com/ubuntu focal/main amd64 alsa-topology-conf all 1.2.2-1 [7364 B]
    Get:17 http://mirrors.aliyun.com/ubuntu focal-updates/main amd64 alsa-ucm-conf all 1.2.2-1ubuntu0.4 [25.4 kB]
    Get:18 http://mirrors.aliyun.com/ubuntu focal-updates/main amd64 libasound2-data all 1.2.2-2.1ubuntu2.1 [20.1 kB]
    Get:19 http://mirrors.aliyun.com/ubuntu focal-updates/main amd64 libasound2 amd64 1.2.2-2.1ubuntu2.1 [335 kB]
    Get:20 http://mirrors.aliyun.com/ubuntu focal/main amd64 libltdl7 amd64 2.4.6-14 [38.5 kB]
    Get:21 http://mirrors.aliyun.com/ubuntu focal/main amd64 libtdb1 amd64 1.4.2-3build1 [44.1 kB]
    Get:22 http://mirrors.aliyun.com/ubuntu focal/main amd64 libogg0 amd64 1.3.4-0ubuntu1 [24.0 kB]
    Get:23 http://mirrors.aliyun.com/ubuntu focal/main amd64 libvorbis0a amd64 1.3.6-2ubuntu1 [87.0 kB]
    Get:24 http://mirrors.aliyun.com/ubuntu focal/main amd64 libvorbisfile3 amd64 1.3.6-2ubuntu1 [16.1 kB]
    Get:25 http://mirrors.aliyun.com/ubuntu focal/main amd64 sound-theme-freedesktop all 0.8-2ubuntu1 [384 kB]
    Get:26 http://mirrors.aliyun.com/ubuntu focal/main amd64 libcanberra0 amd64 0.30-7ubuntu1 [38.1 kB]
    Get:27 http://mirrors.aliyun.com/ubuntu focal/main amd64 libgpm2 amd64 1.20.7-5 [15.1 kB]
    Get:28 http://mirrors.aliyun.com/ubuntu focal-updates/main amd64 libpython3.8 amd64 3.8.5-1~20.04 [1624 kB]
    Get:29 http://mirrors.aliyun.com/ubuntu focal/main amd64 vim-runtime all 2:8.1.2269-1ubuntu5 [5873 kB]
    Get:30 http://mirrors.aliyun.com/ubuntu focal/main amd64 vim amd64 2:8.1.2269-1ubuntu5 [1238 kB]
    debconf: delaying package configuration, since apt-utils is not installed
    Fetched 14.9 MB in 45s (333 kB/s)
    Selecting previously unselected package libmagic-mgc.
    (Reading database ... 4121 files and directories currently installed.)
    Preparing to unpack .../00-libmagic-mgc_1%3a5.38-4_amd64.deb ...
    Unpacking libmagic-mgc (1:5.38-4) ...
    Selecting previously unselected package libmagic1:amd64.
    Preparing to unpack .../01-libmagic1_1%3a5.38-4_amd64.deb ...
    Unpacking libmagic1:amd64 (1:5.38-4) ...
    Selecting previously unselected package file.
    Preparing to unpack .../02-file_1%3a5.38-4_amd64.deb ...
    Unpacking file (1:5.38-4) ...
    Selecting previously unselected package libexpat1:amd64.
    Preparing to unpack .../03-libexpat1_2.2.9-1build1_amd64.deb ...
    Unpacking libexpat1:amd64 (2.2.9-1build1) ...
    Selecting previously unselected package libmpdec2:amd64.
    Preparing to unpack .../04-libmpdec2_2.4.2-3_amd64.deb ...
    Unpacking libmpdec2:amd64 (2.4.2-3) ...
    Selecting previously unselected package libssl1.1:amd64.
    Preparing to unpack .../05-libssl1.1_1.1.1f-1ubuntu2_amd64.deb ...
    Unpacking libssl1.1:amd64 (1.1.1f-1ubuntu2) ...
    Selecting previously unselected package libpython3.8-minimal:amd64.
    Preparing to unpack .../06-libpython3.8-minimal_3.8.5-1~20.04_amd64.deb ...
    Unpacking libpython3.8-minimal:amd64 (3.8.5-1~20.04) ...
    Selecting previously unselected package mime-support.
    Preparing to unpack .../07-mime-support_3.64ubuntu1_all.deb ...
    Unpacking mime-support (3.64ubuntu1) ...
    Selecting previously unselected package readline-common.
    Preparing to unpack .../08-readline-common_8.0-4_all.deb ...
    Unpacking readline-common (8.0-4) ...
    Selecting previously unselected package libreadline8:amd64.
    Preparing to unpack .../09-libreadline8_8.0-4_amd64.deb ...
    Unpacking libreadline8:amd64 (8.0-4) ...
    Selecting previously unselected package libsqlite3-0:amd64.
    Preparing to unpack .../10-libsqlite3-0_3.31.1-4ubuntu0.2_amd64.deb ...
    Unpacking libsqlite3-0:amd64 (3.31.1-4ubuntu0.2) ...
    Selecting previously unselected package libpython3.8-stdlib:amd64.
    Preparing to unpack .../11-libpython3.8-stdlib_3.8.5-1~20.04_amd64.deb ...
    Unpacking libpython3.8-stdlib:amd64 (3.8.5-1~20.04) ...
    Selecting previously unselected package xxd.
    Preparing to unpack .../12-xxd_2%3a8.1.2269-1ubuntu5_amd64.deb ...
    Unpacking xxd (2:8.1.2269-1ubuntu5) ...
    Selecting previously unselected package vim-common.
    Preparing to unpack .../13-vim-common_2%3a8.1.2269-1ubuntu5_all.deb ...
    Unpacking vim-common (2:8.1.2269-1ubuntu5) ...
    Selecting previously unselected package xz-utils.
    Preparing to unpack .../14-xz-utils_5.2.4-1ubuntu1_amd64.deb ...
    Unpacking xz-utils (5.2.4-1ubuntu1) ...
    Selecting previously unselected package alsa-topology-conf.
    Preparing to unpack .../15-alsa-topology-conf_1.2.2-1_all.deb ...
    Unpacking alsa-topology-conf (1.2.2-1) ...
    Selecting previously unselected package alsa-ucm-conf.
    Preparing to unpack .../16-alsa-ucm-conf_1.2.2-1ubuntu0.4_all.deb ...
    Unpacking alsa-ucm-conf (1.2.2-1ubuntu0.4) ...
    Selecting previously unselected package libasound2-data.
    Preparing to unpack .../17-libasound2-data_1.2.2-2.1ubuntu2.1_all.deb ...
    Unpacking libasound2-data (1.2.2-2.1ubuntu2.1) ...
    Selecting previously unselected package libasound2:amd64.
    Preparing to unpack .../18-libasound2_1.2.2-2.1ubuntu2.1_amd64.deb ...
    Unpacking libasound2:amd64 (1.2.2-2.1ubuntu2.1) ...
    Selecting previously unselected package libltdl7:amd64.
    Preparing to unpack .../19-libltdl7_2.4.6-14_amd64.deb ...
    Unpacking libltdl7:amd64 (2.4.6-14) ...
    Selecting previously unselected package libtdb1:amd64.
    Preparing to unpack .../20-libtdb1_1.4.2-3build1_amd64.deb ...
    Unpacking libtdb1:amd64 (1.4.2-3build1) ...
    Selecting previously unselected package libogg0:amd64.
    Preparing to unpack .../21-libogg0_1.3.4-0ubuntu1_amd64.deb ...
    Unpacking libogg0:amd64 (1.3.4-0ubuntu1) ...
    Selecting previously unselected package libvorbis0a:amd64.
    Preparing to unpack .../22-libvorbis0a_1.3.6-2ubuntu1_amd64.deb ...
    Unpacking libvorbis0a:amd64 (1.3.6-2ubuntu1) ...
    Selecting previously unselected package libvorbisfile3:amd64.
    Preparing to unpack .../23-libvorbisfile3_1.3.6-2ubuntu1_amd64.deb ...
    Unpacking libvorbisfile3:amd64 (1.3.6-2ubuntu1) ...
    Selecting previously unselected package sound-theme-freedesktop.
    Preparing to unpack .../24-sound-theme-freedesktop_0.8-2ubuntu1_all.deb ...
    Unpacking sound-theme-freedesktop (0.8-2ubuntu1) ...
    Selecting previously unselected package libcanberra0:amd64.
    Preparing to unpack .../25-libcanberra0_0.30-7ubuntu1_amd64.deb ...
    Unpacking libcanberra0:amd64 (0.30-7ubuntu1) ...
    Selecting previously unselected package libgpm2:amd64.
    Preparing to unpack .../26-libgpm2_1.20.7-5_amd64.deb ...
    Unpacking libgpm2:amd64 (1.20.7-5) ...
    Selecting previously unselected package libpython3.8:amd64.
    Preparing to unpack .../27-libpython3.8_3.8.5-1~20.04_amd64.deb ...
    Unpacking libpython3.8:amd64 (3.8.5-1~20.04) ...
    Selecting previously unselected package vim-runtime.
    Preparing to unpack .../28-vim-runtime_2%3a8.1.2269-1ubuntu5_all.deb ...
    Adding 'diversion of /usr/share/vim/vim81/doc/help.txt to /usr/share/vim/vim81/doc/help.txt.vim-tiny by vim-runtime'
    Adding 'diversion of /usr/share/vim/vim81/doc/tags to /usr/share/vim/vim81/doc/tags.vim-tiny by vim-runtime'
    Unpacking vim-runtime (2:8.1.2269-1ubuntu5) ...
    Selecting previously unselected package vim.
    Preparing to unpack .../29-vim_2%3a8.1.2269-1ubuntu5_amd64.deb ...
    Unpacking vim (2:8.1.2269-1ubuntu5) ...
    Setting up libexpat1:amd64 (2.2.9-1build1) ...
    Setting up libgpm2:amd64 (1.20.7-5) ...
    Setting up libogg0:amd64 (1.3.4-0ubuntu1) ...
    Setting up mime-support (3.64ubuntu1) ...
    Setting up alsa-ucm-conf (1.2.2-1ubuntu0.4) ...
    Setting up libmagic-mgc (1:5.38-4) ...
    Setting up libtdb1:amd64 (1.4.2-3build1) ...
    Setting up libssl1.1:amd64 (1.1.1f-1ubuntu2) ...
    debconf: unable to initialize frontend: Dialog
    debconf: (TERM is not set, so the dialog frontend is not usable.)
    debconf: falling back to frontend: Readline
    debconf: unable to initialize frontend: Readline
    debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.30.0 /usr/local/share/perl/5.30.0 /usr/lib/x86_64-linux-gnu/perl5/5.30 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.30 /usr/share/perl/5.30 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
    debconf: falling back to frontend: Teletype
    Setting up libsqlite3-0:amd64 (3.31.1-4ubuntu0.2) ...
    Setting up libmagic1:amd64 (1:5.38-4) ...
    Setting up file (1:5.38-4) ...
    Setting up xxd (2:8.1.2269-1ubuntu5) ...
    Setting up libasound2-data (1.2.2-2.1ubuntu2.1) ...
    Setting up vim-common (2:8.1.2269-1ubuntu5) ...
    Setting up xz-utils (5.2.4-1ubuntu1) ...
    update-alternatives: using /usr/bin/xz to provide /usr/bin/lzma (lzma) in auto mode
    update-alternatives: warning: skip creation of /usr/share/man/man1/lzma.1.gz because associated file /usr/share/man/man1/xz.1.gz (of link group lzma) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/unlzma.1.gz because associated file /usr/share/man/man1/unxz.1.gz (of link group lzma) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/lzcat.1.gz because associated file /usr/share/man/man1/xzcat.1.gz (of link group lzma) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/lzmore.1.gz because associated file /usr/share/man/man1/xzmore.1.gz (of link group lzma) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/lzless.1.gz because associated file /usr/share/man/man1/xzless.1.gz (of link group lzma) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/lzdiff.1.gz because associated file /usr/share/man/man1/xzdiff.1.gz (of link group lzma) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/lzcmp.1.gz because associated file /usr/share/man/man1/xzcmp.1.gz (of link group lzma) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/lzgrep.1.gz because associated file /usr/share/man/man1/xzgrep.1.gz (of link group lzma) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/lzegrep.1.gz because associated file /usr/share/man/man1/xzegrep.1.gz (of link group lzma) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/lzfgrep.1.gz because associated file /usr/share/man/man1/xzfgrep.1.gz (of link group lzma) doesn't exist
    Setting up libvorbis0a:amd64 (1.3.6-2ubuntu1) ...
    Setting up libltdl7:amd64 (2.4.6-14) ...
    Setting up alsa-topology-conf (1.2.2-1) ...
    Setting up sound-theme-freedesktop (0.8-2ubuntu1) ...
    Setting up libasound2:amd64 (1.2.2-2.1ubuntu2.1) ...
    Setting up libmpdec2:amd64 (2.4.2-3) ...
    Setting up vim-runtime (2:8.1.2269-1ubuntu5) ...
    Setting up readline-common (8.0-4) ...
    Setting up libpython3.8-minimal:amd64 (3.8.5-1~20.04) ...
    Setting up libreadline8:amd64 (8.0-4) ...
    Setting up libvorbisfile3:amd64 (1.3.6-2ubuntu1) ...
    Setting up libpython3.8-stdlib:amd64 (3.8.5-1~20.04) ...
    Setting up libcanberra0:amd64 (0.30-7ubuntu1) ...
    Setting up libpython3.8:amd64 (3.8.5-1~20.04) ...
    Setting up vim (2:8.1.2269-1ubuntu5) ...
    update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vim (vim) in auto mode
    update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vimdiff (vimdiff) in auto mode
    update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/rvim (rvim) in auto mode
    update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/rview (rview) in auto mode
    update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/vi (vi) in auto mode
    update-alternatives: warning: skip creation of /usr/share/man/da/man1/vi.1.gz because associated file /usr/share/man/da/man1/vim.1.gz (of link group vi) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/de/man1/vi.1.gz because associated file /usr/share/man/de/man1/vim.1.gz (of link group vi) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/fr/man1/vi.1.gz because associated file /usr/share/man/fr/man1/vim.1.gz (of link group vi) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/it/man1/vi.1.gz because associated file /usr/share/man/it/man1/vim.1.gz (of link group vi) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/ja/man1/vi.1.gz because associated file /usr/share/man/ja/man1/vim.1.gz (of link group vi) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/pl/man1/vi.1.gz because associated file /usr/share/man/pl/man1/vim.1.gz (of link group vi) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/ru/man1/vi.1.gz because associated file /usr/share/man/ru/man1/vim.1.gz (of link group vi) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/vi.1.gz because associated file /usr/share/man/man1/vim.1.gz (of link group vi) doesn't exist
    update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/view (view) in auto mode
    update-alternatives: warning: skip creation of /usr/share/man/da/man1/view.1.gz because associated file /usr/share/man/da/man1/vim.1.gz (of link group view) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/de/man1/view.1.gz because associated file /usr/share/man/de/man1/vim.1.gz (of link group view) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/fr/man1/view.1.gz because associated file /usr/share/man/fr/man1/vim.1.gz (of link group view) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/it/man1/view.1.gz because associated file /usr/share/man/it/man1/vim.1.gz (of link group view) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/ja/man1/view.1.gz because associated file /usr/share/man/ja/man1/vim.1.gz (of link group view) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/pl/man1/view.1.gz because associated file /usr/share/man/pl/man1/vim.1.gz (of link group view) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/ru/man1/view.1.gz because associated file /usr/share/man/ru/man1/vim.1.gz (of link group view) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/view.1.gz because associated file /usr/share/man/man1/vim.1.gz (of link group view) doesn't exist
    update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/ex (ex) in auto mode
    update-alternatives: warning: skip creation of /usr/share/man/da/man1/ex.1.gz because associated file /usr/share/man/da/man1/vim.1.gz (of link group ex) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/de/man1/ex.1.gz because associated file /usr/share/man/de/man1/vim.1.gz (of link group ex) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/fr/man1/ex.1.gz because associated file /usr/share/man/fr/man1/vim.1.gz (of link group ex) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/it/man1/ex.1.gz because associated file /usr/share/man/it/man1/vim.1.gz (of link group ex) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/ja/man1/ex.1.gz because associated file /usr/share/man/ja/man1/vim.1.gz (of link group ex) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/pl/man1/ex.1.gz because associated file /usr/share/man/pl/man1/vim.1.gz (of link group ex) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/ru/man1/ex.1.gz because associated file /usr/share/man/ru/man1/vim.1.gz (of link group ex) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/ex.1.gz because associated file /usr/share/man/man1/vim.1.gz (of link group ex) doesn't exist
    update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/editor (editor) in auto mode
    update-alternatives: warning: skip creation of /usr/share/man/da/man1/editor.1.gz because associated file /usr/share/man/da/man1/vim.1.gz (of link group editor) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/de/man1/editor.1.gz because associated file /usr/share/man/de/man1/vim.1.gz (of link group editor) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/fr/man1/editor.1.gz because associated file /usr/share/man/fr/man1/vim.1.gz (of link group editor) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/it/man1/editor.1.gz because associated file /usr/share/man/it/man1/vim.1.gz (of link group editor) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/ja/man1/editor.1.gz because associated file /usr/share/man/ja/man1/vim.1.gz (of link group editor) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/pl/man1/editor.1.gz because associated file /usr/share/man/pl/man1/vim.1.gz (of link group editor) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/ru/man1/editor.1.gz because associated file /usr/share/man/ru/man1/vim.1.gz (of link group editor) doesn't exist
    update-alternatives: warning: skip creation of /usr/share/man/man1/editor.1.gz because associated file /usr/share/man/man1/vim.1.gz (of link group editor) doesn't exist
    Processing triggers for libc-bin (2.31-0ubuntu9.1) ...
    Removing intermediate container 48b3c3d7d863
     ---> 801840732350
    Successfully built 801840732350
    Successfully tagged ubuntu-with-vim-dockerfile:latest
    ```

  + ```bash
    root@ubuntu16:~/Dockerfile# docker images
    REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
    ubuntu-with-vim-dockerfile   latest              801840732350        3 minutes ago       167MB
    ubuntu                       latest              d70eaf7277ea        3 weeks ago         72.9MB
    httpd                        latest              3dd970e6b110        5 weeks ago         138MB
    centos                       latest              0d120b6ccaa8        3 months ago        215MB
    hello-world                  latest              bf756fb1ae65        10 months ago       13.3kB
    ```

    

