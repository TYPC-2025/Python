def my_read(filename):
    file=open(filename,'w+',encoding='utf-8')
    file.write('中国共产党万岁')  #写完后，文件的指针在最后
    #seek修改文件指针的位置
    file.seek(0)
    #读取
    s=file.readlines() #读取所有，一行为列表中的一个元素
    print(type(s),s)

    #关闭文件
    file.close()

#主程序运行
if __name__=='__main__':
    my_read('d.txt')