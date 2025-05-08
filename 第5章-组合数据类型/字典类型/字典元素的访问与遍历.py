d={'hello':10,'world':20,'python':30}
"""访问字典中的元素"""
#（1）使用d[key]
print(d['hello'])
#（2）d.get(key)
print(d.get('hello'))

#二者之间是有区别的，若key不存在，d[key]会报错，d.get(key)则可以指定默认值
#print(d['java'])
print(d.get('java'))  #none
print(d.get('java','不存在'))  #不存在

#字典的遍历（得到元组类型）
for item in d.items():
    print(item)

#使用for循环遍历时，分别获取key,value
for key,value in d.items():
    print(key,value)