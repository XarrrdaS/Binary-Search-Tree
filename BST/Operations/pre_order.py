def pre_order_traversal(root):
    if root is None:
        return
    print(root['value'], end=' ')
    pre_order_traversal(root['left'])
    pre_order_traversal(root['right'])