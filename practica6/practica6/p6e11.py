"""
Escribir un programa para jugar a adivinar un número 
(el ordenador "piensa" el número y el usuario lo ha de adivinar). 
El programa empieza pidiendo entre qué números está el número a adivinar, 
se "inventa" un número al azar y luego el usuario va probando valores. 
El programa va decidiendo si son demasiado grandes o pequeños. pista:
import random
import time

minimo = int (input ( "Valor mínimo:"))
max = int (input ( "Valor máximo:"))
secreto = random.randint (mínimo, máximo)
Valor mínimo: 0
Valor máximo: 100
A ver si adivinas un número entero entre 0 y 100.
Escribe un número: 20
Demasiado pequeño! Volver a probar: 30
Demasiado grande! Volver a probar: 27
Correcto! Lo has intentado 3 veces.
"""

import random
#import time

minimo=int(input( "Valor mínimo:"))

maximo=int(input( "Valor máximo:"))

secreto = random.randint (minimo,maximo)

intentos=int(0)

num=int()

print ("A ver si adivinas un número entero entre %d y %d " %(minimo,maximo))

print ("Escribe un numero: ")

while num != secreto:
    
    num=int(input())
    
    if num < secreto:
        
        print ("Demasiado pequiño! Vuelve a probar: ",end=" ")
        
    if num > secreto:
        
        print ("Demasiado grande! Volver a probar: ",end=" ")
        
    if num == secreto:
        
        print ("Correcto! Lo has intentado %d veces." %(intentos))
        
    intentos+=1

print (secreto)




