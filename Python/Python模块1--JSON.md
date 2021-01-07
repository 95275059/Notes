# Python模块1--JSON

### 描述

+ JSON的全称是JavaScript Object Notation，即JavaScript 对象符号，它是一种轻量级、跨平台、跨语言的数据交换格式，其设计意图是把所有事情都用设计的字符串来表示，这样既方便在互联网上传递信息，也方便人进行阅读。
+ 最早的时候，JSON 是 JavaScript 语言的数据交换格式，后来慢慢发展成一种语言无关的数据交换格式，这一点非常类似于 XML
+ JSON 主要在类似于C 的编程语言中广泛使用，这些语言包括 C、C++、C#、Java、JavaScript、Perl、Python 等。
+ JSON 提供了多种语言之间完成数据交换的能力，因此，JSON 也是一种非常理想的数据交换格式。

### JSON数据结构

JSON主要有两种数据结构

+ 由key-value对组成的数据结构。

  这种数据结构在不同的语言中有不同的实现。

  在 JavaScript 中是一个对象；

  在 Python 中是一种 dict 对象；

  在 C 语言中是一个 struct；

  在其他语言中，则可能是 record、dictionary、hash table 等。

+ 有序集合

  这种数据结构在 Python 中对应于列表；
  
  在其他语言中，可能对应于 list、vector、数组和序列等。

上面两种数据结构在不同的语言中都有对应的实现，因此这种简便的数据表示方式完全可以实现跨语言。所以，JSON 可以作为程序设计语言中通用的数据交换格式。

### JSON类型转换Python类型的对应关系

| JSON类型             | Python类型      |
| -------------------- | --------------- |
| 对象（object）       | 字典（dict）    |
| 数组（array）        | 列表（list）    |
| 字符串（string）     | 字符串（str）   |
| 整数（number(int)）  | 整数（int）     |
| 实数（number(real)） | 浮点数（float） |
| true                 | True            |
| false                | False           |
| null                 | None            |

### Python类型转换JSON类型的对应关系

| Python类型                                                   | JSON类型         |
| ------------------------------------------------------------ | ---------------- |
| 字典（dict）                                                 | 对象（object）   |
| 列表（list）和元组（tuple）                                  | 数组（array）    |
| 整数，浮点数，以及整型，浮点型派生的枚举（float,int-& float-derived Enums） | 数值型（number） |
| True                                                         | true             |
| False                                                        | false            |
| None                                                         | null             |

### JSON模块

+ json.dump

  ```python
  json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
  ```

  将obj对象转换成JSON字符串输出到fp流中，fp是一个支持write()方法的类文件对象

  + `obj`: 表示是要序列化的对象。
  + `fp`: 文件描述符，将序列化的str保存到文件中。json模块总是生成str对象，而不是字节对象；因此，fp.write（）必须支持str输入。
  + `skipkeys`: 默认为`False`,如果skipkeys`True`，则将跳过不是基本类型（str，int，float，bool，None）的dict键，不会引发`TypeError`。
  + `ensure_ascii`: 默认值为`True`,能将所有传入的非ASCII字符转义输出。如果`ensure_ascii`为`False`，则这些字符将按原样输出。
  + `check_circular`:默认值为`True`,如果`check_circular`为`False`，则将跳过对容器类型的循环引用检查，循环引用将导致`OverflowError`。
  + `allow_nan`: 默认值为`True`,如果`allow_nan`为`False`，则严格遵守JSON规范,序列化超出范围的浮点值（nan，inf，-inf）会引发`ValueError`。 如果`allow_nan`为`True`,则将使用它们的`JavaScript`等效项（NaN，Infinity，-Infinity）。
  + **`indent`: 设置缩进格式，默认值为`None`**,选择的是最紧凑的表示。如果`indent`是非负整数或字符串，那么JSON数组元素和对象成员将使用该缩进级别进行输入；`indent`为0,负数或“”仅插入换行符；`indent`使用正整数缩进多个空格；如果`indent`是一个字符串（例如“\t”），则该字符串用于缩进每个级别。
  + **`separators`: 去除分隔符后面的空格，默认值为`None`**,如果指定，则分隔符应为（item_separator，key_separator）元组。如果缩进为`None`，则默认为（’’, ’: ’）;要获得最紧凑的JSON表示，可以指定（’,’，’:’）以消除空格。
  + `default`: 默认值为`None`,如果指定，则`default`应该是为无法以其他方式序列化的对象调用的函数。它应返回对象的JSON可编码版本或引发`TypeError`。如果未指定，则引发`TypeError`。
  + **`sort_keys`: 默认值为`False`**,如果`sort_keys`为`True`，则字典的输出将按键值排序。

