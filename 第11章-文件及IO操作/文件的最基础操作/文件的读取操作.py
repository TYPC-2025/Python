def my_read():
    #创建/打开文件
    file=open('a.txt','r',encoding='utf-8')
    #操作文件
    s=file.read()
    print(type(s),s)
    #关闭文件
    file.close()

#主程序运行
if __name__=='__main__':
    my_read()