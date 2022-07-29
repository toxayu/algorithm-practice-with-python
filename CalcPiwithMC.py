# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random, math, time, threading
from multiprocessing import Queue





def CalcPI(NofS, q, lock):
    
    lock.acquire()
    
    Stime = time.time()
    CountArea = 0
    
    for i in range(NofS):
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        if x**2 + y**2 <= 1:
            CountArea += 1
            

            
    PiEst = CountArea*2*2/NofS
    DurTime = time.time() - Stime
    q.put([PiEst, DurTime])
    lock.release()


if __name__ =='__main__':
    Nofs = 10000000
    lock = threading.Lock()
    q = Queue()
    t1 = threading.Thread(target=CalcPI, args=(Nofs,q,lock))
    t2 = threading.Thread(target=CalcPI, args=(Nofs,q,lock))
    t3 = threading.Thread(target=CalcPI, args=(Nofs,q,lock))
    t4 = threading.Thread(target=CalcPI, args=(Nofs,q,lock))
    t5 = threading.Thread(target=CalcPI, args=(Nofs,q,lock))
    t6 = threading.Thread(target=CalcPI, args=(Nofs,q,lock))
    t7 = threading.Thread(target=CalcPI, args=(Nofs,q,lock))
    t8 = threading.Thread(target=CalcPI, args=(Nofs,q,lock))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
   
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    
    qq = []
    while not q.empty():
        qq.append(q.get())
    
    print(qq)
        

#CPE = CalcPI(50000000)
#    
#print(CPE)
##print(100*(PiEst-math.pi)/math.pi)
#print(time.time() - Stime)