## 关于线程

---

### 并发代码
需要让应用的一些代码并发地运行，比较常用的是 `threading` 库，它为操作系统提供的多线程实现提供了一个高层接口。
```py
import threading import Thread
```

- 使用线程
  - 原函数
    ```py
    execute_slowly(glacial, plodding, leaden)
    ``` 
  - 创建一个新的 `Thread` 对象，多线程技术运行 `execute_slowly`
    ```py
    from threading import Thread

    t = Thread(target=execute_slowly, args=(glacial, plodding, leaden))

    t.start() # 调用 start 时，将由 threading 模块执行与 t 线程关联的函数
    ```