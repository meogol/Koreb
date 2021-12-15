import configparser
import logging

from logs import print_logs

setting_res = {'pkg_type': 'tcp', 'client_ip': 'localhost', 'port': '7777', 'taker_ip': '192.168.0.106',
               'face': 'Беспроводная сеть', 'server_ip': 'server_ip', 'gateway_ip': 'gateway_ip'}


def setting_read(logs={'to_log':True, 'to_console': False}):
    config = configparser.ConfigParser()
    try:

        print_logs(logs=logs, msg="Reading settings...", log_type="info")

        config.read("settings.ini", encoding='UTF-8')

        if config is not None:

            check(config, setting_res, "pkg_type", logs)
            check(config, setting_res, "client_ip", logs)
            check(config, setting_res, "port", logs)
            check(config, setting_res, "taker_ip", logs)
            check(config, setting_res, "face", logs)

            check(config, setting_res, "server_ip", logs)
            check(config, setting_res, "gateway_ip", logs)

        print_logs(logs=logs, msg="Settings was read successfully!\n", log_type="info")

    except KeyError:
        print_logs(logs=logs, msg="File does not exist!\n", log_type="exception")



def check(config, result, field, logs={'to_log':True, 'to_console': True}):
    try:
        result[field] = config["setting"][field]
    except KeyError:
        print_logs(logs=logs, msg=field + " is not specified and it is set to the default value", log_type="exception")


if __name__ == '__main__':
    setting_read()
    print(setting_res)
