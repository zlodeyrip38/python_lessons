from time import sleep
from random import randint, choice


print ('Привет меня завут Роджер. А тебя как ?')
name = input()
print('Приятно пазнакомиться, ' + name)
sleep(2)
print('Давай проверим твои знания в математике.')
sleep(2)
print('Ты готов? (да или нет)')

ready = input()
if ready == 'да':
    print('Сколько примеров ты готов решить')
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