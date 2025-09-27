import threading
from threading import Thread
import time

ticket=50

def sale_ticket():
    global ticket
    #每个排队窗口假设有100人
    for i in range(100):
        if ticket>0:
            print(f'{threading.current_thread().name}正在出售第{ticket}张票')
            ticket-=1
        time.sleep(1)

if __name__=='__main__':
    for i in range(3):
        t=Thread(target=sale_ticket)
        t.start()


"""安全性问题：比如
Thread-2 (sale_ticket)正在出售第47张票
Thread-1 (sale_ticket)正在出售第47张票"""

"""同时出售第47张票，显然不可取"""