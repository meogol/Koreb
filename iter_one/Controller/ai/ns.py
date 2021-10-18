from keras import Sequential
from keras.layers import GRU, Dense, Embedding, Flatten, Reshape, LSTM, Dropout

model = Sequential()
model.add(Embedding(9, 128, input_length=100))
model.add(LSTM(128, activation='tanh', return_sequences=True))
model.add(LSTM(512, activation='tanh'))
model.add(Dropout())
model.add(Dense(1000, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
