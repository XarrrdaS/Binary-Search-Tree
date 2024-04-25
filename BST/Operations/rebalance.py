def tree_to_vine(root):
    vine_tail = [None, None, None]
    remainder = vine_tail
    temp_node = None

    while remainder is not None:
        if remainder[1] is None:
            vine_tail = remainder
            remainder = remainder[2]
        else:
            temp_node = remainder[1]
            remainder[1] = temp_node[2]
            temp_node[2] = remainder
            remainder = temp_node
            vine_tail[2] = temp_node

    return vine_tail[2]

def compression(root, count):
    scanner = root
    for _ in range(count):
        child = scanner[2]
        scanner[2] = child[2]
        scanner = scanner[2]
        child[2] = scanner[1]
        scanner[1] = child

def rebalance(root):
    vine = tree_to_vine(root)
    node_count = 0
    temp = vine

    while temp is not None:
        node_count += 1
        temp = temp[2]

    leaf_count = node_count + 1 - 2 ** (node_count.bit_length() - 1)
    compression(vine, int(leaf_count))

    node_count -= leaf_count
    while node_count > 1:
        compression(vine, int(node_count // 2))
        node_count //= 2

    return vine