def in_order_traversal(root):
    if root is None:
        return
    in_order_traversal(root['left'])
    print(root['value'], end=' ')
    in_order_traversal(root['right'])