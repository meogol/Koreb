'''

Class generates complicated lists of commands and writes it into "plots" dictionary key-value
from list of basic commands (command_list), than throws it into neuro network by call

'''

import random

#list of basic commands
command_list = ['up', 'down', 'left', 'right', 'up-left', 'up-right', 'down-left', 'down-right']

first_ip = list()
second_ip = list()
third_ip = list()
forth_ip = list()
fifth_ip = list()
ip = list()

ip = ['192.168.1.1', '192.168.1.0', '192.168.0.1', '192.168.0.0', '192.168.0.2']


#first time filling lists of commands
def randomize_lists():
    for item in range(100):
        first_ip.append(random.choice(command_list))
        second_ip.append(random.choice(command_list))
        third_ip.append(random.choice(command_list))
        forth_ip.append(random.choice(command_list))
        fifth_ip.append(random.choice(command_list))


#function of rerandomizing certain list of commands
def randomize_needed_list(list_name):
    for item in range(100):
        list_name[item] = random.choice(command_list)


randomize_lists()


randomize_needed_list(first_ip)

# dictionary of ip adresses and lists of randomized commands to each adress with 100 elements length
plots = {'192.168.1.1': [first_ip],
         '192.168.1.0': [second_ip],
         '192.168.0.1': [third_ip],
         '192.168.0.0': [forth_ip],
         '192.168.0.2': [fifth_ip]
         }


# function that will send to neuron network ip of final user and command to it
def get_ip_and_command():
    ip_to_send = random.choice(ip)
    if ip_to_send == '192.168.1.1':
        command_to_send = fifth_ip
    else:
        if ip_to_send == '192.168.1.0':
            command_to_send = second_ip
        else:
            if ip_to_send == '192.168.0.1':
                command_to_send = third_ip
            else:
                if ip_to_send == '192.168.0.0':
                    command_to_send = forth_ip
                else:
                    if ip_to_send == '192.168.0.2':
                        command_to_send = fifth_ip

    return ip_to_send, command_to_send
