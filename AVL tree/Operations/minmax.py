def find_min(root):
    current = root
    while current['left'] is not None:
        current = current['left']
    return current['key']

def find_max(root):
    current = root
    while current['right'] is not None:
        current = current['right']
    return current['key']
