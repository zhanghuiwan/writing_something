## 1 生成张量

### 1.1 使用torch.tensor()或者torch.Tensor()来生成张量。
两者主要区别为
- `torch.Tensor(data)`：直接调用`Tensor`构造函数会默认创建一个浮点型张量 (`torch.float32`)。即使输入的数据是整数列表或元组，生成的张量元素也会被转换为浮点数。
- `torch.tensor(data)`：此函数会根据输入数据的类型推断出张量的类型。如果输入的是整数列表，则生成的张量将具有整数类型（例如`torch.int64`），而浮点数列表则会生成浮点类型的张量。


```python
import torch
import torch.nn as nn

# 生成一个2维的，形状为2*3的张量, 元素全为0, 数据类型为32位浮点型
a = torch.Tensor(2,3)
# 生成一个1维的，形状为2的张量, 数据类型为32位浮点型
b = torch.Tensor([2,3])

# 生成一个2维的，形状为2*3的张量,数据类型为torch.int64
c = torch.tensor([[1, 2, 3], [4, 5, 6]])
# 生成一个2维的，形状为2*3的张量，数据类型为64位浮点型, 存储在cpu上, 并且需要梯度
d = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float64, device='cpu', requires_grad=True)
```

### 1.2 一些基本的张量
| 函数                                  | 描述                                                                                                           |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------|
| `torch.zeros(3, 3)`                 | 创建一个形状为 (3, 3) 的全零张量。所有元素都初始化为 0。                                                        |
| `torch.ones(3, 3)`                  | 创建一个形状为 (3, 3) 的全一张量。所有元素都初始化为 1。                                                        |
| `torch.eye(3, 3)`                   | 创建一个形状为 (3, 3) 的单位矩阵（对角线元素为1，其余元素为0）。                                               |
| `torch.rand(3, 3)`                  | 创建一个形状为 (3, 3) 的张量，元素是从均匀分布 $ \text{Uniform}(0, 1) $ 中抽取的随机数，值在 [0, 1) 区间内等概率出现。 |
| `torch.randn(3, 3)`                 | 创建一个形状为 (3, 3) 的张量，元素是从标准正态分布 $ \mathcal{N}(0, 1) $ 中抽取的随机数，均值为 0，方差为 1。       |
| `torch.empty(3, 4)`                 | 创建一个形状为 (3, 4) 的未初始化张量。它不会将内存设置为任何特定值，因此创建速度较快，但内容是未定义的。           |
| `torch.rand_like(h, dtype=torch.float)` | 创建一个与现有张量 `h` 大小相同的新张量，元素是从均匀分布 $ \text{Uniform}(0, 1) $ 中抽取的随机数，并指定数据类型为 `float`。 |



```python
a  = torch.rand(3,4)
a
```

## 2 一些简单函数
### 2.1 基本函数

| 函数                                 | 作用                                                                 |
|------------------------------------|--------------------------------------------------------------------|
| `A.dim()`                          | 获取A的维度                                                        |
| `A.item()`                         | 将Tensor转化为基本数据类型，注意Tensor中只有一个元素的时候才可以使用，一般用于在Tensor中取出数值 |
| `A.numpy()`                        | 将Tensor转化为Numpy类型                                             |
| `A.size()`                         | 查看尺寸                                                             |
| `A.shape`                          | 查看尺寸                                                             |
| `A.dtype`                          | 查看A中元素的类型（张量中的所有元素都具有相同的类型）                                                         |
| `A.view()`                         | 重构张量尺寸，类似于Numpy中的reshape                                   |
| `A.transpose(0, 1)`                | 行列交换                                                             |
| `A[1:], A[-1, -1]=100`             | 切片操作，类似Numpy中的切片                                           |
| `A.zero_()`                        | 归零化                                                               |
| `torch.stack((A, B), dim=-1)`      | 拼接，升维                                                           |
| `torch.diag(A)`                    | 取A对角线元素形成一个一维向量                                         |
| `torch.diag_embed(A)`              | 将一维向量放到对角线中，其余数值为0的Tensor                               |


```python
v = torch.tensor([2.3, 4.2, 3])
print("获取Tensor的值：item() : ", v[1].item())

print("获取Tensor的个数：numel() : ", v.numel())
```

