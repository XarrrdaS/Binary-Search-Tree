def post_order_traversal(root):
    if root is None:
        return
    post_order_traversal(root['left'])
    post_order_traversal(root['right'])
    print(root['value'], end=' ')