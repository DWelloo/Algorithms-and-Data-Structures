from trees import AVL, delete_element


def test_avl():
    lista = [5, 1, 3, 8, 6]
    avl = AVL(lista)
    assert avl.root_of_tree.value == 5
    assert avl.root_of_tree.left_child.value == 3
    assert avl.root_of_tree.right_child.value == 8


def test_add():
    lista = [5, 1, 3, 8, 9, 2, 4, 6, 7, 10, 11]
    avl = AVL(lista)
    avl.add_node(12)
    assert avl.find_node(12).value == 12
    assert avl.find_node(9).right_child == avl.find_node(12)
    assert avl.find_node(31) is None


def test_delete():
    lista = [5, 1, 3, 8, 9, 2, 4, 6, 7, 10, 11]
    avl = AVL(lista)
    delete_element(avl.root_of_tree, 3)
    assert avl.find_node(3) is None
    assert avl.find_node(5).left_child.value != 3
    avl.add_node(4)
    assert avl.find_node(4).quantity == 2
    assert avl.find_node(5).left_child.quantity == 2
    delete_element(avl.root_of_tree, 4)
    assert avl.find_node(4).quantity == 1
    assert avl.find_node(5).left_child.quantity == 1


def test_height():
    lista = [5, 1, 3, 8, 9, 2, 4, 6, 7, 10, 11]
    avl = AVL(lista)
    node1 = avl.find_node(3)
    assert avl.get_height(node1) == 2
    assert avl.get_height(node1.left_child) == 1
    assert avl.get_height(node1.right_child) == 1
    node2 = avl.find_node(15)
    assert avl.get_height(node2) == 0


def test_balance():
    lista = [5, 1, 3, 8, 9, 2, 4, 6, 7, 10, 11]
    avl = AVL(lista)
    node1 = avl.find_node(3)
    assert avl.get_balance(node1) == 0
    assert avl.get_balance(node1.left_child) == 0
    assert avl.get_balance(node1.right_child) == 0
    node2 = avl.find_node(12)
    assert avl.get_balance(node2) == 0
