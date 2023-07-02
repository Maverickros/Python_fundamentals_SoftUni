# On the first line, you will receive a number n. On the second line, you will receive a word. On the following n lines,
# you will be given some strings. You should add them to a list and print them. After that, you should filter out only
# the strings that include the given word and print that list too.

n = int(input())
special_word = input()

strings = []

for _ in range(n):
    string = input()
    strings.append(string)

print(strings)

filtered_strings = []

for string in strings:
    if special_word in string:
        filtered_strings.append(string)
print(filtered_strings)




#my_list = ['apple', 'banana', 'cherry']

#if 'cherry' in my_list:
#    print(my_list)
#else:
#    print('Not found')
