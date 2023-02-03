import random
global current_player

def switch_player():
    global current_player
    if current_player == one_player:
        current_player = two_player
    else:
        current_player = one_player

def choice_player():
    if random.randint(0,2) == 0:
        first = one_player
    else:
        first = two_player
    return first

print('\nИгра "Конфеты".') 
print('\nУсловия игры, на столе лежит N конфкт, за раз вы можете взять не более 28 конфет, '
'\nвыигрывает тот, кто возьмет последнюю конфету')

one_player = input('\nПервый игрок, представьтесь: ')
print('Привет, ' + one_player)
two_player = 'Clever bot'
print(f'Меня зовут {two_player}. Я заберу все твои конфеты!)')

count = int(input('\nСколько конфет на столе? ')) 

current_player = choice_player()

print('\nПервым ходит ' + current_player)

while count > 28:
    if current_player == one_player:
        candy = int(input('\n' + current_player + ', cколько конфет возьмешь? '))
        while candy > 28 or candy < 1:
            candy = int(input('\n' + current_player + ', возьми от 1 до 28 конфет. Сколько возьмешь? '))
    else:
        candy = count % 29
        print(f'{two_player} взял {candy} конфет.')
    count -= candy
    print(f'На столе осталось {count} конфет.')
    switch_player()

print('\n' + current_player + ', поздравляем ты победил!!! Ура!!!')