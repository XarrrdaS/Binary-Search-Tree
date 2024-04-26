def export(root):
        def inner(node):
            if not node:
                return []
            sdat = str(node['value'])
            l, r = inner(node['left']), inner(node['right'])
            cl, cr = len((l or ('',))[0]), len((r or ('',))[0])
            s = max(cl, cr)
            sll, slr = (s - cl + 1) // 2, (s - cl) // 2
            srl, srr = (s - cr) // 2, (s - cr + 1) // 2
            v = [' ' * s + sdat + ' ' * s]
            v.extend([' ' * (s - i - 1) + '/' + ' ' * i + ' ' * len(sdat) +
                      ' ' * i + '\\' + ' ' * (s - i - 1) for i in range(s // 2)])
            v.extend([(' ' * sll + l[i] + ' ' * slr if i < len(l) else ' ' * s) +
                      ' ' * len(sdat) + (' ' * srl + r[i] + ' ' * srr if i < len(r) else ' ' * s)
                      for i in range(max(len(l), len(r)))])
            return v

        if root:
            return '\n'.join(inner(root))
        else:
            return 'Tree is empty!'