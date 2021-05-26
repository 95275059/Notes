# Java笔记12--数组操作

## 遍历数组

+ 方法
  * 普通的for循环
  * for each 循环

+ 打印数组内容

  + 直接打印数组变量，得到的是数组在JVM中的引用地址

    ```java
    int[] ns = { 1, 1, 2, 3, 5, 8 };
    System.out.println(ns); // 类似 [I@7852e922
    ```

  + for each循环

    ```java
    int[] ns = { 1, 1, 2, 3, 5, 8 };
    for (int n : ns) {
        System.out.print(n + ", ");
    }
    ```

  + Java标准库提供的Arrays.toString()可以快速打印数组内容

    ```java
    import java.util.Arrays;
    
    public class Main {
        public static void main(String[] args) {
            int[] ns = { 1, 1, 2, 3, 5, 8 };
            System.out.println(Arrays.toString(ns));
        }
    }
    ```

## 数组排序

+ 常用的排序算法有冒泡排序、插入排序和快速排序

+ 冒泡排序

  ```java
  import java.util.Arrays;
  
  public class Main {
      public static void main(String[] args) {
          int[] ns = { 28, 12, 89, 73, 65, 18, 96, 50, 8, 36 };
          // 排序前:
          System.out.println(Arrays.toString(ns));
          for (int i = 0; i < ns.length - 1; i++) {
              for (int j = 0; j < ns.length - i - 1; j++) {
                  if (ns[j] > ns[j+1]) {
                      // 交换ns[j]和ns[j+1]:
                      int tmp = ns[j];
                      ns[j] = ns[j+1];
                      ns[j+1] = tmp;
                  }
              }
          }
          // 排序后:
          System.out.println(Arrays.toString(ns));
      }
  }
  ```

  冒泡排序的特点是，每一轮循环后，最大的一个数被交换到末尾，因此，下一轮循环就可以“刨除”最后的数，每一轮循环都比上一轮循环的结束位置靠前一位。

+ Java的标准库已经内置了排序功能，我们只需要调用JDK提供的`Arrays.sort()`就可以排序

  ```java
  import java.util.Arrays;
  
  public class Main {
      public static void main(String[] args) {
          int[] ns = { 28, 12, 89, 73, 65, 18, 96, 50, 8, 36 };
          Arrays.sort(ns);
          System.out.println(Arrays.toString(ns));
      }
  }
  ```

  **必须注意，对数组排序实际上修改了数组本身**

  + 例如，排序前的数组是

    ```java
    int[] ns = { 9, 3, 6, 5 };
    ```

    在内存中，这个整型数组表示如下：

    ```ascii
          ┌───┬───┬───┬───┐
    ns───>│ 9 │ 3 │ 6 │ 5 │
          └───┴───┴───┴───┘
    ```

    当我们调用`Arrays.sort(ns);`后，这个整型数组在内存中变为：

    ```ascii
          ┌───┬───┬───┬───┐
    ns───>│ 3 │ 5 │ 6 │ 9 │
          └───┴───┴───┴───┘
    ```

    即变量`ns`指向的数组内容已经被改变了。

  + 如果对一个字符串数组进行排序，例如：

    ```
    String[] ns = { "banana", "apple", "pear" };
    ```

    排序前，这个数组在内存中表示如下：

    ```ascii
                       ┌──────────────────────────────────┐
                   ┌───┼──────────────────────┐           │
                   │   │                      ▼           ▼
             ┌───┬─┴─┬─┴─┬───┬────────┬───┬───────┬───┬──────┬───┐
    ns ─────>│░░░│░░░│░░░│   │"banana"│   │"apple"│   │"pear"│   │
             └─┬─┴───┴───┴───┴────────┴───┴───────┴───┴──────┴───┘
               │                 ▲
               └─────────────────┘
    ```

    调用`Arrays.sort(ns);`排序后，这个数组在内存中表示如下：

    ```ascii
                       ┌──────────────────────────────────┐
                   ┌───┼──────────┐                       │
                   │   │          ▼                       ▼
             ┌───┬─┴─┬─┴─┬───┬────────┬───┬───────┬───┬──────┬───┐
    ns ─────>│░░░│░░░│░░░│   │"banana"│   │"apple"│   │"pear"│   │
             └─┬─┴───┴───┴───┴────────┴───┴───────┴───┴──────┴───┘
               │                              ▲
               └──────────────────────────────┘
    ```

    原来的3个字符串在内存中均没有任何变化，但是`ns`数组的每个元素指向变化了。

