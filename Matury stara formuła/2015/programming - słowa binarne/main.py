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
