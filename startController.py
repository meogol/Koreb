
from iter_two.core.snif.spoofer import Spoofer
from setting_reader import setting_read, setting_res

if __name__ == '__main__':
    setting_read()

    spoofer = Spoofer()
    spoofer.to_process()
