# Напишите программу, которая принимает на вход два числа и проверяет, 
# является ли одно число квадратом другого.
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

""" num1 = int(input('Введите первое число: '))   #Ввод через Enter
num2 = int(input('Введите второе число: '))

if num1 ** 2 == num2 or num2 ** 2 == num1:
    print('да')
else:
    print('нет')
 """

""" some_str = input().split(', ')  #Ввод в строку через запятую и пробел
num1 = int(some_str[0])
num2 = int(some_str[1])

if num1 ** 2 == num2 or num2 ** 2 == num1:
    print('да')
else:
    print('нет') """

num1, num2 = map(int, input().split(', ')) #map берет каждый элемент из массива
if num1 ** 2 == num2 or num2 ** 2 == num1: #и приводит его к типу int
    print('да')
else:
    print('нет')