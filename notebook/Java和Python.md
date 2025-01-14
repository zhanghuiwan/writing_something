# Java
![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1733147370022-f6264843-7a14-487e-a441-7b631efd16de.png)



### 数组
```java
int length = arr.length;

int[] arr = new int[]{1,2,3,4,5};//正确
//或
int[] arr;
arr = new int[]{1,2,3,4,5};//正确
```

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



### 容器
![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020239-13bad4db-f793-4c9c-a5fd-ea7167b1dd31.png)

![](https://cdn.nlark.com/yuque/0/2024/png/39063265/1722617020302-b2b9f42f-d3af-4293-95f0-abd563cdeb67.png)



## collection
```java
add(E obj)

int size()：获取当前集合中实际存储的元素个数
boolean isEmpty()：判断当前集合是否为空集合
boolean contains(Object obj)：判断当前集合中是否存在一个与obj对象equals返回true的元素
boolean containsAll(Collection coll)：判断coll集合中的元素是否在当前集合中都存在。即coll集合是否是当前集合的“子集”
boolean equals(Object obj)：判断当前集合与obj是否相等

void clear()：清空集合元素
boolean remove(Object obj) ：从当前集合中删除第一个找到的与obj对象equals返回true的元素。
boolean removeAll(Collection coll)：从当前集合中删除所有与coll集合中相同的元素。即this = this - this ∩ coll
boolean retainAll(Collection coll)：从当前集合中删除两个集合中不同的元素，使得当前集合仅保留与coll集合中的元素相同的元素，即当前集合中仅保留两个集合的交集，即this  = this ∩ coll；
```

### list
```java
void add(int index, Object ele):在index位置插入ele元素

Object get(int index):获取指定index位置的元素
List subList(int fromIndex, int toIndex):返回从fromIndex到toIndex位置的子集合

int indexOf(Object obj):返回obj在集合中首次出现的位置
int lastIndexOf(Object obj):返回obj在当前集合中末次出现的位置

Object remove(int index):移除指定index位置的元素，并返回此元素
Object set(int index, Object ele):设置指定index位置的元素为ele
```

### set


## map
### map
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

```java
// 遍历map
HashMap<String, Integer> map = new HashMap<>();
map.put("Alice", 25);
map.put("Bob", 30);
map.put("Charlie", 35);

// 1
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
}

// 2
for (String key : map.keySet()) {
    System.out.println("Key: " + key + ", Value: " + map.get(key));
}

// 3
for (Integer value : map.values()) {
    System.out.println("Value: " + value);
}

// 4
map.forEach((key, value) -> {
    System.out.println("Key: " + key + ", Value: " + value);
});

// 5
Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();
while (iterator.hasNext()) {
    Map.Entry<String, Integer> entry = iterator.next();
    System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
}
```



## iterator
+ 集合对象每次调用iterator()方法都得到一个全新的迭代器对象，**默认游标都在集合的第一个元素之前。**
+ Iterator接口的常用方法如下：
    - `public E next()`:返回迭代的下一个元素。
    - `public boolean hasNext()`:如果仍有元素可以迭代，则返回 true。
    - `<font style="color:#0e0e0e;">remove()</font>`<font style="color:#0e0e0e;">: 从集合中移除 next() 返回的最后一个元素（可选操作）。</font>
+ 注意：**在调用it.next()方法之前必须要调用it.hasNext()进行检测**。若不调用，且下一条记录无效，直接调用it.next()会抛出`NoSuchElementException异常`。

```java
Iterator<Integer> iterator = set.iterator();
while (iterator.hasNext()) {
    Integer number = iterator.next();
    if (number % 2 == 0) {
        iterator.remove(); // 移除偶数元素
    }
}


Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();
while (iterator.hasNext()) {
    Map.Entry<String, Integer> entry = iterator.next();
    System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
}
```

# Python
### 集合
```python
# python中空集合使用my_set = set()创建， 
# 默认的 my_dict = {} 是创建字典类型


# 使用大括号 {} 创建
my_set = {1, 2, 3, 4}

# 使用 set() 函数创建
empty_set = set()  # 空集合
my_set2 = set([1, 2, 3])  # 从可迭代对象创建集合
```



```python
# 添加
my_set.add()

# 删除
my_set.remove(2)   # 会抛出错误
my_set.discard(5)  # 不会抛出错误

# 元素是否在集合中
my_set = {1, 2, 3}
print(2 in my_set)  # 输出 True
print(4 not in my_set)  # 输出 True

# 集合长度
len(my_set)

# 用集合去重复
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print(unique_nums)  # 输出 [1, 2, 3, 4, 5]
```





### 字典


### 元组


### 列表
Python 中的列表（list）是一个有序的可变集合，可以存储任意类型的元素，甚至是不同类型的元素。列表是 Python 中最常用的数据结构之一，支持各种基本操作。

以下是 Python 列表的一些基本操作：

1. 创建列表

# 创建空列表
my_list = []

# 创建包含元素的列表
my_list = [1, 2, 3, 4, 5]

# 包含不同类型的元素
my_list = [1, "hello", 3.14, True]

# 使用 `list()` 函数将其他可迭代对象转换为列表
my_list = list((1, 2, 3))  # tuple 转 list

2. 访问列表元素

可以通过索引访问列表的元素，Python 列表的索引从 0 开始。

my_list = [10, 20, 30, 40, 50]

# 访问第一个元素
print(my_list[0])  # 输出: 10

# 访问最后一个元素
print(my_list[-1])  # 输出: 50

# 访问倒数第二个元素
print(my_list[-2])  # 输出: 40

3. 修改列表元素

通过索引可以修改列表中的元素。

my_list = [10, 20, 30]

# 修改第二个元素
my_list[1] = 25  
print(my_list)  # 输出: [10, 25, 30]

4. 添加元素 •	append()：在列表的末尾添加一个元素。  
 •	insert()：在指定位置插入一个元素。  
 •	extend()：将另一个可迭代对象中的所有元素添加到列表末尾。

my_list = [1, 2, 3]

# append() 在末尾添加元素
my_list.append(4)  
print(my_list)  # 输出: [1, 2, 3, 4]

# insert() 在指定位置插入元素
my_list.insert(2, "inserted")  # 在索引 2 的位置插入 "inserted"  
print(my_list)  # 输出: [1, 2, 'inserted', 3, 4]

# extend() 将另一个列表中的元素添加到末尾
my_list.extend([5, 6, 7])  
print(my_list)  # 输出: [1, 2, 'inserted', 3, 4, 5, 6, 7]

5. 删除元素 •	remove()：移除第一个匹配的元素。  
 •	pop()：移除并返回指定位置的元素。如果没有指定位置，默认移除最后一个元素。  
 •	clear()：移除列表中的所有元素。

my_list = [10, 20, 30, 40, 50]

# remove() 移除匹配的元素
my_list.remove(30)  # 移除第一个匹配的 30  
print(my_list)  # 输出: [10, 20, 40, 50]

# pop() 移除并返回最后一个元素
last_element = my_list.pop()  
print(last_element)  # 输出: 50  
print(my_list)  # 输出: [10, 20, 40]

# pop() 移除并返回指定位置的元素
second_element = my_list.pop(1)  
print(second_element)  # 输出: 20  
print(my_list)  # 输出: [10, 40]

# clear() 移除所有元素
my_list.clear()  
print(my_list)  # 输出: []

6. 列表切片

可以使用切片（slicing）操作来访问列表的一部分。

my_list = [1, 2, 3, 4, 5, 6, 7]

# 获取从索引 2 到 4 之间的元素（不包括索引 4）
print(my_list[2:4])  # 输出: [3, 4]

# 获取从索引 3 到列表末尾的元素
print(my_list[3:])  # 输出: [4, 5, 6, 7]

# 获取列表从开始到索引 4 之前的元素（不包括索引 4）
print(my_list[:4])  # 输出: [1, 2, 3, 4]

# 获取列表的副本
print(my_list[:])  # 输出: [1, 2, 3, 4, 5, 6, 7]

7. 查找元素 •	index()：返回元素第一次出现的索引。  
 •	count()：返回元素出现的次数。

my_list = [10, 20, 30, 20, 40]

# 查找元素的索引
index = my_list.index(20)  
print(index)  # 输出: 1

# 计数元素的出现次数
count = my_list.count(20)  
print(count)  # 输出: 2

8. 排序和反转 •	sort()：对列表进行原地排序。  
 •	sorted()：返回一个新的排序后的列表。  
 •	reverse()：反转列表的顺序。  
 •	reversed()：返回一个反转的迭代器。

my_list = [4, 2, 3, 1, 5]

# sort() 原地排序
my_list.sort()  
print(my_list)  # 输出: [1, 2, 3, 4, 5]

# sorted() 返回一个新列表
new_list = sorted(my_list, reverse=True)  
print(new_list)  # 输出: [5, 4, 3, 2, 1]

# reverse() 反转列表顺序
my_list.reverse()  
print(my_list)  # 输出: [5, 4, 3, 2, 1]

# reversed() 返回反转的迭代器
reversed_list = list(reversed(my_list))  
print(reversed_list)  # 输出: [1, 2, 3, 4, 5]

9. 列表推导式

列表推导式（List comprehension）是 Python 提供的用于创建新列表的简洁方式。

# 创建一个包含 0 到 9 的平方数的列表
squares = [x ** 2 for x in range(10)]  
print(squares)  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件的列表推导式
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]  
print(even_squares)  # 输出: [0, 4, 16, 36, 64]

