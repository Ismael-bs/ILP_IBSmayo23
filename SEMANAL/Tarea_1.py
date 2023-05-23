# Calcular el promedio de 3 calificaciones y decir si es aprobado o reprobado.

# ENTRADA DE DATOS
ingresa_calificación_UNO = float ( input ("Escribe la primera calificación: ")) 
ingresa_calificación_DOS = float ( input ("Escribe la segunda calificación: ")) 
ingresa_calificación_TRES = float ( input ("Escribe la tercera calificación: ")) 

# PROCESOS 
promedio = (ingresa_calificación_UNO + ingresa_calificación_DOS + ingresa_calificación_TRES) / 3


# jerarquia de operaciones 1. -pot, raiz, 2 - mult y div, y 3 - suma y resta
#aprobado entre 6  y 10
#Aprobado de pansaso Equivalente a 6
#reprobado Entre 0 y menor que 6
#Promedio Invalido menor que 0 o mayor que 10


# SALIDA DE DATOS
print ("El promedio de calificación es: ", round(promedio,2))
#print (if promedio < 8: 




if (promedio >6 and promedio<10):
    print("APROBADO")

elif(promedio >=0 and promedio <6):
    print("REPROBADO")

elif (promedio <0 or promedio >10):
    print ("ERRO  en Promedio")

elif (promedio == 6):
    print ("PASA pero de PANSASO")

#else :
 #  print ("ERROR  en Promedio")


