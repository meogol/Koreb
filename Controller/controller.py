from Taker.api_core.test import test_request, test_neuro
from Controller.traffic_generator.trafficGenerator import TrafficGenerator
from Controller.cash.commandCache import CommandCache

GOOD_LENTH = 70

class Controller:

    def __init__(self):
        self.improved_cache = test_request(True)                    #Заглушка кэша
        self.trafficGen = TrafficGenerator()                        #Заглушка трафика
        ip, self.traffic = self.trafficGen.get_ip_and_command()
        self.cache_predict = dict()                                 #Доп. кэш от нейронки
        self.command_cache = CommandCache()

    def analyze_package(self):
        com = self.compressed()
        if len(com) > GOOD_LENTH:
            self.run_neuro(5)

    def compressed(self):                                           #Возвращает пережатый list
        ip, com = self.trafficGen.get_ip_and_command()
        i = 0
        while i < len(self.improved_cache):
            while str(self.improved_cache[i]).strip('[]') in str(com).strip('[]'):
                j = 0
                change = False
                while j < len(com) and change == False:
                    k = 0
                    change = True
                    while k < len(self.improved_cache[i]):
                        if com[j + k] != self.improved_cache[i][k]:
                            change = False
                        k += 1
                    if change:
                        com[j] = i
                        for l in range(len(self.improved_cache[i]) - 1):
                            com.pop(j + 1)
                    j += 1
            i += 1
        return com

    def run_neuro(self, new_cache_count):
        self.cache_predict = test_neuro(new_cache_count, self.traffic)
        self.command_cache.append_to_cash(self.cache_predict)


    def send_data(self):
        pass

    def upgrade_taker(self):
        pass

    def update_cache(self):
        pass


if __name__ == '__main__':
    controller = Controller()
    controller.analyze_package()

