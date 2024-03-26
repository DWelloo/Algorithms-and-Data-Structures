from class_Heap import nHeap


def left(k):
    return 3*k + 1

def middle(k):
    return 3*k + 2

def right(k):
    return 3*k + 3

def parent(k):
    return (k-1)//3


def test_add_node():
    tab = nHeap(3)
    assert tab.heap == []

    tab.add_node(1)
    assert tab.heap == [1]

    tab.add_node(2)
    assert tab.heap == [2, 1]
    index = tab.heap.index(2)
    assert 1 == tab.heap[left(index)]

    begin_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tab = nHeap(3)
    for element in begin_values:
        tab.add_node(element)
    assert tab.heap ==  [10, 6, 9, 3, 1, 4, 5, 2, 7, 8]

    index = tab.heap.index(10)
    assert 6 == tab.heap[left(index)]
    assert 9 == tab.heap[middle(index)]
    assert 3 == tab.heap[right(index)]
    index = tab.heap.index(6)
    assert 10 == tab.heap[parent(index)]
    index = tab.heap.index(9)
    assert 10 == tab.heap[parent(index)]
    index = tab.heap.index(3)
    assert 10 == tab.heap[parent(index)]

    index = tab.heap.index(6)
    assert 1 == tab.heap[left(index)]
    assert 4 == tab.heap[middle(index)]
    assert 5 == tab.heap[right(index)]
    index = tab.heap.index(1)
    assert 6 == tab.heap[parent(index)]
    index = tab.heap.index(4)
    assert 6 == tab.heap[parent(index)]
    index = tab.heap.index(5)
    assert 6 == tab.heap[parent(index)]

    index = tab.heap.index(9)
    assert 2 == tab.heap[left(index)]
    assert 7 == tab.heap[middle(index)]
    assert 8 == tab.heap[right(index)]
    index = tab.heap.index(2)
    assert 9 == tab.heap[parent(index)]
    index = tab.heap.index(7)
    assert 9 == tab.heap[parent(index)]
    index = tab.heap.index(8)
    assert 9 == tab.heap[parent(index)]


def test_delete_root():
    begin_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    tab = nHeap(3)
    for element in begin_values:
        tab.add_node(element)

    assert tab.heap == [10, 6, 9, 3, 1, 4, 5, 2, 7, 8]
    index = tab.heap.index(10)
    assert 6 == tab.heap[left(index)]
    assert 9 == tab.heap[middle(index)]
    assert 3 == tab.heap[right(index)]
    index = tab.heap.index(6)
    assert 10 == tab.heap[parent(index)]
    index = tab.heap.index(9)
    assert 10 == tab.heap[parent(index)]
    index = tab.heap.index(3)
    assert 10 == tab.heap[parent(index)]

    index = tab.heap.index(6)
    assert 1 == tab.heap[left(index)]
    assert 4 == tab.heap[middle(index)]
    assert 5 == tab.heap[right(index)]
    index = tab.heap.index(1)
    assert 6 == tab.heap[parent(index)]
    index = tab.heap.index(4)
    assert 6 == tab.heap[parent(index)]
    index = tab.heap.index(5)
    assert 6 == tab.heap[parent(index)]

    index = tab.heap.index(9)
    assert 2 == tab.heap[left(index)]
    assert 7 == tab.heap[middle(index)]
    assert 8 == tab.heap[right(index)]
    index = tab.heap.index(2)
    assert 9 == tab.heap[parent(index)]
    index = tab.heap.index(7)
    assert 9 == tab.heap[parent(index)]
    index = tab.heap.index(8)
    assert 9 == tab.heap[parent(index)]

    tab.delete_root()
    assert tab.heap == [9, 6, 8, 3, 1, 4, 5, 2, 7]
    index = tab.heap.index(9)
    assert 6 == tab.heap[left(index)]
    assert 8 == tab.heap[middle(index)]
    assert 3 == tab.heap[right(index)]
    index = tab.heap.index(6)
    assert 9 == tab.heap[parent(index)]
    index = tab.heap.index(8)
    assert 9 == tab.heap[parent(index)]
    index = tab.heap.index(3)
    assert 9 == tab.heap[parent(index)]

    index = tab.heap.index(6)
    assert 1 == tab.heap[left(index)]
    assert 4 == tab.heap[middle(index)]
    assert 5 == tab.heap[right(index)]
    index = tab.heap.index(1)
    assert 6 == tab.heap[parent(index)]
    index = tab.heap.index(4)
    assert 6 == tab.heap[parent(index)]
    index = tab.heap.index(5)
    assert 6 == tab.heap[parent(index)]

    index = tab.heap.index(8)
    assert 2 == tab.heap[left(index)]
    assert 7 == tab.heap[middle(index)]
    index = tab.heap.index(2)
    assert 8 == tab.heap[parent(index)]
    index = tab.heap.index(7)
    assert 8 == tab.heap[parent(index)]

    tab.delete_root()
    assert tab.heap == [8, 6, 7, 3, 1, 4, 5, 2]
    index = tab.heap.index(8)
    assert 6 == tab.heap[left(index)]
    assert 7 == tab.heap[middle(index)]
    assert 3 == tab.heap[right(index)]
    index = tab.heap.index(6)
    assert 8 == tab.heap[parent(index)]
    index = tab.heap.index(7)
    assert 8 == tab.heap[parent(index)]
    index = tab.heap.index(3)
    assert 8 == tab.heap[parent(index)]

    index = tab.heap.index(6)
    assert 1 == tab.heap[left(index)]
    assert 4 == tab.heap[middle(index)]
    assert 5 == tab.heap[right(index)]
    index = tab.heap.index(1)
    assert 6 == tab.heap[parent(index)]
    index = tab.heap.index(4)
    assert 6 == tab.heap[parent(index)]
    index = tab.heap.index(5)
    assert 6 == tab.heap[parent(index)]

    index = tab.heap.index(7)
    assert 2 == tab.heap[left(index)]
    index = tab.heap.index(2)
    assert 7 == tab.heap[parent(index)]