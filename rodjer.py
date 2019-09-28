from time import sleep
from random import randint, choice


print ('Привет меня завут Роджер. А тебя как?')
name = input()
name = name.title()
print('Приятно пазнакомиться, ' + name)
sleep(1)
print('Давай проверим твои знания в математике.')
sleep(1)
print('Ты готов? (да или нет)')

ready = input()
ready = ready.lower()

while ready not in {'да', 'нет'}:
    print('''Должно быть 'да' или 'нет'
Введите заново''')
    ready = input()
    ready = ready.lower()

if ready == 'да':
    col = '' # количество примеров

    while not col.isdigit():
        print('Сколько примеров ты готов решить')
        col = input()
        while not col.isdigit():
            print('Должна быть цифра')
            col = input()
        while col.isdigit():
            col = int(col)
            while col < 1:
                print('Введите число больше 0')
                col = int(input())

    print('До скольки будем считать? Например, до 100 ')
    max_answer = int(input())
    sleep(1)
    print('Хорошо, тогда начинаем...')
    sleep(1)

    for question in range(col):
        print('пример ' + str(question+1))

        numder1 = randint(1, max_answer)
        numder2 = randint(1, max_answer)

        while  numder1 < numder2:
            numder1 = randint(1, max_answer)

        sign = choice('+-')

        print(numder1,sign,numder2)
else:
    print('''Передумал? Хорошо , может какнибуть в следующий раз ...
Пока!''')