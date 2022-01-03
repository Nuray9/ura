import math
def inp_ut(x):
    while True:
        try:
            text = '{} {} {} '.format("Введите, пожалуйста,Цельсия: ",x,' = ')
            a = float(input(text))
            return a
        except ValueError:
            print("Значение неверное.")

a = inp_ut('a')
b = 9 / 5 * a + 32
print (b)
return a

