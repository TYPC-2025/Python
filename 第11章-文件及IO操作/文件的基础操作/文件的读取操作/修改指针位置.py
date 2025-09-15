def my_read(filename):
    file=open(filename,'w+',encoding='utf-8')
    file.write('中国共产党万岁')  #写完后，文件的指针在最后
    #seek修改文件指针的位置
    file.seek(6) #6个字节，两个中文‘中国’占六个字节，utf-8
    #读取
    s=file.read() #读取全部
    print(type(s),s)

    #关闭文件
    file.close()

#主程序运行
if __name__=='__main__':
    my_read('d.txt')