+ sort 升序倒序排序

  ```java
  import java.util.Arrays;
  import java.util.Collections;
  public class test {
  	public static void main(String[] args) {
  		int[] ns = { 28, 12, 89, 73, 65, 18, 96, 50, 8, 36 };
  		System.out.println(Arrays.toString(ns));
          Arrays.sort(ns);
          System.out.println(Arrays.toString(ns));   
          Integer newns[] = new Integer [ns.length];
          for(int i=0;i<ns.length;i++){
              newns[i]= ns[i];
          }
          Arrays.sort(newns, Collections.reverseOrder());
          System.out.println(Arrays.toString(newns));
  	}
  }
  ```

  + 降序使用：Arrays.sort(scores,Collections.reverseOrder());

    需要注意的是 不能使用基本类型（int,double, char），如果是int型需要改成Integer，float要改成Float

## 多维数组

### 二维数组

+ 二维数组就是数组的数组。

+ 定义一个二维数组如下

  ```java
  public class Main {
      public static void main(String[] args) {
          int[][] ns = {
              { 1, 2, 3, 4 },
              { 5, 6, 7, 8 },
              { 9, 10, 11, 12 }
          };
          System.out.println(ns.length); // 3
      }
  }
  ```

  因为`ns`包含3个数组，因此，`ns.length`为`3`。实际上`ns`在内存中的结构如下：

  ```ascii
                      ┌───┬───┬───┬───┐
           ┌───┐  ┌──>│ 1 │ 2 │ 3 │ 4 │
  ns ─────>│░░░│──┘   └───┴───┴───┴───┘
           ├───┤      ┌───┬───┬───┬───┐
           │░░░│─────>│ 5 │ 6 │ 7 │ 8 │
           ├───┤      └───┴───┴───┴───┘
           │░░░│──┐   ┌───┬───┬───┬───┐
           └───┘  └──>│ 9 │10 │11 │12 │
                      └───┴───┴───┴───┘
  ```

  如果我们定义一个普通数组`arr0`，然后把`ns[0]`赋值给它：

  ```java
  public class Main {
      public static void main(String[] args) {
          int[][] ns = {
              { 1, 2, 3, 4 },
              { 5, 6, 7, 8 },
              { 9, 10, 11, 12 }
          };
          int[] arr0 = ns[0];
          System.out.println(arr0.length); // 4
      }
  }
  ```

  实际上`arr0`就获取了`ns`数组的第0个元素。因为`ns`数组的每个元素也是一个数组，因此，`arr0`指向的数组就是`{ 1, 2, 3, 4 }`。在内存中，结构如下：

  ```ascii
              arr0 ─────┐
                        ▼
                      ┌───┬───┬───┬───┐
           ┌───┐  ┌──>│ 1 │ 2 │ 3 │ 4 │
  ns ─────>│░░░│──┘   └───┴───┴───┴───┘
           ├───┤      ┌───┬───┬───┬───┐
           │░░░│─────>│ 5 │ 6 │ 7 │ 8 │
           ├───┤      └───┴───┴───┴───┘
           │░░░│──┐   ┌───┬───┬───┬───┐
           └───┘  └──>│ 9 │10 │11 │12 │
                      └───┴───┴───┴───┘
  ```

+ 访问二维数组的某个元素需要使用`array[row][col]`

