def sort_tree(root):
    if not root:
        return []
    return sort_tree(root['left']) + [root['key']] + sort_tree(root['right'])

def DSW(nodes):
    if not nodes:
        return None
    mid = len(nodes) // 2
    root = {'key': nodes[mid], 'left': None, 'right': None}
    root['left'] = DSW(nodes[:mid])
    root['right'] = DSW(nodes[mid+1:])
    return root

def rebalance(root):
    nodes = sort_tree(root)
    return DSW(nodes)
