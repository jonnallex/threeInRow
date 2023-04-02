import random

symbols = ['O', 'X', 'Y']
size = 5
score = 10  # начальное количество очков


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

# Функция запроса координат и проверки их корректности
def get_coords():
    while True:
        coords = input('Введите координаты (например, A1): ').strip().upper()
        if len(coords) != 2 or coords[0] not in 'ABCDE' or not coords[1].isdigit() or int(coords[1]) < 1 or int(coords[1]) > 5:
            print('Координаты введены некорректно, попробуйте снова')
        else:
            return coords


score = 10
while score != 0 and score < 50:
    field = create_field()  # создаем поле
    print(f'Очки: {score}')
    print_field(field)  # выводим его на экран

    while True:
        coords1 = get_coords() # получаем координаты первой фигуры
        i1, j1 = int(coords1[1])-1, 'ABCDE'.index(coords1[0])
        coords2 = get_coords() # получаем координаты второй фигуры
        i2, j2 = int(coords2[1])-1, 'ABCDE'.index(coords2[0])

        # проверяем, что координаты отличаются и фигуры можно поменять местами
        if coords1 != coords2 and ((abs(i1-i2) == 1 and j1 == j2) or (abs(j1-j2) == 1 and i1 == i2)):
            field[i1][j1], field[i2][j2] = field[i2][j2], field[i1][j1] # меняем фигуры местами


            # ищем и удаляем совпадения
            for i in range(size):
                for j in range(size):
                    if j < size-2 and field[i][j] == field[i][j+1] == field[i][j+2]:
                        score += 10
                        field = create_field()
                        # field[i][j], field[i][j+1], field[i][j+2] = '', '', ''


                    if i < size-2 and field[i][j] == field[i+1][j] == field[i+2][j]:
                        score += 10
                        field = create_field()
                        # field[i][j], field[i+1][j], field[i+2][j] = '', '', ''


        print(f'Очки: {score}')
        print_field(field) # выводим измененное поле на экран

        # если больше нет фигур для совпадения, выходим из цикла
        if all(not symbol for row in field for symbol in row):
            print('Игра окончена!')
            break

    else:
        print('Координаты введены некорректно, попробуйте снова')
