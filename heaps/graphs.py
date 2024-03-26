from class_Heap import nHeap
from random import randint
import time
from matplotlib import pyplot as plt
import sys
import gc
gc_old = gc.isenabled()
gc.disable()
sys.setrecursionlimit(15000)


lista=[]
for n in range(10000):
    lista.append(randint(1,30000))


def make_graph(n_values, list_of_time, list_of_lbl, title, file_name):
    plt.plot(n_values,list_of_time[0],'o-',label=list_of_lbl[0],markersize=6)
    plt.plot(n_values,list_of_time[1],'o-',label=list_of_lbl[1],markersize=3)
    plt.plot(n_values,list_of_time[2],'o-',label=list_of_lbl[2],markersize=3)
    plt.xlabel("Ilość elementów")
    plt.ylabel("Czas")
    plt.legend()
    plt.title(title)
    plt.savefig(file_name)
    plt.show()


def generate_graphs(lista):
    add_binary_time = []
    add_three_time = []
    add_four_time = []
    del_binary_time = []
    del_three_time = []
    del_four_time = []

    n_values=[i for i in range(1000,10001,1000)]
        
    for i in range(1000,10001,1000):
        start=time.process_time() #tworzenie
        binary_h = nHeap(2)
        for j in range(i):
            binary_h.add_node(lista[j])
        end=time.process_time()
        time_taken=end-start
        add_binary_time.append(time_taken)

        start=time.process_time() #tworzenie
        three_h = nHeap(3)
        for j in range(i):
            three_h.add_node(lista[j])
        end=time.process_time()
        time_taken=end-start
        add_three_time.append(time_taken)

        start=time.process_time() #tworzenie
        four_h = nHeap(4)
        for j in range(i):
            four_h.add_node(lista[j])
        end=time.process_time()
        time_taken=end-start
        add_four_time.append(time_taken)

    for i in range(1000,10001,1000):
        lista=[]
        for n in range(10000):
            lista.append(randint(1,30000))

        binary_h = nHeap(2)
        for j in range(i):
            binary_h.add_node(lista[j])
        start=time.process_time()
        for j in range(i):
            binary_h.delete_root()
        end=time.process_time()
        time_taken=end-start
        del_binary_time.append(time_taken)

        three_h = nHeap(4)
        for j in range(i):
            three_h.add_node(lista[j])
        start=time.process_time()
        for j in range(i):
            three_h.delete_root()
        end=time.process_time()
        time_taken=end-start
        del_three_time.append(time_taken)

        four_h = nHeap(4)
        for j in range(i):
            four_h.add_node(lista[j])
        start=time.process_time()
        for j in range(i):
            four_h.delete_root()
        end=time.process_time()
        time_taken=end-start
        del_four_time.append(time_taken)

    list_of_time_add = [add_binary_time, add_three_time, add_four_time]
    list_of_time_del = [del_binary_time, del_three_time, del_four_time]
    list_of_labels = ["binary", "three_th", "four_th"]

    make_graph(n_values, list_of_time_add, list_of_labels, "Dodanie elementów/tworzenie kopca",
               "create_heaps.png")
    
    make_graph(n_values, list_of_time_del, list_of_labels, "Usuwanie elementów",
               "delete_in_heaps.png")


generate_graphs(lista)


if gc_old:
    gc.enable()
