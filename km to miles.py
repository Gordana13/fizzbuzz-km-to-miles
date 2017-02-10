# -*- encoding: utf-8 -*-
print("Pozdravljeni, to je pretvornik km v milje.")

km = float(raw_input("Prosim, vnesite kilometre: "))
miles = km * 0.62137
print "%s km ima %s milj. " % (km, miles)

vprasanje = raw_input("Ali želite narediti novo pretvorbo, da ali ne? ").lower()

while vprasanje == "da":
    km = float(raw_input("Ponovno vpisite km: "))
    miles = km * 0.62137
    print(miles)

    vprasanje = raw_input("Ali želite narediti novo pretvorbo, da ali ne? ").lower()

if vprasanje == "ne":
    print("Hvala in nasvidenje.")