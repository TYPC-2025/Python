s='伟大的中国梦'
#编码str-->bytes
scode=s.encode(errors='replace') #默认是utf-8,因为utf-8中文占三个字节，英文占一个字节
print(scode)

scode_gbk=s.encode('gbk',errors='replace') #gbk中文占两个字节
print(scode_gbk)


#编码中的出错问题（假设输入有问题）
s2='好  '
scode_error=s2.encode('gbk',errors='replace')  #用？代替编码不出的内容
print(scode_error)

s2='好  '
scode_error=s2.encode('gbk',errors='ignore')  #直接忽略编码不出的内容
print(scode_error)

s2='好  '
scode_error=s2.encode('gbk',errors='strict')  #程序直接报错
print(scode_error)


#解码过程bytes-->str
print(bytes.decode(scode_gbk,'gbk'))
print(bytes.decode(scode,'utf-8'))
