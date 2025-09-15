def copy(src,new_path):
    #文件的复制1就是边读边写操作
    #（1）打开源文件
    file1=open(src,'rb')
    #（2）打开目标文件
    file2=open(new_path,'wb')
    #（3）开始复制，边读边写
    s=file1.read()
    file2.write(s)
    #（4）关闭文件（先打开的后关，后打开的先关）
    file2.close()
    file1.close()

if __name__=='__main__':
    src="E:\多媒体内容安全\Python\Python代码\第11章-文件及IO操作\文件的基础操作\文件的复制\微信图片_20241228184401.jpg" #.代表的是当前目录
    new_path="E:\多媒体内容安全\Python\Python代码\第11章-文件及IO操作\文件的基础操作\文件的写入操作\copy_微信图片_20241228184401.jpg" #..代表返回一级，相当于windows中的后退
    copy(src,new_path)
    print('文件复制完毕')