import re
pattern='\d\.\d+'
#search函数（在整个字符串中查找）
s='I study Python3.11 every day Python2.7'
match=re.search(pattern,s)
print(match)  #只找到第一个数字

s3='4.10 Python I study every day'
s4='Python I study every day'
match4=re.search(pattern,s4)
match3=re.search(pattern,s3)
print(match)
print(match3)
print(match4) #None

print(match.group())
print(match3.group())