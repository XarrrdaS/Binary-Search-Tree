def remove(root):
    nodes_to_remove = input("Enter nodes to remove (space-separated): ").split()
    nodes_to_remove = list(map(int, nodes_to_remove))
    for node_value in nodes_to_remove:
        root = remove_node(root, node_value)
    return root

def remove_node(root, value):
    if not root:
        return None
    if value < root['key']:
        root['left'] = remove_node(root['left'], value)
    elif value > root['key']:
        root['right'] = remove_node(root['right'], value)
    else:
        if not root['left']:
            return root['right']
        elif not root['right']:
            return root['left']
        else:
            successor = get_min_value_node(root['right'])
            root['key'] = successor['key']
            root['right'] = remove_node(root['right'], successor['key'])
    return root

def get_min_value_node(node):
    current = node
    while current['left']:
        current = current['left']
    return current
