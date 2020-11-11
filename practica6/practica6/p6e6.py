"""
Escribe un programa que pida primero dos números (máximo y mínimo) 
y que después te pida números intermedios. 
Para terminar de escribir números, 
escribe un número que no esté comprendido entre los dos valores iniciales. 
El programa termina escribiendo la lista de números.
Escribe un número: 6
Escribe un número mayor que 6: 4
4 no es mayor que 6. Vuelve a probar: 50
Escribe un número entre 6 y 50: 45
Escribe otro número entre 6 y 50: 13
Escribe otro número entre 6 y 50: 4
Los números situados entre 6 y 50 que has escrito son: 45, 13 
"""

    
lista=[]

num1=int(input("Esctibe un numero por favor: "))

num2=int(input("Escribe otro numero mayor que %d :" %(num1)))

while num2<=num1:
    
    num2=int(input("El numero %d no es mayor que numero %d. Vuelve a probar: " %(num2,num1)))
    
print("Escribe un numero entre %d y %d : " %(num1,num2),end=" ")  

numLista=int(input())  #son los numeros entre valores iniciales que guardamos en la lista

if numLista>num1 and numLista<num2:
    
    lista.append(numLista)
    
while numLista>num1 and numLista<num2:
    
    print("Escribe un numero entre %d y %d: " %(num1,num2),end=" ")  
    
    numLista=int(input())
    
    lista.append(numLista)
    
    if numLista>num2 or numLista<num1: #si numlista esta mayor o menor lo borramos de la lista
        
        del lista[-1]
       
print ("Los numeros situados entre %d y %d que has escrito son: " %(num1,num2),end=" ")

for i in lista:
    
    if i != lista[-1]:
        
        print (i,",",end=" ")
        
    else:
        print (i)


"""lista=[]
print ("Escribe un numero: ",end=" ")
num1=int(input())
lista.append(num1) #metemos primer numero en la lista
print ("Escribe un numero mayor que ",num1,":",end=" ")
num2=int(input())
while num2<=num1:   
    print (num2,"no es mayor que ",num1,". Vuelve a probar:",end=" ")
    num2=int(input())
lista.append(num2) #si segundo numero mayor que primero lo guardamos en la lista

#pedimos números entre primeros dos
print ("Escribe un numero entero entre",num1," y ",num2,":",end=" ")
num3=int(input())
while (num3>num1 and num3<num2 ):
    lista.append(num3)
    print ("Escribe un numero entero entre",num1," y ",num2,":",end=" ")
    num3=int(input())
print (*lista, sep=", ")"""
