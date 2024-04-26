def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root['left'])
        right_height = height(root['right'])
        return max(left_height, right_height) + 1

def left_rotation(node):
    new_root = node['right']
    node['right'] = new_root['left']
    new_root['left'] = node
    return new_root

def right_rotation(node):
    new_root = node['left']
    node['left'] = new_root['right']
    new_root['right'] = node
    return new_root

def rebalance(root):
    if root is None:
        return None
    left_height = height(root['left'])
    right_height = height(root['right'])

    if left_height - right_height > 1:
        if height(root['left']['left']) >= height(root['left']['right']):
            root = right_rotation(root)
        else:
            root['left'] = left_rotation(root['left'])
            root = right_rotation(root)
    elif right_height - left_height > 1:
        if height(root['right']['right']) >= height(root['right']['left']):
            root = left_rotation(root)
        else:
            root['right'] = right_rotation(root['right'])
            root = left_rotation(root)

    return root