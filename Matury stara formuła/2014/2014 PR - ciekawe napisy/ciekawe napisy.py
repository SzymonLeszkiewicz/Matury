# Szymon Leszkiewicz
# szymon.leszkiewicz10@gmail.com
from math import sqrt, ceil


def mark():
    print('\n\n')
    print("Szymon Leszkiewicz\nszymon.leszkiewicz10@gmail.com")


def sumaascii(x):
    suma = 0
    for i in x:
        suma += ord(i)
    return suma


def czy_pierwsza(x):
    if x < 2:
        return False

    if x % 2 == 0 and x != 2:
        return False

    for i in range(3, ceil(sqrt(x)), 2):
        if x % i == 0:
            return False
    return True


def poda():
    with open("NAPIS.TXT", 'r') as plik:
        lista = plik.read().split()
        lista = list(map(sumaascii, lista))
        licznik = 0
        for x in lista:
            if czy_pierwsza(x):
                licznik += 1
        print(f'Napisow pierwszych jest: {licznik}\n')


def czy_rosnacy(x):
    x = list(map(ord, x))
    for i in range(len(x) - 1):

        if x[i] >= x[i + 1]:
            return False

    return True


def podb():
    with open("NAPIS.TXT", 'r') as plik:
        lista = plik.read().split()
        for x in lista:
            if czy_rosnacy(x):
                print(x)
    print('\n\n\n')


def podc():
    with open("NAPIS.TXT", 'r') as plik:
        lista = plik.read().split()
        mylist = []
        for x in lista:
            if lista.count(x) > 1:
                mylist.append(x)
                # odp.write(f'{x}\n')
                # del lista[lista.index(x)]

    mylist = set(mylist)
    print(mylist)


poda()
podb()
podc()
mark()
