import re

pattern = r'(?P<day>\d{2})(?P<separator>[.\-/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})'
text = """13/Jul/1928, 10-Nov-1934, 25.Dec.1937
01/Jan-1951, 23/sept/1973, 1/Feb/2016, 33/Jul/1928"""

matches = re.finditer(pattern, text)

ll = [1, 2, 3, 4]

for _ in range(0, 10):
    print(1)


for match in matches:
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')
    print(f'Day: {day}, Month: {month}, Year: {year}')