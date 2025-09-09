import json
#准备高维数据
lst=[
    {'name':'ty','age':18,'score':91},
    {'name':'jd','age':17,'score':93},
    {'name':'kd','age':19,'score':98}
]

#编码
s=json.dumps(lst,ensure_ascii=False,indent=4) #ensure_ascii保证中文正常显示，indent增加数据的缩进，美观
print(type(s),s)

#解码
lst2=json.loads(s)
print(type(lst2),lst2)

#编码到文件中
with open('student.txt','w') as file:
    json.dump(lst,file,ensure_ascii=False,indent=4)

#从文件中解码到程序
with open('student.txt','r') as file:
    lst3=json.load(file)  #直接就是列表类型，根本不用做类型转换
    print(type(lst3),lst3)