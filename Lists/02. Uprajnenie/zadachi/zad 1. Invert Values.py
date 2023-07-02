# Write a program that receives a single string containing positive and negative numbers separated by a single space.
# Print a list containing the opposite of each number.

# противоположно по знак число


list_of_numbers = input().split()  # използвайнки .split() получавам стрингове
opposite_numbers = []
for element in list_of_numbers:       # този елемент трябва да го добавя към opposite_numbers
    current_number =  -int(element)   # слагам минус за да може да обърне числото
    opposite_numbers.append(current_number)
print(opposite_numbers)
