# rzucamy monetą 1000 razy.
# za kazdym razem kiedy wyrzucimy orła to zwiększamy licznik o 1, w przeciwnym wypadku zmniejszamy licznik o -1
# na koniec wypisujemy licznik i znajdujemy średnią

import random
from statistics import mean


def rzucMoneta():
    return random.randint(0, 1)


def Average(list):
    return mean(list)


licznik = 0
srednia = [0] * 1
avg = 0
for i in range(1000):
    if rzucMoneta() == 0:
        licznik += 1
        srednia.append(licznik)
    elif rzucMoneta() == 1:
        licznik -= 1
        srednia.append(licznik)

srednia.pop(0)
avg = Average(srednia)
    # print(srednia)
print("srednia wynikow: ", int(avg))
# print("srednia pokazywanie: ", srednia)
print("wynik koncowy: ", licznik)


