import re

pattern = '\\b[A-Z][a-z]+[ ][A-Z][a-z]+\\b'
text = 'Ivan Ivanov, ivan ivanov, Ivan ivanov, ivan Ivanov, IVan Ivanov, Ivan IvAnov, Ivan	Ivanov, Ivan Ivanov'
matches = re.search(pattern, text)
print(' '.join(matches))
