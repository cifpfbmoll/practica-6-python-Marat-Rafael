"""
Escribe un programa que pida notas y los guarde en una lista. Para terminar de introducir notas, 
escribe una nota que no esté entre 0 y 10. 
El programa termina escribiendo la lista de notas.
Escribe una nota: 7.5
Escribe una nota: 0
Escribe una nota: 10
Escribe una nota: -1
Las notas que has Escrito son [7.5, 0.0, 10.0]
"""



lista_notas=[]

nota=float(input("Escribe una nota: "))

lista_notas.append(nota)

while (nota<10 and nota>0):
    
    nota=float(input("Escribe una nota: "))
    
    lista_notas.append(nota)
    
del lista_notas[-1]  
 
print ("Las notas escritas son: ",end=" ")
    

for i in lista_notas:
    
    if i != lista_notas[-1]:
        
        print (i,",", end=" ")
        
    else:
        print (i)



"""lista_notas=[]
nota=float(input("Escribe una nota"))
while (nota>0 and nota<10):
    lista_notas.append(nota)
    nota=float(input("Escribe una nota: "))
print ("Las notas que has escrito son", end=" ")
#print (lista_notas)
print (*lista_notas, sep=", ")"""
