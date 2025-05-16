"""位置参数"""
def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

#调用
# happy_birthday('ty')  #报错（个数不对）    

# happy_birthday(18,'ty')  #报错（顺序不对）

happy_birthday('ty',18)




