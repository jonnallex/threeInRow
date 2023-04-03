import random

symbols = ['O', 'X', 'Y']
size = 5
score = 10
maxScore = 70


def create_field():
    field = [['', '', '', '', ''] for _ in range(5)]

    for i in range(size):
        for j in range(size):
            while True:
                symbol = random.choice(symbols)
                # check that there will not be three identical symbols in a row horizontally and vertically
                if not ((i >= 2 and field[i - 1][j] == field[i - 2][j] == symbol) or (
                        j >= 2 and field[i][j - 1] == field[i][j - 2] == symbol)):
                    field[i][j] = symbol
                    break
    return field


def print_field(field):
    print('   | A  B  C  D  E')
    print(' -----------------')
    for i in range(size):
        print(f'{i + 1}  | ', end='')
        for j in range(size):
            print(field[i][j] + ' ', end=' ')
        print()


def get_coords(coords_position):
    while True:
        coords = input('Enter ' + coords_position + ' coords (for example: A1): ').strip().upper()
        if len(coords) != 2 or coords[0] not in 'ABCDE' or not coords[1].isdigit() or int(coords[1]) < 1 or int(
                coords[1]) > 5:
            print('Coordinates entered incorrectly, try again')
        else:
            return coords


def process_coords(coords):
    return int(coords[1]) - 1, 'ABCDE'.index(coords[0])


def swap(field, score, coords1, coords2, i1, j1, i2, j2):
    # check that the coordinates are different and the shapes can be swapped
    if coords1 != coords2 and ((abs(i1 - i2) == 1 and j1 == j2) or (abs(j1 - j2) == 1 and i1 == i2)):
        field[i1][j1], field[i2][j2] = field[i2][j2], field[i1][j1]  # swap the characters

        for i in range(size):
            for j in range(size):
                if j < size - 2 and field[i][j] == field[i][j + 1] == field[i][j + 2]:
                    score += 10
                    field = create_field()

                if i < size - 2 and field[i][j] == field[i + 1][j] == field[i + 2][j]:
                    score += 10
                    field = create_field()

    return field, score


field = create_field()
print('Game started!')
print(f'     ╓           ╕\n       Score: {score}\n     ╘           ╛\n')
print_field(field)

while True:
    coords1 = get_coords('first')
    i1, j1 = process_coords(coords1)
    coords2 = get_coords('second')
    i2, j2 = process_coords(coords2)

    field, score = swap(field, score, coords1, coords2, i1, j1, i2, j2)

    print(f'\n     ╓           ╕\n       Score: {score}\n     ╘           ╛\n')
    print_field(field)

    if score >= maxScore:
        print('You win!')
        break
