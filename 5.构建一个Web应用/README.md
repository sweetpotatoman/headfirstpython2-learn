## 构建一个 Web 应用
不论在 web 上做什么，都与请求和响应有关。

---

### Web 应用框架
> 它提供了一组通用的基础技术，可以基于这些技术构建 Web 应用

#### Flask

Flask 提供了一组模块，可以帮助我们构建服务器端 Web 应用，它是一个微 Web 框架，规模很小而且易用。

`python3 -m pip install flask` **---> 可以进行安装**


**简单分析**
```py
from flask import Flask # Flask 是一个类名

app = Flask(__name__) # 创建 Flask 对象的一个实例，并把它赋给 “app”

@app.route('/') 
# 当访问路径为 / 时，route 修饰符会安排 Flask web 服务器调用这个函数

def hello() -> str:
    return 'Hello world from Flask!'

app.run() # 让 Web 应用运行起来
```
- `__name__` 值由 python 解释器维护，在程序代码中的任何地方使用这个值时，**它会设置为当前活动模块的名字**。
- `__name__` 简称 `dunder name`，表示同一个东西
- 函数修饰符可以调整一个现有函数的行为，而无需修改这个函数的代码 **(也就是说，函数得到修饰)**。 ---> `@` 符号


#### HTML 表单
> 使用模版会让 HTML 更易于维护

**模版引擎**  
利用模版引擎，可以应用面向对象的**继承**和**重用**概念生成文本数据，如 Web 页面。  

网站的外观可以在一个顶层 HTML 模版中定义，称为 **基模版**，其它 HTML 页面继承这个模版。  

**`Flask` 提供的模版引擎名为 `Jinja2`**

**处理提交的数据**  
- `@app.route('/search4', methods=['POST'])`
  - 这行代码指出 /search4 URL 只支持 `POST` 方法

**打开调试**
- `app.run(debug=True)`
