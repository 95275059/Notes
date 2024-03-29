# Python笔记38--JSONSchema

## 简介

+ JSON Schema是基于JSON格式，用于定义JSON数据结构以及校验JSON数据内容的一种词汇表
+ JSON Schema官网地址：http://json-schema.org/

## JSON Schema中比较常见的关键字

| 关键字           | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| $schema          | 表示该JSON Schema文件遵循的规范                              |
| title            | 为该JSON Schema文件提供一个标题                              |
| description      | 关于该JSON Schema文件的描述信息                              |
| type             | 表示待校验元素的类型（例如，最外层的type表示待校验的是一个JSON对象，内层type分别表示待校验的元素类型为，整数，字符串，数字） |
| properties       | 定义待校验的JSON对象中，各个key-value对中value的限制条件     |
| required         | 定义待校验的JSON对象中，必须存在的key                        |
| minimum          | 用于约束取值范围，表示取值范围应该大于或等于minimum          |
| exclusiveMinimum | 如果minimum和exclusiveMinimum同时存在，且exclusiveMinimum的值为True，则表示取值范围只能大于minimum<br />或者：用于约束取值范围，表示取值范围只能大于exclusiveMinimum |
| maximum          | 用于约束取值范围，表示取值范围应该小于或等于maximum          |
| exclusiveMaximum | 如果maximum和exclusiveMaximum同时存在，且exclusiveMaximum的值为True，则表示取值范围只能小于maximum<br />或者：用于约束取值范围，表示取值范围只能小于exclusiveMinimum |
| multipleOf       | 用于约束取值，表示取值必须能够被multipleOf所指定的值整除     |
| maxLength        | 字符串类型数据的最大长度                                     |
| minLength        | 字符串类型数据的最小长度                                     |
| pattern          | 使用正则表达式约束字符串类型数据                             |

+ 实例一

  ```python
  # 导入验证器
  from jsonschema import validate
  
  # 编写schema：
  my_schema = {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "title": "TestInfo",
      "description": "some information about test",
      "type": "object",
      "properties": {
          "name": {
              "description": "Name of the test",
              "type": "string"
          },
          "age": {
              "description": "age of test",
              "type": "integer"
          }
      },
      "required": [
          "name", "age"
      ]
  }
  
  # json数据：
  json_data = {
      "name": "python",
      "age": 25
  }
  
  # 验证：
  validate(instance=json_data, schema=my_schema)
  ```

  + validate() 函数将首先验证所提供的模式本身是否有效，因为不这样做会导致不太明显的错误消息，并以不太明显或一致的方式失败。然后再验证json数据。
  + 如果JSON数据实例是无效的，则抛出 jsonschema.exceptions.ValidationError 异常
  + 如果schema模式本身是无效的，则抛出 jsonschema.exceptions.SchemaError 异常

+ $schema

  + 该关键字用于指定JSON Schema版本信息

    实例中指定的版本为：draft-04。

  + 该关键字是可以省略的，当前最新版本为draft-07。

  + 注意：该关键字的值必须使用官方提供的值，不能自己随便写。

+ title和description

  + 这两个关键字都是用来描述对应的JSON元素的

    例一中最外层的title和description是对待校验JSON对象的描述

    而其中，name元素之下的description其实是对待校验JSON对象的一级key（name）的描述，当然，你也可以对name增加title信息。

  + 唯一的区别在于，title相对来说，更加简洁，而description更加倾向于详细描述相关信息。
  + 这两个关键字都是可以省略的。

+ type

  + 该关键字用于限定待校验JSON元素所属的数据类型

    例一中最外层的type关键字值为object，即表示待校验JSON数据为一个JSON对象

    而name下的type关键字值为string，即表示待校验JSON对象中的一级key（name）的数据类型为string。

---

## type常见取值

| type取值 | 对应的python数据类型 |
| -------- | -------------------- |
| object   | Object               |
| array    | List                 |
| integer  | int                  |
| number   | float或int           |
| null     | None                 |
| boolean  | .Boolean             |
| string   | String               |

