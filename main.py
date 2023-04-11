import sys
from random import randint
import tensorflow as tf
import numpy as np
import json
import os
import env
import platform

size = 5
score = env.START_SCORE
maxScore = env.MAX_SCORE
plus_score = env.PLUS_SCORE
fail = 0
print_symbols = env.PRINT_SYMBOLS
epoch_count = env.EPOCH_COUNT

def create_field():
    field = np.zeros((5, 5), dtype=int)

    for i in range(size):
        for j in range(size):
            while True:
                symbol = randint(1, 3)
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
            print(print_symbols[int(field[i][j])] + ' ', end=' ')
        print()


def print_score(score):
    print(f'\n  ╒               ╕\n'
          f'     Score: {score}/{maxScore}\n'
          f'  ╘               ╛\n')


def game_over(score):
    if score >= maxScore:
        print(f'You scored: {score} points\nYour fail: {fail} points\nGame over!')
        return True
    return False


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


def get_matrix_element_number(i, j):
    if i < 0 or i >= 5 or j < 0 or j >= 5:
        raise ValueError("Values i and j must be in range from 0 to 4")
    else:
        element_number = i * 5 + j
        return element_number


def check_swap(field, coords1, coords2, i1, j1, i2, j2):
    field2 = np.copy(field)
    check = False

    if coords1 != coords2 and ((abs(i1 - i2) == 1 and j1 == j2) or (abs(j1 - j2) == 1 and i1 == i2)):
        field2[i1][j1], field2[i2][j2] = field2[i2][j2], field2[i1][j1]  # swap the symbols

        for i in range(size):
            for j in range(size):
                if j < size - 2 and field2[i][j] == field2[i][j + 1] == field2[i][j + 2]:
                    check = True
                    break

                if i < size - 2 and field2[i][j] == field2[i + 1][j] == field2[i + 2][j]:
                    check = True
                    break

    return check


def swap(field, coords1, coords2, i1, j1, i2, j2):
    # check that the coordinates are different and the shapes can be swapped

    check = False
    if coords1 != coords2 and ((abs(i1 - i2) == 1 and j1 == j2) or (abs(j1 - j2) == 1 and i1 == i2)):
        field[i1][j1], field[i2][j2] = field[i2][j2], field[i1][j1]  # swap the symbols

        for i in range(size):
            for j in range(size):
                if j < size - 2 and field[i][j] == field[i][j + 1] == field[i][j + 2]:
                    check = True

                if i < size - 2 and field[i][j] == field[i + 1][j] == field[i + 2][j]:
                    check = True
    else:
        print('Wrong move!')

    field = create_field()
    return field, check


def get_training_json(field, start, end):
    return {
        "start": start,
        "end": end,
        "field": json.dumps(field.tolist())
    }


def write_json_to_file(data, file_path=env.FILE_FOR_TRAINING_PATH):

    if platform.system() != 'Windows':
        file_path = os.path.normpath(file_path)

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            file_data = json.load(f)

        file_data.append(data)
        with open(file_path, 'w') as f:
            json.dump(file_data, f, indent=4)
    else:
        with open(file_path, 'w') as f:
            json.dump([data], f, indent=4)


def get_json_from_file(file_path=env.FILE_FOR_TRAINING_PATH):
    with open(file_path, "r") as f:
        json_content = json.load(f)
    return json_content


def get_fields_from_json(json_data):
    return [[np.array(eval(item["field"])) for item in json_data]]


def get_training_labels(json_data, type):
    training_labels = []
    for value in json_data:
        element = value[type]
        arr = np.zeros((1, 25))
        arr[0, element] = 1
        training_labels.append(arr)

    return np.concatenate(training_labels, axis=0)


def predict_move(board_state):
    prediction = model.predict(np.array(board_state))
    start_position = np.argmax(prediction[0])
    end_position = np.argmax(prediction[1])
    return start_position, end_position


def convert_position_to_coordinate(position):
    letters = ['A', 'B', 'C', 'D', 'E']
    numbers = ['1', '2', '3', '4', '5']

    row = position // 5
    col = position % 5

    col_letter = letters[col]
    row_number = numbers[row]

    coordinate = col_letter + row_number
    return coordinate


# ---------------main-function------------------------------------------------------------------------------------------


print('Game started!')
game_type = input('\nChoose game type: \n1. Your gameplay\n2. AI gameplay\n').strip().upper()

if game_type == '1':

    field = create_field()
    while True:
        print_score(score)
        print_field(field)

        coords1 = get_coords('first')
        i1, j1 = process_coords(coords1)
        coords2 = get_coords('second')
        i2, j2 = process_coords(coords2)

        if check_swap(field, coords1, coords2, i1, j1, i2, j2):
            start = get_matrix_element_number(i1, j1)
            end = get_matrix_element_number(i2, j2)
            # print(start, end)
            # coords1 = convert_position_to_coordinate(start)
            # coords2 = convert_position_to_coordinate(end)
            # print([coords1, coords2])
            write_json_to_file(get_training_json(field, start, end))

        field, check = swap(field, coords1, coords2, i1, j1, i2, j2)

        if check:
            score += plus_score
        else:
            fail += 1

        if game_over(score):
            break

elif game_type == '2':

    input_layer = tf.keras.layers.Input(shape=(5, 5))
    flatten_layer = tf.keras.layers.Flatten()(input_layer)
    dense_layer_1 = tf.keras.layers.Dense(128, activation='relu')(flatten_layer)
    dense_layer_2 = tf.keras.layers.Dense(64, activation='relu')(dense_layer_1)
    start_position_output = tf.keras.layers.Dense(25, activation='softmax', name='start')(dense_layer_2)
    end_position_output = tf.keras.layers.Dense(25, activation='softmax', name='end')(dense_layer_2)

    model = tf.keras.Model(inputs=input_layer, outputs=[start_position_output, end_position_output])

    model.compile(optimizer='adam',
                  loss={
                      'start': 'categorical_crossentropy',
                      'end': 'categorical_crossentropy'
                  },
                  metrics={
                      'start': 'accuracy',
                      'end': 'accuracy'
                  },
                  run_eagerly=True)

    json_data = get_json_from_file()
    training_data = np.concatenate(get_fields_from_json(json_data), axis=0)
    training_labels_start = get_training_labels(json_data, 'start')
    training_labels_end = get_training_labels(json_data, 'end')

    model.fit(
        training_data,
        [training_labels_start, training_labels_end],
        epochs=epoch_count, batch_size=32
    )

    field = create_field()
    while True:
        print_score(score)
        print_field(field)

        start_position, end_position = predict_move([field])
        # print([start_position, end_position])

        coords1 = convert_position_to_coordinate(start_position)
        print('First coords: ' + coords1)
        i1, j1 = process_coords(coords1)

        coords2 = convert_position_to_coordinate(end_position)
        print('Second coords: ' + coords2)
        i2, j2 = process_coords(coords2)
        # print([coords1, coords2])

        if check_swap(field, coords1, coords2, i1, j1, i2, j2):
            start = get_matrix_element_number(i1, j1)
            end = get_matrix_element_number(i2, j2)
            write_json_to_file(get_training_json(field, start, end))

        field, check = swap(field, coords1, coords2, i1, j1, i2, j2)

        if check:
            score += plus_score
        else:
            fail += 1

        if game_over(score):
            break