+ json.dumps

  ```python
  json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan= True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
  ```

  将obj对象转换为JSON字符串，并返回该JSON字符串。

  原字符串不变

+ json.load

  ```python
  json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
  ```

  从 fp 流读取 JSON 字符串，将其恢复成obj对象，其中 fp 是一个支持 write() 方法的类文件对象。

  + `fp`: 文件描述符，将fp（.read（）支持包含JSON文档的文本文件或二进制文件）反序列化为Python对象。

  + `object_hook`: 默认值为`None`,`object_hook`是一个可选函数，此功能可用于实现自定义解码器。指定一个函数，该函数负责把反序列化后的基本类型对象转换成自定义类型的对象。

    它会将（loads的)返回结果字典替换为你所指定的类型,这个功能可以用来实现自定义解码器，如`JSON-RPC`

  + `parse_float`: 默认值为`None`,如果指定了`parse_float`，用来对`JSON` float字符串进行解码,这可用于为`JSON`浮点数使用另一种数据类型或解析器。

  + `parse_int`: 默认值为`None`,如果指定了`parse_int`，用来对`JSON` int字符串进行解码,这可以用于为JSON整数使用另一种数据类型或解析器。

  + `parse_constant`:默认值为`None`,如果指定了`parse_constant`,对`-Infinity`,`Infinity`,`NaN`字符串进行调用。如果遇到了无效的`JSON`符号，会引发异常。

    如果进行反序列化（解码）的数据不是一个有效的`JSON`文档，将会引发 `JSONDecodeError`异常。

  + `object_pairs_hook`参数是可选的，它会将结果以key-value有序列表的形式返回,形式如：`[(k1, v1), (k2, v2), (k3, v3)]`

    如果`object_hook`和`object_pairs_hook`同时指定的话优先返回`object_pairs_hook`

+ json.loads

  ```python
  json.loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)
  ```

  将JSON字符串恢复成obj对象。


### 实例

+ dumps,dump,JSONEncoder

  ```python
  import json
  
  # 将Python对象转JSON字符串（元组会当成数组）
  s = json.dumps(['yeeku', {'favorite': ('coding', None, 'game', 25)}])
  print(s) # ["yeeku", {"favorite": ["coding", null, "game", 25]}]
  
  # 简单的Python字符串转JSON
  s2 = json.dumps("\"foo\bar")
  print(s2) #"\"foo\bar"
  
  # 简单的Python字符串转JSON
  s3 = json.dumps('\\')
  print(s3) #"\\"
  
  # Python的dict对象转JSON，并对key排序
  s4 = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
  print(s4) #{"a": 0, "b": 0, "c": 0}
  
  # 将Python列表转JSON，
  # 并指定JSON分隔符：逗号和冒号之后没有空格（默认有空格）
  s5 = json.dumps([1, 2, 3, {'x': 5, 'y': 7}], separators=(',', ':'))
  # 输出的JSON字符串中逗号和冒号之后没有空格
  print(s5) # '[1,2,3,{"4":5,"6":7}]'
  
  # 指定indent为4，意味着转换的JSON字符串有缩进
  s6 = json.dumps({'Python': 5, 'Kotlin': 7}, sort_keys=True, indent=4)
  print(s6)
  
  # 使用JSONEncoder的encode方法将Python转JSON
  s7 = json.JSONEncoder().encode({"names": ("孙悟空", "齐天大圣")})
  print(s7) # {"names": ["\u5b59\u609f\u7a7a", "\u9f50\u5929\u5927\u5723"]}
  
  f = open('a.json', 'w')
  # 使用dump()函数将转换得到JSON字符串输出到文件
  json.dump(['Kotlin', {'Python': 'excellent'}], f)
  ```

  dumps() 和 dump() 函数的功能、所支持的选项基本相同，只是 dumps() 函数直接返回转换得到的 JSON 字符串，而 dump() 函数则将转换得到的 JSON 字符串输出到文件中。

