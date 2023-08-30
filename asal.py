from simple_colors import *


def main():
    line = int(input("How many lines do you want ? "))
    How_Many(line)


def İs_Prime(numb):
    if numb > 1:
        for i in range(2, int(numb / 2 + 1)):
            if numb % i == 0:
                return False
        else:
            return True
    else:
        return False


def How_Many(Line):
    x = int(input("From which line do you want to start ? "))
    first = x + x * 5
    for i in range(Line):
        for n in range(6):
            if İs_Prime(first) == True:
                print(green(first), end=" ")
                first += 1

            else:
                print((first), end=" ")
                first += 1
        print("")


main()
