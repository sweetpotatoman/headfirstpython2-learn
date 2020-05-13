## 结构化数据

---

### 字典
> 无序的 key/value 对集合

- 字典是无序而且可变的
- 字典存储键值对
- 不能依赖解释器所用的内部顺序  



#### for key/value 简写
通常使用 `for` 循环迭代字典，使用 `kv` 作为键值对的简写，也可以使用别的变量名，**解释器只处理字典的键**

- 这个输出没有值出来，只有键
  ```python 
  for kv in found:
      print(kv)
  ```

- 输出键和值
  ```py
  for k in found:
      print(k, 'was found', found[k], 'time(s).')
  ```

- 指定输出对的字典顺序 --- `sorted`
  ```py
  for k in sorted(found):
      print(k, 'was found', found[k], 'time(s).')
  ```

- 用 "items" 迭代处理字典 --- `items`
  ```py
  for k,v in sorted(found.items()):
      print(k, 'was found', v, 'time(s).')
  ```

#### 字典的键必须初始化
当试图访问一个不存在键的关联值，就会产生 KeyError 的报错

- 初始化健值
  ```py
  found = {}
  
  found['a'] = 0
  found['e'] = 0
  found['i'] = 0
  found['o'] = 0
  found['u'] = 0
  ```
  
- 使用 `in` 和 `not in` 来判断字典的键是否存在，不存在则初始化
  ```py
  fruits = {}

  if 'bananas' in fruits:
      fruits['bananas'] += 1
  else:
      fruits['bananas'] = 1
  ```

  ```py
  if 'pears' not in fruits:
      fruits['pears] = 0
  ```

- 使用 `setdefault` 方法初始化
  ```py
  fruits.setdefault('pears', 0)
  fruits['pears'] += 1
  ```

---

### 集合
> 无序的唯一对象集合
- 保证其中的任何对象不会重复
- 可以完成**并集/交集/差集**操作
  
```py
vowels = {'a','a','e','i'}
vowels //{'a','e','i'}

vowels2 = set('aaei')
vowels2 //{'a','e','i'}
```

#### 集合方法
```py
  vowels = set('aeiou')
  word = 'hello'
  ```
- 并集
  - 使用 `union` 方法让两个集合合并，同时多了一个 `u` 集合
    ```py
    u = vowels.union(set(word))
    ```
  - 将 `u` 集合转换成有序列表
    ```py
    u_list = sorted(list(u))
    u_list // ['a','e','h','i','l','o','u']
    ```

- 差集

  - 使用 `difference` 方法让两个集合进行差集，找出各自没有的元素
    ```py
    d = vowels.difference(set(word))
    d // {'u','i','a'}
    ```

- 交集
  - 使用 `intersection` 方法让两个集合进行交集，找出共有元素
    ```py
    i = vowels.intersection(set(word))
    i // {'e','o'}
    ```

---

### 元组  
> 有序的不可变对象集合 
- **元组是一个不可变的列表**
- 元组 --- 常量列表
- 适合对象不能再被修改，例如该对象不想再被代码修改，可以使用元组    