import random

#
# ------------------------------------------
#
#
# ------------------------------------------
#
#

symbols = ['O', 'X', 'Y']
size = 5

def create_field():
    field = [['', '', '', '', ''] for _ in range(5)] # создаем пустое поле 5x5

    for i in range(size):
        for j in range(size):
            while True:
                symbol = random.choice(symbols) # выбираем случайный символ из списка
                # проверяем, что по горизонтали и вертикали не будет трех одинаковых символов подряд
                if not ((i >= 2 and field[i-1][j] == field[i-2][j] == symbol) or
                        (j >= 2 and field[i][j-1] == field[i][j-2] == symbol)):
                    field[i][j] = symbol
                    break # если символ подходит, выходим из цикла
    return field

# Функция вывода поля на экран
def print_field(field):
    print('  A B C D E')
    for i in range(size):
        print(f'{i+1} ', end='')
        for j in range(size):
            print(field[i][j] + ' ', end='')
        print()
