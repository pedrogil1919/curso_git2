'''
Created on 7 sept 2022

@author: pedro.gil
'''

def avanzar(x, y, a):
    if a == 'N': y += 1
    elif a == 'S': y -= 1
    elif a == 'E': x += 1
    elif a == 'O': x -= 1
    return x, y, a
    
def retroceder(x, y, a):
    if a == 'N': y -= 1
    elif a == 'S': y += 1
    elif a == 'E': x -= 1
    elif a == 'O': x += 1
    return x, y, a

x = 0
y = 0
a = 'N'
    
while True:
    
    instruccion = input("Siguiente instrucción:")
    print("Instrucción solicitada:", instruccion)
    if instruccion == "Q":
        break