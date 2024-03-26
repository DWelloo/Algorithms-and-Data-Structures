from trees import BST, AVL,delete_element,min_val_node
from random import randint
import time
from matplotlib import pyplot as plt
import sys
import gc
gc_old = gc.isenabled()
gc.disable()
sys.setrecursionlimit(15000)

def count_height(main_node):
    if main_node is None:
        return 0
    left_count = 1
    right_count = 1
    if main_node.right_child is not None:
        right_count = right_count + count_height(main_node.right_child)
    if main_node.left_child is not None:
        left_count = left_count + count_height(main_node.left_child)
    return max(left_count, right_count)

def printTree(node, level=0):
    if node != None:
        if node.right_child!=None:
            printTree(node.right_child, level + 1)
        print(' ' * 4 * level + '--> '*bool(level) + str(node.value))
        if node.left_child!=None:
            printTree(node.left_child, level + 1)

def print_tree(nodes, count):
    check_return = True
    for node in nodes:
        if node is not None and\
           (node.right_child is not None or
                node.left_child is not None):
            check_return = False
            break
    if check_return:
        return
    new_nodes = []
    if len(nodes) == 1:
        print(('  ' * ((count * 3 - count) + 2)) +
              f'{nodes[0].value}({nodes[0].quantity})')
    for node in nodes:
        if node is not None:
            new_nodes.append(node.left_child)
            new_nodes.append(node.right_child)
        else:
            new_nodes.append(None)
            new_nodes.append(None)
    str = '  ' * (count * 3 - count)
    for node in nodes:
        if node is None:
            str += '(--) (--)   '
            continue
        if node.left_child is not None:
            str += f'{node.left_child.value}({node.left_child.quantity}) '
        else:
            str += '(--) '
        if node.right_child is not None:
            str += f'{node.right_child.value}({node.right_child.quantity})'
        else:
            str += '(--)'
        str += '   '
    print(str)
    print_tree(new_nodes, count - 1)


lista=[]
lista_sorted=[]
for n in range(10000):
    lista.append(randint(1,30000))

for n in range(10000):
    lista_sorted.append(n)
    
def generate_graphs(lista,rodzaj_danych):
    add_bst_time=[]
    add_avl_time=[]
    find_bst_time=[]
    find_avl_time=[]
    del_bst_time=[]
    del_avl_time=[]
    n_values=[i for i in range(1000,10001,1000)]
        
    for i in range(1000,10001,1000):
        if rodzaj_danych=="Dane_posortowane":
            start=time.process_time()
            bst=BST({0})
            for t in range(i):
                bst.add_node(i)
            end=time.process_time()
        else:
            start=time.process_time()
            bst=BST(lista[0:i-1])
            end=time.process_time()
        time_taken=end-start
        add_bst_time.append(time_taken)

        
        start=time.process_time()
        for j in range(i):
            bst.find_node(lista[j])
        end=time.process_time()
        time_taken=end-start
        find_bst_time.append(time_taken)
        bst=None


        ###########^^^ BST ^^^###########
        ###########vvv AVL vvv###########

        avl=AVL()
        avl_root=None
        start=time.process_time()
        for j in range(i):
            avl_root=avl.add_node(avl_root,lista[j])
        end=time.process_time()
        time_taken=end-start
        add_avl_time.append(time_taken)
        start=time.process_time()
        for j in range(i):
            avl.find_node(avl_root,lista[j])
        end=time.process_time()
        time_taken=end-start
        find_avl_time.append(time_taken)
        avl=None

    for i in range(1000,10001,1000):
        lista=[]
        for n in range(10000):
            lista.append(randint(1,30000))
        bst=BST(lista[0:i-1])
        start=time.process_time()
        for j in range(i):
            delete_element(bst.root_of_tree,lista[j])
        end=time.process_time()
        time_taken=end-start
        del_bst_time.append(time_taken)

        avl=AVL()
        avl_root=None
        for j in range(i):
            avl_root=avl.add_node(avl_root,lista[j])
        start=time.process_time()
        for j in range(i):
            delete_element(avl_root,lista[j])
        end=time.process_time()
        time_taken=end-start
        del_avl_time.append(time_taken)

    
     
    plt.plot(n_values,add_bst_time,'o-',label='bst',markersize=3)
    plt.plot(n_values,add_avl_time,'o-',label='avl',markersize=3)
    plt.xlabel("Ilość elementów")
    plt.ylabel("Czas")
    plt.legend()
    plt.title("Wykres tworzenia drzewa")
    plt.savefig(f'{rodzaj_danych}_Tworzenie_drzewa.png')
    plt.show()

    plt.plot(n_values,find_bst_time,'o-',label='bst_f',markersize=3)
    plt.plot(n_values,find_avl_time,'o-',label='avl_f',markersize=3)
    plt.xlabel("Ilość elementów")
    plt.ylabel("Czas")
    plt.legend()
    plt.title("Wykres znajdowania elementów drzewa")
    plt.savefig(f"{rodzaj_danych}"+"_Znajdowanie_elementów.png")
    plt.show()

    plt.plot(n_values,del_bst_time,'o-',label='bst_d',markersize=3)
    plt.plot(n_values,del_avl_time,'o-',label='avl_d',markersize=3)
    plt.xlabel("Ilość elementów")
    plt.ylabel("Czas")
    plt.legend()
    plt.title("Wykres usuwania elementów drzewa")
    plt.savefig(f"{rodzaj_danych}"+"_Usuwanie_elementów.png")
    plt.show()

#generate_graphs(lista,"Dane_losowe")
#generate_graphs(lista_sorted,"Dane_posortowane")
lista = [5, 1, 3, 8, 9, 2, 4, 6, 7, 10, 11]
bst_1 = BST(lista)
print("BST:")
print(f'list: {lista}')
printTree(bst_1.root_of_tree)
avl_1 = AVL()
avl_root=None
for j in range(len(lista)):
    avl_root=avl_1.add_node(avl_root,lista[j])
print()
print("AVL:")
print(f'list: {lista}')
printTree(avl_root)
if gc_old:
    gc.enable()
