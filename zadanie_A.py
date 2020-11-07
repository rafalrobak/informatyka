#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Przedmiot: Informatyka
# Kierunek studiów: Energetyka
# Semestr: zimowy
# Rok akademicki: 2020/2021
# Data (dzień.miesiąc.rok): 31.11.2020
# Imię: Rafał
# Nazwisko: Robak
# Numer albumu ZUT: 49672

"""
17.Napisz program, który w kolejnych linijkach będzie wypisywać liczby od 1 do 1000 w zapisie binarnym. Czyli w pierwszej linii 0, drugiej 1, trzeciej 10, czwartej 11 itd.
"""
for x in range(1, 1001):
    print("%s"%(bin(x)[2:]))
