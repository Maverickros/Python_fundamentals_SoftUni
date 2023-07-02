numbers = list(map(int, input().split()))

while True:
    command = input().split()

    if command[0] == 'end':
        print(', '.join([str(num) for num in numbers]))
        break

    elif command[0] == 'swap':
        index_one = int(command[1])
        index_two = int(command[2])
        numbers[index_one], numbers[index_two] = numbers[index_two], numbers[index_one]

    elif command[0] == 'multiply':
        index_one = int(command[1])
        index_two = int(command[2])
        product_of_multiply = numbers[index_one] * numbers[index_two]
        numbers[index_one] = product_of_multiply

    elif command[0] == 'decrease':
        numbers = [num - 1 for num in numbers]