"""
Escribe un programa que pida un número (límite) 
y luego te pida números hasta que la suma de los números introducidos supere el límite inicial. 
El programa termina escribiendo la lista de números.
Escribe límite: 50
Escribe un valor: 10
Escribe otro valor: 25
Escribe otro valor: 7
Escribe otro valor: 14
El límite a superar es 50. La lista creada es 10, 25, 7, 14 ya que la suma de estos números es: 56
"""


lista=[]

limite=int(input("Escribe limite, por favor: "))

num=int(input("Escribe un valor por favor: "))

total=int(0)

if num < limite:
    
    lista.append(num)
    
    total=num
    
while total < limite:
    
    print("Escribe otro valor por favor",end=" ")
    
    num=int(input())
    
    total+=num
    
    #lista.append(num)
    
    lista+=[num]
    
print ("El limite a superar es %d"%(limite),end=" ")

print ("La lista creada es: ",end=" ")

for i in lista:
    
    if i != lista[-1]:
        
        print (i,end=",")
        
    else:
        
        print (i,end=".")
        
print (" Suma de estos numeros es: %d"%(total))
    

"""lista=[]
print ("Escribe limite: ",end=" ")
limite=int(input())
print ("Escribe un valor inicial: ",end=" ")
num=int(input())
lista.append(num)
suma=num
while suma<limite:
    print ("Escribe otro valor: ",end=" ")
    num=int(input())
    lista.append(num)
    suma+=num
    #print (suma)
print ("El limite a superar es ",limite,". La lista creada es ",end=" ")   
print (*lista, sep=", ",end=" ")
print ("Suma de estos números es",suma)"""

