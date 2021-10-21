import serial
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

letter = 'A'
print(ord(letter) - ord('A'))

ser = serial.Serial('COM4', 9600)
data = []
labels = []
LETTERLLEN = 80

model = keras.Sequential([
        layers.Dense(LETTERLLEN*3, activation="relu"),
        layers.Dense(64, activation="relu"),
        layers.Dense(32, activation="relu"),
        layers.Dense(26, activation="softmax"),
    ])

model = keras.models.load_model("model.h5")

model.compile(
    optimizer=keras.optimizers.RMSprop(),
    loss=keras.losses.SparseCategoricalCrossentropy(),
    metrics=[keras.metrics.SparseCategoricalAccuracy()],
)


while True:
    letter = input("What is the letter?\n").strip().upper()[:1]
    labels.append(ord(letter)- ord("A"))
    letter_data = []

    for i in range(LETTERLLEN):
        line = ser.readline()[:-2].decode("utf-8").strip().split()
        # print(line)
        if len(line) == 4:
            l = list(map(int, line[1:]))
            letter_data.extend(l)

    if len(letter_data) < LETTERLLEN*3:
        letter_data.append([0]*(LETTERLLEN*3-len(letter_data)))
        
    data.append(letter_data)

    np_data = np.array(data, dtype = np.float)
    np_labels = np.array(labels, dtype = np.float)

    print("data shape",np_data.shape)
    print("labels shape", np_labels.shape)

    model.fit(np_data, np_labels, batch_size=256, epochs=5)

    print(np_data[-1].reshape((-1, LETTERLLEN*3)).shape)

    pred = model.predict(np.array(np_data[-1].reshape((-1, LETTERLLEN*3))))
    print(chr(ord("A") + np.argmax(pred)))

    np.savetxt("data.csv", np_data, delimiter=',')
    np.savetxt("labels.csv", np_labels, delimiter=',')

    print("letter added")

    model.save('model.h5')

    print("model saved")

ser.close()