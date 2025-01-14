# 一些背景知识
## 1. JDK和JRE
JDK (Java Development Kit)：是 Java 程序开发工具包，包含 JRE 和开发人员使用的工 具。

JRE (Java Runtime Environment) ：是 Java 程序的运行时环境，包含 JVM 和运行时所 需要的核心类库。

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617019405-c684dabf-9694-4ab3-ad4c-bb90b78805f2.png)

JDK = JRE + 开发工具集（例如 Javac 编译工具等）

JRE = JVM + Java SE 标准类库



## 2. 源文件名与类名
（1）源文件名是否必须与类名一致？public呢？

```java
如果这个类不是public，那么源文件名可以和类名不一致。但是不便于代码维护。

如果这个类是public，那么要求源文件名必须与类名一致。否则编译报错。

我们建议大家，不管是否是public，都与源文件名保持一致，而且一个源文件尽量只写一个类，目的是为了好维护。
```

（2）一个源文件中是否可以有多个类？public呢？

```java
一个源文件中可以有多个类，编译后会生成多个.class字节码文件。

但是一个源文件只能有一个public的类。
```



## 3. JVM功能说明
**JVM**（`J`ava `V`irtual `M`achine ，Java虚拟机）：是一个虚拟的计算机，是Java程序的运行环境。JVM具有指令集并使用不同的存储区域，负责执行指令，管理数据、内存、寄存器。

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020906-fd9f4ee8-48c1-4f99-9957-010be5ce14cf.png)

### 功能1：实现Java程序的跨平台性
我们编写的Java代码，都运行在**JVM** 之上。正是因为有了JVM，才使得Java程序具备了跨平台性。

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020968-6b70d3b5-fc25-48f8-a36f-56e1c90a6e34.png)

### 功能2：自动内存管理(内存分配、内存回收)
+ Java程序在运行过程中，涉及到运算的`数据的分配`、`存储`等都由JVM来完成
+ Java消除了程序员回收无用内存空间的职责。提供了一种系统级线程跟踪存储空间的分配情况，在内存空间达到相应阈值时，检查并释放可被释放的存储器空间。
+ GC的自动回收，提高了内存空间的利用效率，也提高了编程人员的效率，很大程度上`减少了`因为没有释放空间而导致的`内存泄漏`。

> 面试题：
>
> Java程序还会出现内存溢出和内存泄漏问题吗？  Yes!
>



# Java安装
这里是mac的java安装记录

## 1. jdk下载
下载网址 [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/)

最新的是JDK 22，这里我们下载java 8，直接下滑找到java 8

这里下载需要注册，注册挺简单的，直接按要求填就行

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617019488-60758ece-4256-4fd1-8099-72821bfa142f.png)

## 2. 安装
由于是mac，下载后直接安装，嫌麻烦可以不用设置环境变量路径，直接在终端就能查看到java的版本



![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617019588-79151831-dc72-47cc-8589-bf73704e36c4.png)



## 3. 运行简单的hello world程序
编写简单的hello world程序

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```



命令行运行

```bash
# 运行之后生成HelloWorld.class 字节码文件
javac HelloWorld.java

# 运行
java HelloWorld

# 下面是错误的
java HelloWorld.class # 会报错
```



## 4. vscode插件
可以下载Extension Pack for Java插件，它会自动下载其他插件



## 5. 参考链接
[macOS版Java开发环境搭建](https://download.csdn.net/blog/column/11940101/135385773)（这个链接很细）



# 变量和运算符
## 1. 关键字和标识符
### 关键字
+ 定义：**被Java语言赋予了特殊含义，用做专门用途的字符串（或单词）**
+ 特点：全部关键字都是`小写字母`。
+ 官方地址： [https://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/_keywords.html)

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617019667-816a0b30-147d-4092-bc48-cb99624394f2.png)

>  说明：
>
> 1. 关键字一共`50个`，其中`const`和`goto`是`保留字`(reserved word)。
> 2. `true`，`false`，`null`不在其中，它们看起来像关键字，其实是字面量，表示特殊的布尔值和空值。
>

### 标识符
Java中变量、方法、类等要素命名时使用的字符序列，称为标识符。

技巧：凡是自己可以起名字的地方都叫标识符。

**标识符的命名规则**（必须遵守的`硬性规定`）：

```plain
> 由26个英文字母大小写，0-9 ，_或 $ 组成  
> 数字不可以开头。
> 不可以使用关键字和保留字，但能包含关键字和保留字。
> Java中严格区分大小写，长度无限制。
> 标识符不能包含空格。
```

**标识符的命名规范**（建议遵守的`软性要求`，否则工作时容易被鄙视）:

```plain
> 包名：多单词组成时所有字母都小写：xxxyyyzzz。
  例如：java.lang、com.atguigu.bean
  
> 类名、接口名：多单词组成时，所有单词的首字母大写：XxxYyyZzz
  例如：HelloWorld，String，System等
  
> 变量名、方法名：多单词组成时，第一个单词首字母小写，第二个单词开始每个单词首字母大写：xxxYyyZzz
  例如：age,name,bookName,main,binarySearch,getName
  
> 常量名：所有字母都大写。多单词时每个单词用下划线连接：XXX_YYY_ZZZ
  例如：MAX_VALUE,PI,DEFAULT_CAPACITY
```

注意：在起名字时，为了提高阅读性，要尽量有意义，“见名知意”。

> 更多细节详见《代码整洁之道_关于标识符.txt》《阿里巴巴Java开发手册-1.7.1-黄山版》
>



## 2. 变量
+ 变量的概念：
    - 内存中的一个存储区域，该区域的数据可以在同一类型范围内不断变化
    - 变量的构成包含三个要素：`数据类型`、`变量名`、`存储的值`
    - Java中变量声明的格式：`数据类型 变量名 = 变量值`![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617021031-fe727ffb-ced6-4aa9-a7e5-eaef0bedb75e.png)
+ 变量的作用：用于在内存中保存数据。
+ 使用变量注意：
    - Java中每个变量必须先声明，后使用。
    - 使用变量名来访问这块区域的数据。
    - 变量的作用域：其定义所在的一对{ }内。
    - 变量只有在其`作用域`内才有效。出了作用域，变量不可以再被调用。
    - 同一个作用域内，不能定义重名的变量。

### Java中变量的数据类型
Java中变量的数据类型分为两大类：

+ **基本数据类型**：包括 `整数类型`、`浮点数类型`、`字符类型`、`布尔类型`。 
+ **引用数据类型**：包括`数组`、 `类`、`接口`、`枚举`、`注解`、`记录`。 ![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617019724-c0edd8cc-8638-45c3-8640-37045090151f.png)

### 基本数据类型
Java各整数类型有固定的表数范围和字段长度，不受具体操作系统的影响，以保证Java程序的可移植性。

定义long类型的变量，赋值时需要以"`l`"或"`L`"作为后缀。

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617019811-0f1bc75c-fb17-4516-adea-81f12d9bc2e1.png)

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617019867-0437f42d-5471-41d8-b67c-4b3e3814f3aa.png)

+ 浮点型常量有两种表示形式：
    - 十进制数形式。如：5.12       512.0f        .512   (必须有小数点）
    - 科学计数法形式。如：5.12e2      512E2     100E-2
+ float：`单精度`，尾数可以精确到7位有效数字。很多情况下，精度很难满足需求。    
+ double：`双精度`，精度是float的两倍。通常采用此类型。
+ 定义float类型的变量，赋值时需要以"`f`"或"`F`"作为后缀。
+ Java 的浮点型`常量默认为double型`。

#### 关于浮点型精度的说明
+ 并不是所有的小数都能可以精确的用二进制浮点数表示。二进制浮点数不能精确的表示0.1、0.01、0.001这样10的负次幂。
+ 浮点类型float、double的数据不适合在`不容许舍入误差`的金融计算领域。如果需要`精确`数字计算或保留指定位数的精度，需要使用`BigDecimal类`。

#### 字符类型：char
+ char 型数据用来表示通常意义上“`字符`”（占2字节）
+ Java中的所有字符都使用Unicode编码，故一个字符可以存储一个字母，一个汉字，或其他书面语的一个字符。
+ 字符型变量的三种表现形式：

| 转义字符 | 说明 | Unicode表示方式 |
| :---: | :---: | :---: |
| `\n` | 换行符 | \u000a |
| `\t` | 制表符 | \u0009 |
| `\"` | 双引号 | \u0022 |
| `\'` | 单引号 | \u0027 |
| `\\` | 反斜线 | \u005c |
| `\b` | 退格符 | \u0008 |
| `\r` | 回车符 | \u000d |


    - **形式1：**使用单引号(' ')括起来的`单个字符`。例如：char c1 = 'a';   char c2 = '中'; char c3 =  '9';
    - **形式2：**直接使用 `Unicode值`来表示字符型常量：‘`\uXXXX`’。其中，XXXX代表一个十六进制整数。例如：\u0023 表示 '#'。
    - **形式3：**Java中还允许使用`转义字符‘\’`来将其后的字符转变为特殊字符型常量。例如：char c3 = '\n';  // '\n'表示换行符
+ char类型是可以进行运算的。因为它都对应有Unicode码，可以看做是一个数值。

#### 布尔类型：boolean
+ **boolean类型数据只有两个值：true、false，无其它。**
    - 不可以使用0或非 0 的整数替代false和true，这点和C语言不同。

### 类型提升
基本数据类型的转换规则如图所示：

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617019922-236f0ae9-02c7-4c46-8d39-d7245146dee4.png)







# 数组
获取数组的长度是使用

```java
int length = arr.length;
```

## 1. 数组初始化
### 一维数组静态初始化
如果数组变量的初始化和数组元素的赋值操作同时进行，那就称为静态初始化。

+ **一维数组声明和静态初始化格式1：**

```java
数据类型[] 数组名 = new 数据类型[]{元素1,元素2,元素3,...};

或
    
数据类型[] 数组名;
数组名 = new 数据类型[]{元素1,元素2,元素3,...};
```

    - new：关键字，创建数组使用的关键字。因为数组本身是引用数据类型，所以要用new创建数组实体。

例如，定义存储1，2，3，4，5整数的数组容器。

```java
int[] arr = new int[]{1,2,3,4,5};//正确
//或
int[] arr;
arr = new int[]{1,2,3,4,5};//正确
```

+ **一维数组声明和静态初始化格式2：**

```java
数据类型[] 数组名 = {元素1,元素2,元素3...};//必须在一个语句中完成，不能分成两个语句写
```

例如，定义存储1，2，3，4，5整数的数组容器

```java
int[] arr = {1,2,3,4,5};//正确

int[] arr;
arr = {1,2,3,4,5};//错误
```

### 一维数组动态初始化
数组变量的初始化和数组元素的赋值操作分开进行，即为动态初始化。



动态初始化中，只确定了元素的个数（即数组的长度），而元素值此时只是默认值，还并未真正赋自己期望的值。真正期望的数据需要后续单独一个一个赋值。

**格式：**

```java
数组存储的元素的数据类型[] 数组名字 = new 数组存储的元素的数据类型[长度];

或

数组存储的数据类型[] 数组名字;
数组名字 = new 数组存储的数据类型[长度];
```

+ [长度]：数组的长度，表示数组容器中可以最多存储多少个元素。
+ **注意：数组有定长特性，长度一旦指定，不可更改。**和水杯道理相同，买了一个2升的水杯，总容量就是2升是固定的。

**举例1：正确写法**

```java
int[] arr = new int[5];

int[] arr;
arr = new int[5];

```

**举例2：错误写法**

```java
int[] arr = new int[5]{1,2,3,4,5};//错误的，后面有{}指定元素列表，就不需要在[]中指定元素个数了。
```



### 二维数组静态初始化
**格式：**

```java
int[][] arr = new int[][]{{3,8,2},{2,7},{9,0,1,6}};
```

定义一个名称为arr的二维数组，二维数组中有三个一维数组

+ 每一个一维数组中具体元素也都已初始化
    - 第一个一维数组 arr[0] = {3,8,2};
    - 第二个一维数组 arr[1] = {2,7};
    - 第三个一维数组 arr[2] = {9,0,1,6};
+ 第三个一维数组的长度表示方式：arr[2].length;

> + 注意特殊写法情况：int[] x,y[]; x是一维数组，y是二维数组。
>

+ 举例1：



```java
int[][] arr = {{1,2,3},{4,5,6},{7,8,9,10}};//声明与初始化必须在一句完成

int[][] arr = new int[][]{{1,2,3},{4,5,6},{7,8,9,10}};

int[][] arr;
arr = new int[][]{{1,2,3},{4,5,6},{7,8,9,10}};

arr = new int[3][3]{{1,2,3},{4,5,6},{7,8,9,10}};//错误，静态初始化右边new 数据类型[][]中不能写数字
```

+ 举例2：



```java
public class TwoDimensionalArrayInitialize {
    public static void main(String[] args) {
        //存储多组成绩
        int[][] grades = {
                    {89,75,99,100},
                    {88,96,78,63,100,86},
                    {56,63,58},
                    {99,66,77,88}
                };

        //存储多组姓名
        String[][] names = {
            {"张三","李四", "王五", "赵六"},
            {"刘备","关羽","张飞","诸葛亮","赵云","马超"},
            {"曹丕","曹植","曹冲"},
            {"孙权","周瑜","鲁肃","黄盖"}
        };
    }
}
```

### 二维数组动态初始化
如果二维数组的每一个数据，甚至是每一行的列数，需要后期单独确定，那么就只能使用动态初始化方式了。动态初始化方式分为两种格式：

**格式1：规则二维表：每一行的列数是相同的**

```java
//（1）确定行数和列数
元素的数据类型[][] 二维数组名 = new 元素的数据类型[m][n];
    //其中，m:表示这个二维数组有多少个一维数组。或者说一共二维表有几行
    //其中，n:表示每一个一维数组的元素有多少个。或者说每一行共有一个单元格

//此时创建完数组，行数、列数确定，而且元素也都有默认值

//（2）再为元素赋新值
二维数组名[行下标][列下标] = 值;
```

举例：

```java
int[][] arr = new int[3][2];
```

+ 定义了名称为arr的二维数组
+ 二维数组中有3个一维数组
+ 每一个一维数组中有2个元素
+ 一维数组的名称分别为arr[0], arr[1], arr[2]
+ 给第一个一维数组1脚标位赋值为78写法是：`arr[0][1] = 78;`

**格式2：不规则：每一行的列数不一样**

```java
//（1）先确定总行数
元素的数据类型[][] 二维数组名 = new 元素的数据类型[总行数][];

//此时只是确定了总行数，每一行里面现在是null

//（2）再确定每一行的列数，创建每一行的一维数组
二维数组名[行下标] = new 元素的数据类型[该行的总列数];

//此时已经new完的行的元素就有默认值了，没有new的行还是null

//(3)再为元素赋值
二维数组名[行下标][列下标] = 值;
```

举例：

```java
int[][] arr = new int[3][];
```

+ 二维数组中有3个一维数组。
+ 每个一维数组都是默认初始化值null (注意：区别于格式1）
+ 可以对这个三个一维数组分别进行初始化：arr[0] = new int[3];    arr[1] = new int[1];   arr[2] = new int[2];
+ 注：`int[][]arr = new int[][3]; ` //非法



## 2. 数组排序算法
![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617019971-3bec3cbc-4a46-4cd5-b4a9-7e7a32e4bec9.png)

## 3. Arrays工具类的使用
java.util.Arrays类即为操作数组的工具类，包含了用来操作数组（比如排序和搜索）的各种方法。 比如：

+ `数组元素拼接`
    - static String toString(int[] a) ：字符串表示形式由数组的元素列表组成，括在方括号（"[]"）中。相邻元素用字符 ", "（逗号加空格）分隔。形式为：[元素1，元素2，元素3。。。]
    - static String toString(Object[] a) ：字符串表示形式由数组的元素列表组成，括在方括号（"[]"）中。相邻元素用字符 ", "（逗号加空格）分隔。元素将自动调用自己从Object继承的toString方法将对象转为字符串进行拼接，如果没有重写，则返回类型@hash值，如果重写则按重写返回的字符串进行拼接。
+ `数组排序`
    - static void sort(int[] a) ：将a数组按照从小到大进行排序
    - static void sort(int[] a, int fromIndex, int toIndex) ：将a数组的[fromIndex, toIndex)部分按照升序排列
    - static void sort(Object[] a) ：根据元素的自然顺序对指定对象数组按升序进行排序。
    - static  void sort(T[] a, Comparator<? super T> c) ：根据指定比较器产生的顺序对指定对象数组进行排序。
+ `数组元素的二分查找`
    - static int binarySearch(int[] a, int key)  、static int binarySearch(Object[] a, Object key) ：要求数组有序，在数组中查找key是否存在，如果存在返回第一次找到的下标，不存在返回负数。
+ `数组的复制`
    - static int[] copyOf(int[] original, int newLength)  ：根据original原数组复制一个长度为newLength的新数组，并返回新数组
    - static  T[] copyOf(T[] original,int newLength)：根据original原数组复制一个长度为newLength的新数组，并返回新数组
    - static int[] copyOfRange(int[] original, int from, int to) ：复制original原数组的[from,to)构成新数组，并返回新数组
    - static  T[] copyOfRange(T[] original,int from,int to)：复制original原数组的[from,to)构成新数组，并返回新数组
+ `比较两个数组是否相等`
    - static boolean equals(int[] a, int[] a2) ：比较两个数组的长度、元素是否完全相同
    - static boolean equals(Object[] a,Object[] a2)：比较两个数组的长度、元素是否完全相同
+ `填充数组`
    - static void fill(int[] a, int val) ：用val值填充整个a数组
    - static void fill(Object[] a,Object val)：用val对象填充整个a数组
    - static void fill(int[] a, int fromIndex, int toIndex, int val)：将a数组[fromIndex,toIndex)部分填充为val值
    - static void fill(Object[] a, int fromIndex, int toIndex, Object val) ：将a数组[fromIndex,toIndex)部分填充为val对象

举例：

```java
import java.util.Arrays;

public class ArrayExample {
    public static void main(String[] args) {
        // 声明和初始化数组
        int[] numbers = {5, 2, 9, 1, 6};

        // 排序数组
        Arrays.sort(numbers);
        System.out.println("Sorted array: " + Arrays.toString(numbers));

        // 查找元素
        int index = Arrays.binarySearch(numbers, 9);
        System.out.println("Index of 9: " + index);

        // 填充数组
        int[] filledArray = new int[5];
        Arrays.fill(filledArray, 8);
        System.out.println("Filled array: " + Arrays.toString(filledArray));

        // 比较数组
        boolean isEqual = Arrays.equals(numbers, filledArray);
        System.out.println("Arrays equal: " + isEqual);

        // 复制数组
        int[] copiedArray = Arrays.copyOf(numbers, numbers.length);
        System.out.println("Copied array: " + Arrays.toString(copiedArray));

        // 遍历数组
        System.out.print("Traversed array: ");
        for (int number : numbers) {
            System.out.print(number + " ");
        }
    }
}

```



# 面向对象
学习面向对象内容的三条主线

Java类及类的成员：（重点）属性、方法、构造器；（熟悉）代码块、内部类 

面向对象的特征：封装、继承、多态、（抽象） 

其他关键字的使用：this、super、package、import、static、final、interface、abstract等



## 对象的创建和使用
### 1. 类的属性和方法
属性：该类事物的状态信息。对应类中的 **成员变量**

成员变量 <=> 属性 <=> Field

行为：该类事物要做什么操作，或者基于事物的状态能做什么。对应类中的 **成员方法**

(成员)方法 <=> 函数 <=> Method

#### 成员变量
变量的分类：成员变量与局部变量

在方法体外，类体内声明的变量称为**成员变量**。 

在方法体内部等位置声明的变量称为**局部变量**。

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020031-7e7c2e26-b9e1-4fb7-a756-99be6077253a.png)



