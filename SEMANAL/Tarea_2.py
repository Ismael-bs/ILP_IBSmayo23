# Calcular el área y perímetro de un círculo. 
# P=2pi radio
# A= pi r (al cuadrado)

#ENTRADAS
radio = float ( input ("Escriba el radio "))
PI = 3.1416

#PROCESOS
perimetro = 2*PI* radio

area = PI * (pow( radio , 2 ))


#SALIDA
print ("El perimetro  es: ", round(perimetro,2))
print ("El Area   es: ", round(area,2))




