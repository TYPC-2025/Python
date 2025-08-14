import jieba
#读入文件
with open('杜甫.txt','r',encoding='utf-8') as file:
    s=file.read()
print(s)

#分词
lst=jieba.lcut(s)
print(lst)

#去重操作（使用集合）
set1=set(lst)

#统计词出现的一个频率（使用字典）
d={} #key:词  value:出现的次数
for item in set1:
    if len(item)>=2:
        d[item]=0
# print(d) 输出结果中次数全是0
for item in lst:
    if item in d:
        d[item]=d.get(item)+1
new_lst=[]
for item in d:
    new_lst.append([item,d[item]])

#列表排序
new_lst.sort(key=lambda x:x[1],reverse=True)
print(new_lst[0:11]) #显示前10项

input()