import copy

from deap import base
from deap import creator
from deap import tools
from keras.applications.densenet import layers
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
import random
import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras

from iter_one.Controller.ai import algelitism

text = ""
with open('byteData.txt', 'r') as fp:
    text = fp.readlines()
fp.close()

inputs = keras.Input(shape=4000, name='digits')
x = layers.Dense(20, activation='relu', name='dense_1')(inputs)
outputs = layers.Dense(4000, activation='relu', name='predictions')(x)

model = keras.Model(inputs=inputs, outputs=outputs)
# Укажем конфигурацию обучения (оптимизатор, функция потерь, метрики)
model.compile(optimizer=keras.optimizers.RMSprop(),  # Optimizer
              loss='sparse_categorical_crossentropy',
              metrics=['sparse_categorical_accuracy'])
model.summary()

network = model
tokenizer = Tokenizer(num_words=9, char_level=True)
tokenizer.fit_on_texts(text)
RANDOM_SEED = 42

LENGTH_CHROM = 164020  # длина хромосомы, подлежащей оптимизации
LOW = -1.0
UP = 1.0
ETA = 20

# константы генетического алгоритма
POPULATION_SIZE = 10  # количество индивидуумов в популяции
P_CROSSOVER = 0.9  # вероятность скрещивания
P_MUTATION = 0.1  # вероятность мутации индивидуума
MAX_GENERATIONS = 5000  # максимальное количество поколений
HALL_OF_FAME_SIZE = 2

hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("randomWeight", random.uniform, -1.0, 1.0)
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.randomWeight, LENGTH_CHROM)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)

population = toolbox.populationCreator(n=POPULATION_SIZE)


def getScore(individual):
    set_weights(individual)

    totalReward = training_ai()

    print(totalReward)

    return totalReward,


def set_weights(individual):
    s = []

    a = network.get_weights()

    s.append(np.array(individual[:80000]).reshape(4000, 20))
    s.append(np.array(individual[80000:80020]).reshape(20, ))
    s.append(np.array(individual[80020:160020]).reshape(20, 4000))
    s.append(np.array(individual[160020:164020]).reshape(4000, ))

    network.set_weights(s)


def training_ai():
    global text
    totalReward = 0
    index = 0

    for line in text:
        data = tokenizer.texts_to_sequences([line])

        data_pad = pad_sequences(data, maxlen=4000)

        res_pred = network.predict(data_pad)

        index_non_zero = np.unique(np.where(res_pred != 0))

        if len(res_pred) > len(line):
            totalReward -= 1000
            continue

        res = list()
        first = 0
        last = -1
        for item in index_non_zero:
            if last + 1 == item :
                last = item
                continue

            if last + 1 - first < 3:
                totalReward -= 10
                continue

            res.append(line[first:last + 1])
            first = item
            last = item

        for i in range(10):
            com = copy.deepcopy(text[index-i])
            i_com = 0
            for cache_item in res:
                if com.find(cache_item) != -1:
                    cache_replace = i_com
                    k = len(cache_item)
                    replaceable = com[com.find(cache_item):com.find(cache_item) + k]
                    com = com.replace(replaceable, str(cache_replace))

            res_reward = len(text[index-i]) - len(com)
            totalReward+=res_reward
        index += 1
    return totalReward

toolbox.register("evaluate", getScore)
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("mate", tools.cxSimulatedBinaryBounded, low=LOW, up=UP, eta=ETA)
toolbox.register("mutate", tools.mutPolynomialBounded, low=LOW, up=UP, eta=ETA, indpb=1.0 / LENGTH_CHROM)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("max", np.max)
stats.register("avg", np.mean)

population, logbook = algelitism.eaSimpleElitism(population, toolbox,
                                                 cxpb=P_CROSSOVER,
                                                 mutpb=P_MUTATION,
                                                 ngen=MAX_GENERATIONS,
                                                 halloffame=hof,
                                                 stats=stats,
                                                 verbose=True)

maxFitnessValues, meanFitnessValues = logbook.select("max", "avg")

best = hof.items[0]
print(best)

plt.plot(maxFitnessValues, color='red')
plt.plot(meanFitnessValues, color='green')
plt.xlabel('Поколение')
plt.ylabel('Макс/средняя приспособленность')
plt.title('Зависимость максимальной и средней приспособленности от поколения')
plt.show()
