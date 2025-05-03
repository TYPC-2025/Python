fruits={'apple','orange','pear','grape'}  #无序
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('10个苹果')
        case 'orange',3:
            print('3个橘子')
        case 'pear',4:
            print('4个梨子')
        case 'grape',5:
            print('5串葡萄')

print('---------------------------------------------')

fruits=['apple','orange','pear','grape']  #列表有序
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
    match f,c:
        case 'apple',10:
            print('10个苹果')
        case 'orange',3:
            print('3个橘子')
        case 'pear',4:
            print('4个梨子')
        case 'grape',5:
            print('5串葡萄')

lst=[1,3,5,7,9]
lst.reverse()
print(lst)