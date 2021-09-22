from deap import base
from deap import creator
from deap import tools
from keras.utils.np_utils import to_categorical
from keras_preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer

import algelitism
import random
import matplotlib.pyplot as plt
import numpy as np

import ns
from Taker.graphCore.get_branch_back_recoursive_algorithm import GiveBranchsBack
from Taker.graphCore.graph_generator import GraphGenerator
from Controller.traffic_generator.trafficGenerator import TrafficGenerator

network = ns.model
tg = traf_gen = TrafficGenerator()
graph_gen = GraphGenerator()
give_me_branches = GiveBranchsBack()
tokenizer = Tokenizer(num_words=9, lower=True, split=' ', filters='!"#$%&()*+,./:;<=>?@[\\]^_`{|}~\t\n',
                      char_level=False)
tokenizer.fit_on_texts(['up down left right up-left up-right down-left down-right'])
RANDOM_SEED = 42

NEURONS_IN_LAYERS = [4, 1]  # распределение числа нейронов по слоям (первое значение - число входов)

LENGTH_CHROM = 1958504  # длина хромосомы, подлежащей оптимизации
LOW = -1.0
UP = 1.0
ETA = 20

# константы генетического алгоритма
POPULATION_SIZE = 20  # количество индивидуумов в популяции
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
    totalReward = 0

    set_weights(individual)

    ip, command = tg.get_ip_and_command()

    level = 0
    for item in command:
        graph_gen.create_command(ip, item, level)
        level += 1
        number, value = training_ai(graph_gen.command_list)

        lines = give_me_branches.give_branchs_back(graph_gen.graph.graph_array[0])

        if len(lines) < number:
            totalReward -= 10000

            print(str(totalReward) + "\t" + str(value))
            return totalReward,

        if lines[number] == command:
            totalReward += 100

            print(str(totalReward) + "\t" + str(value))
            return totalReward,
        else:
            totalReward -= 1

    graph_gen.command_list.clear()

    print(str(totalReward) + "\t" + str(value))

    return totalReward,


def set_weights(individual):
    s = []
    s.append(np.array([individual[:1152]]).reshape(9, 128))
    s.append(np.array(individual[1152:66688]).reshape(128, 512))
    s.append(np.array([individual[66688:132224]]).reshape(128, 512))
    s.append(np.array(individual[132224:132736]).reshape(512))
    s.append(np.array([individual[132736:394880]]).reshape(128, 2048))
    s.append(np.array(individual[394880:1443456]).reshape(512, 2048))
    s.append(np.array(individual[1443456:1445504]).reshape(2048, ))
    s.append(np.array(individual[1445504:1957504]).reshape(512, 1000))
    s.append(np.array([individual[1957504:1958504]]).reshape(1000, ))

    network.set_weights(s)


def training_ai(commands):
    text = ""
    for a in commands:  # на этом костыле держится нс =)
        text += a + " "

    data = tokenizer.texts_to_sequences([text])

    categorical_data = to_categorical(data[0], num_classes=9)
    data_pad = pad_sequences(categorical_data, maxlen=100)

    res_pred = network.predict(data_pad)

    print(len(res_pred[-1]))

    number = np.argmax(res_pred[-1])
    value = res_pred[-1][number]

    return number, value


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
