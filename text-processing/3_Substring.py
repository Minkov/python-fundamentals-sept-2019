def substring(word1, word2):
    while word1 in word2:
        word2 = word2.replace(word1, '')

    return word2

word1 = 'ice'
word2 = 'kicegiciceeb'

print(substring(word1, word2))
