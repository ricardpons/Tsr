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

def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

def menu_principal():
    opciones = {
        '1': ('Opción 1 ', ecuacionPrimerGrado),
        '2': ('Opción 2 ', ecuacionSegundoGrado),
        '3': ('Opción 3 ', es_Primo),
        '4': ('Salir', salir)
    }

    generar_menu(opciones, '4')

if __name__ == '__main__':
    menu_principal()