10. 嵌套列表

列表可以包含其他列表，形成嵌套列表（多维数组）。

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 访问嵌套列表的元素
print(my_list[0][1])  # 输出: 2  
print(my_list[1][2])  # 输出: 6

11. 列表的复制

my_list = [1, 2, 3, 4, 5]

# 使用切片来复制列表
new_list = my_list[:]  
print(new_list)  # 输出: [1, 2, 3, 4, 5]

# 使用 copy() 方法来复制
new_list = my_list.copy()  
print(new_list)  # 输出: [1, 2, 3, 4, 5]

总结

```plain
•	Python 列表是一个非常强大的数据结构，支持各种操作，如添加、删除、修改、查找、排序、切片等。
•	列表推导式使得创建新列表变得非常简洁和高效。
•	列表支持嵌套，可以构建多维数组或矩阵。
```

以上是 Python 列表的一些基本操作，理解这些操作对于日常开发中的数据处理非常有用。

### 一点遍历技巧
1. 使用 range() 来生成索引

```python
nums = [10, 20, 30, 40]
for i in range(len(nums)):
    print(i, nums[i])
```

2. 使用 enumerate() 来获取索引和值

enumerate() 是一个非常常用的技巧，它允许在循环时同时获得元素的索引和值，避免手动使用 range()：

