
n = int(input())
# Правим константни промени те са със главни букви ВИНАГИ ГЛАНИ БУКВИ нямат да бъдат изменяни в кода

COMMAND_EVEN = 'even'
COMMAND_ODD = 'odd'
COMMAND_NEGATIVE = 'negative'
COMMAND_POSITIVE = 'positive'

numbers = [int(input()) for _ in range(n)]

filtered_numbers = []

command = input()

for num in numbers:
    # Ако това е вярно тук ще се запази TRUE или FALSE

    filter_command = (
        (command == COMMAND_EVEN and num % 2 == 0 ) or
        (command == COMMAND_ODD and num % 2 != 0) or
        (command == COMMAND_POSITIVE and num >= 0) or
        (command == COMMAND_NEGATIVE and num <= 0)
        )
    # питаме дали нещо от тези проверки е рано на TRUE, то тогава във филтрираните числа искам да ми добавиш NUM
    if filter_command:
        filtered_numbers.append(num)

print(filtered_numbers)