from scapy.all import *


class TrafficClassification():

    @staticmethod
    def ip_and_pkg_from_traffic():
        data = []
        data = rdpcap("TrafficForKoreb.pcapng")

        print()
        print(data)
        print()

        ip_buffer = 'a'
        data_buffer = 'b'
        counter = 0
        data_list = [['0'] * 2 for i in range(len(data))]

        for item in data:
            print(item.payload)
            # item.copy_field_value('load', data_buffer)
            data_list[counter][0] = ip_buffer
            data_list[counter][1] = data_buffer
            counter += 1
        print()
        print(data_list[0][0])
        print()
        print(data_list[0][1])


if __name__ == '__main__':
    TrafficClassification.ip_and_pkg_from_traffic()