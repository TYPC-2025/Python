import os
print('当前工作路径:',os.getcwd())

print('-'*50)

lst=os.listdir()
print('当前路径下的所有目录和文件:',lst)

print('-'*50)

print('指定路径下的所有目录和文件:',os.listdir('E:/生活'))

print('-'*50)

#创建目录
# os.mkdir('中国共产党万岁') #若要创建的文件存在，则程序报错

print('-'*50)

#创建多级目录
# os.makedirs('./aa/bb/cc') #若要创建的文件存在，则程序报错

#删除目录
# os.rmdir('./中国共产党万岁') #若要删除的文件存在，则程序报错

#删除多级目录
# os.removedirs('./aa/bb/cc')

#改变当前工作路径
# os.chdir('E:\多媒体内容安全\Python\Python代码\第10 章-模块及常用的第三方模块')
#若运行上诉程序，则该文件目录从  E:\多媒体内容安全\Python\Python代码\第11 章-文件及IO操作 变成 E:\多媒体内容安全\Python\Python代码\第10 章-模块及常用的第三方模块

#遍历目录树（walk）,相当于递归操作
for dirs,dirlst,filelst in os.walk('E:\多媒体内容安全\Python\Python代码\第11 章-文件及IO操作'):
    print(dirs)
    print(dirlst)
    print(filelst)
    print('---------------------------------')