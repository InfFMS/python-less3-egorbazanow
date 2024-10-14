# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
n =int(input())
N = int(input())
min = n
max = n
k = 0
for i in range(0,N):
    x = int(input())
    if x >= 10 and x <= 99:
        if min<x:
            min = x
        elif max > x:
            max = x
        elif x == 0:
            break
        k += 1
if k !=0:
    print(min, max)
else:
    print('no')
