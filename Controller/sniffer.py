from Controller.controller import Controller
from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from flask import Flask, request
from flask_cors import CORS


class Sniffer:

    def __init__(self):
        self.traffgen = TrafficGenerator()
        self.control = Controller()

    def get_ip_command(self):
        return self.traffgen.get_ip_and_command()
    """
    Sends bytedata of one package to controller
    """
    def send_command_to_controller(self, com):
        self.control.analyze_package(com)

if __name__ == '__main__':
    control = Controller()
    snif = Sniffer()
    while True:
        ip, com = snif.get_ip_command()
        control.analyze_package(com)
