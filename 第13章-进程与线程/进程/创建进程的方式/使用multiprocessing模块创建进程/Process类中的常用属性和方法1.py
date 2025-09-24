from multiprocessing import Process
import os,time
#函数方式创建子进程
def sub_process(name):
    print(f'子进程PID：{os.getpid()},父进程的PID：{os.getppid()},-----------------{name}')

    time.sleep(1)

def sub_process1(name):
    print(f'子进程PID：{os.getpid()},父进程的PID：{os.getppid()},-----------------{name}')

    time.sleep(1)

if __name__=='__main__':
    #主进程
    print('父进程开始执行')
    for i in range(5):
        #创建第一个子进程
        p1=Process(target=sub_process,args=('ty',))
        #创建第二个子进程
        p2=Process(target=sub_process,args=(18,))
        #调用start()启动子进程
        p1.start()
        p2.start()
        print(p1.name,'是否执行完毕',p1.is_alive())
        print(p2.name,'是否执行完毕',p2.is_alive())

        print(p1.name,'pid是:',p1.pid)
        print(p2.name,'pid是:',p2.pid)

        p1.join()
        p2.join()  #若没有这句代码，则多个进程的执行顺序完全是随机的，不受我的控制

        print(p1.name,'是否执行完毕',p1.is_alive())
        print(p2.name,'是否执行完毕',p2.is_alive())
    print('父进程执行完毕')
