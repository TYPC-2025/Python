def my_write():
    #创建/打开文件
    file=open('a.txt','w',encoding='utf-8')
    #操作文件
    file.write('为实现中华民族伟大复兴而努力奋斗')
    #关闭文件
    file.close()

#主程序运行
if __name__=='__main__':
    my_write() #调用函数