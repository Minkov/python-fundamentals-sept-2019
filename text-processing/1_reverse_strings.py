def read_until_command(end_command):
    lines = []

    while True:
        line = input()
        if line == end_command:
            break
        lines.append(line)
    return lines

def reverse_strings(lines):
    for line in lines:
        print(f'{line} - {line[::-1]}')

reverse_strings(read_until_command('end'))