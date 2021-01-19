## 异常处理

---

### 捕获异常
出现一个运行时错误时，会产生一个异常。如果忽略所产生的异常，则称这个异常未捕获，**解释器会终止代码**，然后显示一个运行时错误信息。

```py
# try_example.py

with open('mysite.txt') as fh:
    file_data = fh.read()
print(file_data)

# 当文件不存在
Traceback (most recent call last):
  File "try_example.py", line 1, in <module>
    with open('mysite.txt') as fh:
FileNotFoundError: [Errno 2] No such file or directory: 'mysite.txt'
```

#### 使用 try except 捕获异常
**执行 `try_examples2.py`**
- 当没有找到文件时
  ```
  The data file is missing.
  ```

- 当没权限打开文件时
  ```
  This is not allowed.
  ```

- 定义一个捕获所有异常的 **(catch-all)** except 代码组
  ```
  Some other error occurred.
  ```

#### 从 `sys` 了解异常
标准库提供了一个 sys 模块，可以利用这个模块访问解释器的内部信息。  

`exc_info` 函数提供当前处理的异常有关信息，跳用 exc_info 时会返回一个包括 3 个值的元组:  
1. 指示异常的类型
2. 详细描述异常的值
3. 包含一个回溯跟踪对象

python 扩展了 `try/except` 语法，可以方便地得到 sys.exc_info 函数返回这些信息 --- **(因为解释器采用了一个层次结构组织异常，每个异常都继承了一个名为 Exception 的类)**

**执行 `try_examples3.py`**
- 当遇到没有明确指定的异常时，例如遇到打开的是一个文件夹
  ```py
  Some other error occurred: [Errno 21] Is a directory: 'myfile.txt'
  ```