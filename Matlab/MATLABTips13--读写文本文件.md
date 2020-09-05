# MATLABTips13--读写文本文件

### fopen

+ 打开文件或获得有关打开文件的信息

+ 语法

  + ```matlab
    fileID = fopen(filename)
    ```

    打开文件 `filename` 以便以二进制读取形式进行访问，并返回等于或大于 3 的整数文件标识符。

    **MATLAB® 保留文件标识符 `0`、`1` 和 `2` 分别用于标准输入、标准输出（屏幕）和标准错误。**

    如果 `fopen` 无法打开文件，则 `fileID` 为 `-1`。

  + ```matlab
    fileID = fopen(filename, permission)
    ```

    将打开由 `permission` 指定访问类型的文件。

    + 文件访问类型

      指定为字符向量或字符串向量

      可以使用二进制模式或文本模式打开文件

      在UNIX系统上，两种转换模式具有相同效果。

      若以二进制模式打开文件，指定以下各项之一

      | 文件类型 | 说明                                               |
      | -------- | -------------------------------------------------- |
      | 'r'      | 打开要读取的文件                                   |
      | 'w'      | 打开或创建要写入的新文件。放弃现有内容（如果有）   |
      | 'a'      | 打开或创建要写入的新文件。追加数据到文件末尾       |
      | 'r+'     | 打开要读写的文件                                   |
      | 'w+'     | 打开或创建要读写的新文件。放弃现有内容（如果有）。 |
      | 'a+'     | 打开或创建要读写的新文件。追加数据到文件末尾。     |
      | 'A'      | 打开文件以追加（但不自动刷新）当前输出缓冲区。     |
      | 'W'      | 打开文件以写入（但不自动刷新）当前输出缓冲区。     |

      要以文本模式打开文件，请将字母 `'t'` 附加到 `permission` 参数，例如 `'rt'` 或 `'wt+'`。

  + ```matlab
    fileID = fopen(filename, permission, machinefmt, ecodingIn)
    ```

    + 使用 `machinefmt` 参数另外指定在文件中读写字节或位时的顺序。

      | machinefmt             | 说明                                |
      | ---------------------- | ----------------------------------- |
      | 'n'` 或 `'native'      | 系统字节排序方式（默认）            |
      | 'b'` 或 `'ieee-be'     | Big-endian 排序                     |
      | 'l'` 或 `'ieee-le'     | Little-endian 排序                  |
      | 's'` 或 `'ieee-be.l64' | Big-endian 排序，64 位长数据类型    |
      | 'a'` 或 `'ieee-le.l64' | Little-endian 排序，64 位长数据类型 |

      默认情况下，当前支持的所有平台都使用 little-endian 排序方式对新文件进行排序。

      现有二进制文件可以使用 big-endian 或 little-endian 排序方式。

    + 可选的 `encodingIn` 参数指定与文件相关联的字符编码方案。

      |                |                 |                  |
      | -------------- | --------------- | ---------------- |
      | `'Big5'`       | `'ISO-8859-1'`  | `'windows-874'`  |
      | `'Big5-HKSCS'` | `'ISO-8859-2'`  | `'windows-949'`  |
      | `'CP949'`      | `'ISO-8859-3'`  | `'windows-1250'` |
      | `'EUC-KR'`     | `'ISO-8859-4'`  | `'windows-1251'` |
      | `'EUC-JP'`     | `'ISO-8859-5'`  | `'windows-1252'` |
      | `'EUC-TW'`     | `'ISO-8859-6'`  | `'windows-1253'` |
      | `'GB18030'`    | `'ISO-8859-7'`  | `'windows-1254'` |
      | `'GB2312'`     | `'ISO-8859-8'`  | `'windows-1255'` |
      | `'GBK'`        | `'ISO-8859-9'`  | `'windows-1256'` |
      | `'IBM866'`     | `'ISO-8859-11'` | `'windows-1257'` |
      | `'KOI8-R'`     | `'ISO-8859-13'` | `'windows-1258'` |
      | `'KOI8-U'`     | `'ISO-8859-15'` | `'US-ASCII'`     |
      |                | `'Macintosh'`   | `'UTF-8'`        |
      |                | `'Shift_JIS'`   |                  |

  + ```matlab
    [fileID, errmsg] = fopen(__)
    ```

    如果 `fopen` 打开文件失败，则 `[fileID,errmsg] = fopen(___)` 还将返回一条因系统而异的错误消息。

    否则，`errmsg` 是一个空字符向量。

    可以将此语法与前面语法中的任何输入参数结合使用。

  + ```matlab
    fIDs = fopen('all')
    ```

    返回包含所有打开文件的文件标识符的行向量。

    为标准输入、输出以及错误而保留的标识符不包括在内。

    向量中元素的数量等于打开文件的数量。

  + ```matlab
    filename = fopen(fileID)
    ```

    返回上一次调用 `fopen` 在打开 `fileID` 指定的文件时所使用的文件名。

    输出文件名将解析到完整路径。

    `fopen` 函数不会从文件读取信息来确定输出值。

  + ```matlab
    [filename, permission, machinefmt, encodingOut] = fopen(fileID)
    ```

    还会返回上一次调用 `fopen` 在打开指定文件时所使用的权限、计算机格式以及编码。

    如果是以二进制模式打开的文件，则 `permission` 会包含字母 `'b'`。

    `encodingOut` 输出是一个标准编码方案名称。

    `fopen` 不会从文件读取信息来确定这些输出值。

    无效的 `fileID` 会为所有输出参数返回空字符向量。

