"""关键字参数（没有顺序问题）"""
def happy_birthday(name,age):
    print('祝'+name+'生日快乐')
    print(str(age)+'生日快乐')

#关键字传参
happy_birthday(age=18,name='ty')
