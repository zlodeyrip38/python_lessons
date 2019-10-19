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
    correct_answers = 0  # количество правильных ответов
    fails = 0  # количество ошибок

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

        numder1 = randint(1, count_to)
        numder2 = randint(1, count_to)
        sign = choice('+-')

        if sign == '+':
            while numder1 + numder2 > count_to:
                numder1 = randint(1, count_to)
                numder2 = randint(1, count_to)

            correct_answer = numder1 + numder2

        if sign == '-':
            while numder1 < numder2:
                numder1 = randint(1, count_to)
                numder2 = randint(1, count_to)

            correct_answer = numder1 - numder2

        print('пример ' + str(question+1))
        print(numder1, sign, numder2)


        student_answer = input()

        while not student_answer.isdigit():
            print('Должна быть цифра')
            student_answer = input()

        if correct_answer == int(student_answer):
            print('Правильно, молодец')
            correct_answers += 1
        else:
            print('Неправильно')
            print('Правильныый ответ: ' + str (correct_answer))
            fails += 1

    if fails == 0:
        print('Молодец ты ответил на все вопросы провильно')
    else:
        print()
        print('Правильных ответов: ' + str (correct_answers))
        print('Ошибок: ' + str(fails))

else:
    print('''Передумал? Хорошо, может как-нибудь в следующий раз...
Пока!''')