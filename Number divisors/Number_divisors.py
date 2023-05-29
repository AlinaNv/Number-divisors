#coding=windows-1251
print("Введите число")
X=float(input())
for i in range (1,20000000000):
    if (X%i==0):
        print(i)

