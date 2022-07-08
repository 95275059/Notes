# LinuxTips34--grep&egrep

+ 示例文件

  ```shell
  $ cat employee.txt  
  100  Thomas  Manager    Sales       $5,000  
  200  Jason   Developer  Technology  $5,500  
  300  Raj     Sysadmin   Technology  $7,000  
  400  Nisha   Manager    Marketing   $9,500  
  500  Randy   Manager    Sales       $6,000  
  ```

  ---

## grep

+ 选项

  * **-A<显示行数> 或 --after-context=<显示行数>** : 除了显示符合范本样式的那一行之外，并显示该行之后的内容。
  * **-B<显示行数> 或 --before-context=<显示行数>** : 除了显示符合样式的那一行之外，并显示该行之前的内容。
  * **-C<显示行数> 或 --context=<显示行数>或-<显示行数>** : 除了显示符合样式的那一行之外，并显示该行之前后的内容。
  * 
  
+ grep or 操作

  + 方法一：使用\\|

    ```shell
    grep 'pattern1\|pattern2' filename 
    ```

    ```shell
    root@cxytest:~/test# grep 'Tech\|Sales' employee.txt
    100  Thomas  Manager    Sales       $5,000
    200  Jason   Developer  Technology  $5,500
    300  Raj     Sysadmin   Technology  $7,000
    500  Randy   Manager    Sales       $6,000
    ```

  + 方法二：使用选项-E

    + 如果使用了grep命令的选项-E，则应该使用|来分割多个pattern，以此实现OR操作

      ```shell
      grep -E 'pattern1|pattern2' filename
      ```

      ```shell
      root@cxytest:~/test# grep -E 'Tech|Sales' employee.txt 
      100  Thomas  Manager    Sales       $5,000
      200  Jason   Developer  Technology  $5,500
      300  Raj     Sysadmin   Technology  $7,000
      500  Randy   Manager    Sales       $6,000
      ```

  + 方法三：**使用egrep**

    + **egrep命令等同于'grep -E'**

    ```shell
    egrep 'pattern1|pattern2' filename  
    ```

    ```shell
    root@cxytest:~/test# egrep 'Tech|Sales' employee.txt 
    100  Thomas  Manager    Sales       $5,000
    200  Jason   Developer  Technology  $5,500
    300  Raj     Sysadmin   Technology  $7,000
    500  Randy   Manager    Sales       $6,000
    ```

  + 方法四：使用选项-e

    + 使用grep -e，只能传递一个参数
    + 在单条命令中使用多个-e选项，得到多个pattern，以此实现OR操作

    ```shell
    grep -e pattern1 -e pattern2 filename
    ```

    ```shell
    root@cxytest:~/test# grep -e Tech -e Sales employee.txt 
    100  Thomas  Manager    Sales       $5,000
    200  Jason   Developer  Technology  $5,500
    300  Raj     Sysadmin   Technology  $7,000
    500  Randy   Manager    Sales       $6,000
    ```

  ---

+ grep and 操作

  + 方法一：使用-E 'pattern1.*pattern2'

    + grep命令本身不提供AND功能。
    + 使用-E选项可以实现AND操作

    ```shell
    grep -E 'pattern1.*pattern2' filename  
    grep -E 'pattern1.*pattern2|pattern2.*pattern1' filename 
    ```

    ```shell
    root@cxytest:~/test# grep -E 'Dev.*Tech' employee.txt 
    200  Jason   Developer  Technology  $5,500
    ```

    ```shell
    root@cxytest:~/test# grep -E 'Tech.*Jason' employee.txt 
    root@cxytest:~/test# grep -E 'Jason.*Tech' employee.txt 
    200  Jason   Developer  Technology  $5,500
    root@cxytest:~/test# grep -E 'Thomas.*Sales|Jason.*Tech' employee.txt
    ```

    + 可以看到，pattern1和pattern2是有序的

    ```shell
    root@cxytest:~/test# grep -E 'Thomas.*Sales|Jason.*Tech' employee.txt 
    100  Thomas  Manager    Sales       $5,000
    200  Jason   Developer  Technology  $5,500
    ```

  + 方法二：使用多个grep命令

    + 由**管道符**分割，以此实现AND语义

      ```shell
      grep 'pattern1' filename | grep -E 'pattern2' 
      ```

      ```shell
      root@cxytest:~/test# grep Manager employee.txt | grep Sales
      100  Thomas  Manager    Sales       $5,000
      500  Randy   Manager    Sales       $6,000
      ```

  ---

+ grep not 操作

  + 方法一：使用grep -v

    + -v用来实现反选匹配（invert match），可以匹配得到除指定pattern外的所有lines

      ```shell
      grep -v 'pattern1' filename
      ```

      ```shell
      root@cxytest:~/test# grep -v Sales employee.txt 
      200  Jason   Developer  Technology  $5,500
      300  Raj     Sysadmin   Technology  $7,000
      400  Nisha   Manager    Marketing   $9,500
      ```

  ---

+ 结合管道符，实现更复杂的操作

  ```shell
  root@cxytest:~/test# egrep 'Manager|Developer' employee.txt | grep -v Sales
  200  Jason   Developer  Technology  $5,500
  400  Nisha   Manager    Marketing   $9,500
  ```

  

