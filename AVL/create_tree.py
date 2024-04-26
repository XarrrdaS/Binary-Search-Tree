def height(node):
    if not node:
        return 0
    return node['height']

def balance(node):
    if not node:
        return 0
    return height(node['left']) - height(node['right'])

def rotate_right(y):
    x = y['left']
    T2 = x['right']

    x['right'] = y
    y['left'] = T2

    y['height'] = 1 + max(height(y['left']), height(y['right']))
    x['height'] = 1 + max(height(x['left']), height(x['right']))

    return x

def rotate_left(x):
    y = x['right']
    T2 = y['left']

    y['left'] = x
    x['right'] = T2

    x['height'] = 1 + max(height(x['left']), height(x['right']))
    y['height'] = 1 + max(height(y['left']), height(y['right']))

    return y

def insert(root, key):
    if not root:
        return {'key': key, 'left': None, 'right': None, 'height': 1}
    elif key < root['key']:
        root['left'] = insert(root['left'], key)
    else:
        root['right'] = insert(root['right'], key)

    root['height'] = 1 + max(height(root['left']), height(root['right']))

    balance_factor = balance(root)

    if balance_factor > 1 and key < root['left']['key']:
        return rotate_right(root)

    if balance_factor < -1 and key > root['right']['key']:
        return rotate_left(root)

    if balance_factor > 1 and key > root['left']['key']:
        root['left'] = rotate_left(root['left'])
        return rotate_right(root)

    if balance_factor < -1 and key < root['right']['key']:
        root['right'] = rotate_right(root['right'])
        return rotate_left(root)

    return root

def in_order(node):
    result = []
    if node:
        result.extend(in_order(node['left']))
        result.append(node['key'])
        result.extend(in_order(node['right']))
    return result

def pre_order(node):
    result = []
    if node:
        result.append(node['key'])
        result.extend(pre_order(node['left']))
        result.extend(pre_order(node['right']))
    return result

def post_order(node):
    result = []
    if node:
        result.extend(post_order(node['left']))
        result.extend(post_order(node['right']))
        result.append(node['key'])
    return result

def get_sorted_list(node):
    return in_order(node)

def get_median(sorted_list):
    n = len(sorted_list)
    if n % 2 == 0:
        return (sorted_list[n//2 - 1] + sorted_list[n//2]) / 2
    else:
        return sorted_list[n//2]

def create_tree():
    root = None
    input_values = input("nodes > ").split()
    input_values = list(map(int, input_values))
    for val in input_values:
        root = insert(root, val)
    
    sorted_list = get_sorted_list(root)
    median = get_median(sorted_list)

    print("Sorted:", sorted_list)
    print("Median:", median)
    return root