#### 成员方法
+ 方法 是类或对象行为特征的抽象，用来完成某个功能操作。在某些语言中也称为 函数 或 过程 。
+ 将功能封装为方法的目的是，可以 实现代码重用，减少冗余，简化代码
+ Java里的方法 不能独立存在 ，所有的方法必须定义在类里。







### 2. 类和对象的创建
#### 类的定义
```java
[修饰符] class 类名{

    属性声明; 
    方法声明;

}
```

#### 对象的创建
```java
//方式1：给创建的对象命名 
//把创建的对象用一个引用数据类型的变量保存起来，这样就可以反复使用这个对象了

类名 对象名 = new 类名();

//方式2：
new 类名() //也称为匿名对象
```



#### 匿名对象(anonymous object)
我们也可以不定义对象的句柄，而直接调用这个对象的方法。这样的对象叫做匿名对象。

如：`new Person().shout();`

使用情况

如果一个对象只需要进行一次方法调用，那么就可以使用匿名对象。 我们经常**将匿名对象作为实参传递给一个方法调用**。





### 3. 在谈方法
#### 1. 方法的重载（overload）
##### 概念及特点
方法重载：在同一个类中，允许存在一个以上的同名方法，只要它们的参数列表不同即可。

重载的特点：与修饰符、返回值类型无关，只看参数列表，且参数列表必须不同。(参数个数或参数类型)。调用时，根据方法参数列表的不同来区别。

重载方法调用：JVM通过方法的参数列表，调用匹配的方法。先找个数、类型最匹配的 再找个数和类型可以兼容的，如果同时多个方法可以兼容将会报错

##### 可变个数的形参
在JDK 5.0 中提供了Varargs(variable number of arguments)机制。即当定义一个方法时，形参的类型可以 确定，但是形参的个数不确定，那么可以考虑使用可变个数的形参。

格式：

方法名(参数的类型名 ...参数名)

举例：

//JDK 5.0以前：采用数组形参来定义方法，传入多个同一类型变量 public static void test(int a ,String[] books);

//JDK5.0：采用可变个数形参来定义方法，传入多个同一类型变量

`public static void test(int a ,String...books);`

特点：

1. 可变参数：方法参数部分指定类型的参数个数是可变多个：0个，1个或多个
2. 可变个数形参的方法与同名的方法之间，彼此构成重载
3. 可变参数方法的使用与方法参数部分使用数组是一致的，二者不能同时声明，否则报错。
4. 方法的参数部分有可变形参，需要放在形参声明的最后
5. 在一个方法的形参中，最多只能声明一个可变个数的形参

#### 2. 方法的参数传递机制
形参（formal parameter）：在定义方法时，方法名后面括号()中声明的变量称为形式参数，简称形参。 

实参（actual parameter）：在调用方法时，方法名后面括号()中的使用的值/变量/表达式称为实际 参数，简称实参。 

Java里方法的参数传递方式只有一种： **值传递** 。 即将实际参数值的副本（复制品）传入方法内，而参数本身不受影响。

形参是基本数据类型：**将实参基本数据类型变量的“数据值”传递给形参 形参是引用数据类型：将实参引用数据类型变量的“地址值”传递给形参。**



## 构造器(Constructor)
我们new完对象时，所有成员变量都是默认值，如果我们需要赋别的值，需要挨个为它们再赋值，太麻 烦了。我们能不能在new对象时，直接为当前对象的某个或所有成员变量直接赋值呢？ 可以，Java给我们提供了 构造器（Constructor) ，也称为 构造方法 。

```plain
[修饰符] class 类名{

    [修饰符] 构造器名(){ 
        // 实例初始化代码 
    } 
    [修饰符] 构造器名(参数列表){

        // 实例初始化代码 
    }

}
```

+ 构造器名必须与它所在的类名必须相同。 
+ 它没有返回值，所以不需要返回值类型，也不需要void。
+ 构造器的修饰符**只能是权限修饰符**，不能被其他任何修饰。比如，不能被static、final、 synchronized、abstract、native修饰，不能有return语句返回值。



## 继承(Inheritance)
### 1. 继承中的语法格式
通过 `extends` 关键字，可以声明一个类B继承另外一个类A，定义格式如下：

```java
[修饰符] class 类A {
    ...
}

[修饰符] class 类B extends 类A {
    ...
}

```

类B，称为子类、派生类(derived class)、SubClass

类A，称为父类、超类、基类(base class)、SuperClass

### 2. 继承性的细节说明
**1、子类会继承父类所有的实例变量和实例方法**

父类中声明的实例变量和实例方法代表子类事物也有这个特征。

+ 当子类对象被创建时，在堆中给对象申请内存时，就要看**子类和父类都声明了什么实例变量，这些实例变量都要分配内存。**
+ 当子类对象调用方法时，编译器会先在子类模板中看该类是否有这个方法，如果没找到，会看它的父类甚至父类的父类是否声明了这个方法，遵循`从下往上`找的顺序，找到了就停止，一直到根父类都没有找到，就会报编译错误。

所以继承意味着子类的对象除了看子类的类模板还要看父类的类模板。

**2、子类不能直接访问父类中私有的(private)的成员变量和方法**

子类虽会继承父类私有(private)的成员变量，但子类不能对继承的私有成员变量直接进行访问，可通过继承的get/set方法进行访问。



## 方法的重写（override/overwrite）
1. 注意添加@Override注解
2. 子类重写的方法`必须`和父类被重写的方法具有相同的`方法名称`、`参数列表`。
3. 子类重写的方法的返回值类型`不能大于`父类被重写的方法的返回值类型。（例如：Student < Person）。

> 注意：如果返回值类型是基本数据类型和void，那么必须是相同
>

4. 子类重写的方法使用的访问权限`不能小于`父类被重写的方法的访问权限。（public > protected > 缺省 > private）

> 注意：① 父类私有方法不能重写   ② 跨包的父类缺省的方法也不能重写
>

5. 子类方法抛出的异常不能大于父类被重写方法的异常

此外，子类与父类中同名同参数的方法必须同时声明为非static的(即为重写)，或者同时声明为static的（不是重写）。因为static方法是属于类的，子类无法覆盖父类的方法。



### 重载与重写的区别
方法的重载：方法名相同，形参列表不同。不看返回值类型。

方法的重写：见上面。





## 多态
### 1 对象的多态性
多态性，是面向对象中最重要的概念，在Java中的体现：**对象的多态性：父类的引用指向子类的对象**

格式：（父类类型：指子类继承的父类类型，或者实现的接口类型）

```java
父类类型 变量名 = 子类对象；
```

举例：

```java
Person p = new Student();

Object o = new Person();//Object类型的变量o，指向Person类型的对象

o = new Student(); //Object类型的变量o，指向Student类型的对象
```

对象的多态：在Java中，子类的对象可以替代父类的对象使用。所以，一个引用类型变量可能指向(引用)多种不同类型的对象

### 2 多态的理解
Java引用变量有两个类型：`编译时类型`和`运行时类型`。编译时类型由`声明`该变量时使用的类型决定，运行时类型由`实际赋给该变量的对象`决定。简称：**编译时，看左边；运行时，看右边。**

+ 若编译时类型和运行时类型不一致，就出现了对象的多态性(Polymorphism)
+ 多态情况下，“看左边”：看的是父类的引用（父类中不具备子类特有的方法）  
“看右边”：看的是子类的对象（实际运行的是子类重写父类的方法）

**多态的使用前提：① 类的继承关系  ② 方法的重写**



```java
public class TestPet {
    public static void main(String[] args) {
        //多态引用
        Pet pet = new Dog();
        pet.setNickname("小白");

        //多态的表现形式
        /*
        编译时看父类：只能调用父类声明的方法，不能调用子类扩展的方法；
        运行时，看“子类”，如果子类重写了方法，一定是执行子类重写的方法体；
         */
        pet.eat();//运行时执行子类Dog重写的方法
//      pet.watchHouse();//不能调用Dog子类扩展的方法

        pet = new Cat();
        pet.setNickname("雪球");
        pet.eat();//运行时执行子类Cat重写的方法
    }
}
```



### 3 向上转型或向下转型
首先，一个对象在new的时候创建是哪个类型的对象，它从头至尾都不会变。即这个对象的运行时类型，本质的类型用于不会变。但是，把这个对象赋值给不同类型的变量时，这些变量的编译时类型却不同。

**为什么要类型转换**

因为多态，就一定会有把子类对象赋值给父类变量的时候，这个时候，在`编译期间`，就会出现类型转换的现象。

但是，使用父类变量接收了子类对象之后，**我们就`不能调用`子类拥有，而父类没有的方法了。**这也是多态给我们带来的一点"小麻烦"。所以，想要调用子类特有的方法，必须做类型转换，使得`编译通过`。

向上转型：自动完成

向下转型：（子类类型）父类变量

```java
package com.atguigu.polymorphism.grammar;

public class ClassCastTest {
    public static void main(String[] args) {
        //没有类型转换
        Dog dog = new Dog();//dog的编译时类型和运行时类型都是Dog

        //向上转型
        Pet pet = new Dog();//pet的编译时类型是Pet，运行时类型是Dog
        pet.setNickname("小白");
        pet.eat();//可以调用父类Pet有声明的方法eat，但执行的是子类重写的eat方法体
//        pet.watchHouse();//不能调用父类没有的方法watchHouse

        Dog d = (Dog) pet;
        System.out.println("d.nickname = " + d.getNickname());
        d.eat();//可以调用eat方法
        d.watchHouse();//可以调用子类扩展的方法watchHouse

        Cat c = (Cat) pet;//编译通过，因为从语法检查来说，pet的编译时类型是Pet，Cat是Pet的子类，所以向下转型语法正确
        //这句代码运行报错ClassCastException，因为pet变量的运行时类型是Dog，Dog和Cat之间是没有继承关系的
    }
}
```

### 4 `instanceof` 关键字
为了避免ClassCastException的发生，Java提供了 `instanceof` 关键字，给引用变量做类型的校验。如下代码格式：

```java
//检验对象a是否是数据类型A的对象，返回值为boolean型
对象a instanceof 数据类型A 
```

+ 说明：
    - 只要用instanceof判断返回true的，那么强转为该类型就一定是安全的，不会报ClassCastException异常。
    - 如果对象a属于类A的子类B，a instanceof A值也为true。
    - 要求对象a所属的类与类A必须是子类和父类的关系，否则编译错误。



## Object 类的使用
### 1 如何理解根父类
类 `java.lang.Object`是类层次结构的根类，即所有其它类的父类。每个类都使用 `Object` 作为超类。

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617021089-c9da9892-1aee-4528-9197-be5b36d24e4d.png)

+ Object类型的变量与除Object以外的任意引用数据类型的对象都存在多态引用

```java
method(Object obj){…} //可以接收任何类作为其参数

Person o = new Person();  
method(o);

```

+ 所有对象（包括数组）都实现这个类的方法。
+ 如果一个类没有特别指定父类，那么默认则继承自Object类。例如：

```java
public class Person {
    ...
}
//等价于：
public class Person extends Object {
    ...
}
```

### 2 Object类的方法
根据JDK源代码及Object类的API文档，Object类当中包含的方法有11个。这里我们主要关注其中的6个：

#### 1、(重点)equals()
**= =：** 

+ 基本类型比较值:只要两个变量的值相等，即为true。

```java
int a=5; 
if(a==6){…}
```

+ 引用类型比较引用(是否指向同一个对象)：只有指向同一个对象时，==才返回true。

```java
Person p1=new Person();  	    
Person p2=new Person();
if (p1==p2){…}
```

    - 用“==”进行比较时，符号两边的`数据类型必须兼容`(可自动转换的基本数据类型除外)，否则编译出错

**equals()：**所有类都继承了Object，也就获得了equals()方法。还可以重写。

+ 只能比较引用类型，Object类源码中equals()的作用与“==”相同：比较是否指向同一个对象。	 ![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617021141-c67a391d-b70a-4aea-aa0b-32ceb06ba6e9.png)
+ 格式:obj1.equals(obj2)
+ 特例：当用equals()方法进行比较时，对类File、String、Date及包装类（Wrapper Class）来说，是比较类型及内容而不考虑引用的是否是同一个对象；
    - 原因：在这些类中重写了Object类的equals()方法。
+ 当自定义使用equals()时，可以重写。用于比较两个对象的“内容”是否都相等
+ 重写equals()方法的原则
    - `对称性`：如果x.equals(y)返回是“true”，那么y.equals(x)也应该返回是“true”。
    - `自反性`：x.equals(x)必须返回是“true”。
    - `传递性`：如果x.equals(y)返回是“true”，而且y.equals(z)返回是“true”，那么z.equals(x)也应该返回是“true”。
    - `一致性`：如果x.equals(y)返回是“true”，只要x和y内容一直不变，不管你重复x.equals(y)多少次，返回都是“true”。
    - 任何情况下，x.equals(null)，永远返回是“false”；    x.equals(和x不同类型的对象)永远返回是“false”。
+ **重写举例：**

```java
class User{
    private String host;
    private String username;
    private String password;
    public User(String host, String username, String password) {
        super();
        this.host = host;
        this.username = username;
        this.password = password;
    }
    public User() {
        super();
    }
    public String getHost() {
        return host;
    }
    public void setHost(String host) {
        this.host = host;
    }
    public String getUsername() {
        return username;
    }
    public void setUsername(String username) {
        this.username = username;
    }
    public String getPassword() {
        return password;
    }
    public void setPassword(String password) {
        this.password = password;
    }
    @Override
    public String toString() {
        return "User [host=" + host + ", username=" + username + ", password=" + password + "]";
    }
    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        User other = (User) obj;
        if (host == null) {
            if (other.host != null)
                return false;
        } else if (!host.equals(other.host))
            return false;
        if (password == null) {
            if (other.password != null)
                return false;
        } else if (!password.equals(other.password))
            return false;
        if (username == null) {
            if (other.username != null)
                return false;
        } else if (!username.equals(other.username))
            return false;
        return true;
    }
    
}
```

**面试题：**==和equals的区别

> 从我面试的反馈，85%的求职者“理直气壮”的回答错误…
>

+ == 既可以比较基本类型也可以比较引用类型。对于基本类型就是比较值，对于引用类型就是比较内存地址
+ equals的话，它是属于java.lang.Object类里面的方法，如果该方法没有被重写过默认也是==;我们可以看到String等类的equals方法是被重写过的，而且String类在日常开发中用的比较多，久而久之，形成了equals是比较值的错误观点。
+ 具体要看自定义类里有没有重写Object的equals方法来判断。
+ 通常情况下，重写equals方法，会比较类中的相应属性是否都相等。



#### 2、(重点)toString()
方法签名：public String toString()

① 默认情况下，toString()返回的是“对象的运行时类型 @ 对象的hashCode值的十六进制形式"

② **在进行String与其它类型数据的连接操作时，自动调用toString()方法**

```java
Date now=new Date();
System.out.println(“now=”+now);  //相当于
System.out.println(“now=”+now.toString()); 
```

③ 如果我们直接System.out.println(对象)，默认会自动调用这个对象的toString()

> 因为Java的引用数据类型的变量中存储的实际上时对象的内存地址，但是Java对程序员隐藏内存地址信息，所以不能直接将内存地址显示出来，所以当你打印对象时，JVM帮你调用了对象的toString()。
>

④ 可以根据需要在用户自定义类型中重写toString()方法  
    如String 类重写了toString()方法，返回字符串的值。

```java
s1="hello";
System.out.println(s1);//相当于System.out.println(s1.toString());
```

例如自定义的Person类：

```java
public class Person {  
    private String name;
    private int age;

    @Override
    public String toString() {
        return "Person{" + "name='" + name + '\'' + ", age=" + age + '}';
    }
}
```



## 代码块
在 Java 中，代码块可以分为静态代码块和非静态代码块。它们用于不同的初始化目的。以下是详细的解释和示例。

### 静态代码块
**静态代码块**在类加载时执行，并且只执行一次。它用于初始化类级别的资源，如静态变量。

#### 用法和特点
1. **初始化静态变量**：  
静态代码块通常用于复杂的静态变量初始化。
2. **执行一次**：  
静态代码块在类第一次加载到内存时执行一次，无论创建多少个类的实例。

#### 语法
```java
public class MyClass {
    static {
        // 静态初始化代码
        System.out.println("Static block executed.");
    }
}
```

#### 示例
```java
public class MyClass {
    static {
        System.out.println("Static block executed.");
    }
    
    public static void main(String[] args) {
        MyClass obj1 = new MyClass();
        MyClass obj2 = new MyClass();
    }
}
```

输出：

```plain
Static block executed.
```

无论创建多少个 `MyClass` 实例，静态代码块只执行一次。

### 非静态代码块
**非静态代码块**在每次创建类的实例时执行。它用于初始化实例级别的资源。

#### 用法和特点
1. **初始化实例变量**：  
非静态代码块用于**实例变量的复杂初始化。**
2. **每次实例化时执行**：  
非静态代码块在每次创建类的实例时执行。

#### 语法
```java
public class MyClass {
    {
        // 实例初始化代码
        System.out.println("Non-static block executed.");
    }
}
```

#### 示例
```java
public class MyClass {
    {
        System.out.println("Non-static block executed.");
    }
    
    public static void main(String[] args) {
        MyClass obj1 = new MyClass();
        MyClass obj2 = new MyClass();
    }
}
```

输出：

```plain
Non-static block executed.
Non-static block executed.
```

每次创建 `MyClass` 的实例，非静态代码块都会执行。

### 结合示例
以下示例展示了静态代码块和非静态代码块的结合使用：

```java
public class MyClass {
    static int staticVar;
    int instanceVar;
    
    // 静态代码块
    static {
        staticVar = 10;
        System.out.println("Static block executed. staticVar = " + staticVar);
    }
    
    // 非静态代码块
    {
        instanceVar = 20;
        System.out.println("Non-static block executed. instanceVar = " + instanceVar);
    }
    
    public MyClass() {
        System.out.println("Constructor executed.");
    }
    
    public static void main(String[] args) {
        MyClass obj1 = new MyClass();
        MyClass obj2 = new MyClass();
    }
}
```

输出：

```plain
Static block executed. staticVar = 10
Non-static block executed. instanceVar = 20
Constructor executed.
Non-static block executed. instanceVar = 20
Constructor executed.
```

### 总结
+ **静态代码块**：
    - 用于初始化静态变量或类级别的资源。
    - 只执行一次，在类加载时执行。
    - 语法：`static { /* 静态初始化代码 */ }`
+ **非静态代码块**：
    - 用于初始化实例变量或实例级别的资源。
    - 每次创建实例时执行。
    - 语法：`{ /* 实例初始化代码 */ }`

这些代码块提供了一种灵活的方式来初始化类和实例变量，在某些情况下比构造函数更方便和高效。



## 接口
在 Java 中，`interface` 关键字用于定义接口。接口是抽象类型的一种，用于指定一组方法，而不包含这些方法的实现。接口可以被类实现（通过 `implements` 关键字），并且一个类可以实现多个接口。

