import configparser


def setting_read():
    config = configparser.ConfigParser()
    config.read("settings.ini")

    if config is not None:
        result = {'pkg_type': '"TCP"', 'ip': '"192.168.0.103"', 'port': '"7777"', 'host': '"host"'}

        check(config, result, "pkg_type")
        check(config, result, "ip")
        check(config, result, "port")
        check(config, result, "host")
        return result
    else:
        print('File dose not exist!')


def check(config, result, field):
    try:
        config["setting"][field]
        result[field] = config["setting"][field]
    except KeyError:
        print(field + " is not specified and it is set to the default value")


if __name__ == '__main__':
    u = setting_read()
    print(u)
