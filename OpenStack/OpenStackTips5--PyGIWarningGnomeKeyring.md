# OpenStackTips5--PyGIWarning:GnomeKeyring

+ 警告信息

  ```bash
  /usr/lib/python2.7/site-packages/keyring/backends/Gnome.py:7: PyGIWarning: GnomeKeyring was imported without specifying a version first. Use gi.require_version('GnomeKeyring', '1.0') before import to ensure that the right version gets loaded.
    from gi.repository import GnomeKeyring
  ```

+ 屏蔽方法：修改Gnoma.py

  + 原Gnome.py开头

    ```python
    import os
    try:
        from gi import Repository
        if Repository.get_default().enumerate_versions('GnomeKeyring'):
            from gi.repository import GnomeKeyring
    except ImportError:
        pass
    ```

  + 修改为

    ```python
    import os
    import gi.require_version
    try:
        from gi import Repository
        if Repository.get_default().enumerate_versions('GnomeKeyring'):
            gi.require_version('GnomeKeyring', '1.0')
            from gi.repository import GnomeKeyring
    except ImportError:
        pass
    ```

    

  