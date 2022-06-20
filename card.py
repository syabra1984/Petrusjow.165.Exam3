# Напишите функцию, которая будет принимать номер кредитной карты и показывать только последние 4 цифры.\
# Остальные цифры должны заменяться звездочками.
def kredit_card(card):
    card_show = ''
    n = len(card)
    for i in range(n-4):
        card_show += '*'
    for i in range(4):
        card_show += card[n-4+i]
    print('Номер Вашей кредитной карты: ',card_show)
card = input('Введите номер кредитной карты (16цифр): ')
if card.isdigit() and len(card)==16:
    kredit_card(card)
else:
    print('Введён неверный номер карты')
