from time import sleep
from timeit import default_timer
from random import randint, choice


def select_mode():
    print('''
    Режимы:
    1 - тренировка
    0 - выход
    ''')

    mode = ''
    while not mode.isdigit():
        print('Выбери режим:')
        mode = input()
        while not mode.isdigit():
            print('Должна быть цифра')
            mode = input()

    return mode


# функция возврата временных окончаний
def time_endings(digit):
    last_digit = int(digit[-1])

    if 10<int(digit)<15:
        return ''
    else:

        if last_digit == 1:
            return 'у'
        elif 1<last_digit<5:
            return 'ы'
        else:
            return ''

# функция возврата временных окончаний
def time_spent(time_in_seconds):
    if time_in_seconds < 60:
        seconds = str (time_in_seconds)
        time_spent = seconds + ' секунд' + time_endings(seconds)
    else:
        minutes = time_in_seconds // 60
        seconds = str(time_in_seconds - (minutes*60))
        if int(seconds) > 0:
            time_spent = str(minutes) + ' минут' + time_endings(str(minutes)) + ' и ' + str(seconds) + ' секунд' + \
                         time_endings(str(seconds))
        else:
            time_spent = str(minutes) + ' минут' + time_endings(str(minutes))

    return time_spent


# функция вывода примеров и их проверки
def count():

    answers_quantity = ''  # количество примеров
    count_to = ''  # до скольки будем считать
    correct_answers = 0  # количество правильных ответов
    fails = 0  # количество ошибок
    answers_time = 0  # затраченое время на все ответы

    sleep(1)
    print('Давай проверим твои знания в математике.')

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


        student_answer = ''

        while not student_answer.isdigit():
            print(numder1, sign, numder2)

            start = default_timer()
            student_answer = input()
            stop =default_timer()
            answers_time += round(stop-start)


            if not student_answer.isdigit():
                print('Должна быть цифра')


        if correct_answer == int(student_answer):
            print('Правильно, молодец')
            correct_answers += 1
        else:
            print('Неправильно')
            print('Правильныый ответ: ' + str (correct_answer))
            fails += 1

    if fails == 0:
        print('Молодец ты ответил на все вопросы провильно за ' + time_spent(answers_time))
    else:
        print()
        print('Правильных ответов: ' + str (correct_answers))
        print('Ошибок: ' + str(fails))
        print('Затраченое время ' + time_spent(answers_time))

# основной блок программы
print('Привет меня зовут Роджер. А тебя как ?')
name = input()
name = name.title()
print('Приятно пазнакомиться, ' + name)

sleep(1)

while True:
    mode = select_mode()
    if mode == '1':
        count()
    elif mode == "0":
        break
    else:
        pass