
def convert_to_36(num):
    new_36_id = ""
    degree = 0

    if num != 0:
        while num >= 36**degree:
            degree += 1
    elif num == 0:
        degree = 1

    while degree > 0:
        degree -= 1
        div = num//(36**degree)
        num -= div*(36**degree)

        if div == 0:
            new_36_id += "0"
        elif div == 1:
            new_36_id += "1"
        elif div == 2:
            new_36_id += "2"
        elif div == 3:
            new_36_id += "3"
        elif div == 4:
            new_36_id += "4"
        elif div == 5:
            new_36_id += "5"
        elif div == 6:
            new_36_id += "6"
        elif div == 7:
            new_36_id += "7"
        elif div == 8:
            new_36_id += "8"
        elif div == 9:
            new_36_id += "9"
        elif div == 10:
            new_36_id += "a"
        elif div == 11:
            new_36_id += "b"
        elif div == 12:
            new_36_id += "c"
        elif div == 13:
            new_36_id += "d"
        elif div == 14:
            new_36_id += "e"
        elif div == 15:
            new_36_id += "f"
        elif div == 16:
            new_36_id += "g"
        elif div == 17:
            new_36_id += "h"
        elif div == 18:
            new_36_id += "i"
        elif div == 19:
            new_36_id += "j"
        elif div == 20:
            new_36_id += "k"
        elif div == 21:
            new_36_id += "l"
        elif div == 22:
            new_36_id += "m"
        elif div == 23:
            new_36_id += "n"
        elif div == 24:
            new_36_id += "o"
        elif div == 25:
            new_36_id += "p"
        elif div == 26:
            new_36_id += "q"
        elif div == 27:
            new_36_id += "r"
        elif div == 28:
            new_36_id += "s"
        elif div == 29:
            new_36_id += "t"
        elif div == 30:
            new_36_id += "u"
        elif div == 31:
            new_36_id += "v"
        elif div == 32:
            new_36_id += "w"
        elif div == 33:
            new_36_id += "x"
        elif div == 34:
            new_36_id += "y"
        elif div == 35:
            new_36_id += "z"

    return new_36_id
