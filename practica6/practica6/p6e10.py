"""
Escribe un programa que te pida los nombres y notas de alumnos. 
Si escribes una nota fuera del intervalo de 0 a 10, 
el programa entenderá que no quieres introducir más notas de este alumno. 
Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos. 
Nota: La lista en la que se guardan los nombres y notas tiene esta estructura 
[[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc], [nom3, nota1, nota2, etc], etc]
Dame un nombre: Héctor Quiroga
Escribe una nota: 4
Escribe otra nota: 8.5
Escribe otra nota: 12
Dame otro nombre: Inés Valls
Escribe una nota: 7.5
Escribe otra nota: 1
Escribe otra nota: 2
Escribe otra nota: -5
Dame otro nombre:
Las notas de los alumnos son:
Héctor Quiroga: 4.0 - 8.5
Inés Valls: 7.5 - 1.0 - 2.0
"""

lista = []

mas = True

while mas == True:  
     
    nombre=str(input("Nombre del alumno: ")) 
    
    alumno=[]
    
    alumno.append(nombre)
    
    if nombre != "":  
        
        nota=float(input("notas del alumno: ")) 
        
        alumno.append(nota)
        
        while nota<10:
            
            nota=float(input("notas del alumno: "))
            
            alumno.append(nota)
            
            if nota >10:
                
                del alumno[-1]
                     
        lista.append(alumno)
        
    if nombre == "":
        
        mas=False
    
print ("Las notas de los alumnos son: ")   

for i in lista:
    
    print (i[0],end=": ")
    
    print (*i[1:],sep=" - ")
    
     



