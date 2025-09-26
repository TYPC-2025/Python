from multiprocessing import Queue
if __name__=='__main__':
    q=Queue(3)
    #向队列中添加元素（入队）
    q.put('python')
    q.put('html')
    q.put('php')

    # q.put('css',block=True,timeout=2) #等待2秒之后，如果还没有空位，就抛异常