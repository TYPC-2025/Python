import os.path
print('获取目录或文件的绝对路径:',os.path.abspath('./b.txt'))
print('判断文件在磁盘上是否存在:',os.path.exists('b.txt')) #True 
print('判断文件在磁盘上是否存在:',os.path.exists('newb.txt')) #False
print('判断目录在磁盘上是否存在:',os.path.exists('./好好学习')) #False
print('拼接路径:',os.path.join('E:\多媒体内容安全\Python\Python代码\第11章-文件及IO操作','b.txt'))
print('分割文件名和文件后缀名:',os.path.splitext('b.txt')) #元组类型
print('提取文件名:',os.path.basename(r'E:\多媒体内容安全\Python\Python代码\第11章-文件及IO操作\b.txt'))
print('提取路径:',os.path.dirname(r'E:\多媒体内容安全\Python\Python代码\第11章-文件及IO操作\b.txt'))
print('判断path是否是有效路径:',os.path.isdir(r'E:\多媒体内容安全\Python\Python代码\第11章-文件及IO操作')) #True
print('判断path是否是有效路径:',os.path.isdir(r'E:\多媒体内容安全\Python\Python代码\第11章-文件及IO操作yis')) #False
print('判断file是否是有效文件:',os.path.isfile('b.txt')) #True
print('判断file是否是有效文件:',os.path.isfile('b34.txt')) #False