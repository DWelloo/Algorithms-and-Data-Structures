class Heap_Node:
    def __init__(self):
        self.u=None
        self.val=None
class nHeap:
    def __init__(self,n):
        self.n=n
        self.heap=[]

    def heap_up(self,i):
        if i==0:
            return
        if self.heap[i].val<self.heap[(i-1)//self.n].val:
            self.heap[i],self.heap[(i-1)//self.n]=self.heap[(i-1)//self.n],self.heap[i]
            self.heap_up((i-1)//self.n)

    def find_next(self,i):
        candidates={self.heap[self.n*i+1].val:(self.n*i+1)}
        cand_vals=[self.heap[self.n*i+1].val]
        if self.n*i+2 < len(self.heap):
            for j in range(2,len(self.heap)-(self.n*i+2)+1):
                cand_vals.append(self.heap[self.n*i+j].val)
                candidates[self.heap[self.n*i+j].val]=(self.n*i+j)
        candidate=min(cand_vals)
        candidate_index=candidates[candidate]
        return candidate,candidate_index

    def heap_down(self,i=0):
        if self.n*i+1 >= len(self.heap):
            return
        candidate,candidate_index=self.find_next(i)
        if self.heap[i].val>candidate:
            self.heap[i],self.heap[candidate_index]=self.heap[candidate_index],self.heap[i]
            self.heap_down(candidate_index)

    def add_node(self,val,i):
        new_Node=Heap_Node()
        new_Node.val=val
        new_Node.u=i
        self.heap.append(new_Node)
        self.heap_up(len(self.heap)-1)

    def upload_tab(self,tab):
        for i in range(len(tab)):
            self.add_node(tab[i],i)

    def delete_root(self):
        self.heap[0],self.heap[len(self.heap)-1]=self.heap[len(self.heap)-1],self.heap[0]
        self.heap.pop()
        self.heap_down()

    def get_root(self):
        return self.heap[0]
    
def test():
    new_Heap=nHeap(2)
    arr=[3,1,2,5,0,-3,5]
    new_Heap.upload_tab(arr)
    print(new_Heap.get_root().val)
    new_Heap.delete_root()
    print(new_Heap.get_root().val)

