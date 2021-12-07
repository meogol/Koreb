import configparser
import logging

setting_res = {'pkg_type': 'tcp', 'client_ip': 'localhost', 'port': '7777', 'taker_ip': '192.168.0.106',
               'face': 'Беспроводная сеть', 'server_ip': 'server_ip', 'gateway_ip': 'gateway_ip'}


def setting_read(TO_LOG, TO_CONSOLE):
    config = configparser.ConfigParser()
    try:

        if TO_LOG:
            logging.info("Reading settings...")

        config.read("settings.ini", encoding='UTF-8')

        if config is not None:

            check(config, setting_res, "pkg_type")
            check(config, setting_res, "client_ip")
            check(config, setting_res, "port")
            check(config, setting_res, "taker_ip")
            check(config, setting_res, "face")

            check(config, setting_res, "server_ip")
            check(config, setting_res, "gateway_ip")

        if TO_LOG:
            logging.info("Success!\n")

    except KeyError:
        if TO_LOG:
            logging.exception("File does not exist!\n")
        if TO_CONSOLE:
            print('File does not exist!\n')


def check(config, result, field):
    try:
        result[field] = config["setting"][field]
    except KeyError:
        print(field + " is not specified and it is set to the default value")


if __name__ == '__main__':
    setting_read()
    print(setting_res)
