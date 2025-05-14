#大小写转换
s1='HelloWorld'
new_s1=s1.lower()
print(s1,new_s1)

new_s11=s1.upper()
print(s1,new_s11)

#字符串的分隔
pwd='123%hknv'
lst=pwd.split('%')
print(lst[0],lst[1])

#统计次数
print(s1.count('o'))  #o出现次数为两次

#检索操作
print(s1.find('o'))  #4（首次出现的索引）

print(s1.find('a'))  #不存在，即输出-1

print(s1.index('o'))  #同find

"""  print(s1.index('a')) #报错   """

#判断前缀和后缀
print(s1.startswith('He')) #True

print(s1.endswith('ld')) #True

print(s1.endswith('hu')) #False

print('djsl.md'.endswith('.md')) #True

print('doct.txt'.endswith('.txt')) #True