+ loads,load,decode

  ```python
  import json
  
  # 将JSON字符串恢复成Python列表
  result1 = json.loads('["yeeku", {"favorite": ["coding", null, "game", 25]}]')
  print(result1) # ['yeeku', {'favorite': ['coding', None, 'game', 25]}]
  
  # 将JSON字符串恢复成Python字符串
  result2 = json.loads('"\\"foo\\"bar"')
  print(result2) # "foo"bar
  
  # 定义一个自定义的转化函数
  def as_complex(dct):
      if '__complex__' in dct:
          return complex(dct['real'], dct['imag'])
      return dct
  # 使用自定义的恢复函数
  # 自定义回复函数将real数据转成复数的实部，将imag转成复数的虚部
  result3 = json.loads('{"__complex__": true, "real": 1, "imag": 2}',\
      object_hook=as_complex)
  print(result3) # (1+2j)
  
  f = open('a.json')
  # 从文件流恢复JSON列表
  result4 = json.load(f)
  print(result4) # ['Kotlin', {'Python': 'excellent'}]
  ```

+ JSONEncoder

  ```python
  import json
  
  # 定义JSONEncoder的子类
  class ComplexEncoder(json.JSONEncoder):
      def default(self, obj):
          # 如果要转换的对象是复数类型，程序负责处理
          if isinstance(obj, complex):
              return {"__complex__": 'true', 'real': obj.real, 'imag': obj.imag}
          # 对于其他类型，还使用JSONEncoder的默认处理
          return json.JSONEncoder.default(self, obj)
  s1 = json.dumps(2 + 1j, cls=ComplexEncoder)
  print(s1) # '{"__complex__": "true", "real": 2.0, "imag": 1.0}'
  s2 = ComplexEncoder().encode(2 + 1j)
  print(s2) # '{"__complex__": "true", "real": 2.0, "imag": 1.0}'
  ```

  上面程序扩展了 JSONEncoder 类的子类，并重写了它的 default() 方法，在方法中判断如果要转换的目标类型是复数（complex），程序就会进行自定义转换，即将复数转换成 JSON 对象，且该对象包含 "\_complex_":'true' 属性。

  一旦扩展了 JSONEncoder 的子类之后，程序有两种方式来使用自定义的子类：

  + 在 dumps() 或 dump() 函数中通过 cls 属性指定使用 JSONEncoder 的自定义子类。
  + 直接使用 JSONEncoder 的自定义子类的 encode() 方法来执行转换。
  
+ 自定义解码器

  ```python
  import json
  import collections
  class Person:
      def __init__(self, name, age, gender):
          self.name = name
          self.age = age
          self.gender = gender
  
      def toJSON(self):
          return {
              "name": self.name,
              "age": self.age,
              "gender": self.gender
          }
  
      @staticmethod
      def parseJSON(dct):
          if isinstance(dct, dict):
              p = Person(dct["name"], int(dct['age']), dct['gender'])
              return p
          return dct
  
  s = '{"name": "马云", "age": 54, "gender": "man"}'
  # 测试json.loads方法的object_hook参数
  p = json.loads(s, object_hook=Person.parseJSON)
  print("json.loads 是否将字符串转为字典了: --> " + str(isinstance(p, dict)))
  print("json.loads 是否将字符串转为Person对象了: --> " + str(isinstance(p, Person)))
  
  s = '{"name": "马云", "age": 54, "gender": "man"}'
  # 测试json.loads方法的object_pairs_hook参数
  print("-" * 30 + "> test object_pairs_hook <" + "-" * 30)
  p = json.loads(s, object_hook=Person.parseJSON, object_pairs_hook=collections.OrderedDict)
  # p = json.loads(s, object_hook=Person.parseJSON, object_pairs_hook=Person.parseJSON)
  print("json.loads 测试同时指定object_hook和object_pairs_hook,最终调用哪个参数: --> " + str(type(p)))
  print("json.loads 指定object_pairs_hook结果将会返回一个有序列表 --> {}".format(p))
  ```

  ```python
  json.loads 是否将字符串转为字典了: --> False
  json.loads 是否将字符串转为Person对象了: --> True
  ------------------------------> test object_pairs_hook <------------------------------
  json.loads 测试同时指定object_hook和object_pairs_hook,最终调用哪个参数: --> <class 'collections.OrderedDict'>
  json.loads 指定object_pairs_hook结果将会返回一个有序列表 --> OrderedDict([('name', '马云'), ('age', 54), ('gender', 'man')])
  ```

  

  

  

  
