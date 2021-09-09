import traficGeneratorCore as trafGenCore
import random

class TrafficGenerator():
    def __init__(self):
        pass


    def get_ip_and_command(self):
        """
        :return: returns cortaige type of (ip,lists of commands)
        """
        ip_to_send = random.choice(gen_core.ip)
        if ip_to_send == '192.168.1.1':
            command_to_send = gen_core.plots['192.168.1.1']
        else:
            if ip_to_send == '192.168.1.0':
                command_to_send = gen_core.plots['192.168.1.0']
            else:
                if ip_to_send == '192.168.0.1':
                    command_to_send = gen_core.plots['192.168.0.1']
                else:
                    if ip_to_send == '192.168.0.0':
                        command_to_send = gen_core.plots['192.168.0.0']
                    else:
                        if ip_to_send == '192.168.0.2':
                            command_to_send = gen_core.plots['192.168.0.2']

        return ip_to_send, command_to_send

if __name__ == '__main__':
    traf_gen = TrafficGenerator()
    gen_core = trafGenCore.GeneratorCore()

    gen_core.randomize_inner_lists()
    print(traf_gen.get_ip_and_command())

