from random import randint

# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
"""
# list_1 = [1, 4, 3, 7, 8, 9, 2, 2, 2, 2, 2]
# k = 2
# c = 0
# for i in list_1:
#     if k == i:
#         c += 1
# print(c)


arr = [randint(1, 5) for i in range(int(input('введите длину массива: ')))]
# arr = [1, 4, 3, 7, 8, 9, 2, 2, 2, 2, 2]
print(arr)
find_num = int(input('введите искомое число: '))
# find_num = 2
count = 0
for i in range(len(arr)):
    if find_num == arr[i]:
        count += 1
print(f'искомое число - {find_num}, внутри массива встречается {count} раз!')
"""

print('*' * 50)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
"""
# list_1 = [15, 11, 6, 7, 8, 1]
list_1 = [randint(1, 100) for i in range(int(input('введите длину массива: ')))]
print(list_1)
k = int(input('введите искомое число: '))
min_distance = abs(k - list_1[0])
index = 0  # близкий по величине элемент
for i in range(1, len(list_1)):
    count = abs(k - list_1[i])
    if count < min_distance:
        min_distance = count
        index = i
print(list_1[index])

# arr = [randint(1, 5) for i in range(int(input('введите длину массива: ')))]
arr = [1, 2, 3, 4, 5, 10]
k = 9
min_distance = abs(k - arr[0])
index = 0
for i in range(1, len(arr)):
    count = abs(k - arr[i])
    if count < min_distance:
        min_distance = count
    index = i
print(arr[index])
"""

# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
#
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков
#
"""
scrabble = input('введите только одно слово, которое содержит русские буквы: ')
sum_scrabble = 0
dic = {
    'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
    'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
    'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
    'Й': 4, 'Ы': 4,
    'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
    'Ш': 8, 'Э': 8, 'Ю': 8,
    'Ф': 10, 'Щ': 10, 'Ъ': 10,
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 1,
    'Q': 10, 'Z': 10
}
for i in scrabble.upper():
    sum_scrabble += dic[i]
print(sum_scrabble)
"""