### type取值为object时

涉及的关键字：properties、required、minProperties、maxProperties、propertyNames、dependencies、patternProperties、additionalProperties

#### properties

+ 该关键字的值是一个对象。

+ 用于指定JSON对象中的各种不同key应该满足的校验逻辑

  每个key对应的值，都是一个JSON Schema，则待校验JSON对象通过校验。

  从这里，我们可以看到，只要待校验JSON对象的所有key分别都通过对应的JSON Schema的校验检测，这个对象才算是通过校验。

+ 另外，需要注意的是，省略该关键字和该关键字的值为空对象，具有相同效果

#### required

+ 该关键字的值是一个数组，而数组中的元素必须是字符串，而且必须是唯一的。

+ 该关键字限制了JSON对象中必须包含哪些**一级key**。

  如果一个JSON对象中含有required关键字所指定的所有一级key，则该JSON对象能够通过校验。

+ 另外，需要注意的是，省略该关键字和该关键字的值为空数组，具有相同效果。

#### minProperties, maxProperties

+ 这两个关键字的值都是非负整数。

+ 指定了待校验JSON对象中一级key的个数限制，minProperties指定了待校验JSON对象可以接受的最少一级key的个数，而maxProperties指定了待校验JSON对象可以接受的最多一级key的个数。

+ 另外，需要注意的是，省略minProperties关键字和该关键字的值为0，具有相同效果。

+ 而，如果省略maxProperties关键字则表示对一级key的最大个数没有限制。

+ 例如，如果限制一个JSON对象的一级key的最大个数为5，最小个数为1，则JSON Schema如下：

  ```json
  "minProperties": 1,
  "maxProperties": 5
  ```

#### propertyNames

+ 注意：该关键字，官方说明中支持，但是，有可能你使用的平台或者第三方工具不支持哦。所以，使用需谨慎。

+ 该关键字的值是一个有效的JSON Schema。

  如果待校验JSON对象中的每个一级key都能通过该关键字指定的JSON Schema的校验，那么才认为待校验的JSON对象通过校验。注意，待校验JSON对象的一级key都是string类型。

+ 另外，需要注意的是，省略该关键字和该关键字的值为空JSON Schema，具有相同效果。

#### patternProperties

+ 该关键字的值是一个JSON对象，该JSON对象的每一个一级key都是一个正则表达式，value都是一个JSON Schema。

+ 只有待校验JSON对象中的一级key，通过与之匹配的patternProperties中的一级正则表达式，对应的JSON Schema的校验，才算通过校验。例如，如果patternProperties对应的值如下：

  ```json
  "patternProperties": {
          "^a": {
              "type": "number"
          },
          "^b": {
              "type": "string"
          }
  }
  ```

  上面的JSON Schema表示，待校验JSON对象中，所有以a开头的一级key的value都必须是number，所有以b开头的一级key的value都必须是string。

#### additionalProperties

+ 该关键字的值是一个JSON Schema。

+ 如果待校验JSON对象中存在，既没有在properties中被定义，又没有在patternProperties中被定义，那么这些一级key必须通过additionalProperties的校验。

#### dependencies

待定

#### 实例

```python
# 导入验证器
from jsonschema import validate

# 编写schema：
my_schema = {
    "type": "object",
    "properties": {
        "id": {
            "description": "The unique identifier for a book",
            "type": "integer",
            "minimum": 1
        },
        "price": {
            "type": "number",
            "minimum": 0,
        }
    },
    "patternProperties": {
        "^a": {
            "type": "number"
        },
        "^b": {
            "type": "string"
        }
    },
    "additionalProperties": {
        "type": "string"
    },
    "minProperties": 1,
    "maxProperties": 5,
    "required": [
        "id",
        "name",
        "price"
    ]
}

# json数据：
json_data = {
    "id": 1,
    "name": "python",
    "price": 25
}

# 验证：
print(validate(instance=json_data, schema=my_schema))
```