### 2.2 基本运算

y = x + y 系统将取消引⽤ y 的地址，指向新地址。y指向地址不同。
y[:] = x + y 和 y += x 系统不再分配新空间，y指向的地址相同

| 函数                                 | 作用                                                                 |
|------------------------------------|--------------------------------------------------------------------|
| `torch.abs(A)`                     | 计算绝对值                                                         |
| `torch.add(A, B)`                  | 相加，A和B既可以是Tensor也可以是标量                                               |
| `torch.clamp(A, min, max)`         | 裁剪，A中的数据若小于min或大于max，则变成min或max，即保证范围在[min, max]               |
| `torch.div(A, B)`                  | 相除，A / B，A和B既可以是Tensor也可以是标量                                           |
| `torch.mul(A, B)`                  | 点乘，A * B，A和B既可以是Tensor也可以是标量                                           |
| `torch.pow(A, n)`                  | 求幂，A的n次方                                                     |
| `torch.mm(A, B.T)`                 | 矩阵叉乘，注意与`torch.mul`之间的区别                                       |
| `torch.mv(A, B)`                   | 矩阵与向量相乘，A是矩阵，B是向量，这里的B需不需要转置都是可以的                           |

## 3. cuda相关用法


```python
# 测试GPU环境是否可使用
print(torch.__version__) # pytorch版本
print(torch.version.cuda) # cuda版本
print(torch.cuda.is_available()) # 查看cuda是否可用
 
#使用GPU or CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
 
# 判断某个对象是在什么环境中运行的
a.device
 
# 将对象的环境设置为device环境
A = a.to(device)
 
# 将对象环境设置为CPU
A.cpu().device
 
# 若一个没有环境的对象与另外一个有环境a对象进行交流,则环境全变成环境a
a.to(device)
 
# cuda环境下tensor不能直接转化为numpy类型,必须要先转化到cpu环境中
a.cpu().numpy()
 
# 创建CUDA型的tensor
torch.tensor([1,2], device = device)
```

## 4. 梯度

### 4.1 求导
- 对于非标量的输出 y，比如形状为 (N,) 的向量，并且你想要计算输入 x 对应的梯度，那么你需要指定一个形状与 y 相同的权重张量 gradient。这个权重张量代表了每个输出元素对最终目标（通常是损失函数）的贡献。
- retain_graph=True：用于在调用 backward() 后保持计算图不被释放，以便可以对同一前向传播的结果进行多次反向传播。
- create_graph=True：用于在计算梯度时保留更高阶的梯度信息，使得可以计算二阶或更高阶导数。


```python
# 标量Tensor求导
# 求 f(x) = a*x**2 + b*x + c 的导数
x = torch.tensor(-2.0, requires_grad=True)
a = torch.tensor(1.0)
b = torch.tensor(2.0)
c = torch.tensor(3.0)
y = a*torch.pow(x,2)+b*x+c # 计算y的值
y.backward() # 计算y的梯度，实际上会计算此时关于每一个自变量x的偏导数，求得的结果会存储在每个自变量x的grad属性中
dy_dx =x.grad
dy_dx
```


```python
# 非标量Tensor求导
# 求 f(x) = a*x**2 + b*x + c 的导数
x = torch.tensor([[-2.0,-1.0],[0.0,1.0]], requires_grad=True)
a = torch.tensor(1.0)
b = torch.tensor(2.0)
c = torch.tensor(3.0)
gradient=torch.tensor([[1.0,1.0],[1.0,1.0]]) # 与输出y的形状相同
y = a*torch.pow(x,2)+b*x+c
y.backward(gradient=gradient) 
dy_dx =x.grad
dy_dx
```


```python
#单个自变量求导
# 求 f(x) = a*x**4 + b*x + c 的导数
x = torch.tensor(1.0, requires_grad=True)
a = torch.tensor(1.0)
b = torch.tensor(2.0)
c = torch.tensor(3.0)
y = a * torch.pow(x, 4) + b * x + c
#create_graph设置为True,允许创建更高阶级的导数
#求一阶导
dy_dx = torch.autograd.grad(y, x, create_graph=True)[0]
#求二阶导
dy2_dx2 = torch.autograd.grad(dy_dx, x, create_graph=True)[0]
#求三阶导
dy3_dx3 = torch.autograd.grad(dy2_dx2, x)[0]
print(dy_dx.data, dy2_dx2.data, dy3_dx3)
```


