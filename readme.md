  
![tabelka][./tabelka.png]

Wygenerowałem trzy 300000 elementowe tablice zgodnie z treścią zadania. Zakres liczb dla losowej tablicy to od 0 do 10000.

Najszybszym algorytmem sortującym okazał się **merge sort**, jest to również najbardziej stabilny algorytm spośród wybranych (bardzo zbliżone do siebie wyniki) co było zgodne z oczekiwaniami.

**Quicksort** jest na drugim miejscu pod względem szybkości sortowania tablicy losowych liczb, ale niestety okazał się najmniej stabilnym algorytmem, ponieważ nie działa on na pozostałych dwóch tablicach, głębokość rekurencji jest zbyt duża i program wyrzuca błąd - co było spodziewane przy tym algorytmie.

**Heapsort** to taki wolniejszy **merge sort**, tzn. jest również stabilny, ale mniej efektywny - działa wolniej. Z plusów to potrzebuje tabeli mniej niż **merge sort**, czyli napewno zajmuje mniej pamięci.

Zaimplementowałem najprostszą odsłone algorytmu **bubblesort** i widać to po wynikach, poradził sobie najgorzej ze wszystkich algorytmów, wyniki nie są zbliżone do siebie - jedyne jego zastosowanie widzę przy bardzo małych tablicach.


### Tomasz Rybczyński
