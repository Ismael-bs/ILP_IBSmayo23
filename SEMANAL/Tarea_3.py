# determina la edad de una persona

#PROCESO
import datetime

año_de_nacimiento = float ( input ("Escriba su año de nacimiento "))
año_actual = datetime.datetime.now().year

#PROCESOS 
edad = año_actual - año_de_nacimiento


print ("Para este año ", año_actual)
print ( "tu edad en años es ", edad)