---

### type取值为array

涉及的关键字：items、additionalItems、minItems、maxItems、uniqueItems、contains

#### items

+ 该关键字的值是一个有效的JSON Schema或者一组有效的JSON Schema。

  + 当该关键字的值是一个有效的JSON Schema时，只有待校验JSON数组中的所有元素均通过校验，整个数组才算通过校验。例如，如果items关键字的具体定义如下：

    ```json
    {
       "type": "array",
       "items": {
         "type": "string",
         "minLength": 5 
       }
    }
    ```

    上面的JSON Schema的意思是，待校验JSON数组的元素都是string类型，且最小可接受长度是5。

    ```python
    ["myhome", "green"] #符合要求
    ```

    ```python
    ["home", "green"]  #不符合要求
    ```

  + 当该关键字的值是一组有效的JSON Schema时，只有待校验JSON数组的所有元素通过items的值中对应位置上的JSON Schema的校验，那么，整个待校验JSON数组才算通过校验。

    这里需要注意的是，如果items定义的有效的JSON Schema的数量和待校验JSON数组中元素的数量不一致，那么就要采用**“取小原则”**。即，如果items定义了3个JSON Schema，但是待校验JSON数组只有2个元素，这时，只要待校验JSON数组的前两个元素能够分别通过items中的前两个JSON Schema的校验，那么，我们认为待校验JSON数组通过了校验。而，如果待校验JSON数组有4个元素，这时，只要待校验JSON数组的前三个元素能够通过items中对应的JSON Schema的校验，我们就认为待校验JSON数组通过了校验。

    如果items值如下：

    ```json
    {
        "type": "array",
        "items": [
            {
                "type": "string",
                "minLength": 5
            },
            {
                "type": "number",
                "minimum": 10
            },
            {
                "type": "string"
            }
        ]
    }
    ```

    上面的JSON Schema指出了待校验JSON数组应该满足的条件，数组的第一个元素是string类型，且最小可接受长度为5，数组的第二个元素是number类型，最小可接受的值为10，数组的第三个元素是string类型。那么下面这两个JSON数组明显是符合要求的，具体内容如下：

    ```python
    ["green", 10, "good"]
    ["helloworld", 11]
    ```

    下面这两个JSON数组却是不符合要求的，具体内容如下：

    ```json
    ["green", 9, "good"]
    ["good", 12]
    ```

#### additionalItems

+ 该关键字的值是一个有效的JSON Schema。

+ 需要注意的是，**该关键字只有在items关键字的值为一组有效的JSON Schema的时候，才可以使用**，用于规定超出items中JSON Schema总数量之外的待校验JSON数组中的剩余的元素应该满足的校验逻辑。当然了，只有这些剩余的所有元素都满足additionalItems的要求时，待校验JSON数组才算通过校验。

  其实，你可以这么理解，当items的值为一组有效的JOSN Schema的时候，一般可以和additionalItems关键字组合使用，items用于规定对应位置上应该满足的校验逻辑，而additionalItems用于规定超出items校验范围的所有剩余元素应该满足的条件。如果二者同时存在，那么只有待校验JSON数组同时通过二者的校验，才算真正地通过校验。

+ 另外，需要注意的是，如果items只是一个有效的JSON Schema，那么就不能使用additionalItems，原因也很简单，因为items为一个有效的JSON Schema的时候，其规定了待校验JSON数组所有元素应该满足的校验逻辑。additionalItems已经没有用武之地了。

+ 最后，同样强调一下，省略该关键字和该关键字的值为空JSON Schema，具有相同效果。

