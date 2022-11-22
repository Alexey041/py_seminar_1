#Напишите программу, которая на вход принимает 5 чисел и находит максимальное
#из них.

#- 1, 4, 8, 7, 5 -> 8
#- 78, 55, 36, 90, 2 -> 90

""" numbers =[]
for _ in range(5):
    n = int(input())
    numbers.append(n)
maxx = numbers[0]

for el in numbers:
    if el > maxx:
        maxx = el

print(maxx) """

maxx = int(input())
for _ in range(4):
    n = int(input())
    if n > maxx:
        maxx = n

print(maxx)
