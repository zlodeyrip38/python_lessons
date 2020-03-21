from random import shuffle, choice


# возврощяет колоду карт
def get_deck():
    deck = []

    for suit in ('червы', 'трефы', 'бубы', 'пики'):
        for card in range(2, 11):
            deck.append(f'{card} {suit}')
        for card in ('валет', 'дама', 'король', 'туз'):
            deck.append(f'{card} {suit}')
    shuffle(deck)
    return deck


def get_card_points(card):
    splited_card = card.split()

    card_points = {}

    for card_name in range(2, 11):
        card_points[f'{card_name}'] = card_name
    for card_name in ('валет', 'дама', 'король'):
        card_points[f'{card_name}'] = 10
    card_points['туз'] = choice([1,11])

    return card_points[splited_card[0]]

deck = get_deck()
for _ in range(20):
    my_card = deck.pop()
    points = get_card_points(my_card)
    print(f'Вам выпала карта {my_card}, очки {points}')



your_points = 0
dealer_points = 0
move = 1
more = 'да'

while more == 'да':

    dealer_card = cards.pop()
    dealer_points += dealer_card

    your_cards = []
    
    if move == 1:
        for i in range(2):
            your_card = cards.pop()
            your_cards.append(your_card)
            your_points += your_card
    else:
        your_card = cards.pop()
        your_cards.append(your_card)
        your_points += your_card

    print(f'''
    ===========
    ОЧКИ:
    Крупье: {dealer_points}
    Вы: {your_points}
    ===========
    ''')    
    if move == 1:
        print(f'Вам выпали карты номиналом {your_cards[0]} и {your_cards[1]}')
    else:
        print(f'Вам выпала карта номиналом {your_cards[0]}')
    
    if your_points == 21 or dealer_points == 21:
        if your_points == 21 and dealer_points:
            pass
    
    more = input('Ещё? да или нет\n')
    move +=1

