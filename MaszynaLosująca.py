import random
import time

uczestnicy = []
losowania = int(input("Ile losowań? "))
liczba = int(input("Ilu uczestników losowania? "))

for uczestnik in range(liczba):
    imie = (input(f"Wprowadź uczestnika #{len(uczestnicy) + 1}: "))
    uczestnicy.append(imie)

x = 100/liczba
for zapis in range(liczba):
    print(f"Zapisywanie danych... {x}% ")
    x = 100/liczba + x
    if x >= 100:
        x = 100.0
    else:
        x = x
    time.sleep(0.2)

print(f"""
Uczestnicy losowania to: {uczestnicy[:]}""")

print("""
Tasowanie elementów ...
""")
time.sleep(3.14)

random.shuffle(uczestnicy)

y = 100/losowania
for los in range(losowania):
    print(f"Losowanie w toku... {y}%")
    y = 100/losowania + y
    if y >= 100:
        y = 100.0
    else:
        y = y
    time.sleep(0.01)

wyniki = random.choices(uczestnicy,weights=None,cum_weights=None,k=losowania)
print(f"""
Wyniki losowania to:
""")
lp = 1
while len(wyniki) > 0:
    print(f"""{lp}: {wyniki[0]}
    """)
    del wyniki[0]
    lp += 1

input("Gratulacje dla szczęśliwych zwycięzców!")