### 主要特点
1. **完全抽象**：接口中的方法默认都是抽象的，不包含方法体（JDK 8 引入了默认方法和静态方法，可以包含方法体）。
2. **多重继承**：一个类可以实现多个接口，这是 Java 支持多重继承的一种方式。
3. **常量**：接口中的字段默认都是 `public static final`，即常量。
4. **默认方法和静态方法**：从 Java 8 开始，接口可以包含默认方法和静态方法。

### 定义接口
```java
public interface Animal {
    void makeSound(); // 抽象方法
}
```

### 实现接口
一个类通过 `implements` 关键字实现接口，并提供接口中所有抽象方法的具体实现。

```java
public class Dog implements Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}
```

### 多重实现
一个类可以实现多个接口，用逗号分隔每个接口。

```java
public interface Animal {
    void makeSound();
}

public interface Pet {
    void play();
}

public class Dog implements Animal, Pet {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }

    @Override
    public void play() {
        System.out.println("Playing with the ball.");
    }
}
```

### 默认方法和静态方法（Java 8 及以上）
接口可以包含默认方法（有默认实现的方法）和静态方法。

```java
public interface Animal {
    void makeSound();
    
    default void sleep() {
        System.out.println("Sleeping...");
    }
    
    static void run() {
        System.out.println("Running...");
    }
}

public class Dog implements Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.makeSound(); // 输出: Bark
        dog.sleep(); // 输出: Sleeping...
        Animal.run(); // 输出: Running...
    }
}
```

### 常量
接口中的字段默认都是 `public static final`，即常量。

```java
public interface Constants {
    int MAX_VALUE = 100; // 相当于 public static final int MAX_VALUE = 100;
}
```

### 示例
以下是一个完整的示例，展示了如何定义和使用接口：

```java
public interface Animal {
    void makeSound();
}

public interface Pet {
    void play();
}

public class Dog implements Animal, Pet {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }

    @Override
    public void play() {
        System.out.println("Playing with the ball.");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.makeSound(); // 输出: Bark
        dog.play(); // 输出: Playing with the ball.
    }
}
```

### 关键点
1. **接口方法默认是 **`public`** 和 **`abstract`。
2. **接口字段默认是 **`public static final`。
3. **接口支持多重继承**。
4. **从 Java 8 开始，接口可以包含默认方法和静态方法**。

### 使用场景
1. **定义契约**：接口用于定义类必须实现的方法，确保类提供特定的功能。
2. **多重继承**：通过实现多个接口，一个类可以具有多种行为。
3. **松耦合**：接口有助于降低类之间的耦合，使代码更灵活和可扩展。

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020120-469cbef6-c050-4fdc-b5e2-956a7008f047.png)



## 内部类
在 Java 中，内部类是定义在另一个类内部的类。内部类可以帮助将逻辑相关的类组织在一起，提高代码的封装性和可读性。内部类分为四种类型：成员内部类、静态内部类、局部内部类和匿名内部类。

### 1. 成员内部类
成员内部类是最常见的内部类，定义在另一个类的内部，并作为外部类的一个成员。成员内部类可以访问外部类的所有成员，包括私有成员。

#### 示例
```java
public class OuterClass {
    private String outerField = "Outer field";

    class InnerClass {
        void display() {
            System.out.println("Inner class accessing: " + outerField);
        }
    }

    public static void main(String[] args) {
        OuterClass outer = new OuterClass();
        OuterClass.InnerClass inner = outer.new InnerClass();
        inner.display(); // 输出: Inner class accessing: Outer field
    }
}
```

### 2. 静态内部类
静态内部类使用 `static` 关键字修饰。静态内部类不能直接访问外部类的实例成员，只能访问外部类的静态成员。

#### 示例
```java
public class OuterClass {
    private static String staticOuterField = "Static outer field";

    static class StaticInnerClass {
        void display() {
            System.out.println("Static inner class accessing: " + staticOuterField);
        }
    }

    public static void main(String[] args) {
        OuterClass.StaticInnerClass inner = new OuterClass.StaticInnerClass();
        inner.display(); // 输出: Static inner class accessing: Static outer field
    }
}
```

### 3. 局部内部类
局部内部类定义在一个方法或一个作用域的内部，它们只在这个方法或作用域内有效。

#### 示例
```java
public class OuterClass {
    void methodWithLocalClass() {
        class LocalInnerClass {
            void display() {
                System.out.println("Local inner class in method");
            }
        }
        LocalInnerClass localInner = new LocalInnerClass();
        localInner.display();
    }

    public static void main(String[] args) {
        OuterClass outer = new OuterClass();
        outer.methodWithLocalClass(); // 输出: Local inner class in method
    }
}
```

### 4. 匿名内部类
匿名内部类是一种没有名字的内部类，通常用来简化代码。它们主要用于实现接口或继承类的实例化。

#### 示例
```java
public class OuterClass {
    void createAnonymousClass() {
        Animal animal = new Animal() {
            @Override
            void makeSound() {
                System.out.println("Anonymous inner class making sound");
            }
        }; //这里直接使用匿名内部类，有点像c++中的匿名函数的意思
        animal.makeSound();
    }

    public static void main(String[] args) {
        OuterClass outer = new OuterClass();
        outer.createAnonymousClass(); // 输出: Anonymous inner class making sound
    }
}

abstract class Animal {
    abstract void makeSound();
}
```

### 使用场景
1. **成员内部类**：当内部类的功能与外部类紧密相关，并且需要访问外部类的实例成员时使用。
2. **静态内部类**：当内部类不需要访问外部类的实例成员，只需要访问静态成员时使用。
3. **局部内部类**：当内部类只在一个方法或作用域内使用时，通常用于封装方法内部的复杂逻辑。
4. **匿名内部类**：当需要创建一个简单的类实现接口或继承类并且只需要一次使用时，使用匿名内部类可以简化代码。

### 关键点
1. **成员内部类**：可以访问外部类的所有成员。
2. **静态内部类**：只能访问外部类的静态成员。
3. **局部内部类**：只在定义它的方法或作用域内有效。
4. **匿名内部类**：用于简化代码，实现接口或继承类的单次使用。



## 枚举类
在 Java 中，枚举类（`enum`）是一种特殊的类，用于定义一组常量。枚举类增强了代码的可读性和安全性，特别适用于表示一组固定的常量值。枚举类是类型安全的，意味着编译器可以检查出使用错误的枚举值。

### 定义枚举类
枚举类使用 `enum` 关键字定义，枚举常量之间使用逗号分隔。

#### 示例
```java
public enum Day {
    SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY
}
```

### 使用枚举类
枚举类可以像普通类一样使用，包括在 switch 语句中使用枚举常量。

#### 示例
```java
public class EnumExample {
    public static void main(String[] args) {
        Day today = Day.MONDAY;

        switch (today) {
            case MONDAY:
                System.out.println("Today is Monday.");
                break;
            case TUESDAY:
                System.out.println("Today is Tuesday.");
                break;
            case WEDNESDAY:
                System.out.println("Today is Wednesday.");
                break;
            case THURSDAY:
                System.out.println("Today is Thursday.");
                break;
            case FRIDAY:
                System.out.println("Today is Friday.");
                break;
            case SATURDAY:
                System.out.println("Today is Saturday.");
                break;
            case SUNDAY:
                System.out.println("Today is Sunday.");
                break;
        }
    }
}
```

### 枚举类的高级功能
枚举类不仅仅是简单的常量集合，还可以包含构造函数、方法和字段。

#### 带构造函数和字段的枚举
```java
public enum Color {
    RED("FF0000"), GREEN("00FF00"), BLUE("0000FF");

    private String hexCode;

    private Color(String hexCode) {
        this.hexCode = hexCode;
    }

    public String getHexCode() {
        return hexCode;
    }
}

public class EnumExample {
    public static void main(String[] args) {
        Color color = Color.RED;
        System.out.println(color + " hex code: " + color.getHexCode());
    }
}
```

### 枚举类的方法
所有枚举类都继承自 `java.lang.Enum` 类，包含一些有用的方法：

+ `name()`：返回枚举常量的名称。
+ `ordinal()`：返回枚举常量的序数（从 0 开始）。
+ `values()`：返回包含所有枚举常量的数组。

#### 示例
```java
public class EnumMethodsExample {
    public static void main(String[] args) {
        Color color = Color.GREEN;

        System.out.println("Name: " + color.name());
        System.out.println("Ordinal: " + color.ordinal());

        Color[] colors = Color.values();
        for (Color c : colors) {
            System.out.println(c + " hex code: " + c.getHexCode());
        }
    }
}
```

### 枚举类的实现接口
枚举类可以实现接口，但不能继承其他类，因为枚举类已经继承自 `java.lang.Enum`。

#### 示例
```java
public enum Operation implements Calculator {
    ADDITION {
        @Override
        public int apply(int a, int b) {
            return a + b;
        }
    },
    SUBTRACTION {
        @Override
        public int apply(int a, int b) {
            return a - b;
        }
    };

    interface Calculator {
        int apply(int a, int b);
    }
}

public class EnumInterfaceExample {
    public static void main(String[] args) {
        int result1 = Operation.ADDITION.apply(5, 3);
        int result2 = Operation.SUBTRACTION.apply(5, 3);

        System.out.println("5 + 3 = " + result1);
        System.out.println("5 - 3 = " + result2);
    }
}
```

### 总结
+ **定义常量**：枚举类用于定义一组常量。
+ **类型安全**：编译器可以检查出错误的枚举值使用。
+ **构造函数和方法**：枚举类可以包含构造函数、方法和字段。
+ **继承**：所有枚举类继承自 `java.lang.Enum` 类，不能继承其他类，但可以实现接口。
+ **方法**：枚举类包含 `name()`, `ordinal()`, `values()` 等方法。



## 注解
在 Java 中，注解（Annotation）是一种用于在代码中添加元数据的机制。注解提供了一种形式化的方法，用于为代码中的元素（如类、方法、字段等）添加信息。这些信息可以在编译时或运行时通过反射来读取和处理。

### 常见注解
Java 提供了一些内置注解：

1. **@Override**：用于标记方法，该方法重写了父类或接口中的方法。
2. **@Deprecated**：用于标记元素，该元素已过时，不推荐使用。
3. **@SuppressWarnings**：用于抑制编译器警告。

#### 示例
```java
public class Example {

    @Override
    public String toString() {
        return "Example";
    }

    @Deprecated
    public void oldMethod() {
        System.out.println("This method is deprecated.");
    }

    @SuppressWarnings("unchecked")
    public void methodWithWarnings() {
        List rawList = new ArrayList(); // 这个会导致未经检查的转换警告
        rawList.add("Hello");
    }
}
```

### 自定义注解
你可以定义自己的注解。自定义注解使用 `@interface` 关键字定义。

#### 示例
```java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface MyAnnotation {
    String value();
    int number() default 0;
}
```

#### 使用自定义注解
```java
@MyAnnotation(value = "Test", number = 42)
public class AnnotatedClass {

    @MyAnnotation("Method level annotation")
    public void annotatedMethod() {
        System.out.println("This method is annotated.");
    }
}
```

### 注解的保留策略（Retention Policy）
注解的保留策略决定了注解在什么阶段可用：

1. **RetentionPolicy.SOURCE**：注解只在源码中保留，编译后丢弃。
2. **RetentionPolicy.CLASS**：注解在编译时保留，在运行时不可用（默认）。
3. **RetentionPolicy.RUNTIME**：注解在运行时保留，可以通过反射获取。

### 元注解
元注解用于注解其他注解，Java 提供了几个元注解：

1. **@Retention**：指定注解的保留策略。
2. **@Target**：指定注解的适用目标（如方法、字段、类等）。
3. **@Inherited**：允许子类继承父类的注解。
4. **@Documented**：将注解包含在 Javadoc 中。

#### 示例
```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

@Target({ElementType.TYPE, ElementType.METHOD})
public @interface MyTargetAnnotation {
}
```

### 处理注解
注解可以通过反射来读取和处理。

#### 示例
```java
import java.lang.reflect.Method;

public class AnnotationProcessor {
    public static void main(String[] args) {
        try {
            Class<?> cls = Class.forName("AnnotatedClass");
            if (cls.isAnnotationPresent(MyAnnotation.class)) {
                MyAnnotation annotation = cls.getAnnotation(MyAnnotation.class);
                System.out.println("Class annotation: " + annotation.value() + ", " + annotation.number());
            }

            Method method = cls.getMethod("annotatedMethod");
            if (method.isAnnotationPresent(MyAnnotation.class)) {
                MyAnnotation annotation = method.getAnnotation(MyAnnotation.class);
                System.out.println("Method annotation: " + annotation.value());
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### 示例：使用注解进行简单的单元测试框架
#### 定义注解
```java
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;

@Retention(RetentionPolicy.RUNTIME)
public @interface Test {
}
```

#### 使用注解
```java
public class TestExample {

    @Test
    public void testMethod1() {
        System.out.println("Test method 1 executed.");
    }

    @Test
    public void testMethod2() {
        System.out.println("Test method 2 executed.");
    }

    public void normalMethod() {
        System.out.println("Normal method executed.");
    }
}
```

#### 处理注解
```java
import java.lang.reflect.Method;

