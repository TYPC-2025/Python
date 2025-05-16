"""编写函数实现操作符in的功能"""
def get_find(s,lst):
    for item in lst:
        if s==item:
            return True
    return False
lst=['hello','world','come on']
s=input('请输入你要判断的字符串:')
result=get_find(s,lst)
print('存在'if result else '不存在')