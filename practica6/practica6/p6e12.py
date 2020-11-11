"""
Escribir un programa para jugar a adivinar un número 
(el usuario piensa un número y el programa lo ha de adivinar). 
El programa empieza pidiendo entre qué números está el número a adivinar 
y luego intenta adivinar de qué número se trata. 
El usuario va diciendo si el número que ha dicho el programa es menor, 
mayor o igual al que se ha buscado.
Valor mínimo: 0
Valor máximo: 100
Piensa un número entre 0 y 100 a ver si lo puedo adivinar.
Es 50 ?: mayor
Es 75 ?: menor
Es 62 ?: menor
Es 56 ?: mayor
Es 59 ?: igual
Gracias por jugar!!
Mejoras (opcionales):
    • que al principio el programa se asegure de que el valor máximo es superior al valor mínimo.
    • Que el programa detecte "trampas", por ejemplo, si cuando dices "25" le decimos "mayor" 
    y al decir "26" le decimos "menor", 
    el programa debe decir que estamos haciendo trampas y debe dejar de jugar con nosotros.
"""

import random
minimo=int(input( "Valor mínimo:"))
maximo=int(input( "Valor máximo:"))
while maximo<=minimo:
    print ("El numero %d no es mayor que %d" %(maximo,minimo))
    maximo=int(input( "Valor máximo:"))
intentos=int(0)
respuesta=str()
print ("Piensa un número entre %d y %d a ver si lo puedo adivinar." %(minimo,maximo))
numRandom = random.randint (minimo,maximo)

print ("es %d" %(numRandom),"?: ",end=" ")

while respuesta != "si":    
    respuesta = str(input())
    if respuesta == "mayor":
        minimo = numRandom+1
        numRandom = random.randint (minimo,maximo)        
        print ("es %d" %(numRandom),"?: ")
        
    elif respuesta == "menor":
        maximo = numRandom-1
        numRandom = random.randint (minimo,maximo)
        print ("es %d" %(numRandom),"?: ")
        
    elif respuesta == "si":
        print (" Gracias por jugar !!! ")
        




