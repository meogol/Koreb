from scapy.all import *


class PkgAssembly():

    @staticmethod
    def formation_of_packages():

        data = []
        data = rdpcap("TrafficForKoreb.pcapng")

        print()
        print(data.res)
        print()
        for item in data:
            item.



if __name__ == '__main__':
    PkgAssembly.formation_of_packages()