+ 如果一个JSON Schema如下：

  ```json
  {
      "type": "array",
      "items": [
          {
              "type": "string",
              "minLength": 5
          },
          {
              "type": "number",
              "minimum": 10
          }
      ],
      "additionalItems": {
          "type": "string",
          "minLength": 2
      }
  }
  ```

  上面的JSON Schema的意思是，待校验JSON数组第一个元素是string类型，且可接受的最短长度为5个字符，第二个元素是number类型，且可接受的最小值为10，剩余的其他元素是string类型，且可接受的最短长度为2。

  那么，下面三个JSON数组是能够通过校验的，具体内容如下：

  ```python
  ["green", 10, "good"]
  ["green", 11]
  ["green", 10, "good", "ok"]
  ```

  下面JSON数组是无法通过校验的，具体内容如下：

  ```python
  ["green", 10, "a"]
  ["green", 10, "ok", 2]
  ```

#### minItems, maxItems

+ 这两个关键字的值都是非负整数。

+ 指定了待校验JSON数组中元素的个数限制，minItems指定了待校验JSON数组可以接受的最少元素个数，而maxItems指定了待校验JSON数组可以接受的最多元素个数。

+ 另外，需要注意的是，省略minItems关键字和该关键字的值为0，具有相同效果。而，如果省略maxItems关键字则表示对元素的最大个数没有限制。例如，如果限制一个JSON数组的元素的最大个数为5，最小个数为1，则JSON Schema如下：

  ```python
  "minItems": 1,
  "maxItems": 5
  ```

#### uniqueItems

+ 该关键字的值是一个布尔值，即boolean（true、false）。

+ 当该关键字的值为true时，只有待校验JSON数组中的所有元素都具有唯一性时，才能通过校验。当该关键字的值为false时，任何待校验JSON数组都能通过校验。

+ 另外，需要注意的是，省略该关键字和该关键字的值为false时，具有相同的效果。例如：

  ```python
  "uniqueItems": true
  ```

#### contains

+ **注意：该关键字，官方说明中支持，但是，有可能你使用的平台或者第三方工具不支持哦。所以，使用需谨慎。**
+ 该关键字的值是一个有效的JSON Schema。
+ 只有待校验JSON数组中至少有一个元素能够通过该关键字指定的JSON Schema的校验，整个数组才算通过校验。
+ 另外，需要注意的是，省略该关键字和该关键字的值为空JSON Schema具有相同效果。

+ 完整示例

  ```python
  # 导入验证器
  from jsonschema import validate
  
  # 编写schema：
  my_schema = {
      "type": "array",
      "items": [
          {
              "type": "string",
              "minLength": 5
          },
          {
              "type": "number",
              "minimum": 10
          }
      ],
      "additionalItems": {
          "type": "string",
          "minLength": 2
      },
      "minItems": 1,
      "maxItems": 5,
      "uniqueItems": True
  }
  
  # json数据：
  json_data = ["green", 10, "good", "good"]
  
  # 验证：
  print(validate(instance=["green", 10, "good", "good"], schema=my_schema)) #jsonschema.exceptions.ValidationError
  print(validate(instance=["green", 10, "good", "cc", "dd", "xx"], schema=my_schema)) #jsonschema.exceptions.ValidationError
  print(validate(instance=["green", 10, "good"], schema=my_schema)) #None
  ```

### type取值为integer或number

涉及的关键字：multipleOf、maximum、exclusiveMaximum、minimum、exclusiveMinimum

#### integer和number的区别

+ integer相当于python中的int类型
+ 而number相当于python中的int或float类型。

#### multipleOf

+ 该关键字的值是一个大于0的number，即可以是大于0的int，也可以是大于0的float。

+ 只有待校验的值能够被该关键字的值整除，才算通过校验。

+ 如果含有该关键字的JSON Schema如下：

  ```json
  {
      "type": "integer",
      "multipleOf": 2
  }
  ```

  那么，2、4、6都是可以通过校验的，但是，3、5、7都是无法通过校验的，当然了，2.0、4.0也是无法通过校验的，但是，并不是因为multipleOf关键字，而是因为type关键字。

