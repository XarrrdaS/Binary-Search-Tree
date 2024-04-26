def delete(root):
    if root is None or 'value' not in root:
        return

    # Usuwanie lewego poddrzewa
    delete(root.get('left'))

    # Usuwanie prawego poddrzewa
    delete(root.get('right'))

    # Wypisywanie usuwanego węzła
    print("Deleting node with value:", root['value'])

    # Usuwanie korzenia
    root['left'] = None
    root['right'] = None
    return None