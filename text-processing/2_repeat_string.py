from functools import reduce


def repeat_string(words):
    result = ''
    for word in words:
        result += word * len(word)

    return result


words = input().split()
print(repeat_string(words))
