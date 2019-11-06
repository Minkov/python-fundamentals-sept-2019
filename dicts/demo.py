dd = {5: 'five', 6: 'six', 1: 'one'}
print(dd)


def get_compare_value(x):
    return [x, x % 3]


dd = dict(sorted(dd.items(), key=get_compare_value))
print(dd)
