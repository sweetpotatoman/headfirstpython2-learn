## 存储和管理数据
---
### 数据存储
> python 提供了内置支持来实现文件的**打开（open）、处理（process）和关闭（close）**

>这种通用技术允许你打开一个文件，以某种方式处理其数据 **（读写/追加数据）**，然后完成时关闭文件 **（保存修改）**

---

### open 参数
- `'r'` --- 读数据 **(默认模式)**
- `'w'` --- 写数据，若文件已有数据，则会清空再写入
- `'a'` --- 追加数据
- `'x'` --- 打开新文件来写数据，若文件存在则报错

**写入数据**
  
  ```py
  todos = open('todos.txt', 'a')
  ```
  - `open` 打开一个文件
  - `'a'` 采用 ”追加模式“ 打开这个文件
  - `open` 会返回一个流，将这个文件流赋给这个变量 `todos`
  
  ```py
  print('put out the trash.', file=todos)
  print('feed the cat.', file=todos)
  ```
  ```py
  todos.close()
  ```

**读取数据**
  ```py
  tasks = open('todos.txt')
  ```
  - `open` 的默认模式是 **读**
  ```py
  for chore in tasks:
      print(chore)

  // put out the trash.
  //
  // feed the cat.
  //
  ```
  - 由于 todos.txt 文件中的各行都以一个换行字符结束，这个换行符会作为数据行的一部分读取，所以最后打印了两个换行
  - 一个来自文件，另一个来自 print
  - 可以将 `print(chore)` 改成 `print(chore, end=''` 来抑制 print 追加换行符的默认行为

  ```py
  tasks.close()
  ```

---

### with 语句
结合使用 `open` 函数和 `close` 方法是可以的，但是使用 `with` 语句更为简单

```py
with open('todos.txt') as tasks:
    for chore in tasks:
        print(chore, end='')
```
  - 只要 with 的代码组结束，就会代表你调用了 `close`

#### with 语句管理上下文
with 语句符合 python 中内置的一个编码约定，这称为 **上下文管理协议**。


### split & join
> join 将一个字符串列表转换为一个字符串
```py
names = ['Terry', 'John', 'Michael', 'Graham', 'Eric']
pythons = '|'.join(names)
pythons
// 'Terry|John|Michael|Graham|Eric'
```

> split 方法把这个过程翻过来
```py
individuals = pythons.split('|')
individuals
// ['Terry', 'John', 'Michael', 'Graham', 'Eric']
```
