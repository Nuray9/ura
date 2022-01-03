while True:
    try:
        key = input("Введите NdM: ")
        if 'd' not in key:
            raise d_exception("Запишите d")
        N = int(key[0])
        M = int(key[2:])
        cubes = [[x + 1 for x in range(M)] for _ in range(N)]
        break
    except Exception as e:
        print("Неправильный ввод, запишите d.")

c = [0]
for i in range(len(cubes)):
    cmb = [a + b for a in c for b in cubes[i]]
    c = [x for x in cmb]

for x in sorted((set(c))):
    print(x, '=', round(c.count(x)/len(c) * 100, 2), "%")
