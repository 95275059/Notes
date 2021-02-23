# Anaconda笔记4--conda安装更新失败

## 错误一:raise Response304ContentUnchanged()

```
(python36) C:\Users\CXY>conda install PyMySQL
Solving environment: failed

# >>>>>>>>>>>>>>>>>>>>>> ERROR REPORT <<<<<<<<<<<<<<<<<<<<<<

    Traceback (most recent call last):
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 227, in _load
        mod_etag_headers.get('_mod'))
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 574, in fetch_repodata_remote_request
        raise Response304ContentUnchanged()
    conda.core.subdir_data.Response304ContentUnchanged

    During handling of the above exception, another exception occurred:

    Traceback (most recent call last):
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\exceptions.py", line 819, in __call__
        return func(*args, **kwargs)
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\cli\main.py", line 78, in _main
        exit_code = do_call(args, p)
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\cli\conda_argparse.py", line 77, in do_call
        exit_code = getattr(module, func_name)(args, parser)
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\cli\main_install.py", line 11, in execute
        install(args, parser, 'install')
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\cli\install.py", line 235, in install
        force_reinstall=context.force,
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\solve.py", line 518, in solve_for_transaction
        force_remove, force_reinstall)
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\solve.py", line 451, in solve_for_diff
        final_precs = self.solve_final_state(deps_modifier, prune, ignore_pinned, force_remove)
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\solve.py", line 180, in solve_final_state
        index, r = self._prepare(prepared_specs)
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\solve.py", line 592, in _prepare
        self.subdirs, prepared_specs)
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\index.py", line 215, in get_reduced_index
        new_records = query_all(spec)
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\index.py", line 184, in query_all
        return tuple(concat(future.result() for future in as_completed(futures)))
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 95, in query
        self.load()
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 149, in load
        _internal_state = self._load()
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 233, in _load
        mod_etag_headers.get('_mod'))
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 280, in _read_local_repdata
        _internal_state = self._process_raw_repodata_str(raw_repodata_str)
      File "C:\Users\CXY\Anaconda3\lib\site-packages\conda\core\subdir_data.py", line 317, in _process_raw_repodata_str
        json_obj = json.loads(raw_repodata_str or '{}')
      File "C:\Users\CXY\Anaconda3\lib\json\__init__.py", line 348, in loads
        return _default_decoder.decode(s)
      File "C:\Users\CXY\Anaconda3\lib\json\decoder.py", line 337, in decode
        obj, end = self.raw_decode(s, idx=_w(s, 0).end())
      File "C:\Users\CXY\Anaconda3\lib\json\decoder.py", line 353, in raw_decode
        obj, end = self.scan_once(s, idx)
    json.decoder.JSONDecodeError: Unterminated string starting at: line 205601 column 9 (char 6176578)
```

+ 重点错误

  + raise Response304ContentUnchanged()
  + json.decoder.JSONDecodeError: Unterminated string starting at: line 205601 column 9 (char 6176578)‘

+ 原因

  + https://www.jianshu.com/p/2bca744fcd82

+ 解决方案

  ```shell
  conda clean -i
  ```

  