+ 示例

  + 打开文件

    ```matlab
    fileID = fopen('test.txt');
    disp(fileID);
    tline = fgetl(fileID);
    disp(tline);
    fclose(fileID);
    ```

    ```matlab
    >> file_study
         3
    
    cxy file function test.
    ```

  + 打开文件并制定访问类型、写入顺序、字符编码

    ```
    fileID = fopen('test.txt', 'w', 'n', 'Shift_JIS')
    ```

---

### fprintf

+ 将数据写入文本文件

+ 语法

  + ```matlab
    fprintf(fileID, formatSpec,A1,..,An)
    ```

    按列顺序将 `formatSpec` 应用于数组 `A1,...An` 的所有元素，并将数据写入到一个文本文件。`fprintf` 使用在对 `fopen` 的调用中指定的编码方案。

  + ```matlab
    fprintf(formatSpec,A1,..,An)
    ```

    设置数据的格式并在屏幕上显示结果。

  + ```matlab
    nbytes = fprintf(__)
    ```

    使用前述语法中的任意输入参数返回 `fprintf` 所写入的字节数。

+ 示例

  + 将多个数值和字面文本输出到屏幕。

    ```matlab
    A1 = [9.9, 9900];
    A2 = [8.8,  7.7 ; ...
          8800, 7700];
    formatSpec = 'X is %4.2f meters or %8.3f mm\n';
    fprintf(formatSpec,A1,A2)
    ```

    ```matlab
    X is 9.90 meters or 9900.000 mm
    X is 8.80 meters or 8800.000 mm
    X is 7.70 meters or 7700.000 mm
    ```

    `formatSpec` 输入中的 `%4.2f` 指定输出中每行的第一个值为浮点数，字段宽度为四位数，包括小数点后的两位数。

    `formatSpec` 输入中的 `%8.3f` 指定输出中每行的第二个值为浮点数，字段宽度为八位数，包括小数点后的三位数。

    `\n` 为新起一行的控制字符。

  + 将双精度值输出为整数

    显式将包含分式的双精度值转换为整数值。

    ```matlab
    a = [1.02 3.04 5.06];
    disp(a);
    disp(round(a));
    fprintf('%d\n',round(a));
    ```

    ```matlab
        1.0200    3.0400    5.0600
    
         1     3     5
    
    1
    3
    5
    ```

    `formatSpec` 输入中的 `%d` 将向量 `round(a)` 中的每个值作为有符号整数输出。`\n` 为新起一行的控制字符。

  + 将表格数据写入文本文件

    将指数函数的短标写入到名为exp.txt的文本文件

    ```matlab
    x = 0:.1:1;
    disp(x);
    A = [x; exp(x)];
    disp(A);
    
    fileID = fopen('exp.txt','w');
    fprintf(fileID,'%6s %12s\n','x','exp(x)');
    fprintf(fileID,'%6.2f %12.8f\n',A);
    fclose(fileID);
    ```

    ```matlab
     0    0.1000    0.2000    0.3000    0.4000    0.5000    0.6000    0.7000    0.8000    0.9000    1.0000
    
             0    0.1000    0.2000    0.3000    0.4000    0.5000    0.6000    0.7000    0.8000    0.9000    1.0000
        1.0000    1.1052    1.2214    1.3499    1.4918    1.6487    1.8221    2.0138    2.2255    2.4596    2.7183
    
    ```

    ```matlab
    >> type exp.txt
    
         x       exp(x)
      0.00   1.00000000
      0.10   1.10517092
      0.20   1.22140276
      0.30   1.34985881
      0.40   1.49182470
      0.50   1.64872127
      0.60   1.82211880
      0.70   2.01375271
      0.80   2.22554093
      0.90   2.45960311
      1.00   2.71828183
    ```

  + 获取写入文件的字节数

    将数据写入文件并返回所写入的字节数。

    将数据数组 `A` 写入文件并获取 `fprintf` 所写入的字节数。

    ```matlab
    A = magic(4);
    
    fileID = fopen('myfile.txt','w');
    nbytes = fprintf(fileID,'%5d %5d %5d %5d\n',A);
    disp(nbytes);
    fclose(fileID);
    ```

    ```matlab
        96
    ```

    ```matlab
    >> type myfile.txt
    
       16     5     9     4
        2    11     7    14
        3    10     6    15
       13     8    12     1
    ```

  + 在命令行窗口中显示超链接

    在屏幕上显示超链接（[MathWorks 公司网站](https://www.mathworks.com/)）。

    ```matlab
    url = 'https://www.mathworks.com';
    sitename = 'The MathWorks Web Site';
    
    fprintf('<a href = "%s">%s</a>\n',url,sitename)
    ```

    ```matlab
    The MathWorks Web Site
    ```

    带链接。。

---

### fgetl

+ 读取文件中的行，并删除换行符

+ 语法

  ```matlab
  tline = fgetl(fileID)
  ```

  + 返回指定文件中的下一行，并删除换行符
  + 如果文件非空，则fgetl以字符向量形式返回tline
  + 如果文件为空且仅包含文件末尾标记，则fgetl以数值-1形式返回

+ 示例

  ```matlab
  fileID = fopen('GEO_01-GEO_02-TheoraticalDelay.txt','r');
  tline = fgetl(fileID);
  while ischar(tline);
      disp(tline);
      tline = fgetl(fileID);
  end
  fclose(fileID);
  ```

  输出：

  ```matlab
  12:00,1,140.6528;
  12:01,1,140.6528;
  12:02,1,140.6528;
  12:03,1,140.6528;
  12:04,1,140.6528;
  12:05,1,140.6528;
  12:06,1,140.6528;
  12:07,1,140.6528;
  12:08,1,140.6528;
  12:09,1,140.6528;
  12:10,1,140.6528;
  12:11,1,140.6528;
  12:12,1,140.6528;
  12:13,1,140.6528;
  12:14,1,140.6528;
  12:15,1,140.6528;
  12:16,1,140.6528;
  12:17,1,140.6528;
  12:18,1,140.6528;
  12:19,1,140.6528;
  12:20,1,140.6528;
  12:21,1,140.6528;
  12:22,1,140.6528;
  12:23,1,140.6528;
  12:24,1,140.6528;
  12:25,1,140.6528;
  12:26,1,140.6528;
  12:27,1,140.6528;
  12:28,1,140.6528;
  12:29,1,140.6528;
  12:30,1,140.6528;
  12:31,1,140.6528;
  12:32,1,140.6528;
  12:33,1,140.6528;
  12:34,1,140.6528;
  12:35,1,140.6528;
  12:36,1,140.6528;
  12:37,1,140.6528;
  12:38,1,140.6528;
  12:39,1,140.6528;
  12:40,1,140.6528;
  ```

+ 



