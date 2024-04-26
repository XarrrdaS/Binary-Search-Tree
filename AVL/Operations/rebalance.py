def flatten(root):
    if not root:
        return []
    return flatten(root['left']) + [root['key']] + flatten(root['right'])

def build_balanced(nodes):
    if not nodes:
        return None
    mid = len(nodes) // 2
    root = {'key': nodes[mid], 'left': None, 'right': None}
    root['left'] = build_balanced(nodes[:mid])
    root['right'] = build_balanced(nodes[mid+1:])
    return root

def rebalance(root):
    nodes = flatten(root)
    return build_balanced(nodes)
