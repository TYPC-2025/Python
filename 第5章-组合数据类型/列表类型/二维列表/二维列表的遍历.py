"""创建二维列表"""
lst=[
    ['城市','环比','同比'], #[]之外的逗号一定要加上
    ['北京',102,103],
    ['上海',104,504],
    ['成都',106,542]
]
print(lst)
#遍历二维列表使用双重for循环
for row in lst:
    for item in row:
        print(item,end='\t')
    print()    

#列表生成式生成一个4行5列的二维列表
lst2=[[j for j in range(5)]for i in range(4)]
print(lst2)