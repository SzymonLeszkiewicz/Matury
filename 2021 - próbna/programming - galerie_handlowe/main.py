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
