import re

pattern = '\\b[A-Z][a-z]+[ ][A-Z][a-z]+\\b'
text = """
Ivan     \t Ivanov
Toshko
"""
match = re.split('\s+', text.strip())
print(match)
