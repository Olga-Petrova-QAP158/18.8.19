
amount = 0
tickets = (int(input("Введите количество билетов:")))
for age in range(tickets):
    age = (int(input("Введите возраст посетителя:")))
    if age < 18:
        amount += 0
    elif age >= 18 and age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
if amount == 0:
    print("Дети проходят бесплатно!")
else:
    print("Кол-во билетов:", tickets, "шт." )
if tickets > 3 :
    discount = amount / 100 * 10
    print("Скидка составляет 10%", discount, "руб.")
    print("К оплате с учетом скидки:", amount -discount, "руб.")