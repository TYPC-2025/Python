#写入列表
def my_write_list(file,lst):
    #打开文件
    f=open(file,'a',encoding='utf-8')
    #操作文件
    f.writelines(lst)
    #关闭文件
    f.close()

#主程序运行
if __name__=='__main__':
    #准备数据
    lst=['姓名\t','年龄\t','成绩\n','张三\t','18\t','91']
    my_write_list('c.txt',lst)