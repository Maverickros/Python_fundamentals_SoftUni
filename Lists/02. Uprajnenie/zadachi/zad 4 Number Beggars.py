# You will receive 2 lines of input. On the first line, you will receive a single string of integers, separated by a comma
# and a space ", ". On the second line, you will receive a count of beggars. Your job is to print a list with the sum of
# what each beggar brings home, assuming they all take regular turns, from the first to the last number in the list.
# For example: [1, 2, 3, 4, 5] for 2 beggars will return a result of 9 and 6, as the first one takes [1, 3, 5], the
# second one collects [2, 4]. The same list with 3 beggars would produce a better outcome for the second beggar:
# 5, 7 and 3, as they will respectively take [1, 4], [2, 5], and [3].
# Also, note that not all beggars have to take the same amount of "offers", meaning that the length of the list is not
# necessarily a multiple of n. The list length could be even shorter - i.e., the last beggars will take nothing (0).

# ВХОД
# тук получавам  пари като стрринг
money_as_string = input().split(", ")

# брой просяци
number_of_beggars = int(input())

# създавам празен лист
money_as_digits = []

# всеки път когато сме вътре и имаме 2,4,6 като стринг, в новият лист на ред 16 ще ги записва като числа
for element in money_as_string:
    money_as_digits.append(int(element))
# на края трябва да се принтира лист
final_sum = []

# редно е да си направим един индекс 0-ла и докато този индекс е < брия просяци.
# ако ние четем хората 1,2,3 , при машината това са индекси 0,1,2 , за това индексираме просяците,като началният индекс е:
start_index = 0

while start_index < number_of_beggars:
    # просяк 1 сумата която той взема
    sum_for_current_beggar = 0
    for current_index in range(start_index, len(money_as_digits), number_of_beggars):
      # какво очакваме да се случи, всеки път когато въртим този цикъл, с тази стъпка
        sum_for_current_beggar += money_as_digits[current_index]
    # сумата за 1-я просяк вече не е 0-ла а се променя и към нея се добавя сумата за текущия просяк
    final_sum.append(sum_for_current_beggar)
    # стартовия индекс се увеличава с 1-ца
    start_index += 1

print(final_sum)