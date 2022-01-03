import random

while True:
    try:
        с = int(input("Введите некоторое число: "))
        break
    except (TypeError, ValueError) as e:
        print("Попробуйте снова ввести целое число!", e)
res = []
for x in range(0, с):
    res.append(random.randint(0, 500))

def sort(res):
    n = len(res)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if res[j] > res[j + 1]:
                res[j], res[j + 1] = res[j + 1], res[j]
    return res
print(*sort(res))
