class nHeap:
    def __init__(self,n):
        self.n=n
        self.heap=[]

    def heap_up(self,i):
        if i==0:
            return
        if self.heap[i]>self.heap[(i-1)//self.n]:
            self.heap[i],self.heap[(i-1)//self.n]=self.heap[(i-1)//self.n],self.heap[i]
            self.heap_up((i-1)//self.n)

    def find_next(self,i):
        candidates={self.heap[self.n*i+1]:(self.n*i+1)}
        cand_vals=[self.heap[self.n*i+1]]
        if self.n*i+2 < len(self.heap):
            for j in range(2,len(self.heap)-(self.n*i+2)+1):
                cand_vals.append(self.heap[self.n*i+j])
                candidates[self.heap[self.n*i+j]]=(self.n*i+j)
        candidate=max(cand_vals)
        candidate_index=candidates[candidate]
        return candidate,candidate_index

    def heap_down(self,i=0):
        if self.n*i+1 >= len(self.heap):
            return
        candidate,candidate_index=self.find_next(i)
        if self.heap[i]<candidate:
            self.heap[i],self.heap[candidate_index]=self.heap[candidate_index],self.heap[i]
            self.heap_down(candidate_index)

    def add_node(self,val):
        self.heap.append(val)
        self.heap_up(len(self.heap)-1)

    def delete_root(self):
        self.heap[0],self.heap[len(self.heap)-1]=self.heap[len(self.heap)-1],self.heap[0]
        self.heap.pop()
        self.heap_down()

def printHeap(heap,n, i=0, level=0,flag=False):
    half=int(n/2)
    if len(heap) < 0:
        return
    if flag==True:
        print()
    for j in range(n,half,-1):
        if len(heap) > n*i+j and n>(j-1):
            printHeap(heap,n, n*i+j, level + 1)
    print(' ' * 10 * level + '--> '*bool(level) + str(heap[i]))
    for j in range(half,0,-1):
        if len(heap) > n*i+j and n>(j-1):
            printHeap(heap,n, n*i+j, level + 1)
        if j==1:
            print()
            print()

if __name__ == '__main__':
    h=nHeap(2)
    for i in range(13):
        h.add_node(i)
    print(h.heap)
    printHeap(h.heap,h.n)

    for i in range(3):
        print()

    g=nHeap(3)

    for i in range(13):
        g.add_node(i)
    print(g.heap)
    printHeap(g.heap,g.n)

    for i in range(3):
        print()

    f=nHeap(4)

    for i in range(13):
        f.add_node(i)
    print(f.heap)
    printHeap(f.heap,f.n)

