# Python模块18--JSONSchema

## 参考网址

https://blog.csdn.net/swinfans/article/details/89231682

## 简介

+ `jsonschema` 是JSON Schema的Python实现（支持Python 2.7+ 包括Python3）。

### 功能

- 完全支持 [Draft 7](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.Draft7Validator)，[Draft 6](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.Draft6Validator)，[Draft 4](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.Draft4Validator) 和[Draft 3](https://python-jsonschema.readthedocs.io/en/latest/validate/#jsonschema.Draft3Validator)。
- 延迟验证，可以迭代地报告所有验证错误。
- 可以以编程方式查询哪些属性或项验证失败。

### 安装

+ win

  ```python
  pip install jsonchema
  ```

## API详解

### 模式验证

#### 基础语法

在给定模式下验证JSON实例的最简单方法是使用 `validate()` 函数。

```python
jsonschema.validate(instance, schema, cls=None, *args, **kwargs)
```

+ instance : 要验证的json实例

+ schema : 要使用的模式

+ cls : 被用来验证JSON实例的验证器类

  如果 *cls* 参数未提供，按照规范，将会发生两件事。

  + 首先，如果模式具有包含已知元模式的 `$schema` 属性，那么将使用适当的验证器。由于这个原因，规范建议所有模式都包含 `$schema` 属性。
  + 如果没有找到 `$schema` 属性，则使用最新发布的草案作为验证器类。

  在实例化 *cls* 时，将传递提供的所有的位置参数和关键字参数。

+ 返回值

  验证通过，无返回值，print为None

  验证不通过将抛出异常

  + 如果JSON数据实例是无效的，则抛出 `jsonschema.exceptions.ValidationError` 异常

  + 如果schema模式本身是无效的，则抛出 `jsonschema.exceptions.SchemaError `异常

`validate()` 函数将首先验证所提供的模式本身是否有效，因为不这样做会导致不太明显的错误消息，并以不太明显或一致的方式失败。然后再验证json数据。

如果想要用一个有效的模式验证多个实例，可以在一个特定的验证器上直接使用 `IValidator.validate()` 方法（例如，`Draft7Validator.validate()`）。

### 验证器接口

+ jsonschema 定义了一个所有验证器类都应该遵守的(非正式的)接口。

  ```python
  class jsonschema.IValidator(schema, types=(), resolver=None, format_checker=None)
  ```

  + schema(dict) : 验证器对象将使用的模式。

    这个模式被假定为有效的，如果提供一个了无效的模式可能会导致未定义的行为。

  + resolver : 用于解析 `$ref` 属性（JSON引用）的 *RefResolver* 实例

    如果未提供，则会创建一个。