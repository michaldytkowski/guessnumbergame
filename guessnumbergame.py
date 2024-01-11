import random

randomnumber = random.randint(1, 100)
print(randomnumber)
trycounter = 1

while True:
    number = int(input("Podaj liczbę (1-100): "))
    if number == randomnumber:
        trycounter = trycounter + 1
        print("Wygrales! Potrzebowales " + str(trycounter) + " prob!")
        break
    elif number > randomnumber:
        print("Za duzo liczba!")
        trycounter = trycounter + 1
    elif number < randomnumber:
        print("Za mała liczba!")
        trycounter = trycounter + 1
