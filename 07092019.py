# Игра угадай число
import random

print('Привет! Как тебя зовут?')
name = input()
print('Что ж, ' + name + ', я загадываю число от 1 до 20.')

number = random.randint(1,20)
counter = 0

for counter in range (6):
    if counter == 0:
        print("Папробуй угадать число:")
    else:
        print("Попробуй снова:")

    guess = int(input())

    if guess < number:
        print("Твоё число слишком маленькое")

    if guess > number:
        print("Твоё число слишком большое")

    if guess == number:
        break


if guess == number:
    counter = str(counter+1)
    print("Отлично, " + name + "! Ты справился за " + counter + " раз")

if guess != number:
    number = str (number)
    print("Увы я загадала число " + number)