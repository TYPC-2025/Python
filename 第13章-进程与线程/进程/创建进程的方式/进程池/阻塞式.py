from multiprocessing import Pool
import os,time
#编写任务
def task(name):
    print(f'子进程的PID:{os.getpid()},执行的任务:{name}')
    time.sleep(1)

if __name__=='__main__':
    #主进程
    start=time.time()
    print('父进程开始执行')
    #创建进程池
    p=Pool(3)
    #创建任务
    for i in range(10):
        #以阻塞方式
        p.apply(func=task,args=(i,))

    #关闭进程池不再接受新任务
    p.close()
    p.join() #阻塞父进程，等待所有子进程执行完毕之后，才会执行父进程中的代码
    print('所有子进程执行完毕，父进程执行结束')
    print(time.time()-start)  #用了10秒多的时间