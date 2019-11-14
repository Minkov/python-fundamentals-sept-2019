def read_until_command(end_command):
    lines = []

    while True:
        line = input()
        if line == end_command:
            break
        lines.append(line)
    return lines


def print_quantities(quantities_dict):
    print('Products in stock:')
    for (product, quantity) in quantities_dict.items():
        print(f'- {product}: {quantity}')

    print(f'Total Products: {len(quantities_dict)}')
    print(f'Total Quantity: {sum(quantities_dict.values())}')

def get_products_quantities_dict(lines):
    quantities_dict = {}
    for line in lines:
        (product, quantity_str) = line.split(': ')
        if product not in quantities_dict:
            quantities_dict[product] = 0

        quantities_dict[product] += int(quantity_str)
    return quantities_dict


def solve(lines):
    quantities_dict = get_products_quantities_dict(lines)
    print_quantities(quantities_dict)


lines = read_until_command('statistics')
# lines = ['bread: 4', 'cheese: 2', 'ham: 1', 'bread: 1']
solve(lines)
