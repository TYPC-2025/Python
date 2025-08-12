#导入
import random
#设置随机数的种子（种子相同，随机数也就相同）
random.seed(10)  
print(random.random()) #[0.0,1.0)  后面的random是随机函数
print(random.random())

print('-'*50)

random.seed(10)  
print(random.randint(1,100))  #[1,100]
print(random.randint(1,100))  

for i in range(10):
    print(random.randrange(1,10,3))

print(random.uniform(1,100)) #[a,b]之间的随机小数

lst=[i for i in range(1,11)]
print(random.choice(lst))

#随机的排序
random.shuffle(lst)
print(lst)

random.shuffle(lst)
print(lst)