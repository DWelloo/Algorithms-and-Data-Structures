import algorithm_KMP as kmp
import algorithm_N as n
import algorithm_KR as kr
import gc
import time
from matplotlib import pyplot as plt

gc_old = gc.isenabled()
gc.disable()

def file_reader(file):
    words = []
    with open(file,encoding='utf-8') as fl:
        for line in fl:
            spl = line.split()
            for sp in spl:
                words.append(sp)
    str=""
    for i in range(len(words)):
        str+=words[i]
        str+=" "
    return words,str

file = 'pan-tadeusz.txt'

strings,text=file_reader(file)

quantities=[]
for j in range(100,1001,100):
    quantities.append(j)
times_n=[]
times_kmp=[]
times_kr=[]
for j in range(100,1001,100):

    print("Naiwny")
    start=time.process_time()
    for k in range(j):
        n.find(strings[k],text)
    stop=time.process_time()    
    print(j," słów: ",stop-start," sekund")
    times_n.append(stop-start)

    print("KMP")
    start=time.process_time()
    for k in range(j):
        kmp.find(strings[k],text)
    stop=time.process_time()    
    print(j," słów: ",stop-start," sekund")
    times_kmp.append(stop-start)

    print("KR")
    start=time.process_time()
    for k in range(j):
        kr.find(strings[k],text)
    stop=time.process_time()    
    print(j," słów: ",stop-start," sekund")
    times_kr.append(stop-start)

plt.plot(quantities, times_n, 'o-',
                 label="KMP", markersize=3)

plt.plot(quantities, times_kmp, 'o-',
                 label="Naiwny", markersize=3)

plt.plot(quantities, times_kr, 'o-',
                 label="Rabin", markersize=3)
plt.xlabel("Word\'s quantitties")
plt.ylabel("Time")
plt.legend()
plt.show()
