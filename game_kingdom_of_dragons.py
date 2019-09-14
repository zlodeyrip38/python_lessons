# Игра "Царство драконов"
import random, time

def displayIntro():
    print('''Вы находитесь в землях, заселенными драконами.
    Перед собой вы видите две пещеры.
    В одной из них - дружелюбный дракон,
    который готов поделиться с вами сокровищами.
    Во второй - жадный и голодный дракон, который мигом вас съест.
    
    ''')

def chooseCave():
    cave = ''
    print("нажмите клавишу 1 или 2")
    cave = input()
    cave = int(cave)
    return cave

def checkCave(choosen_cave):
    print("Вы приближаетесь к пещере...")
    time.sleep(3)
    print("Её темнота заставляет вас дрожать от страха...")
    time.sleep(3)
    print("Большой дракон выпрыгивает перед вами! Он раскрывает свою пасть и...")
    time.sleep(3)

    friendly_cave = random.randint(1, 2)

    if choosen_cave == friendly_cave:
        print('...делиться с вами своими сокровищами')
    else:
        print("...моментально съедает вас")

displayIntro()
checkCave(chooseCave())