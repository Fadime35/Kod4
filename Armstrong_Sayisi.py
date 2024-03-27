#Armstrong Sayısı
"""Tüm basamaklarındaki rakamların sayı değerlerinin küpleri toplamı,
kendisine eşit olan sayılara "Armstrong sayı"denir. """

sayi=input("Bir sayı giriniz:")
toplam=0
for i in sayi:
    toplam+=int(i)**3

if(toplam==int(sayi)):
    print(sayi,"armstrong sayısıdır.")
else:
    print(sayi,"armstrong sayısı değildir.")
