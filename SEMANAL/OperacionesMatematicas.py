# Operaciones Matemáticas 

# Declarar o crear las variables
# nombre_completo = "Ismael Bustamante Samano"
# estatura = 1.70
# edad = 30
# correo_electrónico = 'isbustamantesa@gmail'
# status = True # Bool: True / False

# Importar la libreria o biblioteca para usar funciones matemáticas
import math # Matemáticas 

# ENTRADA DE DATOS
#Declarar o crear las variables
número_1 = float(input("Escribe el primer número: ")) #convertir un tipo de dato en otro tipo de dato, en este caso texto a número
número_2 = float(input("Escribe el segundo número: ")) # esto se le llama (CASTEO)

# Declarar constante
PI = 3.1416

# PROCESOS (Cálculos u operaciones Matemáticas y/logísticas)
suma = número_1 + número_2 
resta = número_1 - número_2
mult = número_1 * número_2 
div = número_1 / número_2 

potencia_1  = número_1 ** número_2  
potencia_2 = pow( número_1 , número_2 ) # Los valores o elementos que están dentro se llaman parámetros o argumentos  
cuadrado = número_1 ** 2
cubo = pow (número_2 , 3)

raiz_cuadrada_1 = math.sqrt(9)
raiz_cuadrada_2 = pow( 9, 1/2)
raiz_cúbica = pow( 27, 1/3)

módulo_residuo = número_1 % número_2


# SALIDA DE DATOS
print("la suma es = ",round(suma,2))
print("la resta es = ",round(resta,2))
print("la multiplicación es = ",round(mult,4))
print("la división es = ",div)
print("La constante PI es", PI)
print("La Potencia_1 es = ", potencia_1)
print("La Potencia_2 es = ", potencia_2)
print("El cuadrado  es = ", cuadrado)
print("el Cubo  es = ", cubo)
print("La raiz cuadrada 1 es = ", raiz_cuadrada_1)
print("La raiz cuadrada 2 es = ", raiz_cuadrada_2)
print("La raiz cubica es = ", raiz_cúbica)
print("El residuo es  = ", round(módulo_residuo,3))
