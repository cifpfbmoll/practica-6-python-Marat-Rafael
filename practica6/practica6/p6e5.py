"""
Escribe un programa que te pida números cada vez más grandes y que se guarden en una lista. 
Para acabar de escribir los números, escribe un número que no sea mayor que el anterior. 
El programa termina escribiendo la lista de números:
Escribe un número: 6
Escribe un número mayor que 6: 10
Escribe un número mayor que 10: 12
Escribe un número mayor que 12: 25
Escribe un número mayor que 25: 9
Los números que has escrito son: 6, 10, 12, 25  
(Comentario si os fijáis ya no se imprime la lista tal cual, hay que imprimir uno por uno los valores de la lista,
haced esto así a partir de ahora)
"""
       
    
lista=[]
print ("Escribe un numero: ",end=" ")
num1=int(input()) 

lista.append(num1)

print ("Escribe un numero mayor que %d" %(num1),end=" ")

num2=int(input())

if num2 > num1:
    
    lista.append(num2)
    
while num2 > num1:
    
    num1 = num2
    
    num2=int(input("Escribe un numero mayor que %d "%(num1)))
    
    lista.append(num2)
    
del lista[-1]

for i in lista:
    
    if i != lista[-1]:
        
        print (i,end=", ")
        
    else:
        
        print (i)

    
    

"""
lista=[]
print ("Escribe un numero: ",end=" ")
num1=int(input())
lista.append(num1)
print ("Escribe un numero mayor que ",num1,":",end=" ")
num2=int(input())
lista.append(num2)
while num2>num1:  
    num1=num2
    print ("Escribe un numero mayor que: ",num2,":",end=" ")
    num2=int(input())
    lista.append(num2)
del lista[-1]       
print (lista)
print(*lista, sep=", ")


for i in range (0,len(lista)):    
        print ((lista[i]),end=", ")"""
        
     
    
    