# Pandoc2--使用方法

### Pandoc程序的命令使用方式

```
pandoc <files> <options>
```

+ <files> 为输入的内容，其输入即可以来自文件，也可以来自标准输入甚至网页链接

+ <options> 为参数选项

  | 参数                       | 说明                                              |
  | -------------------------- | ------------------------------------------------- |
  | -f <format>、-r <format>   | 指定输入文件格式，默认为 Markdown；               |
  | -t <format>、-w <format>   | 指定输出文件格式，默认为 HTML；                   |
  | -o <file>                  | 指定输出文件，该项缺省时，将输出到标准输出；      |
  | --highlight-style <style>  | 设置代码高亮主题，默认为 pygments；               |
  | -s                         | 生成有头尾的独立文件（HTML，LaTeX，TEI 或 RTF）； |
  | -S                         | 聪明模式，根据文件判断其格式；                    |
  | --self-contained           | 生成自包含的文件，仅在输出 HTML 文档时有效；      |
  | --verbose                  | 开启 Verbose 模式，用于 Debug；                   |
  | --list-input-formats       | 列出支持的输入格式；                              |
  | --list-output-formats      | 列出支持的输出格式；                              |
  | --list-extensions          | 列出支持的 Markdown 扩展方案；                    |
  | --list-highlight-languages | 列出支持代码高亮的编程语言；                      |
  | --list-highlight-styles    | 列出支持的代码高亮主题；                          |
  | -v、--version              | 显示程序的版本号；                                |
  | -h、--help                 | 显示程序的帮助信息；                              |

  虽然 Pandoc 提供了用于指定输入输出格式的参数，但是很多时候该参数不必使用。Pandoc 已经足够聪明到可以根据文件名判断输入输出格式，所以除非文件名可能造成歧义，否则这两个参数都可以省略。

### 使用示例

#### 信息查看

+ 查看程序支持的输入文件格式

  ```bash
  pandoc --list-input-formats
  ```

+ 查看程序支持代码高亮的编程语言

  ```bash
  pandoc --list-highlight-languages
  ```

#### 生成HTML文档

#### 