# MATLABTips9--size

1. size

   + 数组大小

   + 语法

     + sz = size(A)

       返回一个行向量，其元素是A的相应维度的长度

       + 例如，如果A是一个3*4的矩阵，则size(A)返回向量[3 4]

       如果A是**表或时间表**，则size(A)返回由表中的行数和变量数组成的二元素行向量

     + szdim = size(A,dim)

       当dim为正整数标量时，返回维度dim的长度

       从R2019b开始，还可以将dim指定为正整数向量，以一次查询多个维度长度

       + 例如，size(A,[2 3])，以1*2行向量szdim形式返回A的第二个维度和第三个维度的长度

     + szdim = size(A,dim1,dim2,...,dimN)

       以行向量szdim形式返回维度dim1,dim2,...,dimN的长度**（从R2019b开始）**

     + [sz1,...,szN] = size(__)

       分别返回A的查询维度的长度

   + 实例

     + 数组的大小

       ```matlab
       %创建一个随机四维数组并返回其大小
       A =rand(2,3,4,5);
       sz = size(A)
       sz1 = size(A,2)  %仅查询A的第二个维度的长度
       ```

       output:

       ```matlab
       sz =
       
            2     3     4     5
       
       
       sz1 =
       
            3
       ```

       **从R2019开始**，可以通过指定向量维度参数，一次查询多个维度长度

       ```matlab
       szdim13 = size(A,[1 3])
       ```

       output:

       ```matlab
       szdim13 = 1×2
       
            2     4
       ```

       求A的第二个维度至第四个维度的长度

       ```matlab
       szdim23 = size(A,2:4)
       ```

       output:

       ```matlab
       szdim23 = 1×3
       
            3     4     5
       ```

       可以使用单独的输入参数列出查询的各个维度

       ```matlab
       szdim23 = size(A,2,3,4);
       ```

     + 表大小

       ```matlab
       %创建一个包含5行和4个变量的表
       LastName = {'Smith';'Johnson';'Williams';'Jones';'Brown'};
       Age = [38;43;38;40;49];
       Height = [71;69;64;67;64];
       Weight = [176;163;131;133;119];
       BloodPressure = [124 93; 109 77; 125 83; 117 75; 122 80];
       
       A = table(Age,Height,Weight,BloodPressure,'RowNames',LastName)
       ```

       output:

       ```matlab
       A=5×4 table
                       Age    Height    Weight    BloodPressure
                       ___    ______    ______    _____________
       
           Smith       38       71       176       124     93  
           Johnson     43       69       163       109     77  
           Williams    38       64       131       125     83  
           Jones       40       67       133       117     75  
           Brown       49       64       119       122     80  
       ```

       ```matlab
       %计算该表的大小。尽管 BloodPressure 变量包含两列，但 size 只计算变量数
       sz = size(A)
       ```

       output:

       ```matlab
       sz = 1×2
       
            5     4
       ```

     + 使用单独的参数返回各个维度长度

       ```matlab
       %创建一个随机矩阵，并分别返回行数和列数
       A = rand(4,3);
       [numRows,numCols] = size(A)
       ```

       output:

       ```matlab
       numRows =
       
            4
       
       
       numCols =
       
            3
       ```

       

       

