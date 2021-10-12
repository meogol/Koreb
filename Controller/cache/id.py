
def convert_to_36(num):
    new_36_id = ""
    degree = 0

    while num >= 36**degree:
        degree += 1

    while degree > 0:
        degree -= 1
        div = num//(36**degree)
        num -= div*(36**degree)

        if div == 0:
            new_36_id += "0"
        if div == 1:
            new_36_id += "1"
        if div == 2:
            new_36_id += "2"
        if div == 3:
            new_36_id += "3"
        if div == 4:
            new_36_id += "4"
        if div == 5:
            new_36_id += "5"
        if div == 6:
            new_36_id += "6"
        if div == 7:
            new_36_id += "7"
        if div == 8:
            new_36_id += "8"
        if div == 9:
            new_36_id += "9"
        if div == 10:
            new_36_id += "a"
        if div == 11:
            new_36_id += "b"
        if div == 12:
            new_36_id += "c"
        if div == 13:
            new_36_id += "d"
        if div == 14:
            new_36_id += "e"
        if div == 15:
            new_36_id += "f"
        if div == 16:
            new_36_id += "g"
        if div == 17:
            new_36_id += "h"
        if div == 18:
            new_36_id += "i"
        if div == 19:
            new_36_id += "j"
        if div == 20:
            new_36_id += "k"
        if div == 21:
            new_36_id += "l"
        if div == 22:
            new_36_id += "m"
        if div == 23:
            new_36_id += "n"
        if div == 24:
            new_36_id += "o"
        if div == 25:
            new_36_id += "p"
        if div == 26:
            new_36_id += "q"
        if div == 27:
            new_36_id += "r"
        if div == 28:
            new_36_id += "s"
        if div == 29:
            new_36_id += "t"
        if div == 30:
            new_36_id += "u"
        if div == 31:
            new_36_id += "v"
        if div == 32:
            new_36_id += "w"
        if div == 33:
            new_36_id += "x"
        if div == 34:
            new_36_id += "y"
        if div == 35:
            new_36_id += "z"

    return new_36_id

if __name__ == '__main__':
    print(convert_to_36(129))