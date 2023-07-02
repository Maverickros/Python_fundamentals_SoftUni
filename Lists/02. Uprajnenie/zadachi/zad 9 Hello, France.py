# You want to go to France by train, and the train ticket costs exactly 150$. You do not have enough money, so you
# decide to buy some items with your budget and then sell them at a higher price – with a 40% markup.
# You will receive a collection of items and a budget in the following format:
# {type->price|type->price|type->price……|type->price}
# {budget}
# The prices for each of the types cannot exceed a specific price, which is given below:

items = input().split("|")
budget = float(input())
# тук запазвам цените на продуктите след като съм ги продал увеличените с 40%
sell_prices = []
profit = 0
train_ticket = 150

for item in items:
# тук всеки път имаме {type, price} = индекси 0 и 1
# може да се изписва така но само когато сме сигурни,че променливите от ляво са равни на променливите които ще се разпакетират от дясно
    type, buying_price = item.split("->")
# цената BYYING_PRICE след като имаме SPLIT е станала на стринг, а на мен ми трябва FLOAT,за това добавям
    buying_price = float(buying_price)
# If a price for a particular item is higher than the maximum price, don't buy it
    price_is_valid = False
    if type == 'Clothes':
        if buying_price <= 50.00:
            price_is_valid = True
    elif type == 'Shoes':
        if buying_price <= 35.00:
            price_is_valid = True
    elif type == 'Accessories':
        if buying_price <= 20.50:
            price_is_valid = True
        # знам че цената е валидна
    if price_is_valid:
        # правя проверка за да знам че мога да си го купя
        if budget >= buying_price:
            # тук трябва да намаля бюджета
            budget -= buying_price
            # новата цена на която ще го продам
            sell_price = buying_price * 1.40
            # разликата между покупна цена и продажна цена
            profit += sell_price - buying_price
            sell_prices.append(sell_price)
# END
# OPTION 1
for sell_price in sell_prices:
    print(f'{sell_price:.2f}', end = " ")
print()

#OPTION 2
#print(" ".join([f'{sell_price:.2f}' for sell_price in sell_prices]))

# OPTIN 3
#sell_prices_as_string = []
#for sell_price in sell_prices:
#    sell_prices_as_string.append(f'{sell_price:.2f}')
#print(" ".join(sell_prices_as_string))

print(f'Profit: {profit:.2f}')
total_income = budget + sum(sell_prices)
if total_income >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')