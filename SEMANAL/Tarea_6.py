 # Pedir un número y decir si es par o impar
# se ocupa el de modulo residuo

#ENTRADA DE DATOS

numero = int ( input ("Escribe cualquier número: "))
descubrir = numero / 2

if descubrir % 2 != 0:
    print("Este es un número IMPAR")
else :    
    print( "Número PAR")

