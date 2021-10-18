import numpy as np
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
from tensorflow import keras

from iter_one.Taker.graphCore.get_branch_back_recoursive_algorithm import GiveBranchsBack
from iter_one.Taker.graphCore.graph_generator import GraphGenerator
from iter_one.Controller.traffic_generator.trafficGenerator import TrafficGenerator
from keras import Sequential
from keras.layers import Dense, Embedding, LSTM

traf_gen = TrafficGenerator()
graph = GraphGenerator()
give_me_branches = GiveBranchsBack()
tokenizer = Tokenizer(num_words=9, lower=True, split=' ', filters='!"#$%&()*+,./:;<=>?@[\\]^_`{|}~\t\n',
                      char_level=False)
tokenizer.fit_on_texts(['up down left right up-left up-right down-left down-right'])

model = Sequential()
model.add(Embedding(9, 128, input_length=100))
model.add(LSTM(128, activation='tanh', return_sequences=True))
model.add(LSTM(512, activation='tanh'))
model.add(Dense(4200, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

# for a in range(10000):
#     graph.run_graph()
#
# lines = list()
# for item in graph.graph.graph_array:
#     res = give_me_branches.give_branchs_back(item)
#     lines.extend(res)
traf_gen = TrafficGenerator()

c = 10000

x = list()
y = list()
x_test = list()
y_test = list()
com_list = list()
ii = 0

for item in range(c):
    ip, com = traf_gen.get_ip_and_command()

    for i in range(1, 21):
        text = ""
        for a in com[:i]:  # на этом костыле держится нс =)
            text += a + " "
        data = tokenizer.texts_to_sequences([text])
        # categorical_data = to_categorical(data[0], num_classes=9)
        data_pad = pad_sequences(data, maxlen=100)
        x.append(data_pad[0])

        if com_list.count(com) > 0:
            y.append(com_list.index(com))
        else:
            com_list.append(com)
            y.append(ii)
            ii += 1

for item in range(1000):
    ip, com = traf_gen.get_ip_and_command()

    for i in range(1, 21):
        text = ""
        for a in com[:i]:  # на этом костыле держится нс =)
            text += a + " "
        data = tokenizer.texts_to_sequences([text])
        # categorical_data = to_categorical(data[0], num_classes=9)
        data_pad = pad_sequences(data, maxlen=100)
        x_test.append(data_pad[0])

        if com_list.count(com) > 0:
            y_test.append(com_list.index(com))
        else:
            com_list.append(com)
            y_test.append(ii)
            ii += 1

x = np.array(x)
y = np.array(y)
y = keras.utils.to_categorical(y, 4200)

x_test = np.array(x_test)
y_test = np.array(y_test)
y_test = keras.utils.to_categorical(y_test, 4200)

indeces = np.random.choice(x.shape[0], size=x.shape[0], replace=False)
x = x[indeces]
y = y[indeces]

indeces = np.random.choice(x_test.shape[0], size=x_test.shape[0], replace=False)
x_test = x_test[indeces]
y_test = y_test[indeces]

history = model.fit(x, y, batch_size=200, epochs=10, validation_split=0.2)
model.evaluate(x_test, y_test)
print(history)
print(model.evaluate(x, y))

model.save("first_model")
