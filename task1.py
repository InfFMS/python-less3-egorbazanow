a= int(input())
p = 0
n = 0
while a !=0:
        if a< 0:
            n += 1
        elif a> 0:
            p+=1
        else:
            break
        a = int(input())
print('Положительных ', p)
print('Отрицательных ', n)