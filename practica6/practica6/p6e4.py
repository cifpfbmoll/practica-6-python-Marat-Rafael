
"""
Escribe un programa que te pida dos números, de manera que el segundo sea mayor que el primero. 
El programa termina escribiendo los dos números tal y como se pide:
Escribe un número: 6
Escribe un número mayor que 6: 6
6 no es mayor que 6. Vuelve a introducir un número: 1
1 no es mayor que 6. Vuelve a introducir un número: 8
Los números que has escrito son 6 y 8
"""


   
num1=int(input("Escribe un numero: ")) 

num2=int(input("Escribe un numero mayor que %d " %(num1)))

while num2<=num1:
    
    print ("El numero %d no es mayor que %d. Vuelve a introducir un numero" %(num2,num1),end=" ")
    
    num2=int(input())
    
print ("los numeros que has escrito  son %d y %d " %(num1,num2))


"""num1=int(input("escribe un numero por favor: "))
print ("Escribe un numero mayor que",num1,": ",end=" ")
num2=int(input())
while num1>=num2:
    print ("El numero ",num2," no es mayor que ",num1,".",end=" ")
    print ("Vuelve a escribir segundo numero:",end=" ")
    num2=int(input())
print ("Los números que has escrito son ",num1,"y",num2)    
    """
