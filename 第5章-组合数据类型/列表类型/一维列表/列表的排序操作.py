"""列表的排序操作(列表对象的sort方法)"""

lst=[23,4,34,56,3,53,17]
print('原列表：',lst)

#排序，默认是升序
lst.sort()
print('升序：',lst)

#降序排序
lst.sort(reverse=True)
print('降序：',lst)

print('-------------------------------------------------')

#英语单词也能排序
lst2=['banana','apple','Cat','Orange']
print('原列表：',lst2)

#升序（先排大写，再排小写）
lst2.sort()
print(lst2)

#降序
lst2.sort(reverse=True)
print(lst2)

#忽略大小写进行比较（自己制定规则）
lst2.sort(key=str.lower)
print(lst2)

"""列表的排序操作(内置函数sorted方法)"""
lst=[23,4,34,56,3,53,17]
print('原列表：',lst)

#排序，默认是升序
asc_lst=sorted(lst)
print('升序：',asc_lst)
print('原列表：',lst)

#降序
desc_lst=sorted(lst,reverse=True)
print('降序：',desc_lst)
print('原列表：',lst)

#也能对字符串进行排序
lst2=['banana','apple','Cat','Orange']
print('原列表：',lst2)
#忽略大小写进行排序
new_lst2=sorted(lst2,key=str.lower)
print('排序后的列表：',new_lst2)

new_lst2=sorted(lst2,key=str.lower,reverse=True)
print('排序后的列表：',new_lst2)

