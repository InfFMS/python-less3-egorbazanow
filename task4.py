# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить сумму тех введённых чисел, которые делятся на 5.
s = 0
for i in range(0, 100000):
    x = int(input())
    if x % 5 == 0 and x!=0:
        s = s + x
    elif x == 0:
        break
print(s)