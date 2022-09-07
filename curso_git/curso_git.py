'''
Created on 7 sept 2022

@author: pedro.gil
'''
      
def avanzar(x, y, a):
    'Avanzar una unidad'
    if a == 'N': y += 1
    elif a == 'S': y -= 1
    elif a == 'E': x += 1
    elif a == 'O': x -= 1
    return x, y, a
    
def retroceder(x, y, a):
    'Retroceder una unidad'
    if a == 'N': y -= 1
    elif a == 'S': y += 1
    elif a == 'E': x -= 1
    elif a == 'O': x += 1
    return x, y, a
    
def girar_derecha(x, y, a):
    'Girar a la derecha'
    if a == 'N': a = 'E'
    elif a == 'E': a = 'S'
    elif a == 'S': a = 'O'
    elif a == 'O': a = 'N'
    return x, y, a
    
def girar_izquierda(x, y, a):
    'Girar a la izquierda'
    if a == 'N': a = 'O'
    elif a == 'O': a = 'S'
    elif a == 'S': a = 'E'
    elif a == 'E': a = 'N'
    return x, y, a

x = 0
y = 0
a = 'N'

# Comiento del bucle principal.

while True:
    "Bucle principal"
    instruccion = input("Siguiente instrucción:")
    print("Instrucción solicitada:", instruccion)
    if instruccion == "Q":
        break
    if instruccion == 'A':
        x, y, a = avanzar(x, y, a)
    elif instruccion == 'R':
        x, y, a = retroceder(x, y, a)
    elif instruccion == 'D':
        x, y, a = girar_derecha(x, y, a)
    elif instruccion == 'I':
        x, y, a = girar_izquierda(x, y, a)
    else:
        print("Instrucción incorrecta.")
        
print("Fin del programa")
        