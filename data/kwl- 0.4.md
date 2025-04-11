testing realtime

-   w tesler.flowworks.com logujesz sie na pstepinsky
-   tworzysz nowy projekt - "realtime test A.1    
-   wchodzisz sobie na site NE008 i wybierasz kanal AutoQAQC Flag Level v0.1 jako wejsciowy i AutoQAQC Flag Level v0.2 wyjsciowy
-   piszesz kod pythonowy ktory bedzie wybieral randomowo liczbe od 1 do 100 i zapisywal ja pod timestamp NOW do kanalu wyjsciowego
poza tym bedzie printowal ostatnie 100 wartosci z kanalu wejsciowego
-   zapisujesz jako realtime
-   tworzysz 2 projekt z AutoQAQC Flag Level v0.2 na wejsciu i AutoQAQC Flag Level v0.1 na wyjsciu -> projekt nazwiesz 'realtime test A.2'
-   kod pythonowy w nim bedzie zczytywal ostatnia wartosc z kanalu ( z randomowa liczba wpisana przez A.1) i printowal date oraz liczbe
-   bedzie tworzyl tyle rekordow ile wynosi liczba ktora odczytal, kazdy z nich bedzie mial timestamp od NOW w przeszlosc cofajac sie co 5 min. wartosc pod kazdym timestampem bedzie losowa z przedzialu (-10,-1)
-   zapisujesz A.2 jako realtime
-   weryfikujesz w logach A1. i A2 czy dziala to jak chcialas - A1 zapisuje date z liczba wzbudzajac A2 ktory zapisje x danych z datami wzbudzajac A1 itd ...