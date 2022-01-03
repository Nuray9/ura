import math
   
def inp_ut(x):
        while True:
            try:
                text = '{} {} {} '.format("Введите сторону 1: ",x,' = ')
                a = float(input(text))
                if a<0:
                    print ("Значение неверное.")
                    exit ()
                return a
            except ValueError:
                print("Значение неверное.")
                

a = inp_ut('a')



def inp_ut(x):
    while True:
        try:
            text = '{} {} {} '.format("Введите сторону 2: ",x,' = ')
            b = float(input(text))
            if b<0:
                    print ("Значение неверное.")
                    exit ()
            return b
        except ValueError:
            print("Значение неверное.")

b = inp_ut('a')

def inp_ut(x):
    while True:
        try:
            text = '{} {} {} '.format("Введите угол между сторонами: ",x,' = ')
            c = float(input(text))
            if c<0:
                    print ("Значение неверное.")
                    exit ()
            return c
        except ValueError:
            print("Значение неверное.")

c = inp_ut('a')
    
cc = c * math.pi / 180
d = 2
e = 0.5
z = (a ** d) + (b ** d) - (2 * a * b * math.cos(cc))
v = z ** 0.5
    
print (v)

