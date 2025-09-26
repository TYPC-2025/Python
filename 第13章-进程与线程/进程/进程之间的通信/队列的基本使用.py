from multiprocessing import Queue
if __name__=='__main__':
    #创建一个队列
    q=Queue(3)  #最多只能接收3条消息
    print('队列是否为空:',q.empty()) #True
    print('队列是否为满:',q.full()) #False
    #向队列中添加信息
    q.put('hello')
    q.put('good')
    print('队列是否为空:',q.empty()) #False
    print('队列是否为满:',q.full()) #False
    q.put('excellent')
    print('队列是否为空:',q.empty()) #False
    print('队列是否为满:',q.full()) #True

    print('队列当中有多少条消息:',q.qsize()) #3

    #出队
    print(q.get())
    print('队列当中的信息个数:',q.qsize()) #2(意味着又可以入队)

    #入队
    q.put('value')
    print('队列当中有多少条消息:',q.qsize()) #3

    #出队
    print(q.get())
    print('队列当中的信息个数:',q.qsize()) #2

    #入队
    q.put_nowait('html')
    # q.put_nowait('php') #队列已满，会报错
    # q.put('php') #这个不会报错，会一直等待，等到队列中有空位置的时间，否则程序一直停在原位置

    #遍历出列表中的所有元素
    if not q.empty():
        for i in range(q.qsize()):
            print(q.get_nowait()) #nowait不等待

    print('队列是否为空:',q.empty())
    print('队列是否未满:',q.full())
    print('队列中消息的个数:',q.qsize())