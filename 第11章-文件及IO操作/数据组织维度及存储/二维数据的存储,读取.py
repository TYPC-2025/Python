#存储
def my_write_table():

    lst=[
        ['姓名','爱好','成绩'],
        ['ty','pingpong','91'],
        ['jf','chess','93'],
        ['yd','basketball','89']
    ]
    with open('table.csv','w',encoding='utf-8')as file:
        for item in lst: #item的数据类型是列表
            line=','.join(item)
            file.write(line)
            file.write('\n')

#读取
def my_read_table():
    data=[]
    with open('table.csv','r',encoding='utf-8') as file:
        lst=file.readlines() #每一行是列表中的一个元素
        print(type(lst),lst)
        for item in lst: #lst是字符串类型
            new_lst=item[:len(item)-1].split(',') #结果是列表操作，用逗号分隔 减1是为了不要最后面的\n
            data.append(new_lst)
    print(data)

if __name__=='__main__':
    my_write_table()
    my_read_table()