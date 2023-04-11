import numpy as np
import tensorflow as tf

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

training_data = np.array([
    [
        [3, 3, 0, 0, 0],
        [0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],

])

training_data1 = np.array([
    [
        [0, 0, 0, 0, 0],
        [0, 3, 3, 0, 0],
        [3, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],
])

training_data= np.concatenate((training_data, training_data1), axis=0)


training_labels_start = np.zeros((1, 25))
training_labels_start[0, 7] = 1

training_labels_start1 = np.zeros((1, 25))
training_labels_start1[0, 10] = 1

training_labels_start = np.concatenate((training_labels_start, training_labels_start1), axis=0)

training_labels_end = np.zeros((1, 25))
training_labels_end[0, 2] = 1

training_labels_end1 = np.zeros((1, 25))
training_labels_end1[0, 5] = 1

training_labels_end = np.concatenate((training_labels_end, training_labels_end1), axis=0)

print(training_data)
print(training_labels_start)
print(training_labels_end)

def predict_move(board_state):
    prediction = model.predict(np.array(board_state))
    start_position = np.argmax(prediction[0])
    end_position = np.argmax(prediction[1])
    return start_position, end_position


model.fit(
    training_data,
    [training_labels_start, training_labels_end],
    epochs=40, batch_size=32
)

test_board = np.array([
    [
        [2, 2, 0, 0, 0],
        [0, 0, 2, 0, 0],
        [2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
])
print(predict_move(test_board))
