#match函数（从头开始匹配，字符串开始没有数字，则输出None）
import re #导入
pattern='\d\.\d+' #+限定符.\d 0-9数字出现一次或多次
s='I study Python 3.11 every day' #待匹配字符串
match=re.match(pattern,s,re.I) #re.I 忽略大小写
print(match) #None

s2='3.11I study Python every day'
match2=re.match(pattern,s2)
print(match2)

print('匹配的起始位置:',match2.start())
print('匹配的结束位置:',match2.end())
print('匹配区间的位置元素:',match2.span())
print('待匹配的字符串:',match2.string)
print('匹配的数据:',match2.group())

