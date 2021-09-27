from keras import Sequential
from keras.layers import GRU, Dense, Embedding, Flatten, Reshape, LSTM
from tensorflow import keras

inputs = Embedding(9, 128, input_length=100)
x = LSTM(128, activation='tanh', return_sequences=True)(inputs)
x = LSTM(512, activation='tanh')(x)
outputs = Dense(1000, activation='softmax')(x)
model = keras.Model(inputs, outputs, name="toy_resnet")

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
