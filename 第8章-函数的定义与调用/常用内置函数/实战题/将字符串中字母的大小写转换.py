"""编写函数实现将字符串中字母的大小写转换"""
def upper_lower(x):
    lst=[]
    for item in x:
        if 'A'<=item<='Z':
            lst.append(chr(ord(item)+32))
        elif 'a'<=item<='z':
            lst.append(chr(ord(item)-32))
        else:
            lst.append(item)
    return ''.join(lst)

s1=input('请输入一个字符串:')
new_s=upper_lower(s1)
print(new_s)