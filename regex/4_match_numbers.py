import re

prefix_pattern = r'(^|(?<=\s))'
number_pattern = r'(?P<number>-?\d+([.]\d+)?)'
suffix_pattern = r'($|(?=\s))'

pattern = prefix_pattern + number_pattern + suffix_pattern

text = """
1 -1 123 -123 123.456 -123.456 1.1
1s s-s _55_ _f s-1.1 s2 -1- zs-2 s-3.5 1.2.3 1.
"""

matches = re.finditer(pattern, text)
numbers = [match.group('number') for match in matches]
print(' '.join(numbers))
