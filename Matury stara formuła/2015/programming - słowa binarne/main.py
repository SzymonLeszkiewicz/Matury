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
