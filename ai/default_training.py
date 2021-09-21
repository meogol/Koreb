import numpy as np
from keras.utils.np_utils import to_categorical
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer

from graphCore.get_branch_back_recoursive_algorithm import GiveBranchsBack
from graphCore.graph_generator import GraphGenerator
from traffic_generator.trafficGenerator import TrafficGenerator
from keras import Sequential
from keras.layers import GRU, Dense, Embedding, Flatten, Reshape, LSTM

traf_gen = TrafficGenerator()
graph = GraphGenerator()
give_me_branches = GiveBranchsBack()
tokenizer = Tokenizer(num_words=9, lower=True, split=' ', filters='!"#$%&()*+,./:;<=>?@[\\]^_`{|}~\t\n',
                      char_level=False)
tokenizer.fit_on_texts(['up down left right up-left up-right down-left down-right'])

model = Sequential()
model.add(Embedding(9, 128, input_length=100))
model.add(LSTM(128, return_sequences=True))
model.add(LSTM(512))
model.add(Dense(1000, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

for a in range(100000):
    graph.run_graph()

lines = list()
for item in graph.graph.graph_array:
    res = give_me_branches.give_branchs_back(item)
    lines.extend(res)

c = len(lines)

x = list()
y = list()
for item in lines:
    for i in range(1, 11):
        text = ""
        for a in item[:i]:  # на этом костыле держится нс =)
            text += a + " "
        data = tokenizer.texts_to_sequences([text])
        # categorical_data = to_categorical(data[0], num_classes=9)
        data_pad = pad_sequences(data, maxlen=100)
        x.append(np.array(data_pad))

        text = ""
        for a in item:  # на этом костыле держится нс =)
            text += a + " "
        data1 = tokenizer.texts_to_sequences([text])
        # categorical_data = to_categorical(data1[0], num_classes=9)
        data_pad = pad_sequences(data1, maxlen=100)
        y.append(np.array(data_pad))

x = np.array(x)
y = np.array(y)

indeces = np.random.choice(x.shape[0], size=x.shape[0], replace=False)
x = x[indeces]
y = y[indeces]

history = model.fit(x, y, batch_size=200, epochs=50, validation_split=0.3)
print(history)
