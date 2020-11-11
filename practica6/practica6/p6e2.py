"""Escribe un programa que te pida números y los guarde en una lista. Para terminar de introducir número, simplemente escribe “Salir”. 
El programa termina escribiendo la lista de números.
Escribe un nombre: 14
Escribe una otro nombre: 123
Escribe una otro nombre: -25
Escribe una otro nombre: 123
Escribe una otro nombre: Salir
Los números que has escrito son [14, 123, -25, 123]
"""

numeros=[]

num = input ("Escribe un numero: ")

while num != "salir": 
  
    numeros.append(num)
    
    num = input ("Escribe otro numero: ")   
     
print ("Los números que has escrito son: ",end=" ")

for i in numeros:   
    
    if i != numeros[-1]:
        
        print (i,",",end=" ")
        
    else:
        
        print (i)


"""for i in numeros:
    
    print (i[1:-1],end=",") #no se por que despues de index[0] tambien pone coma
    
    print (i[-1],end=" ")
    
    """
    