```python
# 多个自变量求偏导
x1 = torch.tensor(1.0, requires_grad=True)
x2 = torch.tensor(2.0, requires_grad=True)
y1 = x1 * x2
y2 = x1 + x2
#只有一个因变量,正常求偏导
dy1_dx1, dy1_dx2 = torch.autograd.grad(outputs=y1, inputs=[x1, x2], retain_graph=True)
print(dy1_dx1, dy1_dx2)
# 若有多个因变量，则对于每个因变量,会将求偏导的结果加起来
dy1_dx, dy2_dx = torch.autograd.grad(outputs=[y1, y2], inputs=[x1, x2])
dy1_dx, dy2_dx
print(dy1_dx, dy2_dx)
```


```python
#例2-1-3 利用自动微分和优化器求最小值

 # f(x) = a*x**2 + b*x + c的最小值
x = torch.tensor(0.0, requires_grad=True)  # x需要被求导
a = torch.tensor(1.0)
b = torch.tensor(-2.0)
c = torch.tensor(1.0)
optimizer = torch.optim.SGD(params=[x], lr=0.01)  #SGD为随机梯度下降
print(optimizer)
 
def f(x):
    result = a * torch.pow(x, 2) + b * x + c
    return (result)
 
for i in range(500):
    optimizer.zero_grad()  #将模型的参数初始化为0
    y = f(x)
    y.backward()  #反向传播计算梯度
    optimizer.step()  #更新所有的参数
print("y=", y.data, ";", "x=", x.data)
```

## 5 Dataset and DataLoader


`DataLoader` 是 PyTorch 中用于加载数据集并提供迭代器接口的类。以下是 `DataLoader` 的各个参数及其说明：

```python
DataLoader(
    dataset,
    batch_size=1,
    shuffle=False,
    sampler=None,
    batch_sampler=None,
    num_workers=0,
    collate_fn=None,
    pin_memory=False,
    drop_last=False,
    timeout=0,
    worker_init_fn=None,
    multiprocessing_context=None,
)
```


| 参数               | 类型          | 默认值   | 描述                                                                                                           |
|------------------|-------------|--------|------------------------------------------------------------------------------------------------------------|
| `dataset`        | Dataset     | 必填项  | 数据集对象，决定数据从哪里读取以及如何读取。必须实现 `__len__` 和 `__getitem__` 方法。                                            |
| `batch_size`     | int         | 1      | 每个批次（batch）的数据量大小。                                                                            |
| `shuffle`        | bool        | False  | 如果为 `True`，则在每个 epoch 开始时打乱数据集。对于训练集通常设置为 `True`，而对于验证集或测试集则为 `False`。                    |
| `sampler`        | Sampler     | None   | 自定义样本采样器。如果指定了 `sampler`，则忽略 `shuffle` 参数。常用的是 `RandomSampler` 和 `SequentialSampler`。                     |
| `batch_sampler`  | BatchSampler| None   | 自定义批次采样器。如果指定了 `batch_sampler`，则忽略 `batch_size`、`shuffle` 和 `sampler` 参数。                                    |
| `num_workers`    | int         | 0      | 加载数据时使用的子进程数。设置为 0 表示在主进程中加载数据。增加此参数可以加快数据加载速度，但也会占用更多内存和CPU资源。              |
| `collate_fn`     | callable    | None   | 用于合并一个批次的数据样本的函数。默认情况下，PyTorch 会自动将张量堆叠在一起。如果你的数据结构更复杂，可能需要自定义此函数。            |
| `pin_memory`     | bool        | False  | 如果为 `True`，则将数据加载到固定内存（pinned memory），以便更快地传输到GPU。适用于使用GPU进行训练的情况。                          |
| `drop_last`      | bool        | False  | 如果数据集大小不能被 `batch_size` 整除，则最后一个不完整的批次是否丢弃。如果为 `True`，则最后一个批次会被丢弃。                      |
| `timeout`        | numeric     | 0      | 等待数据加载的最大时间（以秒为单位）。如果超过此时间仍未获取到数据，则抛出异常。0 表示无超时限制。                                     |
| `worker_init_fn` | callable    | None   | 每个工作进程初始化时调用的函数。可用于设置随机种子等操作。                                                   |
| `multiprocessing_context` | context | None  | 设置多进程上下文，指定如何启动子进程。适用于高级用户，通常不需要更改。                                          |


