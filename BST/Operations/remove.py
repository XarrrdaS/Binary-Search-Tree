def remove(tree, elements):
    for element in elements:
        tree = remove_element(tree, element)
    return tree

def remove_element(node, element):
    if node is None:
        return None

    if element < node['value']:
        node['left'] = remove_element(node['left'], element)
    elif element > node['value']:
        node['right'] = remove_element(node['right'], element)
    else:
        if node['left'] is None and node['right'] is None:
            return None
        elif node['left'] is None:
            return node['right']
        elif node['right'] is None:
            return node['left']
        else:
            successor = find_min(node['right'])
            node['value'] = successor['value']
            node['right'] = remove_element(node['right'], successor['value'])

    return node

def find_min(node):
    while node is not None and node['left'] is not None:
        node = node['left']
    return node