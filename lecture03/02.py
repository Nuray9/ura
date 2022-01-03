print("Введите значения")
print("a=? ")
a = int(input())
if a<0:
    print("Неверно")
    exit()
print("b=? ")
b = int(input())
if b<0:
    print("Неверно")
    exit()
while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
gcd = a + b
print(gcd)
