# -*- encoding: utf-8 -*-
stevilo = 0

while stevilo <= 100:
    stevilo = int(raw_input("Vnesite število med 1 in 100: "))
    for stevilo in range (1, stevilo + 1):
        print(stevilo)

        if stevilo % 3 == 0 and stevilo % 5 == 0:
            print("fizzbuzz")
            continue
        elif stevilo % 5 == 0:
            print("buzz")
        elif stevilo % 3 == 0:
            print("fizz")
    break