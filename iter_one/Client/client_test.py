import requests

from iter_one.Controller.traffic_generator.trafficGenerator import TrafficGenerator



def send_server_pakage(pkg, ip="15"):
    r = requests.post("http://127.0.0.1:5000/post_server_pkg/", data={'ip': ip, 'pkg': pkg})
    print(r)
    return 1


def send_taker_pakage(pkg, ip="15"):
    r = requests.post("http://127.0.0.1:5000/post_taker_pkg/", data={'ip': ip, 'pkg': pkg})
    print(r)
    return 1


if __name__ == '__main__':

    trafficGen = TrafficGenerator()
    ip, traffic = trafficGen.get_ip_and_command()
    send_taker_pakage(traffic)