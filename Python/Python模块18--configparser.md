# Python模块18--configparser

## 简介

### 模块名

+ python2下该模块名为ConfigParser
+ python3下该模块改名为configparser

### 功能

+ configparser是用来解析ini配置文件的解析器
+ ini文件结构
  + 键值对可用=或者:进行分隔
  + section的名字是区分大小写的,而key的名字是不区分大小写的
  + 键值对中头部和尾部的空白符会被去掉
  + 值可以为多行
  + 配置文件可以包含注释，注释以#或者;为前缀

+ Python的ConfigParser Module中定义了3个类对INI文件进行操作

  分别是RawConfigParser、ConfigParser、SafeConfigParser。

  RawCnfigParser是最基础的INI文件读取类，ConfigParser、SafeConfigParser支持对%(value)s变量的解析。

### default_section

`onfigparser`有`default_section`的概念,默认为`[DEFAULT]`节,也就是之后的所有的`section`都有该默认`section`中的键值对

## 使用

### 读取配置文件

+ ```python
  cf = configparser.ConfigParser()
  filename = cf.read(filename)
  ```

  读取文件内容

+ ```python
  sections_list = cf.sections()
  ```

  得到所有的section, 并以列表形式返回

+ ```python
  cf.options(section)
  ```

  得到section下所有的option

+ ```python
  cf.items(option)
  ```

  得到该section所有的键值对

+ ```python
  cf.get(section,option)
  ```

  得到section中option的值，返回string类型的结果

+ ```python
  cf.getint(section,option)
  ```

  得到section中option的值，返回int类型的结果

### 修改配置文件

+ ```python
  cf.write(filename)
  ```

  将configparser对象写入.ini类型的文件

+ ```python
  cf.add_section(new_section)
  ```

  添加一个新的section

+ ```python
  cf.set(section,option,value)
  ```

  对section中的option信息进行写入

+ ```python
  cf.remove_section(section)
  ```

  删除文件中的某个section

+ ```python
  cf.remove_option(section,option)
  ```

  删除文件中某个section下的option的数值

## 代码

```python
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 18:49:43 2021

@author: CXY
"""

import six
if six.PY2:
    import ConfigParser as cp
else:
    import configparser as cp

class ConfigHandler():
    def __init__(self,config_file):
        self.config_path = config_file
        try:
            self.configparser = cp.ConfigParser(allow_no_value=True)
            self.configparser.read(self.config_path)
        except cp.ParsingError():
            print('Parse %s failed'%self.config_path)

    def write_file(self):
        with open(self.config_path, 'w') as configfile:
            self.configparser.write(configfile)
            
    def add_section(self, section, option=None):
        #add a section and specified options to the config file
        #only add a section to the config file if option is empty
        if option is not None and type(option) is not dict:
            print('Dictionary format is required for parameter \'option\'!')
            return False
        elif option is not None:
            try:
                self.configparser.add_section(section)
                for key, value in option.items():
                    self.configparser.set(section, key, value)
                self.write_file()
                return True
            except cp.DuplicateSectionError:
                print('Section [%s] already exists in %s!, add section [%s] and related options to %s failed!' % (section, self.config_path, section, self.config_path))
                return False
            except:
                print("Add section [%s] and related options to %s failed!" % (section, self.config_path))
                return False
        else:
            try:
                self.configparser.add_section(section)
                self.write_file()
                return True
            except cp.DuplicateSectionError:
                print('Section [%s] already exists in %s, add section [%s] to %s failed!' % (section, self.config_path, section, self.config_path))
                return False
            except:
                print("Add section [%s] to %s failed!" % (section, self.config_path))
                return False
        
    def remove_section(self, section, option = None):
        #remove specified options of a section from the config file
        #remove the entire section from the config file if parameter option is empty
        if option is not None and type(option) is not list:
            print('List format is required for parameter \'option\'!')
            return False
        elif option is not None:
            try:
                for opt in option:
                    self.configparser.remove_option(section, opt)
                self.write_file()
                return True
            except cp.NoSectionError:
                print('Section [%s] not found in %s, remove related options of section [%s] from %s failed!' % (section, self.config_path, section, self.config_path))
                return False
            except:
                print("Remove related options of section [%s] from %s failed!" % (section, self.config_path))
                return False
        else:
            try:
                option = self.get_section(section)
                for opt in option:
                    self.configparser.remove_option(section, opt)
                self.configparser.remove_section(section)
                self.write_file()
                return True
            except cp.NoSectionError:
                print('Section [%s] not found in %s, remove section [%s] and its options from %s failed!' % (section, self.config_path, section, self.config_path))
                return False
            except:
                print("Remove section [%s] from %s failed!" % (section, self.config_path))
                return False
    
    def modify_section(self, section, option=None):
        #modify the specified options of a section in the config file
        if option is not None and type(option) is not dict:
            print('Dictionary format is required for parameter \'option\'!')
            return False
        elif option is not None:
            try:
                for key, value in option.items():
                    self.configparser.set(section, key, value)
                self.write_file()
                return True
            except cp.NoSectionError:
                print('Section [%s] not found in %s, modify related options of section [%s] in %s failed!' % (section, self.config_path, section, self.config_path))
                return False
            except:
                print("Modify related options of section [%s] in %s failed!" % (section, self.config_path))
                return False
        else:
            print('Parameter \'option\' cannot be empty!')
    
    def get_section(self, section, option=None):
        #get the specified options information of a section in the config file
        #get the entire options information of a section in the config file if parameter option is empty
        if option is not None and type(option) is not list and type(option) is not str:
            print('List format or string format is required for parameter \'option\'!')
            return None
        elif option is not None and type(option) is str:
            try:
                result = self.configparser.get(section, option)
                return result
            except cp.NoSectionError:
                print('Section [%s] not found in %s, get option [%s:%s] in %s failed!' % (section, self.config_path, section, option, self.config_path))
                return None
            except cp.NoOptionError:
                print('Option %s of [%s] not found in %s, get option [%s:%s] in %s failed!' % (option, section, self.config_path, section, option, self.config_path))
                return None
            except:
                print("Get option [%s:%s] in %s failed!" % (section, option, self.config_path))
                return None         
        elif option is not None and type(option) is list:
            try:
                result = {}
                for opt in option:
                    result[opt] = self.configparser.get(section, opt)
                return result
            except cp.NoSectionError:
                print('Section [%s] not found in %s, get specified options of [%s] in %s failed!' % (section, self.config_path, section, self.config_path))
                return None
            except cp.NoOptionError:
                print('Some option of [%s] not found in %s, get specified options of [%s] in %s failed!' % (section, self.config_path, section, self.config_path))
                return None
            except:
                print("Get specified options of [%s] in %s failed!" % (section, self.config_path))
                return None
        else:
            try:
                result = {}
                for key, value in self.configparser.items(section):
                    result[key] = value
                return result
            except cp.NoSectionError:
                print("Section [%s] not found in %s, get [%s] information in %s failed!" % (section, self.config_path, section, self.config_path))
                return None
            except cp.NoOptionError:
                print('Some option of [%s] not found in %s, get [%s] information in %s failed!' % (section, self.config_path, section, self.config_path))
                return None
```

