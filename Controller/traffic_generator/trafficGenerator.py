import random

from Controller.traffic_generator.traficGeneratorCore import GeneratorCore


class TrafficGenerator():
    def __init__(self):
        self.gen_core = GeneratorCore()
        self.gen_core.randomize_inner_lists()
        self.buffer_for_random_command = list()
        self.buffer_for_transit = list()


    def get_ip_and_command(self):
        """
        возвращает случайный кортеж вида (ip, [массив команд]) из заранее сгенерированного dict
        :return: returns random cortaige type of (ip,list of commands)
        """
        ip_to_send = random.choice(self.gen_core.ip)
        if ip_to_send == '192.168.1.1':
            self.buffer_for_random_command = self.gen_core.plots['192.168.1.1']
            number_of_plots = len(self.buffer_for_random_command)

            random_item = random.randint(0, number_of_plots*100)

            if random_item < number_of_plots*10:                            # в 10% случаев выбор из 25% вариантов
                counter = random.randint(0, round(number_of_plots*0.25))
                self.buffer_for_transit = self.buffer_for_random_command[counter]

            elif random_item < number_of_plots*25:                          # в 15% случаев выбор из 17% вариантов
                counter = random.randint(round(number_of_plots*0.26), round(number_of_plots*0.42))
                self.buffer_for_transit = self.buffer_for_random_command[counter]

            elif random_item < number_of_plots*75:                          # в 50% случаев выбор из 7% вариантов
                counter = random.randint(round(number_of_plots*0.43), round(number_of_plots*0.49))
                self.buffer_for_transit = self.buffer_for_random_command[counter]

            elif random_item < number_of_plots*90:                          # в 15% случаев выбор из 20% вариантов
                counter = random.randint(round(number_of_plots*0.50), round(number_of_plots*0.69))
                self.buffer_for_transit = self.buffer_for_random_command[counter]

            else:                                                             # в 10% случаев выбор из 30% вариантов
                counter = random.randint(round(number_of_plots*0.70), number_of_plots-1)
                self.buffer_for_transit = self.buffer_for_random_command[counter]

            command_to_send = self.buffer_for_transit
        # else:
        #     if ip_to_send == '192.168.1.0':
        #         self.buffer_for_random_command = self.gen_core.plots['192.168.1.0']
        #         command_to_send = random.choice(self.buffer_for_random_command)
        #     else:
        #         if ip_to_send == '192.168.0.1':
        #             self.buffer_for_random_command = self.gen_core.plots['192.168.0.1']
        #             command_to_send = random.choice(self.buffer_for_random_command)
        #         else:
        #             if ip_to_send == '192.168.0.0':
        #                 self.buffer_for_random_command = self.gen_core.plots['192.168.0.0']
        #                 command_to_send = random.choice(self.buffer_for_random_command)
        #             else:
        #                 if ip_to_send == '192.168.0.2':
        #                     self.buffer_for_random_command = self.gen_core.plots['192.168.0.2']
        #                     command_to_send = random.choice(self.buffer_for_random_command)

        return ip_to_send, command_to_send


if __name__ == '__main__':
    traf_gen = TrafficGenerator()
    gen_core = GeneratorCore()

    gen_core.randomize_inner_lists()
    traf_gen.get_ip_and_command()
    a=1
