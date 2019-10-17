todos = []

max_priority = 0

while True:
    command = input().split('-')
    if command[0] == 'End':
        break

    priority = int(command[0])
    text = command[1]
    todos.append([priority, text])
    max_priority = max(max_priority, priority)

result = [None] * len(todos)
for todo in todos:
    priority = todo[0]
    text = todo[1]
    result.insert(priority, text)
print([x for x in result if x])