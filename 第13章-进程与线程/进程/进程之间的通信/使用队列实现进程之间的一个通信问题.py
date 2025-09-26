"""队列是共享的，写和出用的是一个队列"""
from multiprocessing import Process,Queue
import time
a=100
#入队
def write_msg(q):  #q队列
    global a
    if not q.full():
        for i in range(6):
            a-=10
            q.put(a)
            print('a入队时的值:',a)

#出队
def read_msg(q):
    time.sleep(1)
    while not q.empty():
        print('出队时的值:',q.get())

if __name__=='__main__':
    print('父进程开始执行')
    q=Queue() #没有指定参数，则消息个数没有上限
    #创建两个子进程
    p1=Process(target=write_msg,args=(q,))
    p2=Process(target=read_msg,args=(q,))

    #启动子进程
    p1.start()
    p2.start()

    #等待写的进程执行结束，再去执行主进程
    p1.join()
    p2.join()
    print('父进程执行完毕')