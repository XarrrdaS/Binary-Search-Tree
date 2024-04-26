def find_min(node):
    # Base case: If the node is None, return None
    if node is None:
        return None
    
    # Traverse to the leftmost node to find the minimum value
    while 'left' in node and node['left'] is not None:
        node = node['left']
    
    # Return the minimum value
    return node['value']


def find_max(node):
    # Base case: If the node is None, return None
    if node is None:
        return None
    
    # Traverse to the rightmost node to find the maximum value
    while 'right' in node and node['right'] is not None:
        node = node['right']
    
    # Return the maximum value
    return node['value']