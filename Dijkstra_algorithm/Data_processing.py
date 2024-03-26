from Node_class import Node

def read_map(file) -> list: # fields[y][x]
    fields = []
    with open(file) as fl:
        for line in fl:
            spaces=line.count(" ")
            row = []
            ln = line.split()
            for i in range(spaces):
                #if it's not supposed to go through this node, i.e.  1 node 1
                #val must be so that it's more optimal to go
                #999
                #1 1
                #so 3*9+1=28
                row.append(28)
            for number in ln[0]:
                row.append(int(number))
            fields.append(row)
    return fields

def make_nodes(fields):
    rows=len(fields)
    nodes = [[0 for x in range(len(fields[y]))] for y in range(rows)]
    for y in range(rows):
        for x in range(len(fields[y])):
            node = Node()
            node.val = fields[y][x]
            node.x=x
            node.y=y
            nodes[y][x]=node
    for y in range(rows):
        for x in range(len(fields[y])):
            if x - 1 >= 0 and y>=0 and y<len(fields):
                nodes[y][x].left = nodes[y][x-1]
            if x + 1 < len(fields[y]) and y>=0 and y<len(fields):
                nodes[y][x].right = nodes[y][x+1]
            if y - 1 >= 0 and x>=0 and x<len(fields[y-1]):
                nodes[y][x].up = nodes[y-1][x]
            if y + 1 < len(fields) and x>=0 and x<len(fields[y+1]):
                nodes[y][x].down = nodes[y+1][x]
    return nodes