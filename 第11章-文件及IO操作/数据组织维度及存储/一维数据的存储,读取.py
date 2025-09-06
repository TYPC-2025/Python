def my_write():
    #一维数据，可以使用列表，元组，集合，不能使用字典
    lst=['张三','李四','王五','陈立','马奇']
    with open('student.csv','w') as file:
        file.write(','.join(lst))

def my_read():
    with open('student.csv','r') as file:
        s=file.read()
        lst=s.split(',') #用逗号分隔
        print(lst)

if __name__=='__main__':
    my_write()
    my_read()
