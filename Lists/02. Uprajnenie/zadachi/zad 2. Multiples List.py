# Write a program that receives two numbers (factor and count). It should create a list with a length of the given
# count that contains only integer numbers, which are multiples of the given factor. The numbers should be only
# positive, and they should be arranged in ascending order, starting from the value of the factor.


# 1 factor
# factor-a трябва да е първото число
# 2 колко числа търябва да има в този лист

factor = int(input())
count = int(input())
list_of_numbers = []

for multiplier in range(1, count + 1):
    list_of_numbers.append(factor * multiplier)
print(list_of_numbers)