def count_occurrences(words):
    words_occurrences = {}
    for word in words:
        if word not in words_occurrences:
            words_occurrences[word] = 0
        words_occurrences[word] += 1

    return words_occurrences


def get_words_with_odd_occurrence(words_occurrences):
    return [word for (word, count)
            in words_occurrences.items()
            if count % 2 == 1]


def solve(words_str):
    words = [word.lower() for word in words_str.split(' ')]
    word_occurrences = count_occurrences(words)
    words_with_odd_occurrence = get_words_with_odd_occurrence(word_occurrences)
    print(' '.join(words_with_odd_occurrence))

solve(input())
#
# tests = [
#     'Java C# PHP PHP JAVA C java',
#     '3 5 5 hi pi HO Hi 5 ho 3 hi pi',
#     'a a A SQL xx a xx a A a XX c',
# ]
#
# [solve(test) for test in tests]