```python
import numpy as np
 
class ImageDataset:
    def __init__(self, raw_data):
        self.raw_data = raw_data
 
    def __len__(self):
        return len(self.raw_data)
 
    def __getitem__(self, index):
        image, label = self.raw_data[index]
        return image, label
 
class DataLoader:
    def __init__(self, dataset, batch_size):
        self.dataset = dataset
        self.batch_size = batch_size
 
    def __iter__(self):
        self.indexs = np.arange(len(self.dataset))
        self.cursor = 0
        np.random.shuffle(self.indexs)
        return self
 
    def __next__(self):
        begin = self.cursor
        end = self.cursor + self.batch_size
        if end > len(self.dataset):
            raise StopIteration()
        self.cursor = end
        batched_data = []
        for index in self.indexs[begin:end]:
            item = self.dataset[index]
            batched_data.append(item)
        return batched_data
 
# Example usage
images = [(f"image{i}", i) for i in range(100)]
dataset = ImageDataset(images)
loader = DataLoader(dataset, 5)
 
for index, batched_data in enumerate(loader):
    print(f"Batch {index + 1}:", batched_data)
pass
```

## 6 神经网络


### 6.1 简单的线性模型


```python
import random
import torch
# 生成数据集，传入真实的w，b以及需要生成的数据集数量
def synthetic_data(w, b, num_examples):  
    """生成y=Xw+b+噪声"""
    X = torch.normal(0, 1, (num_examples, len(w)))
    y = torch.matmul(X, w) + b
    y += torch.normal(0, 0.01, y.shape)
    # 这里的-1 是一个特殊的维度值，它告诉PyTorch自动计算该维度的大小，使得总的元素数量与原张量相同。而 1 则明确指定了另一个维度的大小。
    return X, y.reshape((-1, 1))

# 小批量读取数据集，batch_size为每次读取的大小，每次返回batch_size大小的数据
def data_iter(batch_size, features, labels):
    num_examples = len(features)
    indices = list(range(num_examples))
    # 这些样本是随机读取的，没有特定的顺序
    random.shuffle(indices)
    for i in range(0, num_examples, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_examples)])
        yield features[batch_indices], labels[batch_indices]

# 生成数据集
true_w = torch.tensor([2, -3.4])
true_b = 4.2
features, labels = synthetic_data(true_w, true_b, 1000)

```


```python
# 定义模型
def linreg(X, w, b):  #@save
    """线性回归模型"""
    return torch.matmul(X, w) + b


# 定义损失函数
def squared_loss(y_hat, y):  #@save
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

# 定义优化算法
def sgd(params, lr, batch_size):  #@save
    """小批量随机梯度下降"""
    # 告诉 PyTorch 不要跟踪计算图中的梯度信息。因为我们只是在这里更新参数，而不是计算新的梯度，所以不需要梯度跟踪。
    with torch.no_grad():
        for param in params:
            param -= lr * param.grad / batch_size
            param.grad.zero_() # 将梯度清0


# 初始化模型参数，随机生成w，b
w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

# 定义参数
lr = 0.03
num_epochs = 4
net = linreg
loss = squared_loss
batch_size = 10

# 训练
for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        l = loss(net(X, w, b), y)  # X和y的小批量损失
        # 因为l形状是(batch_size,1)，而不是一个标量。l中的所有元素被加到一起，
        # 并以此计算关于[w,b]的梯度
        '''
        l.sum().backward() 计算标量损失相对于模型参数 w 和 b 的梯度。这个操作会将梯度存储在对应的参数张量的 .grad 属性中。
        在 PyTorch 中，backward() 方法实际上会沿着计算图反向传播梯度。这意味着它会计算损失相对于所有参与计算的
        张量的梯度，并将这些梯度存储在相应的张量的 .grad 属性中。
        '''
        l.sum().backward()  
        sgd([w, b], lr, batch_size)  # 使用参数的梯度更新参数
    with torch.no_grad(): # 确保在评估期间不计算梯度
        train_l = loss(net(features, w, b), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')


print(f'w的估计误差: {true_w - w.reshape(true_w.shape)}')
print(f'b的估计误差: {true_b - b}')
```

