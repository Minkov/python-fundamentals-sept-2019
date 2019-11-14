numbers = list(map(int, input().split(', ')))

indices_for = []

for i in range(len(numbers)):
    number = numbers[i]
    if number % 2 == 0:
        indices_for.append(i)
print(indices_for)

indices_comprehension = [i for i in range(len(numbers))
                         if numbers[i] % 2 == 0]
print(indices_comprehension)

indices_lambdas = list(filter(lambda i: numbers[i] % 2 == 0,
                              range(len(numbers))))

print(indices_lambdas)
