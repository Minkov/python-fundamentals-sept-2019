

def read_count_lines(n):
    return [input() for _ in range(n)]


def get_words_with_synonyms(lines):
    word_synonyms_dict = {}
    n = len(lines)
    for i in range(0, n, 2):
        word = lines[i]
        synonym = lines[i + 1]
        if word not in word_synonyms_dict:
            word_synonyms_dict[word] = []

        word_synonyms_dict[word].append(synonym)
    return word_synonyms_dict


def print_words(word_synonyms_dict):
    for (word, synonyms) in word_synonyms_dict.items():
        print(f'{word} - {", ".join(synonyms)}')


def solve(lines):
    word_synonyms_dict = get_words_with_synonyms(lines)
    print_words(word_synonyms_dict)


n = int(input())
lines = read_count_lines(n * 2)
# lines = [
#     'task',
#     'problem',
#     'task',
#     'assignment',
# ]
solve(lines)
