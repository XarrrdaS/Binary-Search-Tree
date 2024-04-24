def rebalance(root):
    nodes = []
    inorder_traversal(root, nodes)

    return build_balanced_tree(nodes, 0, len(nodes) - 1)

def inorder_traversal(node, nodes):
    if node is None or 'value' not in node:
        return

    inorder_traversal(node.get('left'), nodes)
    nodes.append(node)
    inorder_traversal(node.get('right'), nodes)

def build_balanced_tree(nodes, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    node = nodes[mid]

    root = {'value': node['value']}
    root['left'] = build_balanced_tree(nodes, start, mid - 1)
    root['right'] = build_balanced_tree(nodes, mid + 1, end)

    return root