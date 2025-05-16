"""默认值参数（函数定义时传值）"""
def happy_birthday(name='ty',age=18):
    print('祝'+name+'生日快乐')
    print(str(age)+'岁生日快乐')

#调用
happy_birthday()  #可以不用传参
happy_birthday('tyc')  #位置传参
happy_birthday(age=19)  #关键字传参，name采用默认值
# happy_birthday(19)  #报错，使用位置传参的方式，19被传给了name

"""当位置参数和默认值参数同时存在的时候，位置参数在后面程序会报错"""
"""当位置参数和默认值参数同时存在的时候，位置参数在前，默认值参数在后"""
"""必须把默认参数写在非默认参数后面"""