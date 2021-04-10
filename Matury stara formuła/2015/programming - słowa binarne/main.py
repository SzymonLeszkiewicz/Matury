# Szymon Leszkiewicz
# szymon.leszkiewicz10@gmail.com

def mark():
    print('\n\n')
    print("Szymon Leszkiewicz\nszymon.leszkiewicz10@gmail.com")


def bintodec(x):
    suma = 0
    potega = 1
    for i in x[::-1]:
        suma += potega * (ord(i) - 48)
        potega *= 2
    return suma


def poda():
    with open("slowa.txt") as plik:
        x = plik.read().split()
        licznik = 0
        for i in x:
            if i.count('0') > i.count('1'):
                licznik += 1
        with open("odp.txt", 'a') as odp:
            odp.write(f'a):\n')
            odp.write(f'{licznik}\n')


def blok(x):
    czy_przejscie = False

    if x[0] == '1':
        return False
    for i in range(len(x) - 1):

        if x[i] != x[i + 1] and czy_przejscie == False:
            czy_przejscie = True
        elif x[i] != x[i + 1] and czy_przejscie == True:
            return False
    return czy_przejscie


def podb():
    with open("slowa.txt") as plik:
        x = plik.read().split()
        licznik = 0
        for i in x:
            if blok(i):
                licznik += 1
        with open("odp.txt", 'a') as odp:
            odp.write(f'b):\n')
            odp.write(f'{licznik}\n')


def ilezer(x):
    '''liczymy jaki jest najdl nieprzerwany ciag zer'''
    dlu = x.split('1')
    lista = list(map(len, dlu))
    return max(lista)


def podc():
    with open("slowa.txt") as plik:
        with open("odp.txt", 'a') as odp:
            odp.write(f'c):\n')
            x = plik.read().split()
            naj = 0
            for i in x:
                if naj < ilezer(i):
                    naj = ilezer(i)
            licznik = 0
            for i in x:
                if naj == ilezer(i):
                    odp.write(f'{i}\n')
            odp.write(f'{naj}\n')


poda()
podb()
podc()
mark()
