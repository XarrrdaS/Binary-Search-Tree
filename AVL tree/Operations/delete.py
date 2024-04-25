def delete(root):
    if not root:
        return None
    root['left'] = delete(root['left'])
    root['right'] = delete(root['right'])
    return None