+ 二维数组的每个数组元素的长度并不要求相同，例如，可以这么定义`ns`数组：

  ```java
  int[][] ns = {
      { 1, 2, 3, 4 },
      { 5, 6 },
      { 7, 8, 9 }
  };
  ```

  这个二维数组在内存中的结构如下：

  ```ascii
                      ┌───┬───┬───┬───┐
           ┌───┐  ┌──>│ 1 │ 2 │ 3 │ 4 │
  ns ─────>│░░░│──┘   └───┴───┴───┴───┘
           ├───┤      ┌───┬───┐
           │░░░│─────>│ 5 │ 6 │
           ├───┤      └───┴───┘
           │░░░│──┐   ┌───┬───┬───┐
           └───┘  └──>│ 7 │ 8 │ 9 │
                      └───┴───┴───┘
  ```

  遍历这样的数组，可以使用两层嵌套的for循环

  ```java
  for (int[] arr : ns) {
      for (int n : arr) {
          System.out.print(n);
          System.out.print(', ');
      }
      System.out.println();
  }
  ```

  或者使用Java标准库的`Arrays.deepToString()`：
  
  ```java
  import java.util.Arrays;
  
  public class Main {
      public static void main(String[] args) {
          int[][] ns = {
              { 1, 2, 3, 4 },
              { 5, 6, 7, 8 },
              { 9, 10, 11, 12 }
          };
          System.out.println(Arrays.deepToString(ns));
      }
  }
  ```

### 三维数组

+ 三维数组就是二维数组的数组。

+ 可以这么定义一个三维数组：

  ```java
  int[][][] ns = {
      {
          {1, 2, 3},
          {4, 5, 6},
          {7, 8, 9}
      },
      {
          {10, 11},
          {12, 13}
      },
      {
          {14, 15, 16},
          {17, 18}
      }
  };
  ```

  它在内存中的结构如下：

  ```ascii
                                ┌───┬───┬───┐
                     ┌───┐  ┌──>│ 1 │ 2 │ 3 │
                 ┌──>│░░░│──┘   └───┴───┴───┘
                 │   ├───┤      ┌───┬───┬───┐
                 │   │░░░│─────>│ 4 │ 5 │ 6 │
                 │   ├───┤      └───┴───┴───┘
                 │   │░░░│──┐   ┌───┬───┬───┐
          ┌───┐  │   └───┘  └──>│ 7 │ 8 │ 9 │
  ns ────>│░░░│──┘              └───┴───┴───┘
          ├───┤      ┌───┐      ┌───┬───┐
          │░░░│─────>│░░░│─────>│10 │11 │
          ├───┤      ├───┤      └───┴───┘
          │░░░│──┐   │░░░│──┐   ┌───┬───┐
          └───┘  │   └───┘  └──>│12 │13 │
                 │              └───┴───┘
                 │   ┌───┐      ┌───┬───┬───┐
                 └──>│░░░│─────>│14 │15 │16 │
                     ├───┤      └───┴───┴───┘
                     │░░░│──┐   ┌───┬───┐
                     └───┘  └──>│17 │18 │
                                └───┴───┘
  ```

+ 如果我们要访问三维数组的某个元素，例如，`ns[2][0][1]`，只需要顺着定位找到对应的最终元素`15`即可。

### N维数组

理论上，我们可以定义任意的N维数组。

但在实际应用中，除了二维数组在某些时候还能用得上，更高维度的数组很少使用。

## 命令行参数

+ Java程序的入口是`main`方法，而`main`方法可以接受一个命令行参数，它是一个`String[]`数组。

+ 这个命令行参数由JVM接收用户输入并传给`main`方法：

  ```java
  public class Main {
      public static void main(String[] args) {
          for (String arg : args) {
              System.out.println(arg);
          }
      }
  }
  ```

+ 我们可以利用接收到的命令行参数，根据不同的参数执行不同的代码。

  例如，实现一个`-version`参数，打印程序版本号：

  ```java
  public class Main {
      public static void main(String[] args) {
          for (String arg : args) {
              if ("-version".equals(arg)) {
                  System.out.println("v 1.0");
                  break;
              }
          }
      }
  }
  ```

  上面这个程序必须在命令行执行，我们先编译它：

  ```java
  $ javac Main.java
  ```

  然后，执行的时候，给它传递一个`-version`参数：

  ```java
  $ java Main -version
  v 1.0
  ```

  这样，程序就可以根据传入的命令行参数，作出不同的响应。

  