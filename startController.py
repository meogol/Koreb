from iter_two.core.snif.sniffer import Sniffer
from setting_reader import setting_read, setting_res

if __name__ == '__main__':
    setting_read()

    sniffer = Sniffer()
    sniffer.traff_file_read(pkg=setting_res.get("pkg_type"), ip=setting_res.get("controller_ip"), port=setting_res.get("controller_port"))
