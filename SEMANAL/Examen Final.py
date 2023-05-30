# EJERCICIO DE EVALUACIÓN:
#Realizar un programa que realice un cuestionario con las siguientes 12 preguntas, muestre su resultado x / 12 y mostrar el promedio:
# Entrada de datos
aciertos = 0
calificacion_final = (aciertos * 10 ) / 12

print("Por favor seleccionar la Pregunta Correcta" )
print("1. Herramienta de programación, parecido al lenguaje español utilizado para crear código:")
print (" a) IDE     b) Pseudocódigo     c) Compilador     d) ANSI / ISO" )
x1 = (input(" Ingresa selección : "))
if (x1 == "b"):
    aciertos = aciertos +1

print("2. Conjunto de símbolos, letras, números, imágenes, audio y video organizadas y que son relevantes en un tiempo y forma determinados.")
print (" a) Información     b) Datos     c) Programa     d) Código" )
x2 = (input(" Ingresa selección : "))
if (x2 == "d"):
    aciertos = aciertos +1

print ("3. Instituciones encargadas de estandarizar reglas y simbología de los Diagramas de Flujo.")
print ( "    a) IEEE     b) IDE     c) ANSI/ISO     d) VSCode   " )
x3 = (input(" Ingresa selección : "))
if (x3 == "a"):
    aciertos = aciertos +1

print ("4. Serie de pasos consecutivos, ordenados y finitos que se siguen para resolver un problema.")
print ( "    a) Proceso     b) Solución     c) Función     d) Algoritmo " )
x4 = (input(" Ingresa selección : "))
if (x4 == "a"):
    aciertos = aciertos +1

print ("5. Conjunto de elementos que se relacionan para cumplir una función determinada.")
print ( "   a) Estructura     b) Datos     c) Operación     d) Sistema " )
x5 = (input(" Ingresa selección : "))
if (x5 == "c"):
    aciertos = aciertos +1

print ("6. Componente de un IDE que se encarga de traducir el código fuente a código máquina")
print ( "  a) Depurador     b) Editor de Texto     c) Terminal de Salida     d) Compilador/Intérprete " )
x6 = (input(" Ingresa selección : "))
if (x6 == "c"):
    aciertos = aciertos +1

print ("7. Elemento que se usa para almacenar una cantidad donde cambia su valor.")
print ( "   a) Constante     b) Variable     c) Librería     d) Tipo de Dato " )
x7 = (input(" Ingresa selección : "))
if (x7 == "b"):
    aciertos = aciertos +1

print ("8. Conjunto de símbolos, letras, números que no tienen un significado..")
print ( "   a) Datos     b) Estructura     c) Información     d) Sistema" )
x8 = (input(" Ingresa selección : "))
if (x8 == "a"):
    aciertos = aciertos +1

print ("9. Disciplina que argumenta conclusiones a partir de premisas mediante un razonamiento.")
print ( "  a) Filosofía     b) Sociología     c) Lógica     d) Argumentación" )
x9 = (input(" Ingresa selección : "))
if (x9 == "b"):
    aciertos = aciertos +1

print ("10. Medida, patrón, modelo o norma universal para realizar una actividad o producir un objeto.")
print ( "   a) Evento     b) Estándar     c) Calidad     d) Productividad" )
x10 = (input(" Ingresa selección : "))
if (x10 == "a"):
    aciertos = aciertos +1

print ("11. Conjunto de elementos ordenados que componen y son la base de algo físico o no físico.")
print ( "  a) Estructura     b) Sistema     c) Objeto     d) Virtual " )
x11 = (input(" Ingresa selección : "))
if (x11 == "b"):
    aciertos = aciertos +1

print ("12. Conjunto de instrucciones (código) que indican a la computadora tareas a realizar.")
print ( "  a) Operaciones/Cálculos     b) Sintaxis     c) Programa de Computadora     d) Comando" )
x12 = (input(" Ingresa selección : "))
if (x12 == "c"):
    aciertos = aciertos +1

calificacion_final = (aciertos * 10 ) / 12
print ("Tus aciertos fueron: ", aciertos)
print ("tu calificacion es : ",round ( calificacion_final, 4))
if (calificacion_final >= 9 and calificacion_final <=10):
    print ( "Excelente en Conocimiento APROBADO ")
elif(calificacion_final >=7 and calificacion_final <9):
    print ("APROBADO")
elif(calificacion_final >=6 and calificacion_final <7):
    print ("APROBADO de MILAGRO")
else:
    print ("NO ACREDITO  R E P R O B A D O")
