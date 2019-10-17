wagons_count = int(input())
wagons = [0] * wagons_count

command = input().split(' ')

while command[0] != 'End':
    if command[0] == 'add':
        wagons[len(wagons) - 1] += int(command[1])
    elif command[0] == 'insert':
        index = int(command[1])
        people = int(command[2])
        wagons[index] += people
    elif command[0] == 'leave':
        index = int(command[1])
        people = int(command[2])
        wagons[index] -= people
    command = input().split(' ')

print(wagons)