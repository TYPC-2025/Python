lst=[34,52,56,23,78]
 #（1）排序操作
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print('原列表:',lst)
print('升序:',asc_lst)
print('降序:',desc_lst)


#（2）reversed 反向
new_lst=reversed(lst)
print(type(new_lst)) #<class 'list_reverseiterator'> 迭代器对象
print(list(new_lst))


#（3）zip
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj))  #<class 'zip'>
print(list(zipobj))

#（4）enumerate
enum=enumerate(y,start=1)
print(type(enum))
print(tuple(enum))

z=[20,30,59,48,67]
enum2=enumerate(z,start=1)
print(type(enum2))
print(list(enum2))

#（5）all
lst2=[10,20,'',40]
print(all(lst2)) #False
print(all(lst)) #True

#（6）any
print(any(lst2)) #True

#（7）next
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)  
print(next(zipobj)) #('a', 10)
print(next(zipobj)) #('b', 20)
print(next(zipobj)) #('c', 30)
print(next(zipobj)) # ('d', 40)

#（8）filter
def fun(num):
    return num%2==1

obj=filter(fun,range(10))
print(list(obj))   #返回奇数

#（9）map
def upper(x):
    return x.upper()

new_lst2=['hello','world','python']
obj2=map(upper,new_lst2)
print(list(obj2))











