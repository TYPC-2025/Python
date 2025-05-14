#替换
s='win'
print(s.replace('win','winner'))

s1='HelloWorld'
new_s1=s1.replace('o','一定会成功的')
print(new_s1)

s1='HelloWorld'
new_s1=s1.replace('o','一定会成功的',1) #最后一个参数是替换次数，默认是全部替换
print(new_s1)

#居中，然后使用fillchar填充
print(s.center(20))

print(s.center(20,'*'))

#去掉字符串左右的空格
s='    hello    world     '
print(s.strip())  #去掉左右
print(s.lstrip()) #去掉左边的
print(s.rstrip()) #去掉右边的

#去掉指定的字符
s3='dl-helloworld'
print(s3.strip('ld'))

print(s3.lstrip('ld'))

print(s3.rstrip('ld'))