from tkinter import *
from math import sqrt
import sys


## First grade equation##

def ecuacionPrimerGrado():
    a = float(input('Introduzca el valor de A :'))
    b = float(input('Introduzca el valor de  B :'))
    
    if a != 0 :
        x= -b/a
        return print('La solucion es  : x=%4.3f' % (x)) 
       
    if a == 0:
        return print('La ecuacion no tiene solucion')


## Second grade equation##
def ecuacionSegundoGrado():
    a = float(input('Introduzca el valor de A :'))
    b = float(input('Introduzca el valor de B :'))
    c = float(input('introducue el valor de c :'))
    x1 = (-b + sqrt(b**2 -4 *a*c)) / (2*a)

    x2 = (-b - sqrt(b**2 -4 *a*c)) / (2*a)
    
    return print('La solucion es : x1=%4.3f y x2=%4.3f ' % (x1,x2))

## Numeros primos ##
def es_Primo():
    num=int(input('Introduzca un numero :'))
    prime = True
    divisor = 2
    while divisor < num :
        if num % divisor == 0:
            prime = False
        divisor +=1
    if prime :
        return print('El numero  ' ,num,' es primo ')
    else:
        return print('El numero ',num,'no es primo ')


def salir():
    print('Saliendo')
    sys.exit()


## Creacion del menu ##
root =  Tk()
menubar = Menu(root)
root.config(menu=menubar)
root.mainloop
filemenu =Menu(menubar,tearoff=0)

menubar.add_cascade(label='Ecuaciones')

if __name__ == '__main__':
    menu_principal()