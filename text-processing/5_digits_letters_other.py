# def solve(s):
#     digits = ''
#     letters = ''
#     other = ''
#     for ch in s:
#         if ch.isdigit():
#             digits += ch
#         elif ch.isalpha():
#             letters += ch
#         else:
#             other += ch
#     print(digits)
#     print(letters)
#     print(other)

def solve(s):
    print(''.join([ch for ch in s if ch.isdigit()]))
    print(''.join([ch for ch in s if ch.isalpha()]))
    print(''.join([ch for ch in s if not ch.isalnum()]))


solve('Agd#53Dfg^&4F53')