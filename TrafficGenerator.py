import random

comand_list = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']

first_ip = list()
second_ip = list()
third_ip = list()
forth_ip = list()
fifth_ip = list()

for item in range(100):
    first_ip.append(random.choice(comand_list))
    second_ip.append(random.choice(comand_list))
    third_ip.append(random.choice(comand_list))
    forth_ip.append(random.choice(comand_list))
    fifth_ip.append(random.choice(comand_list))

plots = {'192.168'}
