from iter_two.core.server.server import Server
from setting_reader import setting_read, setting_res

if __name__ == '__main__':
    setting_read()

    server = Server(socket_type="server", host=str(setting_res.get('host')), port=int(setting_res.get('port')), ip=str(setting_res.get('taker_ip')))
    server.init_listener()

    input("End")
