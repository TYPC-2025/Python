#索引

s='helloworld'
for i in range(0,len(s)):
    print(i,s[i],end='\t\t')
print('\n----------------------------')    
for i in range(-len(s),0):
    print(i,s[i],end='\t\t')

#切片

s='helloworld'
s1=s[0:5:2]
print(s1)
# 省略开始位置，start默认从0开始
print(s[:5:1])
# 省略开始位置和步长（步长默认为1）
print(s[:5:])
# 省略结束位置（则一直读到字符串的最后）
print(s[0::1])
# 省略结尾和步长
print(s[5::])
print(s[5:])
# 将字符串进行逆序输出
print(s[::-1])
print(s[-1:-11:-1])

#序列的相关操作和函数的使用

s='helloworld'
print('e在helloworld中存在吗？',('e'in s))
print('a在helloworld中存在吗？',('a'in s))

s='helloworld'
print('e在helloworld中不存在吗？',('e'not in s))
print('a在helloworld中不存在吗？',('a'not in s))
#序列内置函数的使用
print('len():',len(s))
print('max():',max(s))
print('min():',min(s))
#序列对象的方法，使用序列名称，打点调用
print('s.index():',s.index('o'))#o在s中第一次出现的索引位置4

print('s.count():',s.count('o'))
