# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить минимальное и максимальное из введённых чисел.
a = int(input())
min = a
max = a
while a !=0:
    if max>a:
        max = a
    elif min < a:
        min = a
    a = int(input())
print(max, min)


