# На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, 
# которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное 
# количество монет, которые нужно перевернуть.
# Пример:
# 5 -> 1 0 1 1 0
# Ответ: 2

import random
                                               # или так
                                               # from collections import Counter

n = int(input('Введите количество монеток: '))
temp = []
for i in range(n):
    orel_reshka = round(random.uniform(0,1))
    temp.append(orel_reshka)
print(temp)

count = 0                                      # count = Counter(temp)
for i in temp:                                 # print(perevorot)
    if i == 0:                                 # perevorot = count[0]
        count += 1                             # .get и нужный ключ
print(count)