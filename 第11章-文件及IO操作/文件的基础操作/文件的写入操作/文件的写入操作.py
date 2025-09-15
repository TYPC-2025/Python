def my_write(s):
    #创建/打开文件
    file=open('b.txt','a',encoding='utf-8')
    #写入内容
    file.write(s)
    file.write('\n')
    #关闭文件
    file.close()

#主程序运行
if __name__=='__main__':
    my_write('中国共产党万岁')
    my_write('只有中国共产党才能救中国')