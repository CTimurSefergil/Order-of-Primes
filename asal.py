from simple_colors import *


def main():
    Satır = int(input("Kaç Satır İstersiniz ? "))
    Kaç_Satır(Satır)


def Asal_Mı(Sayı):
    if Sayı > 1:
        for i in range(2, int(Sayı / 2 + 1)):
            if Sayı % i == 0:
                return False
        else:
            return True
    else:
        return False


def Kaç_Satır(Satır):
    x = int(input("Kaçıncı Satırdan Başlasın ? "))
    İlk = x + x * 5
    for i in range(Satır):
        for n in range(6):
            if Asal_Mı(İlk) == True:
                print(green(İlk), end=" ")
                İlk += 1

            else:
                print((İlk), end=" ")
                İlk += 1
        print("")


main()
