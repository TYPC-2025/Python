import os
#删除文件（若要删除的文件不存在，则程序报错）
# os.remove('./a.txt') #删除a.txt文件

#重命名文件（重命名已经重命名的文件，程序将会报错）
# os.rename('./a.txt','newa.txt') #将a.txt重命名为newa.txt

#转换时间格式
import time
def date_format(longtime):
    s=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))
    return s
#获取文件信息
info=os.stat(r'E:\Multimedia Content Security\基础学习\Python\Python代码\第11章-文件及IO操作\aa.txt')
print(type(info),info)
print('最近一次访问时间:',date_format(info.st_atime))
print('文件的创建时间:',date_format(info.st_ctime))
print('最近一次修改时间:',date_format(info.st_mtime))
print('文件的大小（单位是字节）:',info.st_size)

#启动路径下的文件
#打开计算机
os.startfile('calc.exe')
#启动python解释器
# os.startfile(r'D:\Python\python.exe') #r是所有转义字符\都失效