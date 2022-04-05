import random
kosc = int
razy = int
def gra(kosc,razy):
    kosc = int(input("Ile ścian ma rzucana przez ciebie kość? "))
    razy = int(input("Ile razy chcesz rzucić kością? "))
    try:
        list = []
        while razy > 0:
            wynik = random.randrange(1,kosc)
            print(wynik)
            list.append(wynik)
            razy = razy-1
        print("Suma wyrzuconych wartości to", sum(list))            
    except ValueError:
        print("Podana wartość nie jest liczbą.")
        input("")
def wyrzucanie_statystyk(kosc,razy):
    try:
        list = []
        while razy > 0:
            wynik = random.randrange(1,kosc)
            print(wynik)
            while wynik == 1:
                print("Przerzucamy kości o wartości 1")
                wynik = random.randrange(1,kosc)
                print(wynik)
            list.append(wynik)
            razy = razy-1
        for wartość in range(2):
            print("Usuwam najniższą wartość", min(list))
            list.remove(min(list))
        print("Suma wyrzuconych wartości to", sum(list))
        stats.append(sum(list))
    except ValueError:
        print("Podana wartość nie jest liczbą.")
        input("")
choice = input("Dla losowania statystyk wpisz 's', a dla gry wpisz 'g' ")
if choice == "s":
    statystyki = int((input("Ile statystyk chcesz wylosować? ")))
    kosc = int(input("Ile ścian ma rzucana przez ciebie kość? "))
    razy = int(input("Ile razy chcesz rzucić kością dla każdej ze statystyk? "))
    stats = []
    while statystyki > 0:
        wyrzucanie_statystyk(kosc,razy)
        statystyki -= 1
    print("Wyrzucone przez Ciebie statystyki to:", stats[:])
    input("")
elif choice == "g":
    while choice == "g":
        gra(kosc,razy)
else:
    print("Wybrana została nieprawidłowa wartość.")
