# # Требуется вывести все целые степени двойки
# # (т.е. числа вида 2k), не превосходящие числа N.
# # Пример:
# # 10 -> 1 2 4 8

vvod = int(input('Введите число: '))
chislo = 1
print(f'Все целые степени двойки от числа {vvod}: ')
while chislo <= vvod:
    print(chislo, end = ' ')
    chislo *= 2