
"""编写函数实现提取指定字符串中的数字并求和"""
def get_digit(x):
    s=0
    lst=[] # 存储提取出来的数字
    for item in x:
        if item.isdigit():  #如果是数字
            lst.append(int(item))
    # 求和
    s=sum(lst)
    return lst,s
#准备函数的调用
s=input('请输入一个字符串:')

#函数调用
lst,s=get_digit(s) #解包
print('提取的数字列表为:',lst)
print('累加和为:',s)