+ 如果含有multipleOf关键字的JSON Schema如下：

  ```json
  {
      "type": "number",
      "multipleOf": 2.0
  }
  ```

  那么，2、2.0、4、4.0都是可以通过校验的，但是，3、3.0、3、3.0都是无法通过校验的。

+ 另外，需要注意的是，省略该关键字则不对待校验数值进行该项校验。

#### maximum

+ 该关键字的值是一个number，即可以是int，也可以是float。

+ 该关键字规定了待校验元素可以通过校验的最大值。即传入的值必须小于等于maximum。

+ 省略该关键字，即表示对待校验元素的最大值没有要求。

#### exclusiveMaximum

+ 该关键字的值是一个number。

+ 该关键字和maximum一样，规定了待校验元素可以通过校验的最大值，不同的是待校验元素只能小于exclusiveMaximum指定的值。

#### minimum、exclusiveMinimum

minimum、exclusiveMinimum关键字的用法和含义与maximum、exclusiveMaximum相似。唯一的区别在于，一个约束了待校验元素的最小值，一个约束了待校验元素的最大值。

### type取值为string

涉及的关键字：maxLength、minLength、pattern、format

#### maxLength

+ 该关键字的值是一个非负整数。

+ 该关键字规定了待校验JSON元素可以通过校验的最大长度，即待校验JSON元素的最大长度必须小于等于该关键字的值。

+ 另外，需要注意的是，如果省略该关键字则表示对待校验元素的最大长度没有限制。

#### minLength

+ 该关键字的值是一个非负整数。

+ 该关键字规定了待校验JSON元素可以通过校验的最小长度，即待校验JSON元素的最小长度必须大于或者等于该关键字的值。

+ 另外，需要注意的是，如果省略该关键字和该关键字的值为0，具有相同效果。

#### pattern

+ 该关键字的值是一个正则表达式。
+ 只有待校验JSON元素符合该关键字指定的正则表达式，才算通过校验。

#### format

+ 该关键字的值可以是以下取值：

  date、date-time（时间格式）、email（邮件格式）、hostname（网站地址格式）、ipv4、ipv6、uri等等。

  ```json
  {
      "type": "string",
      "format": "email"
  }
  ```

+ 使用format关键字时，在实例化validator时必须给它传format_checker参数,fromat_checker参数的值即是各种版本的JSON模式规范的验证器类，如：
  [Draft 7](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.Draft7Validator)
  [Draft 6](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.Draft6Validator)
  [Draft 4](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.Draft4Validator)
  [Draft 3](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.Draft3Validator)

  当你实例化validator时,如果没有给它传format_checker参数, jsonschema是不会自动校验schema中的format关键字的.因此,你需要做以下步骤:

  + 额外导入JSON Schema某个版本的模式规范如：

    ```python
    from jsonschema import draft7_format_checker
    ```

  + 实例化validator时传入：

    ```python
    validate(instance=json_data, schema=my_schema, format_checker=draft7_format_checker)
    ```

### 全类型可用

即不局限于某个type，涉及的关键字：enum、const、allOf、anyOf、oneOf、not、default

#### enum

+ 该关键字的值是一个数组，该数组至少要有一个元素，且数组内的每一个元素都是唯一的。

+ 如果待校验的JSON元素和数组中的某一个元素相同，则通过校验。否则，无法通过校验。

+ 注意，该数组中的元素值可以是任何值，包括null。

+ 省略该关键字则表示无须对待校验元素进行该项校验

+ 例如：

  ```python
  {
      "type": "number",
      "enum": [2, 3, null, "hello"]
  }
  ```

#### const

+ 该关键字的值可以是任何值，包括null。
+ 如果待校验的JSON元素的值和该关键字指定的值相同，则通过校验。否则，无法通过校验。
+ 省略该关键字则表示无须对待校验元素进行该项校验。
+ **注意，该关键字部分第三方工具，并不支持。**

#### allOf

+ 该关键字的值是一个非空数组，数组里面的每个元素都必须是一个有效的JSON Schema。
+ 只有待校验JSON元素通过数组中所有的JSON Schema校验，才算真正通过校验。

