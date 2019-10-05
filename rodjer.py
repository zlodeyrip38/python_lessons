from time import sleep
from random import randint, choice


print('Привет меня завут Роджер. А тебя как ?')
name = input()
name = name.title()
print('Приятно пазнакомиться, ' + name)
sleep(1)
print('Давай проверим твои знания в математике.')
sleep(1)

print('Ты готов? (да или нет)')
ready = input()
while ready not in {'да', 'нет'}:
    print('''Должно быть 'да' или 'нет'
Введи заново''')
    ready = input()

if ready == 'да':

    answers_quantity = ''  # количество примеров
    count_to = ''  # до скольки будем считать

    while not answers_quantity.isdigit():
        print('Сколько примеров ты готов решить?')
        answers_quantity = input()

        if answers_quantity.isdigit():
            while int(answers_quantity) < 1:
                print('Введи число больше 0')
                answers_quantity = input()
                while not answers_quantity.isdigit():
                    print('Должна быть цифра')
                    answers_quantity = input()
        else:
            print('Должна быть цифра')

    while not count_to.isdigit():
        print('До скольки будем считать? Например, до 100 ')
        count_to = input()

        if count_to.isdigit():
            while int(count_to) < 2:
                print('Введи число больше 1')
                count_to = input()
                while not count_to.isdigit():
                    print('Должна быть цифра')
                    count_to = input()
        else:
            print('Должна быть цифра')

    print('Хорошо, тогда начинаем...')
    sleep(1)

    answers_quantity = int(answers_quantity)
    count_to = int(count_to)

    for question in range(answers_quantity):
        print('пример ' + str(question+1))

        numder1 = randint(1, count_to)
        numder2 = randint(1, count_to)

        while numder1 < numder2:
            numder1 = randint(1, count_to)

        sign = choice('+-')

        print(numder1, sign, numder2)



else:
    print('''Передумал? Хорошо, может как-нибудь в следующий раз...
Пока!''')