
def print_len(pkg, msg="", dst="", print_pkg=True):
    if print_pkg:
        print('\n' + str(pkg))
    print(dst + '\n' + msg + str(len(pkg)))