import random

while True:
    try:
        c = int(input("Введите некоторое число: "))
        break
    except (TypeError, ValueError) as e:
        print("Попробуйте снова ввести число!", e)

res = []
for x in range(0, c):
    res = random.sample(range(0, 500), c)
print(*res)