public class TestRunner {
    public static void main(String[] args) {
        try {
            Class<?> cls = Class.forName("TestExample");
            Object obj = cls.newInstance();

            for (Method method : cls.getDeclaredMethods()) {
                if (method.isAnnotationPresent(Test.class)) {
                    method.invoke(obj);
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### 总结
+ **注解用于在代码中添加元数据**。
+ **Java 提供了内置注解和元注解**。
+ **可以定义自定义注解**。
+ **注解的保留策略决定了注解在什么阶段可用**。
+ **注解可以通过反射来读取和处理**。



## 包装类
在 Java 中，包装类（Wrapper Class）是基本数据类型的对象表示形式。每个基本数据类型都有对应的包装类，这些包装类位于 `java.lang` 包中。包装类使得基本数据类型可以作为对象处理，从而提供了在集合框架中使用基本数据类型等功能。

### 基本数据类型和对应的包装类
| 基本数据类型 | 包装类 |
| --- | --- |
| `byte` | `Byte` |
| `short` | `Short` |
| `int` | `Integer` |
| `long` | `Long` |
| `float` | `Float` |
| `double` | `Double` |
| `char` | `Character` |
| `boolean` | `Boolean` |


### 自动装箱和拆箱
从 Java 5 开始，自动装箱（Autoboxing）和拆箱（Unboxing）简化了基本数据类型与包装类之间的转换。

+ **自动装箱**：将基本数据类型自动转换为对应的包装类对象。
+ **拆箱**：将包装类对象自动转换为对应的基本数据类型。

#### 示例
```java
public class AutoboxingExample {
    public static void main(String[] args) {
        // 自动装箱
        Integer integerObject = 100;
        Double doubleObject = 55.5;

        // 拆箱
        int intValue = integerObject;
        double doubleValue = doubleObject;

        System.out.println("Integer value: " + intValue);
        System.out.println("Double value: " + doubleValue);
    }
}
```

### 包装类的用途
1. **在集合框架中使用基本数据类型**：集合框架（如 `ArrayList`、`HashMap` 等）只能存储对象，不能直接存储基本数据类型。
2. **提供实用方法**：包装类提供了许多实用方法，用于基本数据类型的操作、转换等。

### 常用方法
包装类提供了许多常用方法，例如：

+ **解析字符串**：将字符串解析为基本数据类型。
+ **比较**：比较两个值。
+ **转换**：在不同数据类型之间转换。

#### 示例
```java
public class WrapperMethodsExample {
    public static void main(String[] args) {
        // 字符串解析
        int intValue = Integer.parseInt("123");
        double doubleValue = Double.parseDouble("45.67");

        // 比较
        Integer a = 10;
        Integer b = 20;
        int comparisonResult = Integer.compare(a, b);

        // 转换
        String intString = Integer.toString(100);
        String doubleString = Double.toString(50.5);

        System.out.println("Parsed int: " + intValue);
        System.out.println("Parsed double: " + doubleValue);
        System.out.println("Comparison result: " + comparisonResult);
        System.out.println("Integer to string: " + intString);
        System.out.println("Double to string: " + doubleString);
    }
}
```

### 包装类的常量池
对于 `Boolean`、`Byte`、`Character`（值在 `0` 到 `127` 范围内）、`Short` 和 `Integer`（值在 `-128` 到 `127` 范围内）包装类，Java 使用常量池来缓存对象，从而提高性能和减少内存消耗。

#### 示例
```java
public class WrapperPoolExample {
    public static void main(String[] args) {
        Integer a = 127;
        Integer b = 127;
        Integer c = 128;
        Integer d = 128;

        System.out.println(a == b); // 输出: true
        System.out.println(c == d); // 输出: false
    }
}
```

### 注意事项
1. **性能影响**：频繁的装箱和拆箱可能会影响性能，尤其是在大量数据处理时。
2. **空指针异常**：使用包装类时需要注意可能的空指针异常，例如 `Integer` 对象为 `null` 时，拆箱会导致空指针异常。

### 总结
+ **包装类提供基本数据类型的对象表示**。
+ **自动装箱和拆箱简化了基本数据类型和包装类之间的转换**。
+ **包装类在集合框架中使用基本数据类型、提供实用方法等方面有重要作用**。
+ **包装类的常量池用于缓存常用的对象，提高性能**。





# String 类
在 Java 中，`String` 类用于表示字符串。`String` 是一种不可变类，一旦创建，其值就不能被改变。`String` 类位于 `java.lang` 包中，提供了许多方法来操作和处理字符串。

### 创建字符串
可以通过以下几种方式创建字符串：

1. **使用字符串字面值**：

```java
String str1 = "Hello, World!";
```

2. **使用 **`new`** 关键字**：

```java
String str2 = new String("Hello, World!");
```

### 字符串的不可变性
`String` 对象一旦创建，其值就不能被改变。任何对字符串的修改操作都会创建一个新的字符串对象。

```java
String str = "Hello";
str = str.concat(", World!"); // 创建了一个新的字符串对象
System.out.println(str); // 输出: Hello, World!
```

### 常用方法
#### 字符串长度
```java
String str = "Hello, World!";
int length = str.length();
System.out.println("Length: " + length); // 输出: 13
```

#### 字符串拼接
```java
String str1 = "Hello";
String str2 = "World";
String result = str1.concat(", ").concat(str2).concat("!");
System.out.println(result); // 输出: Hello, World!
```

#### 字符串比较
```java
String str1 = "Hello";
String str2 = "hello";

// 使用 equals 方法
boolean isEqual = str1.equals(str2);
System.out.println("isEqual: " + isEqual); // 输出: false

// 忽略大小写比较
boolean isEqualIgnoreCase = str1.equalsIgnoreCase(str2);
System.out.println("isEqualIgnoreCase: " + isEqualIgnoreCase); // 输出: true
```

#### 字符串查找
```java
String str = "Hello, World!";
int index = str.indexOf("World");
System.out.println("Index: " + index); // 输出: 7
```

#### 字符串替换
```java
String str = "Hello, World!";
String replacedStr = str.replace("World", "Java");
System.out.println(replacedStr); // 输出: Hello, Java!
```

#### 字符串截取
```java
String str = "Hello, World!";
String substr = str.substring(7, 12);
System.out.println(substr); // 输出: World
```

#### 字符串分割
```java
String str = "apple,banana,cherry";
String[] fruits = str.split(",");
for (String fruit : fruits) {
    System.out.println(fruit);
}
// 输出:
// apple
// banana
// cherry
```

#### 字符串转换
```java
String str = "12345";
int num = Integer.parseInt(str);
System.out.println(num); // 输出: 12345

int anotherNum = 54321;
String anotherStr = Integer.toString(anotherNum);
System.out.println(anotherStr); // 输出: 54321
```

### 字符串池
Java 中的字符串池（String Pool）是一个特殊的内存区域，用于存储字符串字面值。当创建一个字符串字面值时，Java 会首先检查字符串池，如果池中已经存在该字符串，就会直接返回该字符串的引用，而不是创建新的字符串对象。这可以节省内存并提高性能。

```java
String str1 = "Hello";
String str2 = "Hello";
System.out.println(str1 == str2); // 输出: true

String str3 = new String("Hello");
System.out.println(str1 == str3); // 输出: false
```

### StringBuilder 和 StringBuffer
由于 `String` 是不可变的，所以每次修改字符串都会创建一个新的字符串对象。如果需要频繁修改字符串，推荐使用 `StringBuilder` 或 `StringBuffer`，它们是可变的，并提供了更高效的字符串操作方法。

+ **StringBuilder**：用于单线程环境，不是线程安全的，但性能较高。
+ **StringBuffer**：用于多线程环境，是线程安全的，但性能稍低。

#### 示例
```java
// 使用 StringBuilder
StringBuilder sb = new StringBuilder("Hello");
sb.append(", World!");
System.out.println(sb.toString()); // 输出: Hello, World!

// 使用 StringBuffer
StringBuffer sbf = new StringBuffer("Hello");
sbf.append(", World!");
System.out.println(sbf.toString()); // 输出: Hello, World!
```

### 总结
+ `String`** 类用于表示不可变的字符串**。
+ **常用方法包括长度、拼接、比较、查找、替换、截取、分割和转换**。
+ **字符串池用于节省内存和提高性能**。
+ `StringBuilder`** 和 **`StringBuffer`** 提供了可变的字符串操作，更适合频繁修改字符串的场景**。



# 一些常用类
## 1. java.lang.System类
+ System类代表系统，系统级的很多属性和控制方法都放置在该类的内部。该类位于`java.lang包`。
+ 由于该类的构造器是private的，所以无法创建该类的对象。其内部的成员变量和成员方法都是`static的`，所以也可以很方便的进行调用。
+ 成员变量   Scanner scan = new Scanner(System.in);
    - System类内部包含`in`、`out`和`err`三个成员变量，分别代表标准输入流(键盘输入)，标准输出流(显示器)和标准错误输出流(显示器)。
+ 成员方法
    - `native long currentTimeMillis()`：  
该方法的作用是返回当前的计算机时间，时间的表达格式为当前计算机时间和GMT时间(格林威治时间)1970年1月1号0时0分0秒所差的毫秒数。
    - `void exit(int status)`：  
该方法的作用是退出程序。其中status的值为0代表正常退出，非零代表异常退出。使用该方法可以在图形界面编程中实现程序的退出功能等。
    - `void gc()`：  
该方法的作用是请求系统进行垃圾回收。至于系统是否立刻回收，则取决于系统中垃圾回收算法的实现以及系统执行时的情况。
    - `String getProperty(String key)`：  
该方法的作用是获得系统中属性名为key的属性对应的值。系统中常见的属性名以及属性的作用如下表所示：![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020183-a93aeb60-9dc4-461f-9cfb-935f79c895ad.png)

## 2. java.lang.Runtime类
每个 Java 应用程序都有一个 `Runtime` 类实例，使应用程序能够与其运行的环境相连接。

`public static Runtime getRuntime()`： 返回与当前 Java 应用程序相关的运行时对象。应用程序不能创建自己的 Runtime 类实例。

`public long totalMemory()`：返回 Java 虚拟机中初始化时的内存总量。此方法返回的值可能随时间的推移而变化，这取决于主机环境。默认为物理电脑内存的1/64。

`public long maxMemory()`：返回 Java 虚拟机中最大程度能使用的内存总量。默认为物理电脑内存的1/4。

`public long freeMemory()`：回 Java 虚拟机中的空闲内存量。调用 gc 方法可能导致 freeMemory 返回值的增加。



## 3. Math
## 4. 日期
# 容器
## Java集合框架体系
Java 集合可分为 Collection 和 Map 两大体系：

+ Collection接口：用于存储一个一个的数据，也称`单列数据集合`。
    - List子接口：用来存储有序的、可以重复的数据（主要用来替换数组，"动态"数组）
        * 实现类：ArrayList(主要实现类)、LinkedList、Vector
    - Set子接口：用来存储无序的、不可重复的数据（类似于高中讲的"集合"）
        * 实现类：HashSet(主要实现类)、LinkedHashSet、TreeSet
+ Map接口：用于存储具有映射关系“key-value对”的集合，即一对一对的数据，也称`双列数据集合`。(类似于高中的函数、映射。(x1,y1),(x2,y2) ---> y = f(x) )
    - HashMap(主要实现类)、LinkedHashMap、TreeMap、Hashtable、Properties
+ JDK提供的集合API位于java.util包内
+ 图示：集合框架全图

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020239-13bad4db-f793-4c9c-a5fd-ea7167b1dd31.png)



![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020302-b2b9f42f-d3af-4293-95f0-abd563cdeb67.png)

## Collection接口及方法
+ JDK不提供此接口的任何直接实现，而是提供更具体的子接口（如：Set和List）去实现。
+ Collection 接口是 List和Set接口的父接口，该接口里定义的方法既可用于操作 Set 集合，也可用于操作 List 集合。方法如下：

### 2.1 添加
（1）add(E obj)：添加元素对象到当前集合中  
（2）addAll(Collection other)：添加other集合中的所有元素对象到当前集合中，即this = this ∪ other

### 2.2 判断
（3）int size()：获取当前集合中实际存储的元素个数  
（4）boolean isEmpty()：判断当前集合是否为空集合  
（5）boolean contains(Object obj)：判断当前集合中是否存在一个与obj对象equals返回true的元素  
（6）boolean containsAll(Collection coll)：判断coll集合中的元素是否在当前集合中都存在。即coll集合是否是当前集合的“子集”  
（7）boolean equals(Object obj)：判断当前集合与obj是否相等

### 2.3 删除
（8）void clear()：清空集合元素  
（9） boolean remove(Object obj) ：从当前集合中删除第一个找到的与obj对象equals返回true的元素。  
（10）boolean removeAll(Collection coll)：从当前集合中删除所有与coll集合中相同的元素。即this = this - this ∩ coll  
（11）boolean retainAll(Collection coll)：从当前集合中删除两个集合中不同的元素，使得当前集合仅保留与coll集合中的元素相同的元素，即当前集合中仅保留两个集合的交集，即this  = this ∩ coll；

### 2.4 其它
（12）Object[] toArray()：返回包含当前集合中所有元素的数组  
（13）hashCode()：获取集合对象的哈希值  
（14）iterator()：返回迭代器对象，用于集合遍历

## 3. Iterator(迭代器)接口
### 3.1 Iterator接口
+ 在程序开发中，经常需要遍历集合中的所有元素。针对这种需求，JDK专门提供了一个接口`java.util.Iterator`。`Iterator`接口也是Java集合中的一员，但它与`Collection`、`Map`接口有所不同。
    - Collection接口与Map接口主要用于`存储`元素
    - `Iterator`，被称为迭代器接口，本身并不提供存储对象的能力，主要用于`遍历`Collection中的元素
+ Collection接口继承了java.lang.Iterable接口，该接口有一个iterator()方法，那么所有实现了Collection接口的集合类都有一个iterator()方法，用以返回一个实现了Iterator接口的对象。
    - `public Iterator iterator()`: 获取集合对应的迭代器，用来遍历集合中的元素的。
    - 集合对象每次调用iterator()方法都得到一个全新的迭代器对象，**默认游标都在集合的第一个元素之前。**
+ Iterator接口的常用方法如下：
    - `public E next()`:返回迭代的下一个元素。
    - `public boolean hasNext()`:如果仍有元素可以迭代，则返回 true。
    - `<font style="color:#0e0e0e;">remove()</font>`<font style="color:#0e0e0e;">: 从集合中移除 next() 返回的最后一个元素（可选操作）。</font>
+ 注意：**在调用it.next()方法之前必须要调用it.hasNext()进行检测**。若不调用，且下一条记录无效，直接调用it.next()会抛出`NoSuchElementException异常`。

```java
import java.util.Iterator;
import java.util.TreeSet;

public class Main {
    public static void main(String[] args) {
        TreeSet<Integer> set = new TreeSet<>();
        set.add(3);
        set.add(1);
        set.add(2);

        Iterator<Integer> iterator = set.iterator();
        while (iterator.hasNext()) {
            Integer number = iterator.next();
            System.out.println(number);
        }
    }
}

// 另一个例子
Iterator<Integer> iterator = set.iterator();
while (iterator.hasNext()) {
    Integer number = iterator.next();
    if (number % 2 == 0) {
        iterator.remove(); // 移除偶数元素
    }
}

// 遍历剩余元素
iterator = set.iterator();
while (iterator.hasNext()) {
    Integer number = iterator.next();
    System.out.println(number);
}
```

## 4. Collection子接口1：List
### 4.1 List接口特点
+ 鉴于Java中数组用来存储数据的局限性，我们通常使用`java.util.List`替代数组
+ List集合类中`元素有序`、且`可重复`，集合中的每个元素都有其对应的顺序索引。
+ JDK API中List接口的实现类常用的有：`ArrayList`、`LinkedList`和`Vector`。

### 4.2 List接口方法
List除了从Collection集合继承的方法外，List 集合里添加了一些`根据索引`来操作集合元素的方法。

+ 插入元素
    - `void add(int index, Object ele)`:在index位置插入ele元素
    - boolean addAll(int index, Collection eles):从index位置开始将eles中的所有元素添加进来
+ 获取元素
    - `Object get(int index)`:获取指定index位置的元素
    - List subList(int fromIndex, int toIndex):返回从fromIndex到toIndex位置的子集合
+ 获取元素索引
    - int indexOf(Object obj):返回obj在集合中首次出现的位置
    - int lastIndexOf(Object obj):返回obj在当前集合中末次出现的位置
+ 删除和替换元素
    - `Object remove(int index)`:移除指定index位置的元素，并返回此元素
    - `Object set(int index, Object ele)`:设置指定index位置的元素为ele

### 4.3 List接口主要实现类：ArrayList
+ ArrayList 是 List 接口的`主要实现类`
+ 本质上，ArrayList是对象引用的一个”变长”数组
+ Arrays.asList(…) 方法返回的 List 集合，既不是 ArrayList 实例，也不是 Vector 实例。 Arrays.asList(…) 返回值是一个固定长度的 List 集合

### 4.4 List的实现类之二：LinkedList
+ 对于频繁的插入或删除元素的操作，建议使用LinkedList类，效率较高。这是由底层采用链表（双向链表）结构存储数据决定的。
+ 特有方法：
    - void addFirst(Object obj)
    - void addLast(Object obj)	
    - Object getFirst()
    - Object getLast()
    - Object removeFirst()
    - Object removeLast()

### 4.5 List的实现类之三：Vector
+ Vector 是一个`古老`的集合，JDK1.0就有了。大多数操作与ArrayList相同，**区别之处在于Vector是**`**线程安全**`**的。**
+ 在各种List中，最好把`ArrayList作为默认选择`。当插入、删除频繁时，使用LinkedList；Vector总是比ArrayList慢，所以尽量避免使用。
+ 特有方法：
    - void addElement(Object obj)
    - void insertElementAt(Object obj,int index)
    - void setElementAt(Object obj,int index)
    - void removeElement(Object obj)
    - void removeAllElements()

## 5. Collection子接口2：Set
### 5.1 Set接口概述
+ Set接口是Collection的子接口，Set接口相较于Collection接口没有提供额外的方法
+ **Set 集合不允许包含相同的元素**，如果试把两个相同的元素加入同一个 Set 集合中，则添加操作失败。
+ Set集合支持的遍历方式和Collection集合一样：foreach和Iterator。
+ Set的常用实现类有：HashSet、TreeSet、LinkedHashSet。

### 5.2 Set主要实现类：HashSet
#### 5.2.1 HashSet概述
+ HashSet 是 Set 接口的主要实现类，大多数时候使用 Set 集合时都使用这个实现类。
+ HashSet 按 Hash 算法来存储集合中的元素，因此具有很好的存储、查找、删除性能。
+ HashSet 具有以下`特点`：
    - 不能保证元素的排列顺序
    - HashSet 不是线程安全的
    - 集合元素可以是 null
+ HashSet 集合`判断两个元素相等的标准`：两个对象通过 `hashCode()` 方法得到的哈希值相等，并且两个对象的 `equals() `方法返回值为true。
+ 对于存**放在Set容器中的对象**，**对应的类一定要重写hashCode()和equals(Object obj)方法**，以实现对象相等规则。即：“相等的对象必须具有相等的散列码”。
+ HashSet集合中元素的无序性，不等同于随机性。这里的无序性与元素的添加位置有关。具体来说：我们在添加每一个元素到数组中时，具体的存储位置是由元素的hashCode()调用后返回的hash值决定的。导致在数组中每个元素不是依次紧密存放的，表现出一定的无序性。

#### 5.2.2 HashSet中添加元素的过程：
+ 第1步：当向 HashSet 集合中存入一个元素时，HashSet 会调用该对象的 hashCode() 方法得到该对象的 hashCode值，然后根据 hashCode值，通过某个散列函数决定该对象在 HashSet 底层数组中的存储位置。
+ 第2步：如果要在数组中存储的位置上没有元素，则直接添加成功。
+ 第3步：如果要在数组中存储的位置上有元素，则继续比较：

> 第2步添加成功，元素会保存在底层数组中。
>
> 第3步两种添加成功的操作，由于该底层数组的位置已经有元素了，则会通过`链表`的方式继续链接，存储。
>

    - 如果两个元素的hashCode值不相等，则添加成功；
    - 如果两个元素的hashCode()值相等，则会继续调用equals()方法：
        * 如果equals()方法结果为false，则添加成功。
        * 如果equals()方法结果为true，则添加失败。

### 5.3 Set实现类之二：LinkedHashSet
+ LinkedHashSet 是 HashSet 的子类。
+ LinkedHashSet 根据元素的 hashCode 值来决定元素的存储位置，但它同时使用`双向链表`维护元素的次序，这使得元素看起来是以`添加顺序`保存的。
+ LinkedHashSet`插入性能略低`于 HashSet，但在`迭代访问` Set 里的全部元素时有很好的性能。

### 5.4 Set实现类之三：TreeSet
#### 5.4.1 TreeSet概述
+ TreeSet 是 SortedSet 接口的实现类，TreeSet 可以按照添加的元素的指定的属性的大小顺序进行遍历。
+ TreeSet底层使用`红黑树`结构存储数据
+ 新增的方法如下： (了解)
    - Comparator comparator()
    - Object first()
    - Object last()
    - Object lower(Object e)
    - Object higher(Object e)
    - SortedSet subSet(fromElement, toElement)
    - SortedSet headSet(toElement)
    - SortedSet tailSet(fromElement)
+ TreeSet特点：不允许重复、实现排序（自然排序或定制排序）
+ TreeSet 两种排序方法：`自然排序`和`定制排序`。默认情况下，TreeSet 采用自然排序。
    - `自然排序`：TreeSet 会调用集合元素的 compareTo(Object obj) 方法来比较元素之间的大小关系，然后将集合元素按升序(默认情况)排列。
        * 如果试图把一个对象添加到 TreeSet 时，则该对象的类必须实现 Comparable 接口。
        * 实现 Comparable 的类必须实现 compareTo(Object obj) 方法，两个对象即通过 compareTo(Object obj) 方法的返回值来比较大小。
    - `定制排序`：如果元素所属的类没有实现Comparable接口，或不希望按照升序(默认情况)的方式排列元素或希望按照其它属性大小进行排序，则考虑使用定制排序。定制排序，通过Comparator接口来实现。需要重写compare(T o1,T o2)方法。
        * 利用int compare(T o1,T o2)方法，比较o1和o2的大小：如果方法返回正整数，则表示o1大于o2；如果返回0，表示相等；返回负整数，表示o1小于o2。
        * 要实现定制排序，需要将实现Comparator接口的实例作为形参传递给TreeSet的构造器。
+ 因为只有相同类的两个实例才会比较大小，所以向 TreeSet 中添加的应该是`同一个类的对象`。
+ 对于 TreeSet 集合而言，它判断`两个对象是否相等的唯一标准`是：两个对象通过 `compareTo(Object obj) 或compare(Object o1,Object o2)`方法比较返回值。返回值为0，则认为两个对象相等。

## 6. Map接口
Map接口的常用实现类：`HashMap`、`LinkedHashMap`、`TreeMap`和``Properties`。其中，HashMap是 Map 接口使用`频率最高`的实现类。

### 6.2 Map接口的常用方法
+ **添加、修改操作：**
    - Object put(Object key,Object value)：将指定key-value添加到(或修改)当前map对象中
    - void putAll(Map m):将m中的所有key-value对存放到当前map中
+ **删除操作：**
    - Object remove(Object key)：移除指定key的key-value对，并返回value
    - void clear()：清空当前map中的所有数据
+ **元素查询的操作：**
    - Object get(Object key)：获取指定key对应的value
    - boolean containsKey(Object key)：是否包含指定的key
    - boolean containsValue(Object value)：是否包含指定的value
    - int size()：返回map中key-value对的个数
    - boolean isEmpty()：判断当前map是否为空
    - boolean equals(Object obj)：判断当前map和参数对象obj是否相等
+ **元视图操作的方法：**
    - Set keySet()：返回所有key构成的Set集合
    - Collection values()：返回所有value构成的Collection集合
    - Set entrySet()：返回所有key-value对构成的Set集合

### 6.3 Map的主要实现类：HashMap
#### 6.3.1 HashMap概述
+ HashMap是 Map 接口`使用频率最高`的实现类。
+ HashMap是线程不安全的。允许添加 null 键和 null 值。
+ 存储数据采用的哈希表结构，底层使用`一维数组`+`单向链表`+`红黑树`进行key-value数据的存储。与HashSet一样，元素的存取顺序不能保证一致。
+ HashMap `判断两个key相等的标准`是：两个 key 的hashCode值相等，通过 equals() 方法返回 true。
+ HashMap `判断两个value相等的标准`是：两个 value 通过 equals() 方法返回 true。

### 6.4 Map实现类之二：LinkedHashMap
+ LinkedHashMap 是 HashMap 的子类
+ 存储数据采用的哈希表结构+链表结构，在HashMap存储结构的基础上，使用了一对`双向链表`来`记录添加元素的先后顺序`，可以保证遍历元素时，与添加的顺序一致。
+ 通过哈希表结构可以保证键的唯一、不重复，需要键所在类重写hashCode()方法、equals()方法。

### 6.5 Map实现类之三：TreeMap
+ TreeMap存储 key-value 对时，需要根据 key-value 对进行排序。TreeMap 可以保证所有的 key-value 对处于`有序状态`。
+ TreeSet底层使用`红黑树`结构存储数据
+ TreeMap 的 Key 的排序：
    - `自然排序`：TreeMap 的所有的 Key 必须实现 Comparable 接口，而且所有的 Key 应该是同一个类的对象，否则将会抛出 ClasssCastException
    - `定制排序`：创建 TreeMap 时，构造器传入一个 Comparator 对象，该对象负责对 TreeMap 中的所有 key 进行排序。此时不需要 Map 的 Key 实现 Comparable 接口
+ TreeMap判断`两个key相等的标准`：两个key通过compareTo()方法或者compare()方法返回0。

## 7. Collections工具类
参考操作数组的工具类：Arrays，Collections 是一个操作 Set、List 和 Map 等集合的工具类。

### 7.1 常用方法
Collections 中提供了一系列静态的方法对集合元素进行排序、查询和修改等操作，还提供了对集合对象设置不可变、对集合对象实现同步控制等方法（**均为static方法**）：

**排序操作：**

+ reverse(List)：反转 List 中元素的顺序
+ shuffle(List)：对 List 集合元素进行随机排序
+ sort(List)：根据元素的自然顺序对指定 List 集合元素按升序排序
+ sort(List，Comparator)：根据指定的 Comparator 产生的顺序对 List 集合元素进行排序
+ swap(List，int， int)：将指定 list 集合中的 i 处元素和 j 处元素进行交换

**查找**

+ Object max(Collection)：根据元素的自然顺序，返回给定集合中的最大元素
+ Object max(Collection，Comparator)：根据 Comparator 指定的顺序，返回给定集合中的最大元素
+ Object min(Collection)：根据元素的自然顺序，返回给定集合中的最小元素
+ Object min(Collection，Comparator)：根据 Comparator 指定的顺序，返回给定集合中的最小元素
+ int binarySearch(List list,T key)在List集合中查找某个元素的下标，但是List的元素必须是T或T的子类对象，而且必须是可比较大小的，即支持自然排序的。而且集合也事先必须是有序的，否则结果不确定。
+ int binarySearch(List list,T key,Comparator c)在List集合中查找某个元素的下标，但是List的元素必须是T或T的子类对象，而且集合也事先必须是按照c比较器规则进行排序过的，否则结果不确定。
+ int frequency(Collection c，Object o)：返回指定集合中指定元素的出现次数

**复制、替换**

+ void copy(List dest,List src)：将src中的内容复制到dest中
+ boolean replaceAll(List list，Object oldVal，Object newVal)：使用新值替换 List 对象的所有旧值
+ 提供了多个unmodifiableXxx()方法，该方法返回指定 Xxx的不可修改的视图。

**添加**

+ boolean addAll(Collection  c,T... elements)将所有指定元素添加到指定 collection 中。

**同步**

+ Collections 类中提供了多个 synchronizedXxx() 方法，该方法可使将指定集合包装成线程同步的集合，从而可以解决多线程并发访问集合时的线程安全问题：



# 泛型
所谓泛型，就是允许在定义类、接口时通过一个`标识`表示类中某个`属性的类型`或者是某个方法的`返回值或参数的类型`。这个类型参数将在使用时（例如，继承或实现这个接口、创建对象或调用方法时）确定（即传入实际的类型参数，也称为类型实参）。

**把一个集合中的内容限制为一个特定的数据类型，这就是generic背后的核心思想。**

**1、<类型>这种语法形式就叫泛型。**

+ <类型>的形式我们称为类型参数，这里的"类型"习惯上使用T表示，是Type的缩写。即：。
+ ：代表未知的数据类型，我们可以指定为，，等。
    - 类比方法的参数的概念，我们把，称为类型形参，将称为类型实参，有助于我们理解泛型
+ 这里的T，可以替换成K，V等任意字母。

**2、在哪里可以声明类型变量****<****T>**

+ 声明类或接口时，在类名或接口名后面声明泛型类型，我们把这样的类或接口称为`泛型类`或`泛型接口`。

```java
【修饰符】 class 类名<类型变量列表> 【extends 父类】 【implements 接口们】{
    
}
【修饰符】 interface 接口名<类型变量列表> 【implements 接口们】{
    
}

//例如：
public class ArrayList<E>    
public interface Map<K,V>{
    ....
}    
```

+ 声明方法时，在【修饰符】与返回值类型之间声明类型变量，我们把声明了类型变量的方法，称为泛型方法。

```java
[修饰符] <类型变量列表> 返回值类型 方法名([形参列表])[throws 异常列表]{
    //...
}

//例如：java.util.Arrays类中的
public static <T> List<T> asList(T... a){
    ....
}
```

## 通配符的使用
当我们声明一个变量/形参时，这个变量/形参的类型是一个泛型类或泛型接口，例如：Comparator类型，但是我们仍然无法确定这个泛型类或泛型接口的类型变量的具体类型，此时我们考虑使用类型通配符 ? 。

**通配符的理解**

使用类型通配符：？ 

比如：`List<?>`，`Map<?,?>`

            `List<?>`是`List<String>`、`List<Object>`等各种泛型List的父类。

**通配符的读与写**

**写操作：**

将任意元素加入到其中不是类型安全的：

```java
Collection<?> c = new ArrayList<String>();

c.add(new Object()); // 编译时错误
```

因为我们不知道c的元素类型，我们不能向其中添加对象。add方法有类型参数E作为集合的元素类型。我们传给add的任何参数都必须是一个未知类型的子类。因为我们不知道那是什么类型，所以我们无法传任何东西进去。

唯一可以插入的元素是null，因为它是所有引用类型的默认值。

**读操作：**

另一方面，读取List<?>的对象list中的元素时，永远是安全的，因为不管 list 的真实类型是什么，它包含的都是Object。

举例1：

```java
public class TestWildcard {
    public static void m4(Collection<?> coll){
        for (Object o : coll) {
            System.out.println(o);
        }
    }
}
```

举例2：

```java
public static void main(String[] args) {
    List<?> list = null;
    list = new ArrayList<String>();
    list = new ArrayList<Double>();
    // list.add(3);//编译不通过
    list.add(null);

    List<String> l1 = new ArrayList<String>();
    List<Integer> l2 = new ArrayList<Integer>();
    l1.add("尚硅谷");
    l2.add(15);
    read(l1);
    read(l2);
}

public static void read(List<?> list) {
    for (Object o : list) {
        System.out.println(o);
    }
}

```



# 文件和IO流
## 1. File类
### 1.1 file的实例化
`File` 类可以通过以下几种方式进行实例化：

1. **通过文件路径实例化**：

```java
File file = new File("path/to/file.txt");
```

2. **通过目录和文件名实例化**：

```java
File dir = new File("path/to");
File file = new File(dir, "file.txt");
```

3. **通过父路径和子路径名实例化**：

```java
File file = new File("path/to", "file.txt");
```

### 1.2 file的常用方法
#### 1、获取文件和目录基本信息
+ public String getName() ：获取名称
+ public String getPath() ：获取路径
+ `public String getAbsolutePath()`：获取绝对路径
+ public File getAbsoluteFile()：获取绝对路径表示的文件
+ `public String getParent()`：获取上层文件目录路径。若无，返回null
+ public long length() ：获取文件长度（即：字节数）。不能获取目录的长度。
+ public long lastModified() ：获取最后一次的修改时间，毫秒值

> 如果File对象代表的文件或目录存在，则File对象实例初始化时，就会用硬盘中对应文件或目录的属性信息（例如，时间、类型等）为File对象的属性赋值，否则除了路径和名称，File对象的其他属性将会保留默认值。
>

#### 2、列出目录的下一级
+ public String[] list() ：返回一个String数组，表示该File目录中的所有子文件或目录。
+ public File[] listFiles() ：返回一个File数组，表示该File目录中的所有的子文件或目录。

#### 3、File类的重命名功能
+ public boolean renameTo(File dest):把文件重命名为指定的文件路径。

#### 4、判断功能的方法
+ `public boolean exists()` ：此File表示的文件或目录是否实际存在。
+ `public boolean isDirectory()` ：此File表示的是否为目录。
+ `public boolean isFile()` ：此File表示的是否为文件。
+ public boolean canRead() ：判断是否可读
+ public boolean canWrite() ：判断是否可写
+ public boolean isHidden() ：判断是否隐藏

> 如果文件或目录不存在，那么exists()、isFile()和isDirectory()都是返回true
>

#### 5、创建、删除功能
+ `public boolean createNewFile()` ：创建文件。若文件存在，则不创建，返回false。
+ `public boolean mkdir()` ：创建文件目录。如果此文件目录存在，就不创建了。如果此文件目录的上层目录不存在，也不创建。
+ `public boolean mkdirs()` ：创建文件目录。如果上层文件目录不存在，一并创建。
+ `public boolean delete()` ：删除文件或者文件夹  
删除注意事项：① Java中的删除不走回收站。② 要删除一个文件目录，请注意该文件目录内不能包含文件或者文件目录。

> API中说明：delete方法，如果此File表示目录，则目录必须为空才能删除。
>



## 2. IO流
### 2.1 字节流和字符流的区别
**字节流（Byte Stream）**

+ **数据单位**：字节流以 **8-bit** 字节为单位处理数据。
+ **适用范围**：适用于任何类型的文件，包括文本文件和二进制文件（如图像、音频、视频等）。
+ **常用类**：`InputStream` 和 `OutputStream` 及其子类（如 `FileInputStream`、`FileOutputStream`、`BufferedInputStream`、`BufferedOutputStream` 等）。

**字符流（Character Stream）**

+ **数据单位**：字符流以 **16-bit** 字符为单位处理数据。Java 中的字符是基于 Unicode 编码的，每个字符占用 2 个字节（16 位）。
+ **适用范围**：适用于处理文本数据。字符流会自动进行字符编码和解码，因此特别适合处理基于字符的文件（如文本文件）。
+ **常用类**：`Reader` 和 `Writer` 及其子类（如 `FileReader`、`FileWriter`、`BufferedReader`、`BufferedWriter` 等）。

**字节流与字符流的对比**

| 特性 | 字节流（Byte Stream） | 字符流（Character Stream） |
| --- | --- | --- |
| 数据单位 | 8-bit 字节 | 16-bit 字符 |
| 适用范围 | 适用于所有文件类型（包括二进制文件） | 适用于文本文件 |
| 常用基类 | `InputStream` 和 `OutputStream` | `Reader` 和 `Writer` |
| 常用子类 | `FileInputStream`、`FileOutputStream`、`BufferedInputStream`、`BufferedOutputStream` | `FileReader`、`FileWriter`、`BufferedReader`、`BufferedWriter` |
| 处理方式 | 不进行字符编码和解码，需要手动处理编码问题 | 自动处理字符编码和解码 |


### 2.2 流的API
+ Java的IO流共涉及40多个类，实际上非常规则，都是从如下4个抽象基类派生的。

| （抽象基类） | 输入流 | 输出流 |
| :---: | :---: | :---: |
| 字节流 | InputStream | OutputStream |
| 字符流 | Reader | Writer |


+ 由这四个类派生出来的子类名称都是以其父类名作为子类名后缀。

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020479-9c58089c-bdae-47ae-9935-865017f08f5d.png)

**常用的节点流：** 　

+ 文件流： FileInputStream、FileOutputStrean、FileReader、FileWriter 
+ 字节/字符数组流： ByteArrayInputStream、ByteArrayOutputStream、CharArrayReader、CharArrayWriter 
    - 对数组进行处理的节点流（对应的不再是文件，而是内存中的一个数组）。

**常用处理流：**

+ 缓冲流：BufferedInputStream、BufferedOutputStream、BufferedReader、BufferedWriter
    - 作用：增加缓冲功能，避免频繁读写硬盘，进而提升读写效率。
+ 转换流：InputStreamReader、OutputStreamReader
    - 作用：实现字节流和字符流之间的转换。
+ 对象流：ObjectInputStream、ObjectOutputStream
    - 作用：提供直接读写Java对象功能

## 3. 字符流 FileReader\FileWriter
### 3.1 Reader与Writer
Java提供一些字符流类，以字符为单位读写数据，专门用于处理文本文件。不能操作图片，视频等非文本文件。

> 常见的文本文件有如下的格式：.txt、.java、.c、.cpp、.py等
>
> 注意：.doc、.xls、.ppt这些都不是文本文件。
>

#### 3.1.1 字符输入流：Reader
`java.io.Reader`**抽象类是表示用于读取字符流的所有类的父类**，可以读取字符信息到内存中。它定义了字符输入流的基本共性功能方法。

+ `public int read()`： 从输入流读取一个字符。 虽然读取了一个字符，但是会自动提升为int类型。返回该字符的Unicode编码值。如果已经到达流末尾了，则返回-1。
+ `public int read(char[] cbuf)`： 从输入流中读取一些字符，并将它们存储到字符数组 cbuf中 。每次最多读取cbuf.length个字符。返回实际读取的字符个数。如果已经到达流末尾，没有数据可读，则返回-1。 
+ `public int read(char[] cbuf,int off,int len)`：从输入流中读取一些字符，并将它们存储到字符数组 cbuf中，从cbuf[off]开始的位置存储。每次最多读取len个字符。返回实际读取的字符个数。如果已经到达流末尾，没有数据可读，则返回-1。 
+ `public void close()` ：关闭此流并释放与此流相关联的任何系统资源。

> 注意：当完成流的操作时，必须调用close()方法，释放系统资源，否则会造成内存泄漏。
>

#### 3.1.2 字符输出流：Writer
`java.io.Writer `抽象类是表示用于写出字符流的所有类的超类，将指定的字符信息写出到目的地。它定义了字节输出流的基本共性功能方法。

+ `public void write(int c)` ：写出单个字符。
+ `public void write(char[] cbuf) `：写出字符数组。 
+ `public void write(char[] cbuf, int off, int len) `：写出字符数组的某一部分。off：数组的开始索引；len：写出的字符个数。 
+ `public void write(String str) `：写出字符串。 
+ `public void write(String str, int off, int len)` ：写出字符串的某一部分。off：字符串的开始索引；len：写出的字符个数。
+ `public void flush() `：刷新该流的缓冲。  
+ `public void close()` ：关闭此流。

> 注意：当完成流的操作时，必须调用close()方法，释放系统资源，否则会造成内存泄漏。
>

### 3.2 FileReader 与 FileWriter
#### 3.2.1 FileReader
`java.io.FileReader `类用于读取字符文件，构造时使用系统默认的字符编码和默认字节缓冲区。

+ `FileReader(File file)`： 创建一个新的 FileReader ，给定要读取的File对象。   
+ `FileReader(String fileName)`： 创建一个新的 FileReader ，给定要读取的文件的名称。

#### 3.2.2 FileWriter
`java.io.FileWriter `类用于写出字符到文件，构造时使用系统默认的字符编码和默认字节缓冲区。

+ `FileWriter(File file)`： 创建一个新的 FileWriter，给定要读取的File对象。   
+ `FileWriter(String fileName)`： 创建一个新的 FileWriter，给定要读取的文件的名称。  
+ `FileWriter(File file,boolean append)`： 创建一个新的 FileWriter，指明是否在现有文件末尾追加内容。

#### 3.2.3 小结
1. 因为出现流资源的调用，为了避免内存泄漏，**需要使用try-catch-finally处理异常**
2. **对于输入流来说，File类的对象必须在物理磁盘上存在**，否则执行就会报FileNotFoundException。如果传入的是一个目录，则会报IOException异常。
3. **对于输出流来说，File类的对象是可以不存在的。**

> 如果File类的对象不存在，则可以在输出的过程中，自动创建File类的对象  
如果File类的对象存在，  
    > 如果调用FileWriter(File file)或FileWriter(File file,false)，输出时会新建File文件覆盖已有的文件  
    > 如果调用FileWriter(File file,true)构造器，则在现有的文件末尾追加写出内容。
>

### 3.3  关于flush（刷新）
在 Java 的输入输出（I/O）操作中，`flush()` 方法用于刷新流。这意味着将缓冲区中的数据强制写出到目标设备或文件中，而不是等待缓冲区满了或者流关闭时再写出。不同的输出流类（如 `Writer`、`OutputStream`、`BufferedWriter` 等）都有 `flush()` 方法。

#### 为什么需要 `flush()`
+ **缓冲区机制**：为了提高 I/O 操作的效率，Java 的输出流通常使用缓冲区来暂存数据。只有当缓冲区满了或者流关闭时，缓冲区中的数据才会写出到目标设备或文件中。
+ **及时写出数据**：有时我们需要确保数据立即写出，例如在实时日志记录、网络通信等场景下，等待缓冲区满才写出数据是不合适的。此时可以使用 `flush()` 方法。

#### 什么时候需要 `flush()`
+ **实时日志记录**：在记录日志时，需要确保日志信息立即写出，以便及时监控系统状态。
+ **网络通信**：在网络通信中，需要确保消息立即发送到另一端，以减少延迟。
+ **频繁小块写入**：当频繁写入小块数据时，使用 `flush()` 可以确保数据及时写出，而不是等待缓冲区满。
+ `flush()` ：刷新缓冲区，流对象可以继续使用。
+ `close() `：先刷新缓冲区，然后通知系统释放资源。流对象不可以再被使用了。

注意：即便是flush()方法写出了数据，操作的最后还是要调用close方法，释放系统资源。

## 4. 字节流 FileInputStream\FileOutputStream
如果我们读取或写出的数据是非文本文件，则Reader、Writer就无能为力了，必须使用字节流。

### 4.1 InputStream和OutputStream
#### 4.1.1 字节输入流：InputStream
`java.io.InputStream `抽象类是表示字节输入流的所有类的超类，可以读取字节信息到内存中。它定义了字节输入流的基本共性功能方法。

+ `public int read()`： 从输入流读取一个字节。返回读取的字节值。虽然读取了一个字节，但是会自动提升为int类型。如果已经到达流末尾，没有数据可读，则返回-1。 
+ `public int read(byte[] b)`： 从输入流中读取一些字节数，并将它们存储到字节数组 b中 。每次最多读取b.length个字节。返回实际读取的字节个数。如果已经到达流末尾，没有数据可读，则返回-1。 
+ `public int read(byte[] b,int off,int len)`：从输入流中读取一些字节数，并将它们存储到字节数组 b中，从b[off]开始存储，每次最多读取len个字节 。返回实际读取的字节个数。如果已经到达流末尾，没有数据可读，则返回-1。 
+ `public void close()` ：关闭此输入流并释放与此流相关联的任何系统资源。

> 说明：close()方法，当完成流的操作时，必须调用此方法，释放系统资源。
>

#### 4.1.2 字节输出流：OutputStream
`java.io.OutputStream `抽象类是表示字节输出流的所有类的超类，将指定的字节信息写出到目的地。它定义了字节输出流的基本共性功能方法。

+ `public void write(int b)` ：将指定的字节输出流。虽然参数为int类型四个字节，但是只会保留一个字节的信息写出。
+ `public void write(byte[] b)`：将 b.length字节从指定的字节数组写入此输出流。  
+ `public void write(byte[] b, int off, int len)` ：从指定的字节数组写入 len字节，从偏移量 off开始输出到此输出流。  
+ `public void flush() ` ：刷新此输出流并强制任何缓冲的输出字节被写出。  
+ `public void close()` ：关闭此输出流并释放与此流相关联的任何系统资源。

> 说明：close()方法，当完成流的操作时，必须调用此方法，释放系统资源。
>

### 4.2 FileInputStream 与 FileOutputStream
#### 4.2.1 FileInputStream
`java.io.FileInputStream `类是文件输入流，从文件中读取字节。

+ `FileInputStream(File file)`： 通过打开与实际文件的连接来创建一个 FileInputStream ，该文件由文件系统中的 File对象 file命名。 
+ `FileInputStream(String name)`： 通过打开与实际文件的连接来创建一个 FileInputStream ，该文件由文件系统中的路径名 name命名。

#### 4.2.2 FileOutputStream
`java.io.FileOutputStream `类是文件输出流，用于将数据写出到文件。

+ `public FileOutputStream(File file)`：创建文件输出流，写出由指定的 File对象表示的文件。 
+ `public FileOutputStream(String name)`： 创建文件输出流，指定的名称为写出文件。
+ `public FileOutputStream(File file, boolean append)`：  创建文件输出流，指明是否在现有文件末尾追加内容。



## 5. 缓冲流
+ `为了提高数据读写的速度`，Java API提供了带缓冲功能的流类：缓冲流。
+ 缓冲流要“套接”在相应的节点流之上，根据数据操作单位可以把缓冲流分为：
    - **字节缓冲流**：`BufferedInputStream`，`BufferedOutputStream` 
    - **字符缓冲流**：`BufferedReader`，`BufferedWriter`
+ 缓冲流的基本原理：在创建流对象时，内部会创建一个缓冲区数组（缺省使用`8192个字节(8Kb)`的缓冲区），通过缓冲区读写，减少系统IO次数，从而提高读写的效率。

### 5.1 构造器
+ `public BufferedInputStream(InputStream in)` ：创建一个 新的字节型的缓冲输入流。 
+ `public BufferedOutputStream(OutputStream out)`： 创建一个新的字节型的缓冲输出流。

代码举例：

```java
// 创建字节缓冲输入流
BufferedInputStream bis = new BufferedInputStream(new FileInputStream("abc.jpg"));
// 创建字节缓冲输出流
BufferedOutputStream bos = new BufferedOutputStream(new FileOutputStream("abc_copy.jpg"));
```

+ `public BufferedReader(Reader in)` ：创建一个 新的字符型的缓冲输入流。 
+ `public BufferedWriter(Writer out)`： 创建一个新的字符型的缓冲输出流。

### 5.2 字符缓冲流特有方法
字符缓冲流的基本方法与普通字符流调用方式一致，不再阐述，我们来看它们具备的特有方法。

+ BufferedReader：`public String readLine()`: 读一行文字。 
+ BufferedWriter：`public void newLine()`: 写一行行分隔符,由系统属性定义符号。



## 6. 转换流
## 7. 数据流，对象流
## 8. 其他流
### 8.1 标准输入、输出流
+ System.in和System.out分别代表了系统标准的输入和输出设备
+ 默认输入设备是：键盘，输出设备是：显示器
+ System.in的类型是InputStream
+ System.out的类型是PrintStream，其是OutputStream的子类FilterOutputStream 的子类
+ 重定向：通过System类的setIn，setOut方法对默认设备进行改变。
    - public static void setIn(InputStream in)
    - public static void setOut(PrintStream out)



### 8.3 Scanner类
构造方法

+ Scanner(File source) ：构造一个新的 Scanner，它生成的值是从指定文件扫描的。 
+ Scanner(File source, String charsetName) ：构造一个新的 Scanner，它生成的值是从指定文件扫描的。 
+ Scanner(InputStream source) ：构造一个新的 Scanner，它生成的值是从指定的输入流扫描的。 
+ Scanner(InputStream source, String charsetName) ：构造一个新的 Scanner，它生成的值是从指定的输入流扫描的。

常用方法：

+ boolean hasNextXxx()： 如果通过使用nextXxx()方法，此扫描器输入信息中的下一个标记可以解释为默认基数中的一个 Xxx 值，则返回 true。
+ Xxx nextXxx()： 将输入信息的下一个标记扫描为一个Xxx





# 关键字
## 1. this关键字
+ 在Java中，this关键字不算难理解，它的作用和其词义很接近。
    - 它在方法（准确的说是实例方法或非static的方法）内部使用，表示调用该方法的对象
    - 它在构造器内部使用，表示该构造器正在初始化的对象。
+ this可以调用的结构：成员变量、方法和构造器

### 1.2 实例方法或构造器中使用当前对象的成员
在实例方法或构造器中，如果使用当前类的成员变量或成员方法可以在其前面添加this，增强程序的可读性。不过，通常我们都习惯省略this。

但是，当形参与成员变量同名时，如果在方法内或构造器内需要使用成员变量，必须添加this来表明该变量是类的成员变量。即：我们可以用this来区分`成员变量`和`局部变量`。比如：

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617021190-73b602ac-7336-4149-a20b-ed7eb79e3a73.png)

另外，使用this访问属性和方法时，如果在本类中未找到，会从父类中查找。这个在继承中会讲到。

### 1.2 同一个类中构造器互相调用
this可以作为一个类中构造器相互调用的特殊格式。

+ this()：调用本类的无参构造器
+ this(实参列表)：调用本类的有参构造器

```java
public class Student {
    private String name;
    private int age;

    // 无参构造
    public Student() {
        this("",18);//调用本类有参构造器
    }

    // 有参构造
    public Student(String name) {
        this();//调用本类无参构造器
        this.name = name;
    }
    // 有参构造
    public Student(String name,int age){
        this(name);//调用本类中有一个String参数的构造器
        this.age = age;
    }
 }
```

注意：

+ 不能出现递归调用。比如，调用自身构造器。
    - 推论：如果一个类中声明了n个构造器，则最多有 n - 1个构造器中使用了"this(形参列表)"
+ this()和this(实参列表)只能声明在构造器首行。
    - 推论：在类的一个构造器中，最多只能声明一个"this(参数列表)"



## 2. 关键字：super
### 2.1 super的理解
在Java类中使用super来调用父类中的指定操作：

+ super可用于访问父类中定义的属性
+ super可用于调用父类中定义的成员方法
+ super可用于在子类构造器中调用父类的构造器

注意：

+ 尤其当子父类出现同名成员时，可以用super表明调用的是父类中的成员
+ super的追溯不仅限于直接父类
+ super和this的用法相像，this代表本类对象的引用，super代表父类的内存空间的标识

### 2.2 super的使用场景
#### 2.2.1 子类中调用父类被重写的方法
+ 如果子类没有重写父类的方法，只要权限修饰符允许，在子类中完全可以直接调用父类的方法；
+ 如果子类重写了父类的方法，在子类中需要通过`super.`才能调用父类被重写的方法，否则默认调用的子类重写的方法

## 3. 小结：this与super
**1、this和super的意义**

this：当前对象

+ 在构造器和非静态代码块中，表示正在new的对象
+ 在实例方法中，表示调用当前方法的对象

super：引用父类声明的成员

**2、this和super的使用格式**

+ this
    - this.成员变量：表示当前对象的某个成员变量，而不是局部变量
    - this.成员方法：表示当前对象的某个成员方法，完全可以省略this.
    - this()或this(实参列表)：调用另一个构造器协助当前对象的实例化，只能在构造器首行，只会找本类的构造器，找不到就报错
+ super
    - super.成员变量：表示当前对象的某个成员变量，该成员变量在父类中声明的
    - super.成员方法：表示当前对象的某个成员方法，该成员方法在父类中声明的
    - super()或super(实参列表)：调用父类的构造器协助当前对象的实例化，只能在构造器首行，只会找直接父类的对应构造器，找不到就报错



## 4 native关键字的理解
使用native关键字说明这个方法是原生函数，也就是这个方法是用`C/C++`等非Java语言实现的，并且`被编译成了DLL`，由Java去调用。

+ 本地方法是有方法体的，用c语言编写。由于本地方法的方法体源码没有对我们开源，所以我们看不到方法体
+ 在Java中定义一个native方法时，并不提供实现体。

**1. 为什么要用native方法**

Java使用起来非常方便，然而有些层次的任务用java实现起来不容易，或者我们对程序的效率很在意时，例如：Java需要与一些底层操作系统或某些硬件交换信息时的情况。native方法正是这样一种交流机制：它为我们提供了一个非常简洁的接口，而且我们无需去了解Java应用之外的繁琐的细节。

**2. native声明的方法，对于调用者，可以当做和其他Java方法一样使用**

native method的存在并不会对其他类调用这些本地方法产生任何影响，实际上调用这些方法的其他类甚至不知道它所调用的是一个本地方法。JVM将控制调用本地方法的所有细节。



## 5.关键字：static
+ 使用范围：
    - 在Java类中，可用static修饰属性、方法、代码块、内部类
+ 被修饰后的成员具备以下特点：
    - 随着类的加载而加载
    - 优先于对象存在
    - 修饰的成员，被所有对象所共享
    - **访问权限允许时，可不创建对象，直接被类调用**

### 5.1 静态变量
#### 语法格式
使用static修饰的成员变量就是静态变量（或类变量、类属性）

```java
[修饰符] class 类{
    [其他修饰符] static 数据类型 变量名;
}
```

#### 静态变量的特点
+ 静态变量的默认值规则和实例变量一样。
+ 静态变量值是所有对象共享。
+ 静态变量在本类中，可以在任意方法、代码块、构造器中直接使用。
+ **如果权限修饰符允许，在其他类中可以通过“**`类名.静态变量`**”直接访问，也可以通过“**`对象.静态变量`**”的方式访问（但是更推荐使用类名.静态变量的方式）。**
+ **静态变量的get/set方法也静态的，当局部变量与静态变量**`重名时`**，使用“**`类名.静态变量`**”进行区分。**

### 5.2 静态方法
#### 语法格式
用static修饰的成员方法就是静态方法。

```java
[修饰符] class 类{
    [其他修饰符] static 返回值类型 方法名(形参列表){
        方法体
    }
}
```

#### 静态方法的特点
+ 静态方法在本类的任意方法、代码块、构造器中都可以直接被调用。
+ **只要权限修饰符允许，静态方法在其他类中可以通过“类名.静态方法“的方式调用。也可以通过”对象.静态方法“的方式调用（但是更推荐使用类名.静态方法的方式）。**
+ 在static方法内部只能访问类的static修饰的属性或方法，不能访问类的非static的结构。
+ **静态方法可以被子类继承，但不能被子类重写。**
+ 静态方法的调用都只看编译时类型。
+ 因为不需要实例就可以访问static方法，**因此static方法内部不能有this，也不能有super**。如果有重名问题，使用“类名.”进行区别。





## 6.final关键字
在 Java 中，`final` 关键字有多个用途，可以用来修饰变量、方法和类。它的主要作用是防止修改，具体如下：

1. **修饰变量**：
    - 当 `final` 修饰变量时，该变量的值在初始化之后不能被改变。它可以是成员变量、局部变量或者静态变量。
    - 对于引用类型变量，`final` 确保引用本身不可改变，但是引用对象的内容可以改变。
2. **修饰方法**：
    - 当 `final` 修饰方法时，该方法不能被子类重写（override）。
3. **修饰类**：
    - 当 `final` 修饰类时，该类不能被继承。

### 示例
#### 1. 修饰变量
##### 1.1 成员变量
```java
public class MyClass {
    final int instanceVar = 10;
    final static int staticVar = 20;

    public MyClass() {
        // instanceVar = 15; // 错误：无法为 final 变量赋值
    }

    public static void main(String[] args) {
        MyClass obj = new MyClass();
        System.out.println(obj.instanceVar); // 输出: 10
        System.out.println(MyClass.staticVar); // 输出: 20
    }
}
```

##### 1.2 局部变量
```java
public class MyClass {
    public static void main(String[] args) {
        final int localVar = 30;
        // localVar = 35; // 错误：无法为 final 变量赋值
        System.out.println(localVar); // 输出: 30
    }
}
```

##### 1.3 引用类型变量
```java
public class MyClass {
    public static void main(String[] args) {
        final MyClass obj = new MyClass();
        // obj = new MyClass(); // 错误：无法为 final 引用赋值
        obj.instanceMethod();
    }

    public void instanceMethod() {
        System.out.println("Instance method executed.");
    }
}
```

#### 2. 修饰方法
```java
public class ParentClass {
    public final void finalMethod() {
        System.out.println("This method cannot be overridden.");
    }
}

public class ChildClass extends ParentClass {
    // public void finalMethod() {
    //     System.out.println("Trying to override.");
    // } // 错误：无法重写 final 方法
}
```

#### 3. 修饰类
```java
public final class FinalClass {
    // 类内容
}

// public class SubClass extends FinalClass {
// } // 错误：无法继承 final 类
```

### 使用场景
1. **常量**：`final` 变量可以用来定义常量，通常与 `static` 一起使用。

```java
public class Constants {
    public static final int MAX_SIZE = 100;
}
```

2. **方法锁定**：防止子类修改某些关键方法的实现。

```java
public class BaseClass {
    public final void importantMethod() {
        // 重要的实现
    }
}
```

3. **类锁定**：防止类被继承，通常用于工具类。

```java
public final class UtilityClass {
    // 工具方法
}
```

### 总结
+ `final`** 修饰变量**：值在初始化后不能被修改。
+ `final`** 修饰方法**：方法不能被子类重写。
+ `final`** 修饰类**：类不能被继承。

`final` 关键字在保证程序安全性和稳定性方面起到了重要作用，尤其是在设计不可变对象、常量和重要方法时。



## 7. abstract关键字
在 Java 中，`abstract` 关键字用于定义抽象类和抽象方法。它的主要作用是为创建模板类和方法提供一种机制，使得类和方法可以定义而不实现，以便在子类中实现具体的行为。

### 1. 抽象类
抽象类是不能被实例化的类，通常包含一个或多个抽象方法。抽象类可以包含具体的方法（即已经实现的方法），也可以包含成员变量。

#### 定义抽象类
```java
public abstract class Animal {
    // 抽象方法（没有方法体）
    public abstract void makeSound();
    
    // 具体方法
    public void sleep() {
        System.out.println("Sleeping...");
    }
}
```

### 2. 抽象方法
抽象方法是在抽象类中声明的方法，没有方法体（实现）。子类必须重写（实现）这些抽象方法。

#### 定义抽象方法
```java
public abstract class Animal {
    // 抽象方法
    public abstract void makeSound();
}
```

### 3. 继承抽象类
具体的子类必须继承抽象类并实现所有的抽象方法。如果子类没有实现所有的抽象方法，那么子类也必须被声明为抽象类。

#### 继承抽象类并实现抽象方法
```java
public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

public class Main {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.makeSound(); // 输出: Bark
        dog.sleep(); // 输出: Sleeping...
    }
}
```

#### 继承抽象类但不实现所有抽象方法
```java
public abstract class Bird extends Animal {
    // 这个类没有实现 makeSound() 方法，所以它必须声明为抽象类
}
```

### 使用场景
1. **定义模板类**：抽象类常用于定义一组相关类的公共行为，同时允许具体的子类实现特定的行为。

```java
public abstract class Vehicle {
    public abstract void startEngine();
    public void stopEngine() {
        System.out.println("Engine stopped.");
    }
}

public class Car extends Vehicle {
    @Override
    public void startEngine() {
        System.out.println("Car engine started.");
    }
}
```

2. **策略模式和工厂模式**：抽象类在设计模式中经常被用作定义接口和实现不同的策略或产品。

### 关键点
+ **抽象类不能被实例化**。
+ **抽象类可以包含抽象方法和具体方法**。
+ **抽象方法只能在抽象类中定义**。
+ **子类必须实现所有抽象方法，除非子类也是抽象类**。

### 示例代码
以下是一个完整的示例，展示了如何使用抽象类和抽象方法：

```java
public abstract class Animal {
    public abstract void makeSound();

    public void sleep() {
        System.out.println("Sleeping...");
    }
}

public class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

public class Cat extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal dog = new Dog();
        Animal cat = new Cat();

        dog.makeSound(); // 输出: Bark
        cat.makeSound(); // 输出: Meow

        dog.sleep(); // 输出: Sleeping...
        cat.sleep(); // 输出: Sleeping...
    }
}
```

### 总结
+ `abstract` 关键字用于定义抽象类和抽象方法。
+ 抽象类可以包含抽象方法和具体方法。
+ 抽象方法必须由子类实现。
+ 抽象类不能被实例化。



# 异常
## 1. Java异常体系
### 1.1 Throwable
`java.lang.Throwable` 类是Java程序执行过程中发生的异常事件对应的类的根父类。

**Throwable中的常用方法：**

+ `public void printStackTrace()`：打印异常的详细信息。包含了异常的类型、异常的原因、异常出现的位置、在开发和调试阶段都得使用printStackTrace。
+ `public String getMessage()`：获取发生异常的原因。

### 1.2 Error 和 Exception
Throwable可分为两类：Error和Exception。分别对应着`java.lang.Error`与`java.lang.Exception`两个类。

**Error：**Java虚拟机无法解决的严重问题。如：JVM系统内部错误、资源耗尽等严重情况。一般不编写针对性的代码进行处理。

+ 例如：StackOverflowError（栈内存溢出）和OutOfMemoryError（堆内存溢出，简称OOM）。

**Exception:** 其它因编程错误或偶然的外在因素导致的一般性问题，需要使用针对性的代码进行处理，使程序继续运行。否则一旦发生异常，程序也会挂掉。例如：

+ 空指针访问
+ 试图读取不存在的文件
+ 网络连接中断
+ 数组角标越界

> 说明：
>
> 1. 无论是Error还是Exception，还有很多子类，异常的类型非常丰富。当代码运行出现异常时，特别是我们不熟悉的异常时，不要紧张，把异常的简单类名，拷贝到API中去查去认识它即可。
> 2. 我们本章讲的异常处理，其实针对的就是Exception。
>

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617021295-939a83ab-f090-4dfe-b0ec-5466a86037dd.png)

### 1.3 编译时异常和运行时异常
Java程序的执行分为编译时过程和运行时过程。有的错误只有在`运行时`才会发生。比如：除数为0，数组下标越界等。

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617021399-85430233-5fae-4469-95ce-80f06f2077cc.png)

因此，根据异常可能出现的阶段，可以将异常分为：

在 Java 中，异常是程序中发生的非正常情况。异常分为两大类：编译时异常（Checked Exception）和运行时异常（Runtime Exception）。这两类异常有不同的处理机制和应用场景。下面是它们的详细区别：

#### 编译时异常（Checked Exception）
##### 特点
+ **必须处理**：编译时异常是强制程序员在编译时必须处理的异常。程序必须显式地捕获这些异常或声明抛出，否则代码将无法编译通过。
+ **常见场景**：编译时异常通常发生在与外部资源交互时，比如文件操作、数据库连接、网络通信等。
+ **继承关系**：所有编译时异常都是 `java.lang.Exception` 类的子类，但不是 `java.lang.RuntimeException` 类的子类。

##### 示例
```java
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

public class CheckedExceptionExample {
    public static void main(String[] args) {
        try {
            File file = new File("example.txt");
            FileReader fr = new FileReader(file);
            // 读取文件内容...
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

在上面的例子中，`FileReader` 的构造方法可能会抛出 `FileNotFoundException`，这是一种编译时异常。必须通过 `try-catch` 块捕获或通过 `throws` 关键字声明抛出。

#### 运行时异常（Runtime Exception）
##### 特点
+ **非强制处理**：运行时异常是在程序运行期间可能发生的异常。编译器不要求程序员显式地捕获或声明这些异常。
+ **常见场景**：运行时异常通常是由程序中的错误引起的，比如空指针访问、数组越界、类型转换错误等。
+ **继承关系**：所有运行时异常都是 `java.lang.RuntimeException` 类及其子类。

##### 示例
```java
public class RuntimeExceptionExample {
    public static void main(String[] args) {
        String str = null;
        System.out.println(str.length()); // 会抛出 NullPointerException
    }
}
```

在上面的例子中，`str.length()` 会抛出 `NullPointerException`，这是一种运行时异常。程序员可以选择捕获或不捕获这个异常。

#### 编译时异常与运行时异常的区别
| 特性 | 编译时异常（Checked Exception） | 运行时异常（Runtime Exception） |
| --- | --- | --- |
| 强制处理 | 是，必须通过 `try-catch` 块捕获或通过 `throws` 声明 | 否，可以选择处理或不处理 |
| 发生时间 | 编译时由编译器检查 | 程序运行时发生 |
| 继承关系 | 继承自 `Exception` 类，但不包括 `RuntimeException` | 继承自 `RuntimeException` 类 |
| 常见场景 | 外部资源交互，如文件、数据库、网络等 | 程序逻辑错误，如空指针、数组越界、类型转换等 |
| 示例 | `IOException`, `SQLException`, `ClassNotFoundException` | `NullPointerException`, `ArrayIndexOutOfBoundsException`, `ClassCastException` |


![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020558-a1beaae6-2b36-44f0-9a53-48e408da4da0.png)

## 2. 常见的错误和异常
### 2.1 Error
最常见的就是VirtualMachineError，它有两个经典的子类：StackOverflowError、OutOfMemoryError。

```java
package com.atguigu.exception;

import org.junit.Test;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class TestCheckedException {
    @Test
    public void test06() {
        Thread.sleep(1000);//休眠1秒  InterruptedException
    }

    @Test
    public void test07(){
        Class c = Class.forName("java.lang.String");//ClassNotFoundException
    }

    @Test
    public void test08() {
        Connection conn = DriverManager.getConnection("....");  //SQLException
    }
    @Test
    public void test09()  {
        FileInputStream fis = new FileInputStream("尚硅谷Java秘籍.txt"); //FileNotFoundException
    }
    @Test
    public void test10() {
        File file = new File("尚硅谷Java秘籍.txt");
        FileInputStream fis = new FileInputStream(file);//FileNotFoundException
        int b = fis.read();//IOException
        while(b != -1){
            System.out.print((char)b);
            b = fis.read();//IOException
        }
        
        fis.close();//IOException
    }
}
```

### 2.2 常见的编译时异常（Checked Exception）
编译时异常是指那些必须在编译时显式捕获或声明抛出的异常。以下是一些常见的编译时异常及其示例：

#### 1. `IOException`
表示输入/输出操作失败或中断。

```java
import java.io.FileReader;
import java.io.IOException;

public class IOExceptionExample {
    public static void main(String[] args) {
        try {
            FileReader fr = new FileReader("nonexistentfile.txt");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

#### 2. `FileNotFoundException`
表示试图打开一个文件却失败了。

```java
import java.io.FileNotFoundException;
import java.io.FileReader;

public class FileNotFoundExceptionExample {
    public static void main(String[] args) {
        try {
            FileReader fr = new FileReader("nonexistentfile.txt");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

#### 3. `SQLException`
表示数据库访问出错或其他数据库访问错误。

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class SQLExceptionExample {
    public static void main(String[] args) {
        try {
            Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "username", "password");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
```

#### 4. `ClassNotFoundException`
表示找不到指定的类。

```java
public class ClassNotFoundExceptionExample {
    public static void main(String[] args) {
        try {
            Class.forName("com.example.NonExistentClass");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
    }
}
```

#### 5. `InterruptedException`
表示一个线程在等待、睡眠或其他等待状态下被中断。

```java
public class InterruptedExceptionExample {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        });
        thread.start();
        thread.interrupt();
    }
}
```

### 2.3 常见的运行时异常（Runtime Exception）
运行时异常是在程序运行期间可能发生的异常，不需要在编译时显式捕获或声明。以下是一些常见的运行时异常及其示例：

#### 1. `NullPointerException`
表示程序试图在空对象上调用方法。

```java
public class NullPointerExceptionExample {
    public static void main(String[] args) {
        String str = null;
        System.out.println(str.length()); // 会抛出 NullPointerException
    }
}
```

#### 2. `ArrayIndexOutOfBoundsException`
表示数组下标越界。

```java
public class ArrayIndexOutOfBoundsExceptionExample {
    public static void main(String[] args) {
        int[] arr = new int[5];
        System.out.println(arr[10]); // 会抛出 ArrayIndexOutOfBoundsException
    }
}
```

#### 3. `ArithmeticException`
表示数学运算错误，比如除以零。

```java
public class ArithmeticExceptionExample {
    public static void main(String[] args) {
        int result = 10 / 0; // 会抛出 ArithmeticException
    }
}
```

#### 4. `ClassCastException`
表示类型转换错误。

```java
public class ClassCastExceptionExample {
    public static void main(String[] args) {
        Object obj = new String("test");
        Integer num = (Integer) obj; // 会抛出 ClassCastException
    }
}
```

#### 5. `IllegalArgumentException`
表示传递了非法或不适当的参数。

```java
public class IllegalArgumentExceptionExample {
    public static void main(String[] args) {
        Thread thread = new Thread(null); // 会抛出 IllegalArgumentException
    }
}
```

### 总结
+ **编译时异常**：必须在编译时显式捕获或声明，包括 `IOException`、`FileNotFoundException`、`SQLException`、`ClassNotFoundException`、`InterruptedException` 等。
+ **运行时异常**：在程序运行期间可能发生，不需要在编译时显式捕获或声明，包括 `NullPointerException`、`ArrayIndexOutOfBoundsException`、`ArithmeticException`、`ClassCastException`、`IllegalArgumentException` 等。



## 3. 异常的处理
在 Java 中，异常处理是通过 `try-catch` 块、`finally` 块以及 `throws` 关键字来实现的。以下是 Java 中常见的异常处理方式的详细介绍和示例：

### 1. `try-catch` 块
`try-catch` 块用于捕获和处理可能在 `try` 块中抛出的异常。每个 `try` 块后面可以跟一个或多个 `catch` 块，来处理不同类型的异常。

#### 示例
```java
public class TryCatchExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; // 可能会抛出 ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("捕获到 ArithmeticException: " + e.getMessage());
        }
    }
}
```

### 2. `try-catch-finally` 块
`finally` 块用于在异常处理后执行清理代码，无论是否抛出异常，`finally` 块中的代码都会被执行。

#### 示例
```java
public class TryCatchFinallyExample {
    public static void main(String[] args) {
        try {
            int result = 10 / 0; // 可能会抛出 ArithmeticException
        } catch (ArithmeticException e) {
            System.out.println("捕获到 ArithmeticException: " + e.getMessage());
        } finally {
            System.out.println("这是 finally 块，无论是否抛出异常，这段代码都会执行。");
        }
    }
}
```

### 3. `try-with-resources` 语句
`try-with-resources` 语句用于自动管理资源，如文件流和数据库连接等。在 `try` 块中声明的资源会在结束时自动关闭，无需显式地在 `finally` 块中关闭资源。

#### 示例
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TryWithResourcesExample {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("捕获到 IOException: " + e.getMessage());
        }
    }
}
```

### 4. `throws` 关键字
`throws` 关键字用于在方法声明中指明该方法可能抛出的异常类型。**调用该方法的代码需要处理这些异常。**

#### 示例
```java
public class ThrowsExample {
    public static void main(String[] args) {
        try {
            methodThatThrowsException();
        } catch (Exception e) {
            System.out.println("捕获到异常: " + e.getMessage());
        }
    }

    public static void methodThatThrowsException() throws Exception {
        throw new Exception("这是一个示例异常");
    }
}
```

方法重写throws时，对于方法签名是有严格要求的。复习：

```plain
（1）方法名必须相同
（2）形参列表必须相同
（3）返回值类型
    - 基本数据类型和void：必须相同
    - 引用数据类型：<=
（4）权限修饰符：>=，而且要求父类被重写方法在子类中是可见的
（5）不能是static，final修饰的方法
```

此外，对于throws异常列表要求：

+ 如果父类被重写方法的方法签名后面没有 “throws  编译时异常类型”，那么重写方法时，方法签名后面也不能出现“throws  编译时异常类型”。
+ 如果父类被重写方法的方法签名后面有 “`throws  编译时异常类型`”，那么重写方法时，throws的编译时异常类型必须 <= 被重写方法throws的编译时异常类型，或者不throws编译时异常。
+ 方法重写，对于“`throws 运行时异常类型`”没有要求。

```java
package com.atguigu.keyword;

import java.io.IOException;

class Father{
    public void method()throws Exception{
        System.out.println("Father.method");
    }
}
class Son extends Father{
    @Override
    public void method() throws IOException,ClassCastException {
        System.out.println("Son.method");
    }
}
```



### 5. 自定义异常
在 Java 中，你可以创建自己的异常类，继承自 `Exception` 或 `RuntimeException`。

（1）要继承一个异常类型

			自定义一个编译时异常类型：自定义类继承`java.lang.Exception`。

			自定义一个运行时异常类型：自定义类继承`java.lang.RuntimeException`。

（2）建议大家提供至少两个构造器，一个是无参构造，一个是(String message)构造器。

（3）自定义异常需要提供`serialVersionUID`

1. **自定义的异常只能通过throw抛出。**
2. 自定义异常最重要的是异常类的名字和message属性。当异常出现时，可以根据名字判断异常类型。比如：`TeamException("成员已满，无法添加"); `、 `TeamException("该员工已是某团队成员");`
3. 自定义异常对象只能手动抛出。抛出后由try..catch处理，也可以甩锅throws给调用者处理。

#### `throw`关键字
+ 可以抛出的异常必须是Throwable或其子类的实例。下面的语句在编译时将会产生语法错误：

```java
throw new String("want to throw");
```

+ throw语句会导致程序执行流程被改变，throw语句是明确抛出一个异常对象，因此它`下面的代码将不会执行`。
+ 如果当前方法没有try...catch处理这个异常对象，throw语句就会`代替return语句`提前终止当前方法的执行，并返回一个异常对象给调用者。

#### 示例
```java
public class CustomExceptionExample {
    public static void main(String[] args) {
        try {
            validateAge(15);
        } catch (InvalidAgeException e) {
            System.out.println("捕获到自定义异常: " + e.getMessage());
        }
    }

    public static void validateAge(int age) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("年龄必须大于或等于 18 岁");
        }
    }
}

// 自定义异常类
class InvalidAgeException extends Exception {
    public InvalidAgeException(String message) {
        super(message);
    }
}
```

### 总结
+ `try-catch`** 块**：用于捕获和处理异常。
+ `try-catch-finally`** 块**：在处理异常后执行清理代码。
+ `try-with-resources`** 语句**：用于自动管理和关闭资源。
+ `throws`** 关键字**：用于声明方法可能抛出的异常。
+ **自定义异常**：创建自己的异常类以处理特定的异常情况。



+ Java程序的执行过程中如出现异常，会生成一个异常类对象，该异常对象将被提交给Java运行时系统，这个过程称为`抛出(throw)异常`。如果一个方法内抛出异常，该异常对象会被抛给调用者方法中处理。如果异常没有在调用者方法中处理，它继续被抛给这个调用方法的上层方法。这个过程将一直继续下去，直到异常被处理。这一过程称为`捕获(catch)异常`。**如果一个异常回到main()方法，并且main()也不处理，则程序运行终止。**
+ 如果有多个catch分支，并且多个异常类型有父子类关系，必须保证小的子异常类型在上，大的父异常类型在下。否则，报错。
+ catch中常用异常处理的方式![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617021519-920e8262-8a7d-4e1f-9366-87f461326a78.png)
    - `public String getMessage()`：获取异常的描述信息，返回字符串
    - `public void printStackTrace()`：打印异常的跟踪栈信息并输出到控制台。包含了异常的类型、异常的原因、还包括异常出现的位置，在开发和调试阶段，都得使用printStackTrace()。
+ 不论在try代码块中是否发生了异常事件，catch语句是否执行，catch语句是否有异常，**catch语句中是否有return，finally块中的语句都会被执行。**





![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020615-03ab12b4-41aa-4031-acaa-ddb451f1e005.png)







# mac vscode配置maven
## 1. maven的安装
1. 下载：[https://maven.apache.org/download.cgi](https://maven.apache.org/download.cgi)
2. 解压放到合适的位置
3. 配置环境变量

```plain
vim ~/.bash_profile

export PATH=$PATH:/User/langhang/apache-maven-3.9.6/bin

source ~/.bash_profile

# 注意，这个bash的环境变量，vs code中可能用的是zsh，则需要配置zsh的环境变量

mvn -v

```

4. 在setting.xml文件中可以配置本地仓库路径和阿里云镜像地址

```xml
<localRepository>/Users/langhang/apache-maven-3.9.8/my-maven-repository</localRepository>



<!-- 阿里云镜像 -->
    <mirror>
      <id>alimaven</id>

      <mirrorOf>central</mirrorOf>

      <name>aliyun maven</name>

      <url>http://maven.aliyun.com/nexus/content/repositories/central/</url>

    </mirror>

```



## 2. vscode的配置
![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020717-f53f5215-a60a-4290-9bb2-d42a71a2527d.png)

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020840-1d892f91-d413-4018-862e-0e4a9b2421ea.png)



参考链接：[**macbook maven下载 mac安装maven**](https://blog.51cto.com/u_12204/10287395)

[手把手教你怎么在vscode中创建maven工程（图文结合）](https://www.php.cn/faq/482947.html)

[配置 Maven 并创建项目-VScode](https://zhuanlan.zhihu.com/p/583363069)

# 啦啦啦
## 1. Scanner：键盘输入功能的实现
+ 如何从键盘获取不同类型（基本数据类型、String类型）的变量：使用Scanner类。
+ 键盘输入代码的四个步骤：
    1. 导包：`import java.util.Scanner;`
    2. 创建Scanner类型的对象：`Scanner scan = new Scanner(System.in);`
    3. 调用Scanner类的相关方法（`next() / nextXxx()`），来获取指定类型的变量
    4. 释放资源：`scan.close();`
+ 注意：需要根据相应的方法，来输入指定类型的值。如果输入的数据类型与要求的类型不匹配时，会报异常 导致程序终止。

### 1.1 各种类型的数据输入
**案例：**小明注册某交友网站，要求录入个人相关信息。如下：

请输入你的网名、你的年龄、你的体重、你是否单身、你的性别等情况。

```java
//① 导包
import java.util.Scanner;

public class ScannerTest1 {

    public static void main(String[] args) {
        //② 创建Scanner的对象
        //Scanner是一个引用数据类型，它的全名称是java.util.Scanner
        //scanner就是一个引用数据类型的变量了，赋给它的值是一个对象（对象的概念我们后面学习，暂时先这么叫）
        //new Scanner(System.in)是一个new表达式，该表达式的结果是一个对象
        //引用数据类型  变量 = 对象;
        //这个等式的意思可以理解为用一个引用数据类型的变量代表一个对象，所以这个变量的名称又称为对象名
        //我们也把scanner变量叫做scanner对象
        Scanner scanner = new Scanner(System.in);//System.in默认代表键盘输入
        
        //③根据提示，调用Scanner的方法，获取不同类型的变量
        System.out.println("欢迎光临你好我好交友网站！");
        System.out.print("请输入你的网名：");
        String name = scanner.next();

        System.out.print("请输入你的年龄：");
        int age = scanner.nextInt();

        System.out.print("请输入你的体重：");
        double weight = scanner.nextDouble();

        System.out.print("你是否单身（true/false)：");
        boolean isSingle = scanner.nextBoolean();

        System.out.print("请输入你的性别：");
        char gender = scanner.next().charAt(0);//先按照字符串接收，然后再取字符串的第一个字符（下标为0）

        System.out.println("你的基本情况如下：");
        System.out.println("网名：" + name + "\n年龄：" + age + "\n体重：" + weight + 
                           "\n单身：" + isSingle + "\n性别：" + gender);
        
        //④ 关闭资源
        scanner.close();
    }
}
```



## 2. 如何获取一个随机数
如何产生一个指定范围的随机整数？

1、Math类的random()的调用，会返回一个[0,1)范围的一个double型值

2、Math.random() * 100  --->  [0,100)  
      (int)(Math.random() * 100)	---> [0,99]  
      (int)(Math.random() * 100) + 5  ----> [5,104]

3、如何获取`[a,b]`范围内的随机整数呢？`(int)(Math.random() * (b - a + 1)) + a`

4、举例

```java
class MathRandomTest {
    public static void main(String[] args) {
        double value = Math.random();
        System.out.println(value);

        //[1,6]
        int number = (int)(Math.random() * 6) + 1; //
        System.out.println(number);
    }
}

```



## 3. 关键字：package、import的使用
### package
package，称为包，用于指明当前文件中定义的类、接口等结构**所在的包。**

**语法格式**

`package 顶层包名.子包名 ;`

说明：

+ 一个源文件只能有一个声明包的package语句，package语句作为Java源文件的第一条语句出现。若缺省该语句，则指定为无名包。
+ 同一个包下可以声明多个结构（类、接口），但是不能定义同名的结构（类、接口）。不同的包下 可以定义同名的结构（类、接口）

### import(导入)
为了使用定义在其它包中的Java类，需用import语句来显式引入指定包下所需要的类。相当于 import语 句告诉编译器到哪里去寻找这个类 。

**语法格式**

`import 包名.类名;`

+ import语句，声明在包的声明和类的声明之间。 如果需要导入多个类或接口，那么就并列显式多个import语句即可



## 4. Java的封装性
### *.1. Java如何实现数据封装
实现封装就是控制类或成员的可见性范围。这就需要依赖访问控制修饰符，也称为权限修饰符来控 制。

权限修饰符： public 、 protected 、 缺省 、 private 。具体访问范围如下：

| 修饰符 | 本类内部 | 本包内 | 其他包的子类 | 其他包非子类 |
| --- | --- | --- | --- | --- |
| private | √ | × | × | × |
| 缺省 | √ | √ | × | × |
| protected | √ | √ | √ | × |
| public | √ | √ | √ | √ |


具体修饰的结构：

外部类：public、缺省 成员变量、成员方法、构造器、成员内部类：public、protected、缺省、private

### *.2. 封装性的体现
**成员变量/属性私有化**。私有化类的成员变量，使用 private 修饰成员变量，提供公共的get和set方法，对外暴露获取和修改属性的功能。

**私有化方法**



## 5. 理解main方法的语法
**由于JVM需要调用类的main()方法，所以该方法的访问权限必须是public，又因为JVM在执行main()方法时不必创建对象，所以该方法必须是static的**，该方法接收一个String类型的数组参数，该数组中保存执行Java命令时传递给所运行的类的参数。 

又因为main() 方法是静态的，我们不能直接访问该类中的非静态成员，**必须创建该类的一个实例对象后，才能通过这个对象去访问类中的非静态成员**，这种情况，我们在之前的例子中多次碰到。

**命令行参数用法举例**

```java
public class CommandPara {
    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            System.out.println("args[" + i + "] = " + args[i]);
        }
    }
}

```

```java
//运行程序CommandPara.java
java CommandPara "Tom" "Jerry" "Shkstart"
```

```java
//输出结果
args[0] = Tom
args[1] = Jerry
args[2] = Shkstart

```

**main() 方法是静态的，必须创建该类的一个实例对象后，才能通过这个对象去访问类中的非静态成员**

```java
public class Example {
    // 非静态成员变量
    private String message;

    // 构造函数
    public Example(String message) {
        this.message = message;
    }

    // 非静态方法
    public void printMessage() {
        System.out.println(message);
    }

    // 静态方法
    public static void main(String[] args) {
        // 无法在静态上下文中直接访问非静态成员
        // System.out.println(message); // 错误
        // printMessage(); // 错误

        // 创建类的实例
        Example example = new Example("Hello, World!");
        
        // 通过实例访问非静态成员
        example.printMessage();
    }
}

```



## 6.单例模式（Singleton）
所谓类的单例设计模式，就是采取一定的方法保证在整个的软件系统中，对某个类**只能存在一个对象实例**，并且该类只提供一个取得其对象实例的方法。

**实现思路**

如果我们要让类在一个虚拟机中只能产生一个对象

1. 首先必须将`类的构造器的访问权限设置为private`，这样，就不能用new操作符在类的外部产生类的对象了，但在类内部仍可以产生该类的对象。
2. 因为在类的外部开始还无法得到类的对象，`只能调用该类的某个静态方法`以返回类内部创建的对象，静态方法只能访问类中的静态成员变量，所以，指向类内部产生的`该类对象的变量也必须定义成静态的`。

### 单例模式的两种实现方式
#### 饿汉式
```java
class Singleton {
    // 1.私有化构造器
    private Singleton() {
    }

    // 2.内部提供一个当前类的实例
    // 4.此实例也必须静态化
    private static Singleton single = new Singleton();

    // 3.提供公共的静态的方法，返回当前类的对象
    public static Singleton getInstance() {
        return single;
    }
}

```

#### 懒汉式
```java
class Singleton {
    // 1.私有化构造器
    private Singleton() {
    }
    // 2.内部提供一个当前类的实例
    // 4.此实例也必须静态化
    private static Singleton single;
    // 3.提供公共的静态的方法，返回当前类的对象
    public static Singleton getInstance() {
        if(single == null) {
            single = new Singleton();
        }
        return single;
    }
}

```

#### 饿汉式 vs 懒汉式
饿汉式：

+ 特点：`立即加载`，即在使用类的时候已经将对象创建完毕。
+ 优点：实现起来`简单`；没有多线程安全问题。
+ 缺点：当类被加载的时候，会初始化static的实例，静态变量被创建并分配内存空间，从这以后，这个static的实例便一直占着这块内存，直到类被卸载时，静态变量被摧毁，并释放所占有的内存。因此在某些特定条件下会`耗费内存`。

懒汉式：

+ 特点：`延迟加载`，即在调用静态方法时实例才被创建。
+ 优点：实现起来比较简单；当类被加载的时候，static的实例未被创建并分配内存空间，当静态方法第一次被调用时，初始化实例变量，并分配内存，因此在某些特定条件下会`节约内存`。
+ 缺点：在多线程环境中，这种实现方法是完全错误的，`线程不安全`，根本不能保证单例的唯一性。
    - 说明：在多线程章节，会将懒汉式改造成线程安全的模式。



## 7. 工厂模式
### 简单工厂模式
在简单工厂模式中创建实例的方法通常为静态（static）方法，因此简单工厂模式（**Simple Factory Pattern）**又叫作静态工厂方法模式（Static Factory Method Pattern）。简单工厂模式每增加一个产品就要增加一个具体产品类和一个对应的具体工厂类，这增加了系统的复杂度，违背了“开闭原则”。  
简单工厂模式的主要角色如下：

简单工厂（SimpleFactory）：是简单工厂模式的核心，负责实现创建所有实例的内部逻辑。工厂类的创建产品类的方法可以被外界直接调用，创建所需的产品对象。  
抽象产品（Product）：是简单工厂创建的所有对象的父类，负责描述所有实例共有的公共接口。  
具体产品（ConcreteProduct）：是简单工厂模式的创建目标。

**实现**

```java
// 抽象产品
public interface Car {
    void name();
}

// 具体产品
public class Lamborghini implements Car{
    @Override
    public void name() {
        System.out.println("兰博基尼");
    }
}

public class Porsche implements Car{
    @Override
    public void name() {
        System.out.println("保时捷");
    }
}

// 简单工厂
public class CarFactory {
    //创建产品的方法
    public static Car getCar(String car){
        if ("保时捷".equals(car)){
           return new Porsche();
        }else if ("兰博基尼".equals(car)){
           return new Lamborghini();
        }else {
            return null;
        }
    }
}


// 使用方法
public class Consumer {
    public static void main(String[] args) {

        //直接调用工厂类创建产品的方法，不需要知道具体的细节，只需要知道产品名就行
        Car car = CarFactory.getCar("兰博基尼");
        Car car1 = CarFactory.getCar("保时捷");

        car.name();//兰博基尼
        car1.name();//保时捷
    }
}

```



### 工厂方法模式
**工厂方法模式的主要角色如下。**

抽象工厂（Abstract Factory）：提供了创建产品的接口，调用者通过它访问具体工厂的工厂方法 newProduct() 来创建产品。  
具体工厂（ConcreteFactory）：主要是实现抽象工厂中的抽象方法，完成具体产品的创建。  
抽象产品（Product）：定义了产品的规范，描述了产品的主要特性和功能。  
具体产品（ConcreteProduct）：实现了抽象产品角色所定义的接口，由具体工厂来创建，它同具体工厂之间一一对应。

```java
// 抽象产品
public interface Car {
    void name();
}

// 具体产品
public class Lamborghini implements Car{
    @Override
    public void name() {
        System.out.println("兰博基尼");
    }
}

public class Porsche implements Car{
    @Override
    public void name() {
        System.out.println("保时捷");
    }
}

//抽象工厂
public interface CarFactory {
    Car getCar();
}

//具体工厂
public class LamborghiniFactory implements CarFactory{
    @Override
    public Car getCar() {
        return new Lamborghini();
    }
}

//具体工厂
public class PorscheFactory implements CarFactory{
    @Override
    public Car getCar() {
        return new Porsche();
    }
}

// 测试类
public class Consumer {
    public static void main(String[] args) {
        //调用具体工厂，由具体工厂实现
        Car car = new LamborghiniFactory().getCar();
        Car car1 = new PorscheFactory().getCar();

        car.name();//兰博基尼
        car1.name();//保时捷

    }
}


```



### 抽象工厂模式（Abstract Factory Pattern）
抽象工厂模式是一种创建型设计模式，它提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。该模式的核心思想是将对象的创建和使用分离，使得客户端代码无需知道具体对象的创建细节，只需通过工厂接口来创建所需的对象。

#### 解决的问题
1. **产品族的一致性**：抽象工厂模式用于创建一系列相关或相互依赖的对象，这些对象通常属于同一个产品族。确保创建的对象在概念上是相关的，并且在系统中是一致的。
2. **客户端与具体类解耦**：客户端代码不依赖于具体的类，而是依赖于抽象工厂接口，从而使得系统更易于维护和扩展。

#### 示例场景
假设我们正在开发一个 GUI 库，需要支持多种操作系统（例如 Windows 和 Mac）。每种操作系统都有自己的按钮和文本框风格。我们可以使用抽象工厂模式来创建这些组件，而无需在客户端代码中指定具体的类。

#### 代码示例
##### 步骤 1：定义抽象产品接口
```java
// 按钮接口
public interface Button {
    void paint();
}

// 文本框接口
public interface TextField {
    void display();
}
```

##### 步骤 2：实现具体产品类
```java
// Windows 风格的按钮
public class WindowsButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering a button in Windows style.");
    }
}

// Windows 风格的文本框
public class WindowsTextField implements TextField {
    @Override
    public void display() {
        System.out.println("Displaying a text field in Windows style.");
    }
}

// Mac 风格的按钮
public class MacButton implements Button {
    @Override
    public void paint() {
        System.out.println("Rendering a button in Mac style.");
    }
}

// Mac 风格的文本框
public class MacTextField implements TextField {
    @Override
    public void display() {
        System.out.println("Displaying a text field in Mac style.");
    }
}
```

##### 步骤 3：定义抽象工厂接口
```java
// 抽象工厂接口，定义创建按钮和文本框的方法
public interface GUIFactory {
    Button createButton();
    TextField createTextField();
}
```

##### 步骤 4：实现具体工厂类
```java
// Windows 风格的工厂类
public class WindowsFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public TextField createTextField() {
        return new WindowsTextField();
    }
}

// Mac 风格的工厂类
public class MacFactory implements GUIFactory {
    @Override
    public Button createButton() {
        return new MacButton();
    }

    @Override
    public TextField createTextField() {
        return new MacTextField();
    }
}
```

##### 步骤 5：客户端代码
```java
public class Application {
    private Button button;
    private TextField textField;

    public Application(GUIFactory factory) {
        button = factory.createButton();
        textField = factory.createTextField();
    }

    public void render() {
        button.paint();
        textField.display();
    }

    public static void main(String[] args) {
        GUIFactory factory;
        String os = "Windows"; // 或 "Mac"
        
        if (os.equals("Windows")) {
            factory = new WindowsFactory();
        } else {
            factory = new MacFactory();
        }
        
        Application app = new Application(factory);
        app.render();
    }
}
```

#### 总结
通过使用抽象工厂模式，我们实现了以下几点：

1. **产品族一致性**：确保创建的按钮和文本框都属于同一个风格（Windows 或 Mac）。
2. **客户端与具体类解耦**：客户端代码依赖于抽象工厂接口，而不是具体的实现类，使得系统更易于维护和扩展。
3. **易于扩展**：添加新的产品族（例如 Linux 风格）只需实现新的具体工厂类和产品类，而无需修改客户端代码。

抽象工厂模式适用于创建一系列相关或相互依赖的对象的场景，尤其是在需要确保不同产品之间的一致性时。



# 问题总结
## 1. java输出中System.out.println和System.err.println有什么区别？
**1. 输出流的不同**：

+ `System.out.println` 使用标准输出流 `System.out`。通常用于打印一般的输出信息。
+ `System.err.println` 使用标准错误流 `System.err`。通常用于打印错误信息和异常。

**2. 显示优先级**：

+ `System.err.println` 的输出通常会被优先显示，这样可以确保错误信息尽快引起注意。

**3. 输出流重定向**：

+ 在某些情况下（例如重定向输出到文件），`System.out` 和 `System.err` 可以被重定向到不同的目的地，这样可以将普通的输出和错误信息分开处理。
+ 

## 2. 为什么执行java HelloWorld.class 会报错？
在命令行中执行 Java 程序时，应该使用类名而不是文件名。

`java HelloWorld`这条命令将运行 `HelloWorld` 类的 `main` 方法，并输出 "Hello, World!"。



## 3. Java8、JDK8、JDK1.8有什么区别
（1）Java与JDK的区别与关系

在用户眼中，Java是Java应用；

在程序员眼中，Java是Java开发工具，所以Java等价于JDK。

（2）JDK8与JDK1.8的区别与关系

JDK8或者JDK1.8是由于自从JDK1.5/JDK5命名方式改变后遗留的新旧命令方式问题。所以JDK8或者JDK1.8也是同一个东西。

（3）JDK与J2SE的区别与关系

JAVA就是指JDK开发工具，所以我们可以理解为JAVA等价于JDK。又因为JAVA有3个版本：J2SE J2EE J2ME，所以J2SE是JDK的3个版本中的其中一个，即标准版本。

简而言之：我们口中说的Java8、JDK8、JDK1.8其实都是同一个东西。



## 4. 面试题：对象名中存储的是什么呢？
答：对象地址。类、数组都是引用数据类型，引用数据类型的变量中存储的是对象的地址，或者说指向堆中对象的首地址。



## 5. 初始化实例变量有几种方法
4种（执行顺序依次执行）

**1. 在声明时初始化**

**2. 使用非静态代码块初始化**

**3. 使用构造函数初始化**

**4. 使用 set 方法初始化**

```java
public class MyClass {
    static int staticVar;
    
    int instanceVar = 20; //正确
    
    int instanceVar;
    instanceVar = 20;    // 这样写是错的
    
    public MyClass() {
        System.out.println("Constructor executed.");
    }
    
    public static void main(String[] args) {
        MyClass obj1 = new MyClass();
        MyClass obj2 = new MyClass();
    }
}
```



你的代码在声明和初始化 `instanceVar` 时出现了语法错误。在类体中直接写 `instanceVar = 20;` 是不合法的。要初始化实例变量，你可以使用构造函数或非静态代码块。

以下是正确的代码示例，展示了如何使用构造函数和非静态代码块来初始化实例变量：

### 使用非静态代码块
```java
public class MyClass {
    static int staticVar;
    int instanceVar;

    // 非静态代码块
    {
        instanceVar = 20;
        System.out.println("Non-static block executed. instanceVar = " + instanceVar);
    }

    public MyClass() {
        System.out.println("Constructor executed.");
    }

    public static void main(String[] args) {
        MyClass obj1 = new MyClass();
        MyClass obj2 = new MyClass();
    }
}
```

### 使用构造函数
```java
public class MyClass {
    static int staticVar;
    int instanceVar;

    public MyClass() {
        instanceVar = 20;
        System.out.println("Constructor executed. instanceVar = " + instanceVar);
    }

    public static void main(String[] args) {
        MyClass obj1 = new MyClass();
        MyClass obj2 = new MyClass();
    }
}
```

### 代码解析
+ **非静态代码块**：在每次创建实例时执行，用于初始化实例级别的变量。
+ **构造函数**：在每次创建实例时执行，用于初始化实例级别的变量。

### 执行结果
运行上述任何一种代码时，输出如下：

```plain
Non-static block executed. instanceVar = 20
Constructor executed.
Non-static block executed. instanceVar = 20
Constructor executed.
```

或

```plain
Constructor executed. instanceVar = 20
Constructor executed. instanceVar = 20
```



## 6. java中的vector和arraylist
在 Java 中，`Vector` 是一个实现了可增长数组的类，它在 Java 1.0 版引入，是一种同步的动态数组。`Vector` 类位于 `java.util` 包中，类似于 `ArrayList`，但它是线程安全的。

### Vector 的特点
1. **线程安全**：`Vector` 的所有方法都是同步的，因此是线程安全的，适用于多线程环境。
2. **动态数组**：`Vector` 可以根据需要自动调整其大小，以容纳新增元素。
3. **随机访问**：`Vector` 支持通过索引快速访问元素。
4. **自动扩容**：当 `Vector` 的容量不足时，它会自动增加容量，以容纳更多的元素。

### 创建 Vector
你可以通过以下几种方式创建 `Vector`：

1. **默认构造函数**：创建一个初始容量为 10 的空 `Vector`。
2. **指定初始容量**：创建一个具有指定初始容量的空 `Vector`。
3. **指定初始容量和容量增量**：创建一个具有指定初始容量和容量增量的空 `Vector`。
4. **使用另一个集合**：创建一个包含另一个集合中的元素的 `Vector`。

#### 示例
```java
import java.util.Vector;

public class VectorExample {
    public static void main(String[] args) {
        // 使用默认构造函数
        Vector<Integer> vector1 = new Vector<>();

        // 指定初始容量
        Vector<Integer> vector2 = new Vector<>(20);

        // 指定初始容量和容量增量
        Vector<Integer> vector3 = new Vector<>(10, 5);

        // 使用另一个集合
        Vector<Integer> vector4 = new Vector<>(vector1);
    }
}
```

### Vector 的常用方法
`Vector` 提供了许多方法来操作其元素，包括添加、删除、获取和遍历元素。

#### 添加元素
```java
Vector<String> vector = new Vector<>();
vector.add("Element 1"); // 添加到末尾
vector.add(0, "Element 0"); // 在指定位置添加
vector.addElement("Element 2"); // 添加到末尾
```

#### 删除元素
```java
vector.remove("Element 0"); // 删除指定元素
vector.remove(0); // 删除指定位置的元素
vector.removeElement("Element 2"); // 删除指定元素
vector.removeAllElements(); // 删除所有元素
```

#### 获取元素
```java
String element = vector.get(0); // 获取指定位置的元素
String firstElement = vector.firstElement(); // 获取第一个元素
String lastElement = vector.lastElement(); // 获取最后一个元素
```

#### 遍历元素
```java
for (String elem : vector) {
    System.out.println(elem);
}

for (int i = 0; i < vector.size(); i++) {
    System.out.println(vector.get(i));
}
```

#### 检查元素
```java
boolean contains = vector.contains("Element 1"); // 检查是否包含指定元素
int index = vector.indexOf("Element 1"); // 查找指定元素的位置
boolean isEmpty = vector.isEmpty(); // 检查是否为空
```

### Vector 和 ArrayList 的比较
1. **线程安全**：`Vector` 是同步的（线程安全），而 `ArrayList` 不是。
2. **性能**：由于 `Vector` 的同步开销，它在单线程环境中的性能通常低于 `ArrayList`。
3. **扩容策略**：`Vector` 的默认扩容策略是当前容量的两倍，而 `ArrayList` 的默认扩容策略是增加当前容量的 50%。

### 示例：使用 Vector
```java
import java.util.Vector;

public class VectorExample {
    public static void main(String[] args) {
        Vector<String> vector = new Vector<>();

        // 添加元素
        vector.add("Element 1");
        vector.add("Element 2");
        vector.add("Element 3");

        // 获取元素
        System.out.println("First element: " + vector.firstElement());
        System.out.println("Last element: " + vector.lastElement());

        // 遍历元素
        for (String element : vector) {
            System.out.println("Element: " + element);
        }

        // 删除元素
        vector.remove("Element 2");
        System.out.println("After removal, vector: " + vector);

        // 检查元素
        boolean contains = vector.contains("Element 3");
        System.out.println("Vector contains 'Element 3': " + contains);
    }
}
```

### 总结
+ `Vector`** 是一种同步的动态数组，适用于多线程环境**。
+ **提供了丰富的方法用于添加、删除、获取和遍历元素**。
+ **与 **`ArrayList`** 相比，**`Vector`** 是线程安全的，但在单线程环境中性能较低**。

## 7. java中length、length()、size()的区别
在Java中，`length`、`length()`和`size()`是用于获取不同类型数据结构大小的方法或属性。它们的区别如下：

1. `length`:
    - **适用于数组**。
    - 它是一个数组的属性（不是方法）。
    - 用于获取数组的长度（元素个数）。
    - 例如：

```java
int[] numbers = {1, 2, 3, 4, 5};
int length = numbers.length; // length = 5
```

2. `length()`:
    - **适用于字符串**（`String`类）。
    - 它是`String`类的一个方法。
    - 用于获取字符串的长度（字符数）。
    - 例如：

```java
String text = "Hello, world!";
int length = text.length(); // length = 13
```

3. `size()`:
    - **适用于集合**（如`ArrayList`、`HashSet`、`HashMap`等）。
    - 它是集合类的一个方法。
    - 用于获取集合中元素的个数。
    - 例如：

```java
ArrayList<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
int size = list.size(); // size = 2
```

总结：

+ 使用`length`来获取数组的长度。
+ 使用`length()`来获取字符串的长度。
+ 使用`size()`来获取集合的大小。

每个方法或属性适用于不同的数据结构，不能混用。例如，不能对数组调用`length()`方法，也不能对字符串或集合使用`length`属性。

