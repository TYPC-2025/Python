from multiprocessing import Process
import os,time
#函数中的代码是进程要执行的代码
def test():
    print(f'我是子进程，我的PIP是：{os.getpid()},我的父进程是：{os.getppid()}')
    time.sleep(1) #休眠一秒

if __name__=='__main__':
    print('主进程开始执行')
    lst=[]
    #创建五个子进程
    for i in range(5):
        #创建子进程
        p=Process(target=test)
        #启动子进程
        p.start()
        #启动中的进程添加到列表中
        lst.append(p)
    #开始遍历lst,列表中有五个子进程
    for item in lst:
        item.join() #阻塞主进程
    print('主进程执行结束')
    #主进程要等到所有的子进程执行结束，才执行上面这句代码
