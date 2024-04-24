def build_bst(numbers_str):
    numbers = [int(num) for num in numbers_str.replace(',', ' ').replace(';', ' ').split()]
    if not numbers:
        return None

    root = {'value': numbers[0], 'left': None, 'right': None}
    for num in numbers[1:]:
        current = root
        while True:
            if num < current['value']:
                if current['left'] is None:
                    current['left'] = {'value': num, 'left': None, 'right': None}
                    break
                else:
                    current = current['left']
            else:
                if current['right'] is None:
                    current['right'] = {'value': num, 'left': None, 'right': None}
                    break
                else:
                    current = current['right']

    return root