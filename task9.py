# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
N = int(input())
k = 0
n = 0
b = 1
c = 100
for i in range(N):
    x = int(input())
    if x%3 == 0  and 10<x<100:
        k+=1
        if b<x:
            b = x
        if c>x:
            c=x
if k>0 and c<100:
    print(c,b)
elif k>0 and c ==0:
    print(b,b)
else:
    print('no')
