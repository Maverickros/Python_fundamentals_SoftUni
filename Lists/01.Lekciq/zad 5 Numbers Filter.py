# On the first line, you will receive a single number n. On the following n lines, you will receive integers.
# After that, you will be given one of the following commands:

# • even
# • odd
# • negative
# • positive

# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

# числата които ще вкарваме
n = int(input())
#Инизиализираме един празен списък
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)
#print(numbers)

# тази команда казва по какъв начин да се групират числата
command = input()
filtered_numbers = []

if command == 'even':
    for num in numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)

elif command == 'odd':
    for num in numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)

elif command == 'negative':
    for num in numbers:
        if num < 0:
            filtered_numbers.append(num)

elif command == 'positive':
    for num in numbers:
        if num >= 0:
            filtered_numbers.append(num)

print(filtered_numbers)



