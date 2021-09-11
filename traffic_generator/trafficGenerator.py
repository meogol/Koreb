import random

from traffic_generator.traficGeneratorCore import GeneratorCore


class TrafficGenerator():
    def __init__(self):
        self.gen_core = GeneratorCore()
        self.gen_core.randomize_inner_lists()
        self.buffer_for_random_command = list()


    def get_ip_and_command(self):
        """
        возвращает случайный кортеж вида (ip, [массив команд]) из заранее сгенерированного dict
        :return: returns random cortaige type of (ip,list of commands)
        """
        ip_to_send = random.choice(self.gen_core.ip)
        if ip_to_send == '192.168.1.1':
            self.buffer_for_random_command = self.gen_core.plots['192.168.1.1']
            command_to_send = random.choice(self.buffer_for_random_command)
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
    print(traf_gen.get_ip_and_command())
    a=1