### 6.2 多层感知机


```python
from torch import nn

# 定义网络
def net_mul_layer(X):
    """多层感知机的前向传播"""
    H = torch.relu(X @ W1 + b1)  # 隐藏层
    return H @ W2 + b2  # 输出层

# 定义损失函数
def squared_loss(y_hat, y):  #@save
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2


# 初始化模型参数
num_inputs, num_outputs, num_hiddens = 2, 1, 8

W1 = nn.Parameter(torch.randn(
    num_inputs, num_hiddens, requires_grad=True) * 0.01)
b1 = nn.Parameter(torch.zeros(num_hiddens, requires_grad=True))
W2 = nn.Parameter(torch.randn(
    num_hiddens, num_outputs, requires_grad=True) * 0.01)
b2 = nn.Parameter(torch.zeros(num_outputs, requires_grad=True))

params = [W1, b1, W2, b2]

# 定义训练参数
lr = 0.03
net = net_mul_layer
loss = squared_loss
num_epochs = 40
batch_size = 10
optimizer = torch.optim.SGD(params, lr=lr)


# 训练
for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        optimizer.zero_grad()
        l = loss(net(X), y)  # 前向传播计算损失
        l.mean().backward()  # 反向传播计算梯度
        optimizer.step()  # 更新参数
    with torch.no_grad(): # 确保在评估期间不计算梯度
        train_l = loss(net(features), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')


```


```python
from torch import nn

# 定义损失函数
def squared_loss(y_hat, y):  #@save
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

# 定义网络以及初始化参数
net = nn.Sequential(nn.Linear(2, 8),
                    nn.ReLU(),
                    nn.Linear(8, 1))
def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, std=0.01)

net.apply(init_weights)

# 定义训练参数
lr = 0.0003
# net = net_mul_layer
loss = squared_loss
num_epochs = 400
batch_size = 10
optimizer = torch.optim.SGD(net.parameters(), lr=lr)


# 训练
for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        optimizer.zero_grad()
        l = loss(net(X), y)  # 前向传播计算损失
        l.mean().backward()  # 反向传播计算梯度
        optimizer.step()  # 更新参数
    with torch.no_grad(): # 确保在评估期间不计算梯度
        train_l = loss(net(features), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')




```


```python
from torch import nn

# 定义损失函数
def squared_loss(y_hat, y):  #@save
    """均方损失"""
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

# 定义网络以及初始化参数
class MLP(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(MLP, self).__init__()
        # 定义层
        self.hidden = nn.Linear(input_size, hidden_size)  # 隐藏层
        self.relu = nn.ReLU()  # 激活函数
        self.output = nn.Linear(hidden_size, output_size)  # 输出层

    def forward(self, x):
        # 定义前向传播逻辑
        x = self.hidden(x)  # 隐藏层
        x = self.relu(x)    # 激活函数
        x = self.output(x)  # 输出层
        return x

# 使用模型
net = MLP(input_size=2, hidden_size=8, output_size=1)
def init_weights(m):
    if type(m) == nn.Linear:
        nn.init.normal_(m.weight, std=0.01)

net.apply(init_weights)

# 定义训练参数
lr = 0.03
# net = net_mul_layer
loss = squared_loss
num_epochs = 40
batch_size = 10
optimizer = torch.optim.SGD(net.parameters(), lr=lr)


# 训练
for epoch in range(num_epochs):
    for X, y in data_iter(batch_size, features, labels):
        optimizer.zero_grad()
        l = loss(net(X), y)  # 前向传播计算损失
        l.mean().backward()  # 反向传播计算梯度
        optimizer.step()  # 更新参数
    with torch.no_grad(): # 确保在评估期间不计算梯度
        train_l = loss(net(features), labels)
        print(f'epoch {epoch + 1}, loss {float(train_l.mean()):f}')


```
