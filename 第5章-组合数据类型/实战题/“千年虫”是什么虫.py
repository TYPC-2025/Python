"""
原列表:[88,89,90,0,99]
结果:['1988','1989','1990','2000','1999']
"""
lst=[88,89,90,0,99]
print(lst)

for index in range(len(lst)):
    if str(lst[index])!='0':
        lst[index]='19'+str(lst[index])
    else:
        lst[index]='200'+str(lst[index])
print(lst) 

"""for index,value in enumerate(lst):
    if str(value)!='0':
        lst[index]='19'+str(value)
    else:
        lst[index]='200'+str(value)
print(lst) 