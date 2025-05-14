#（1）使用占位符进行格式化
name='ty'
age=18
score=3.84
print('name:%s,age:%d,score:%f' % (name,age,score))

#（2）f-string
print(f'name:{name},age:{age},score:{score}')

#（3）使用字符串的format方法
print('name:{0},age:{1},score:{2}'.format(name,age,score))
print('name:{2},age:{0},score:{1}'.format(age,score,name))