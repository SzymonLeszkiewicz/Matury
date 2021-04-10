# Szymon Leszkiewicz
# szymon.leszkiewicz10@gmail.com
def mark():
    print("Szymon Leszkiewicz\nszymon.leszkiewicz10@gmail.com")


def pod1():
    print("a)")
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
    print('\n\n')


def podb():
    print("b)")
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
    minm, min = 0, 9999
    maxm, max = 0, 0
    for i in miasta.items():
        if i[1][0] < min:
            min = i[1][0]
            minm = i[0]
        if i[1][0] > max:
            max = i[1][0]
            maxm = i[0]
    print('\n\n')
    print('min', min, minm)
    print('max',max, maxm)
    print('\n\n')


def podc():
    print("c)")
    with open('galerie.txt', 'r') as plik:
        miasta = {}
        for i in range(50):
            dane = plik.readline().split()
            miasto = dane[1]
            dane = list(map(int, dane[2::]))
            pow = []
            for x in range(0, len(dane), 2):
                if dane[x] == 0:
                    break
                pow.append(dane[x] * dane[x + 1])
            miasta[miasto] = len(set(pow))
        minm, min = 0, 9999
        maxm, max = 0, 0
        for i in miasta.items():
            if i[1] < min:
                min = i[1]
                minm = i[0]
            if i[1] > max:
                max = i[1]
                maxm = i[0]

        print(min, minm)
        print(max, maxm)
    print()


pod1()
podb()
podc()

mark()
