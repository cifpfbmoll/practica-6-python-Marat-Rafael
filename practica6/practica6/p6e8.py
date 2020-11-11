"""
Escribe un programa que te pida primero un número 
y luego te pida números hasta que la suma de los números introducidos coincida con el número inicial. 
El programa termina escribiendo la lista de números.
Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 45
45 es demasiado grande. Escribe otro valor: 1
Escribe otro valor: 39
El límite a alcanzar es 50. La lista creada es: 10, 1, 39
"""


lista=[]

limit=int(input("Enter limit: "))

num=int(input("Enter number: "))

total=int(0)

total+=num

lista.append(num)

if total > limit:
    
        total-=num
        
        del lista[-1]
        
        print ("%d es demaciado grande. " %(num),end=" ") 
        
while total < limit:
    print ("Escribe otro numero: ",end=" ")
    
    num=int(input())
    
    total+=num
    
    lista.append(num)
    
    if total > limit:
        
        total-=num
        
        del lista[-1]
        
        print ("%d es demaciado grande. " %(num),end=" ")        
         
if total == limit:
    
    print ("Limite a alcanzar es %d .La lista creada es: " %(limit),end=" ")     
    
for i in lista:
    
    if i != lista[-1]:
        print (i,",",end=" ")
    else:
        print (i,end=" ")


