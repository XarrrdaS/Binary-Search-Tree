def build_bst(values):
    def insert(root, value):
        if root is None:
            return {'value': value, 'left': None, 'right': None}
        if value < root['value']:
            root['left'] = insert(root['left'], value)
        else:
            root['right'] = insert(root['right'], value)
        return root

    root = None
    for value in values:
        root = insert(root, value)
    return root