def pod1():
    with open('galerie.txt', 'r') as plik:
        kraje = {}
        for i in range(50):
            dane = plik.readline().split()
            if dane[0] not in kraje:
                kraje[dane[0]] = 1
            else:
                kraje[dane[0]] += 1

        for i in kraje.items():
            print(i)


def podb():
    with open('galerie.txt', 'r') as plik:
        miasta = {}
        for i in range(50):
            dane = plik.readline().split()
            # print('test ',dane)
            miasto = dane[1]
            dane = list(map(int, dane[2::]))
            suma = 0
            galerii = 0
            for x in range(0, len(dane), 2):
                if dane[x] == 0:
                    break
                lokal = dane[x] * dane[x + 1]
                suma += lokal
                galerii += 1
            miasta[miasto] = suma, galerii

        for i in miasta.items():
            print(i)
