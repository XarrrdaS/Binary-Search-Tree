def find_min(node):
    if node is None:
        return None
    while 'left' in node and node['left'] is not None:
        node = node['left']
    return node['value']

def find_max(node):
    if node is None:
        return None
    while 'right' in node and node['right'] is not None:
        node = node['right']
    return node['value']