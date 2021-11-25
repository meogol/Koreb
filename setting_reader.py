import configparser

setting_res = {'pkg_type': 'tcp', 'ip': 'localhost', 'port': '7777', 'host': '192.168.0.103', 'face': 'Беспроводная сеть',
               'server_ip': 'server_ip', 'gateway_ip': 'gateway_ip'}


def setting_read():
    config = configparser.ConfigParser()
    try:
        config.read("settings.ini")

        if config is not None:

            check(config, setting_res, "pkg_type")
            check(config, setting_res, "ip")
            check(config, setting_res, "port")
            check(config, setting_res, "host")
            check(config, setting_res, "face")

            check(config, setting_res, "server_ip")
            check(config, setting_res, "gateway_ip")

    except KeyError:
        print('File dose not exist!')


def check(config, result, field):
    try:
        result[field] = config["setting"][field]
    except KeyError:
        print(field + " is not specified and it is set to the default value")


if __name__ == '__main__':
    setting_read()
    print(setting_res)
