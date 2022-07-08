# PythonDjango8--返回非HTML数据

可能需要对各种图像，CSV文件，pdf文件数据进行处理再返回，因此不能把这些数据直接放入静态链接，而需要通过django动态返回这些数据

## 返回图像

* 图像是二进制数据

* 示例

  ```python
  from django.http import HttpResponse
  import os
  
  # 获取项目MyDjango36根路径
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  
  def send_image(request):
      image_data = open(os.path.join(BASE_DIR, "static", "小林家的龙女仆1.jpg"), 'rb').read()
      return HttpResponse(image_data, content_type='image/png')
  ```

  ```python
  re_path(r'^ImageData/$', Data.send_image),
  ```

  * 这个例子返回提前指定的图片

* 示例：根据用户选择返回不同图像

  ```python
  # 获取项目MyDjango36根路径
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  
  def send_choose_image(request):
      id = request.GET.get('id')
      image_data = open(os.path.join(BASE_DIR, 'static', f'小林家的龙女仆{id}.jpg'), 'rb').read()
      return HttpResponse(image_data, content_type='image/png')
  ```

  ```python
  re_path(r'^chooseImageData/$', Data.send_choose_image),
  ```

## 返回CSV格式的数据

* 示例：以附件形式下载CSV格式的数据

  ```python
  import csv
  
  def send_csv(request):
      response = HttpResponse(content_type='text/csv')
      response['Content-Disposition'] = "attachment;filename=data.csv"   # 将文件作为一个附件来下载
      passengers = [122, 554, 466, 343, 567, 453]
      writer = csv.writer(response)
      writer.writerow(['Year', 'Airline Passengers'])
      for year, num in zip(range(2000, 2006), passengers):
          writer.writerow([year, num])
      return response
  ```

  ```python
  re_path(r'^CSVData/$', Data.send_csv),
  ```

## 返回pdf格式数据

* 在Python中并没有提供直接生成PDF数据的API，需要使用第三方API:reportlab

### reportlab

* 安装

  ```python
  pip install reportlab
  ```

* 可生成的文档类型

  * 将文本直接写入PDF
    * 设置字体
    * 输出中文，默认的字体不支持中文
  * 将图像写入PDF

* 示例：生成PDF文档

  ```python
  from reportlab.pdfgen.canvas import Canvas
  from reportlab.pdfbase.ttfonts import TTFont
  from reportlab.pdfbase.pdfmetrics import *
  from reportlab.lib.utils import ImageReader
  import os
  # 获取项目MyDjango36根路径
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  # 默认的字体不支持中文，需要换成支持中文的字体
  # 将字体变成全局的
  font = TTFont(name='default_font', filename=os.path.join(BASE_DIR, 'static', '肥滚滚.ttf'))   # 装载字体
  registerFont(font=font)   # 注册字体
  
  c = Canvas(filename='my.pdf')
  
  # 写入文字
  # 设置字体颜色，最后的参数alpha指定透明度，不设置的话就是不透明
  c.setFillColorRGB(1, 0, 0)   # 设置字体为红色
  # 设置字体和大小
  c.setFont('default_font', 40)
  # 坐标原点在页面的左下角
  c.drawString(200, 300, 'Hello')
  c.drawString(350, 300, '世界')
  
  # 写入图片
  # 可以是Web图片，也可以是本地数据
  # 如果是Web图片，直接填入网址即可
  image = ImageReader(os.path.join(BASE_DIR, 'static', '小林家的龙女仆1.jpg'))
  c.drawImage(image, 210, 100, width=200, height=150)
  c.showPage()
  c.save()from reportlab.pdfgen.canvas import Canvas
  from reportlab.pdfbase.ttfonts import TTFont
  from reportlab.pdfbase.pdfmetrics import *
  from reportlab.lib.utils import ImageReader
  import os
  # 获取项目MyDjango36根路径
  BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  # 默认的字体不支持中文，需要换成支持中文的字体
  # 将字体变成全局的
  font = TTFont(name='default_font', filename=os.path.join(BASE_DIR, 'static', '肥滚滚.ttf'))   # 装载字体
  registerFont(font=font)   # 注册字体
  
  # 创建画布
  c = Canvas(filename='my.pdf')
  
  # 写入文字
  # 设置字体颜色，最后的参数alpha指定透明度，不设置的话就是不透明
  c.setFillColorRGB(1, 0, 0)   # 设置字体为红色
  # 设置字体和大小
  c.setFont('default_font', 40)
  # 坐标原点在页面的左下角
  c.drawString(200, 300, 'Hello')
  c.drawString(350, 300, '世界')
  
  # 写入图片
  # 可以是Web图片，也可以是本地数据
  image = ImageReader(os.path.join(BASE_DIR, 'static', '小林家的龙女仆1.jpg'))
  c.drawImage(image, 210, 100, width=200, height=150)
  c.showPage()
  c.save()
  ```

### 返回PDF格式数据

* 示例1：简单的pdf示例

  ```python
  from reportlab.pdfgen.canvas import Canvas
  from reportlab.pdfbase.ttfonts import TTFont
  from reportlab.pdfbase.pdfmetrics import *
  from reportlab.lib.utils import ImageReader
  
  
  def send_pdf(request):
  
      response = HttpResponse(content_type='application/pdf')
      # 直接显示PDF文档，如果要作为附件进行下载，需要设置Content-Disposition
      # response['Content-Disposition'] = 'attachment;filename=mypdf.pdf'
      c = Canvas(response)
      c.drawString(100, 100, 'I love you!')
      c.showPage()
      c.save()
      return response
  ```

  ```python
  re_path(r'^PDFData/$', Data.send_pdf),
  ```

* 示例2：设置字体以及加入图片等

  ```python
  from reportlab.pdfgen.canvas import Canvas
  from reportlab.pdfbase.ttfonts import TTFont
  from reportlab.pdfbase.pdfmetrics import *
  from reportlab.lib.utils import ImageReader
  font = TTFont(name='default_font', filename=os.path.join(BASE_DIR, 'static', '肥滚滚.ttf'))  # 装载字体
  registerFont(font=font)  # 注册字体
  
  def send_pdf(request):
      response = HttpResponse(content_type='application/pdf')
      # 直接显示PDF文档，如果要作为附件进行下载，需要设置Content-Disposition
      # response['Content-Disposition'] = 'attachment;filename=mypdf.pdf'
      c = Canvas(response)
      image = ImageReader(os.path.join(BASE_DIR, 'static', '小林家的龙女仆3.jpg'))
      c.drawImage(image, 200, 200, width=150, height=150)
      c.setFillColorRGB(0,0,1)
      c.setFont('default_font', 50)
      c.drawString(150, 100, 'Hello, 世界')
      c.showPage()
      c.save()
      return response
  ```

  

