class Node:
    def __init__(self, element):
        self.value = element
        self.left_child = None
        self.right_child = None
        self.height = 1
        self.quantity=1

class BST:
    def __init__(self, list_of_values=None):
        self.root_of_tree = None
        if list_of_values is not None:
            for element in list_of_values:
                self.add_node(element)

    def add_node(self, element):
        if self.root_of_tree is None:
            self.root_of_tree = Node(element)
            return
        return self.add_node_with_root(self.root_of_tree, element)

    def add_node_with_root(self, node, element):
        if element < node.value:
            if node.left_child is None:
                node.left_child = Node(element)
            else:
                self.add_node_with_root(node.left_child, element)
        elif element > node.value:
            if node.right_child is None:
                node.right_child = Node(element)
            else:
                self.add_node_with_root(node.right_child, element)
        else:
            node.quantity += 1

    def find_node(self, element):
        if self.root_of_tree is None:
            return None
        return self.find_node_with_root(self.root_of_tree, element)

    def find_node_with_root(self, node, element):
        if element == node.value:
            return node
        elif element < node.value and node.left_child is not None:
            return self.find_node_with_root(node.left_child, element)
        elif element > node.value and node.right_child is not None:
            return self.find_node_with_root(node.right_child, element)
        else:
            return None

def delete_element(root,element):
    if root==None:
        return root
    if element<root.value:
        root.left_child=delete_element(root.left_child,element)
    elif element>root.value:
        root.right_child=delete_element(root.right_child,element)
    else:
        if root.left_child==None:
            tmp=root.right_child
            root=None
            return tmp
        elif root.right_child==None:
            tmp=root.left_child
            root=None
            return tmp
        tmp=min_val_node(root.right_child)
        root.value=tmp.value
        root.right_child=delete_element(root.right_child,tmp.value)
    return root

def min_val_node(node):
    tmp=node
    while(tmp.left_child!=None):
        tmp=tmp.left_child
    return tmp

class AVL:
    def add_node(self, node, element):
        if node==None:
            return Node(element)
        elif element == node.value:
            node.quantity += 1
        elif element < node.value:
            node.left_child = self.add_node(node.left_child, element)
        else:
            node.right_child = self.add_node(node.right_child, element)

        node.height = 1 + max(self.get_height(node.left_child),
                              self.get_height(node.right_child))

        balance = self.getBalance(node)
        if balance > 1:
            if element < node.left_child.value:
                return self.right_Rotate(node)
            else:
                node.left_child = self.left_Rotate(node.left_child)
                return self.right_Rotate(node)

        if balance < -1:
            if element > node.right_child.value:
                return self.left_Rotate(node)
            else:
                node.right_child = self.right_Rotate(node.right_child)
                return self.left_Rotate(node)

        return node
    
    def find_node(self, node, element):
        if node==None:
            return False
        if node.value == element:
            return True
        elif node.value < element:
            return self.find_node(node.right_child,element)
        elif node.value > element:
            return self.find_node(node.left_child,element)
        return False

    def delete_node(self, node, element):
        if not node:
            return node
        elif element < node.value:
            node.left_child = self.delete_node(node.left_child, element)
        elif element > node.value:
            node.right_child = self.delete_node(node.right_child, element)
        else:
            if node.left_child is None:
                temp = node.right_child
                node = None
                return temp
            elif node.right_child is None:
                temp = node.left_child
                node = None
                return temp
            temp = min_val_node(node.right_child)
            node.value = temp.value
            node.right_child = self.delete_node(node.right_child,
                                          temp.value)
        if node is None:
            return node

        node.height = 1 + max(self.get_height(node.left_child),
                              self.get_height(node.right_child))

        balance = self.getBalance(node)

        if balance > 1:
            if self.getBalance(node.left_child) >= 0:
                return self.right_Rotate(node)
            else:
                node.left_child = self.left_Rotate(node.left_child)
                return self.right_Rotate(node)
        if balance < -1:
            if self.getBalance(node.right_child) <= 0:
                return self.left_Rotate(node)
            else:
                node.right_child = self.right_Rotate(node.right_child)
                return self.left_Rotate(node)
        return node

    def left_Rotate(self, node):
        tmpr = node.right_child
        tmp2 = tmpr.left_child
        tmpr.left_child = node
        node.right_child = tmp2
        node.height = 1 + max(self.get_height(node.left_child),
                           self.get_height(node.right_child))
        tmpr.height = 1 + max(self.get_height(tmpr.left_child),
                           self.get_height(tmpr.right_child))
        return tmpr

    def right_Rotate(self, node):
        tmpl = node.left_child
        tmp2 = tmpl.right_child
        tmpl.right_child = node
        node.left_child = tmp2
        node.height = 1 + max(self.get_height(node.left_child),
                           self.get_height(node.right_child))
        tmpl.height = 1 + max(self.get_height(tmpl.left_child),
                           self.get_height(tmpl.right_child))
        return tmpl

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.get_height(node.left_child) - self.get_height(node.right_child)

