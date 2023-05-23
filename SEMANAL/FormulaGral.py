# Aplicacion de la fórmula general
# Debemos pedir A B y C

import math # Matemáticas 


#ENTRADA
a = float ( input ("Escribe el valor para a: "))
b = float ( input ("Escribe el valor para b: "))
c = float ( input ("Escribe el valor para c: "))

#PROCESO
x1=  (((-b)+ (pow((b**2)-(4 * (a * c)),1/2)))/(2*a))

x2= ((-b)- (pow((b**2)-(4 * (a * c)),1/2)))/(2*a)



#Salida 
#round(módulo_residuo,3))

#print ("El valor de X 1 es igual ", x1)
print ("El valor de X 2 es igual ", x2)
print ("El valor de X 1 es igual ", round (x1,2))






