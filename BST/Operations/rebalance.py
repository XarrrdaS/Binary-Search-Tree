def rebalance(root):
    nodes = []
    def traverse(node):
        if node is not None:
            traverse(node['left'])
            nodes.append(node)
            traverse(node['right'])

    traverse(root)

    n = len(nodes)
    m = int(2 ** (n.bit_length() - 1) - 1)
    curr = root
    for i in range(m):
        curr['left'] = nodes[i]
        curr = curr['left']
        nodes[i]['right'] = nodes[i + 1] if i + 1 < n else None

    while m > 1:
        curr = root
        for i in range(m):
            curr = curr['left']
            curr['right'] = nodes[i + m + 1] if i + m + 1 < n else None
        m //= 2

    return root