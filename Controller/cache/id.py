
def convert_to_19(num):
    new_19_id = ""
    degree = 0

    while num >= 19**degree:
        degree += 1

    while degree > 0:
        degree -= 1
        div = num//(19**degree)
        num -= div*(19**degree)
        if div == 18:
            new_19_id += "z"
        elif(div == 17):
            new_19_id += "y"
        elif(div == 16):
              new_19_id += "w"
        elif(div == 15):
              new_19_id += "v"
        elif(div == 14):
            new_19_id += "u"
        elif(div == 13):
            new_19_id += "t"
        elif(div == 12):
            new_19_id += "s"
        elif(div == 11):
            new_19_id += "r"
        elif(div == 10):
            new_19_id += "q"
        elif(div == 9):
            new_19_id += "p"
        elif(div == 8):
            new_19_id += "o"
        elif(div == 7):
            new_19_id += "n"
        elif(div == 6):
            new_19_id += "m"
        elif(div == 5):
            new_19_id += "l"
        elif(div == 4):
            new_19_id += "k"
        elif(div == 3):
            new_19_id += "j"
        elif(div == 2):
            new_19_id += "i"
        elif(div == 1):
            new_19_id += "h"
        elif(div == 0):
            new_19_id += "g"
    return new_19_id

if __name__ == '__main__':
    print(convert_to_19(76))