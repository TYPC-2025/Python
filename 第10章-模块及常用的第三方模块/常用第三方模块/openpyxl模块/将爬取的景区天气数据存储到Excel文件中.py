import weather
import openpyxl
html=weather.get_html() #发请求，得响应结果
lst=weather.parse_html(html) #解析数据

#创建一个新的excel文件簿
workbook=openpyxl.Workbook() #创世对象
#在excel文件中创建工作表
sheet=workbook.create_sheet('景区天气')
#向工作表中添加数据
for item in lst:
    sheet.append(item) #一次添加一行
#保存文件
workbook.save('景区天气.xlsx')