#### oneOf

+ 该关键字的值是一个非空数组，数组里面的每个元素都必须是一个有效的JSON Schema。
+ 如果待校验JSON元素能且只能通过数组中的某一个JSON Schema校验，才算真正通过校验。不能通过任何一个校验和能通过两个及以上的校验，都不算真正通过校验。

#### not

+ 该关键字的值是一个JSON Schema。
+ 只有待校验JSON元素不能通过该关键字指定的JSON Schema校验的时候，待校验元素才算通过校验。

#### ==default==

+ 该关键字的值是没有任何要求的。
+ 该关键字常常用来指定待校验JSON元素的默认值，当然，这个默认值最好是符合要求的，即能够通过相应的JSON Schema的校验。
+ 另外，需要注意的是，该关键字除了提示作用外，并不会产生任何实质性的影响。

### type关键字

+ 需要特别注意的是，type关键字的值可以是一个string，也可以是一个数组。

+ 如果type的值是一个string，则其值只能是以下几种：null、boolean、object、array、number、string、integer。

+ 如果type的值是一个数组，则数组中的元素都必须是string，且其取值依旧被限定为以上几种。

  只要待校验JSON元素是其中的一种，则通过校验。

## JSON Schema比较复杂的示例

```python
from jsonschema import validate, draft7_format_checker
from jsonschema.exceptions import SchemaError, ValidationError


schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "book info",
    "description": "some information about book",
    "type": "object",
    "properties": {
        "id": {
            "description": "The unique identifier for a book",
            "type": "integer",
            "minimum": 1
        },
        "name": {
            "description": "book name",
            "type": "string",
            "minLength": 3,
            "maxLength": 30
        },
        "info": {
            "description": "simple information about book",
            "type": "string",
            "minLength": 10,
            "maxLength": 60
        },
        "price": {
            "description": "book price",
            "type": "number",
            "multipleOf": 0.5,
            # 这里没有取等，5.0<price<99999.0
            "minimum": 5.0,
            "maximum": 99999.0,
            # 若使用下面这两个关键字则 5.0<=price<=99999.0
            # "exclusiveMinimum": 5.0,
            # "exclusiveMaximum": 99999.0
        },
        "tags": {
            "type": "array",
            "items": [
                {
                    "type": "string",
                    "minLength": 2,
                    "macLength": 8
                },
                {
                    "type": "number",
                    "minimum": 1.0
                }
            ],
            "additonalItems": {
                "type": "string",
                "miniLength": 2
            },
            "miniItems": 1,
            "maxItems": 5,
            "uniqueItems": True
        },
        "date": {
            "description": "书籍出版日期",
            "type": "string",
            "format": "date",
        },
        "bookcoding": {
            "description": "书籍编码",
            "type": "string",
            "pattern": "^[A-Z]+[a-zA-Z0-9]{12}$"
        },
        "other": {
            "description": "其他信息",
            "type": "object",
            "properties": {
                "info1": {
                    "type": "string"
                },
                "info2": {
                    "type": "string"
                }
            }
        }
    },
    "minProperties": 3,
    "maxProperties": 7,
    "required": [
        "id", "name", "info", "price"
    ]
}

json_data = {
    "id": 1,
    "name": "jarvis手册",
    "info": "贾维斯平台使用手册1",
    "price": 5.5,
    "tags": ["jar"],
    "date": "2019-5-25",
    "other": {
        "info1": "1111",
        "info2": "222"
    }
}


try:
    validate(instance=json_data, schema=schema, format_checker=draft7_format_checker)
except SchemaError as e:
    print("验证模式schema出错：\n出错位置：{}\n提示信息：{}".format(" --> ".join([i for i in e.path]), e.message))
except ValidationError as e:
    print("json数据不符合schema规定：\n出错字段：{}\n提示信息：{}".format(" --> ".join([i for i in e.path]), e.message))
else:
    print("验证成功！")
```







