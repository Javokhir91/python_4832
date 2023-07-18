"""
# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – орел.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 1 0 1 1 0
# 2

import random
from itertools import count

coins = int(input("number of coins: "))  # количество монет
eagle = 0
tails = 0
for i in range(coins):
    bitcoin = random.randint(0, 1)
    print(bitcoin, end=' ')
    if bitcoin == 1:  # если
        eagle += 1
    elif bitcoin == 0:
        tails += 1
print('\n')
if eagle > tails:
    print(f'minimum number of coins to flip: {tails}')  # минимальное количество монет, которые нужно перевернуть
elif eagle == tails:
    print(f'the minimum number of coins tossed is: {eagle}')  # монет, которые нужно перевернуть равны
else:
    print(f'minimum number of coins to flip: {eagle}')  # минимальное количество монет, которые нужно перевернуть


# немного забегая в перед ;D

coin = int(input(": "))
coins = [random.randint(0, 1) for i in range(coin)]
print(coins)
if coins.count(0) < coins.count(1):
    print(coins.count(0))
elif coins.count(0) == coins.count(1):
    print(coins.count(0))
else:
    print(coins.count(1))
"""

"""
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
4 4 -> 2 2
5 6 -> 2 3


sum_num = 5
mult_num = 6
num_x, num_y = 0, 0
for x in range(1, 1001):  # 1 2
    for y in range(1, 1001):  # 1 2 3
        if x + y == sum_num and x * y == mult_num:
            num_x, num_y = x, y
print(num_x, num_y)

"""

"""
# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("enter number: "))
# n = 10
coun = 1
# Цикл while
# while n > coun:
#     print(coun, end=" ")
#     coun *= 2
# Цикл for
for i in range(n):
    if coun < n:
        print(coun, end=' ')
        coun *= 2
        
"""
