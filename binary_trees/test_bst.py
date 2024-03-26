from trees import BST, delete_element


def test_bst():
    lista = [5, 1, 3, 8, 6]
    bst = BST(lista)
    assert bst.root_of_tree.value == 5
    assert bst.root_of_tree.left_child.value == 1
    assert bst.root_of_tree.right_child.value == 8


def test_add():
    lista = [5, 1, 3, 8, 9, 2, 4, 6, 7, 10, 11]
    bst = BST(lista)
    bst.add_node(12)
    assert bst.find_node(12).value == 12
    assert bst.find_node(11).right_child == bst.find_node(12)
    assert bst.find_node(31) is None


def test_delete():
    lista = [5, 1, 3, 8, 9, 2, 4, 6, 7, 10, 11]
    bst = BST(lista)
    delete_element(bst.root_of_tree, 3)
    assert bst.find_node(3) is None
    assert bst.find_node(1).right_child.value != 3
    bst.add_node(4)
    assert bst.find_node(4).quantity == 2
    assert bst.find_node(2).right_child.quantity == 2
    bst.delete_element(4)
    assert bst.find_node(4).quantity == 1
    assert bst.find_node(2).right_child.quantity == 1
