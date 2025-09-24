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
    print('主进程开始执行')
    for i in range(5):
        #创建第一个子进程
        p1=Process()  #没有给定target参数，不会执行自己编写的函数中的代码,会调用执行Process类中的run方法
        #创建第二个子进程
        p2=Process()

        p1.start() #调用Process类中的run方法执行
        p2.start()

        #强制终止进程
        p1.terminate()
        p2.terminate()
    print('主进程执行结束')