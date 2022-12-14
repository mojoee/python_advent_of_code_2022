from anytree import Node, RenderTree, AsciiStyle, PostOrderIter
import anytree

class NodeS(Node):
    def __init__(self, name, parent, size, isdirectory):
        super(NodeS, self).__init__(name=name, parent=parent)
        self.size = size
        self.isdir = isdirectory


def process_command(command: str, current_parent):
    #$ cd fcqv#
    if command.split(" ")[1] == "cd":
        new_parent = command.split(" ")[2]
        new_parent = change_parent(new_parent, current_parent)
        return new_parent
    elif command.split(" ")[1] == "ls":
        return current_parent


def change_parent(new_parent, current_parent):
    if new_parent == "..":
        new_parent = current_parent.parent
    else:
        new_parents = anytree.search.findall(current_parent, lambda node: node.name == new_parent)
        for p in new_parents:
            if p == current_parent:
                continue
            else:
                new_parent = p
    return new_parent

def create_node(dict, item, node):
    name = item.split(" ")[-1]
    if item.startswith("dir"):
        size = 0
        isdirectory = True
        prefix = "d"
    else:
        size = int(item.split(" ")[0])
        isdirectory = False
        prefix = "f"
    dict[prefix+name] = NodeS(name=name, parent=node, size=size, isdirectory=isdirectory)


if __name__ == "__main__":
    with open("./day7/input.txt", "r") as f:
        data = f.read().splitlines()
    root = Node("/") #root
    cwd = "/"
    current_parent = root
    nodes = {}
    nodes[cwd] = current_parent
    for j, item in enumerate(data[2:]):
        if item.startswith("$"):
            current_parent = process_command(item, current_parent)
        else:
            create_node(nodes, item, current_parent)

    print(RenderTree(nodes["/"], style=AsciiStyle()).by_attr())
    total_size = 0
    for name, node in nodes.items():
        if node.name == '/':
            continue
        if not node.isdir:
            continue
        node_sum = sum([x.size for x in PostOrderIter(node)])
        if node_sum <= 100000:
            # print(f"{name}: {size}")
            total_size += node_sum
    print(total_size)
