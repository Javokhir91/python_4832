from random import randint
"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.
Input: 11 6
2 4 6 8 10 12 10 8 6 4 2
3 6 9 12 15 18
Output: 6 12
"""
lst = [2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2]
lst2 = [3, 6, 9, 12, 15, 18]
lst3 = []
for i in lst:
    for j in lst2:
        if i == j:
            lst3.append(j)
lst3 = sorted(set(lst3))
print(*lst3)

exit()
"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
4 -> 1 2 3 4
9
"""
# (lst[i % len(lst)])
lst = [randint(1, 10) for i in range(7)]
# lst = [4, 3, 2, 1]
lst2 = []
lst3 = []
for i in range(len(lst)):
    if len(lst) >= 3:
        lst2.append((lst[i:i+3]))
        if len(lst2[i]) >= 3:
            lst3.append((sum(lst2[i])))
# print(lst)
# print(lst2)
# print(lst3)
max_i = lst3[0]
for i in lst3:
    if i > max_i:
        max_i = i
print(max_i)
