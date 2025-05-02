data=eval(input('请输入要匹配的数据：'))
match data:
    case {'name':'ty','hobby':'ping-pong'}:
        print('字典')
    case [10,20,30]:
        print('列表')
    case (10,20,40):
        print('元组')
    case _:   #输入的字符串之类的需要加 引号，由于eval函数
        print('相当于if语句中的else')