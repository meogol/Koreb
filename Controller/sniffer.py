from Controller.traffic_generator.trafficGenerator import TrafficGenerator


class Sniffer:
    def __init__(self):
        self.traffgen = TrafficGenerator()

    def get_ip_command(self):
        return self.traffgen.get_ip_and_command
