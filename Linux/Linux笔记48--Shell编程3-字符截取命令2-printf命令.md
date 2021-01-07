# Linux笔记48--Shell编程3-字符截取命令2-printf命令

### printf `'`输出类型输出格式`'` 输出内容

+ 输出类型：

  %ns:		输出字符串。n是数字指代输出几个字符

  %ni:		 输出整数。n是数字指代输出几个数字

  %m.nf:	输出浮点数。m和n是数字，分别指代输出的浮点数位数和小数位数。

  ​				 例：%8.2f代表共输出8位数，两位小数，6位整数

+ 输出格式

  | 输出格式 |                           |
  | -------- | ------------------------- |
  | \a       | 输出警告声音              |
  | \b       | 输出退格键，即Backspace键 |
  | \f       | 清除屏幕                  |
  | \n       | 换行                      |
  | \r       | 回车，即Enter键           |
  | \t       | 水平输出退格键，即Tab键   |
  | \v       | 垂直输出退格键，即Tab键   |

### 实例

+ printf '%s %s %s \n' 1 2 3 4 5 6

  输出：

  1 2 3

  4 5 6 

  注：'%s %s %s\n'会被认为每三个字符为一组输出

+ printf '%s' student.txt

  输出：

  student.txt

  注：**printf将student.txt直接看成一个字符串，而不是一个文件名**

+ cat student.txt | printf '%s'

  输出：没有输出

  **注：printf与管道符结合也不能输出文件内容**

+ printf '%s' $(cat student.txt)

  输出：IDNameGenderMark1LimingM862ScM903GaoM83

  **注：不调整输出格式，连着输出一整个字符串**

+ printf '%s\t%s\t%s\t%s\n' $(cat student.txt)

  输出：

  ID	Name	Gender	Mark
  1	  Liming   M	          86
  2	  Sc	       M	          90
  3	  Gao	    M	          83

  注：调整输出格式

### 在awk命令的输出中支持print和printf命令

+ print：print会在每个输出之后自动加入一个换行符（Linux默认没有print命令）
+ printf：printf是标准格式输出命令，并不会自动加入换行符，如果需要换行，需要手工加入换行符

