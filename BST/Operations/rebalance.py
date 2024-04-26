def rebalance(root):
    # Tworzenie listy wierzchołków
    nodes = []
    curr = root['left']
    while curr is not None:
        nodes.append(curr)
        curr = curr['left']

    # Wykonanie rotacji DSW
    n = len(nodes)
    m = int(2 ** (n.bit_length() - 1) - 1)  # Use int() here
    curr = root
    for i in range(m):
        curr['left'] = nodes[i]
        curr = curr['left']
        nodes[i]['right'] = nodes[i + 1] if i + 1 < n else None

    # Przywrócenie równowagi
    while m > 1:
        curr = root
        for i in range(m):
            curr = curr['left']
            curr['right'] = nodes[i + m + 1] if i + m + 1 < n else None
        m //= 2

    return root