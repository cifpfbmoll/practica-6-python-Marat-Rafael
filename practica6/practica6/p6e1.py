
"""Escribe un programa que te pida palabras y las guarde en una lista. 
Para terminar de introducir palabras, simplemente pulsa Enter. 
El programa termina escribiendo la lista de palabras.
Escribe una palabra: viaje
Escribe más palabras: aventura
Escribe más palabras: cómic
Escribe más palabras:
Las palabras que has Escrito son [ 'viaje', 'aventura', 'cómic']
"""



lista=[]

palabra = input('Escribe una palabra: ')

while palabra != '':
    
    lista.append(palabra)
    
    palabra = input('Escribe otra palabra: ')
    
print ("las palabras que has escrito son: ", end=" ")

for i in lista:
    
    if i != lista[-1]:
        
        print(i,end=", ")
        
    else:
        
        print (i)


