def rebalance(root):
    # Create a list of nodes (including both left and right subtrees)
    nodes = []
    def traverse(node):
        if node is not None:
            traverse(node['left'])
            nodes.append(node)
            traverse(node['right'])

    traverse(root)

    # Perform DSW balancing
    n = len(nodes)
    m = int((n - 1) // 2)  # More accurate calculation for middle element(s)

    for i in range(m):
        # Left Rotation (considering both left and right children)
        temp = nodes[i]['right']
        nodes[i]['right'] = nodes[i + m + 1]
        if nodes[i + m + 1]:
            nodes[i + m + 1]['left'] = temp

        # Right Rotation (considering both left and right children)
        temp = nodes[i]['left']
        nodes[i]['left'] = nodes[i - m - 1] if i - m - 1 >= 0 else None
        if nodes[i - m - 1]:
            nodes[i - m - 1]['right'] = temp

    # Reconstruct the tree from the balanced node list
    def build_tree(nodes, i):
        if i >= n:
            return None
        node = nodes[i]
        node['left'] = build_tree(nodes, 2 * i + 1)
        node['right'] = build_tree(nodes, 2 * i + 2)
        return node

    return build_tree(nodes, 0)
