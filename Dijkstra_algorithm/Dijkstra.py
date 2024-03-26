import sys
from Node_class import Node
from Heap_class import nHeap,Heap_Node
from Data_processing import read_map,make_nodes
file=sys.argv[1]

def Dijkstra(file):
    #process data into nodes
    fields=read_map(file)
    nodes=make_nodes(fields)
    l_nodes=0
    for y in range(len(nodes)):
        for x in range(len(nodes[y])):
            l_nodes+=1
    q=[]
    cost=[9*l_nodes+1 for i in range(l_nodes)]
    i=0
    for y in range(len(nodes)):
        for x in range(len(nodes[y])):
            n=nodes[y][x]
            n.u=i
            q.append(n)
            i+=1   
    #find one of the '0' nodes
    start=Node()
    for i in range(l_nodes):
        if q[i].val==0:
            start=q[i]
            break
    cost[start.u]=0
    #initialize priority queue (in this case binary heap), which will be used to quickly
    #find lowest cost element in graph
    queue=nHeap(2)
    queue.upload_tab(cost)
    #main loop, updating costs and predecessors until all nodes are processed
    for i in range(l_nodes):
        cur=Node()
        ind=queue.get_root().u
        queue.delete_root()
        cur=q[ind]
        neibs=find_neib(cur)
        if neibs!=None:
            for el in neibs:
                if cost[el.u]>cost[cur.u]+el.val:
                    cost[el.u]=cost[cur.u]+el.val
                    #because it's a priority queue and because of the number of iterations of
                    #for loop, even thought heap contains multiple cost values for each graph node
                    #the higher (outdated) costs will never be accessed 
                    queue.add_node(cost[cur.u]+el.val,el.u)
                    el.pred=cur.u
    #backtracking to find optimal pathway between endpoints and print it
    backtrack=[]
    last=Node()
    for i in range(l_nodes):
        if q[i].val==0 and q[i].pred!=-1:
            last=q[i]
            last_cords=(last.y,last.x)
            backtrack.append(last_cords)
            break
    while(last!=start):
        last=q[last.pred]
        last_cords=(last.y,last.x)
        backtrack.append(last_cords)
    print_way(backtrack,nodes)

def find_neib(q_node):
    neibs=[]
    if q_node.up:
        neibs.append(q_node.up)
    if q_node.down:
        neibs.append(q_node.down)
    if q_node.left:
        neibs.append(q_node.left)
    if q_node.right:
        neibs.append(q_node.right)
    return neibs

def print_way(tab,nodes):
    cost=0
    tab=tab[::-1]
    flag=0
    for y in range(len(nodes)):
        print(sep='')
        for x in range(len(nodes[y])):
            for el in tab:
                if x==el[1] and y==el[0]:
                    print(nodes[y][x].val,end=' ')
                    cost+=nodes[y][x].val
                    flag=1
                    break
            if flag==0:
                print(' ',end=' ')
            flag=0
    for i in range(2):
        print()
    print("Total cost=",cost,sep='')

def main(file):
    Dijkstra(file)

if __name__ == '__main__':
    main(file)