```python
nums = [10, 20, 30, 40]
for index, value in enumerate(nums):
    print(index, value)
```



```plain
•	输出：
0 10
1 20
2 30
3 40
```





enumerate() 还可以指定起始索引：

```plain
for index, value in enumerate(nums, start=1):
    print(index, value)
```

```plain
•	输出：
1 10
2 20
3 30
4 40
```



3. 使用 zip() 来同时遍历多个序列

zip() 是一个用于同时遍历多个序列的函数。如果你有多个列表，并且希望在同一循环中遍历它们，可以使用 zip()：

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(name, age)
```



如果两个序列的长度不相等，zip() 会根据最短的序列进行配对，丢弃多余的部分。可以使用 itertools.zip_longest() 来处理长度不一致的情况：

```python
from itertools import zip_longest
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30]
for name, age in zip_longest(names, ages, fillvalue=None):
    print(name, age)
```

```plain
•	输出：Alice 25
Bob 30
Charlie None
```





4. 反向遍历列表

如果你需要反向遍历一个列表，可以使用 reversed() 函数或者直接使用 range 生成逆序索引：

```plain

```



5. 使用列表推导式（List Comprehension）来简化代码

在循环中对列表进行处理时，列表推导式是一个非常强大的工具，能将常见的循环操作简化为一行代码：

```plain
nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]
print(squared)
```



你也可以在列表推导式中添加条件：

```plain
even_squared = [x**2 for x in nums if x % 2 == 0]
print(even_squared)
```



```plain
•	输出：[4, 16]
```

### 排序技巧
<font style="color:#0e0e0e;">sorted(nums)</font><font style="color:#0e0e0e;"> 返回一个新的排序列表，原始列表 </font><font style="color:#0e0e0e;">nums</font><font style="color:#0e0e0e;"> 不变。</font>

<font style="color:#0e0e0e;">nums.sort() 在原列表上进行排序，修改 nums 本身。</font>

<font style="color:#0e0e0e;">强大的sorted函数</font>

```plain
是的，sorted() 函数可以对列表进行排序。在 Python 中，sorted() 是一个内置函数，可以对任何可迭代对象（如列表、元组、字符串等）进行排序，并返回一个新的排序后的列表。

使用 sorted() 对列表排序

1. 默认排序

对于数字列表，sorted() 默认按升序排序：

my_list = [5, 2, 8, 1, 3]
sorted_list = sorted(my_list)
print(sorted_list)

输出：

[1, 2, 3, 5, 8]

2. 降序排序

要按降序对列表排序，可以设置 reverse=True：

my_list = [5, 2, 8, 1, 3]
sorted_list_desc = sorted(my_list, reverse=True)
print(sorted_list_desc)

输出：

[8, 5, 3, 2, 1]

3. 排序字符串列表

对于字符串列表，sorted() 会按字母顺序进行排序：

my_list = ['banana', 'apple', 'cherry', 'date']
sorted_list = sorted(my_list)
print(sorted_list)

输出：

['apple', 'banana', 'cherry', 'date']

4. 使用自定义排序规则

你可以使用 key 参数提供一个排序的依据函数。例如，按字符串的长度进行排序：

my_list = ['banana', 'apple', 'cherry', 'date']
sorted_list_by_length = sorted(my_list, key=len)
print(sorted_list_by_length)

输出：

['date', 'apple', 'banana', 'cherry']

5. 排序列表中的元组

如果列表中包含元组，可以根据元组的元素进行排序。例如，按元组的第二个元素排序：

my_list = [(1, 2), (3, 1), (5, 0)]
sorted_list_by_second_element = sorted(my_list, key=lambda x: x[1])
print(sorted_list_by_second_element)

输出：

[(5, 0), (3, 1), (1, 2)]

注意事项

	•	sorted() 返回一个新列表，原列表不发生改变。如果你希望对原列表进行排序，可以使用 list.sort() 方法，它会直接在原列表上进行排序，并返回 None。
	•	sorted() 可以对任何可迭代对象进行排序，不仅限于列表。

总结

	•	sorted() 可以对列表进行排序，默认按升序排列，可以通过 reverse=True 实现降序排列。
	•	通过 key 参数可以自定义排序规则，支持更复杂的排序需求。
```

