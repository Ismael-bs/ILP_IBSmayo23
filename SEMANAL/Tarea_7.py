#7. Pedir el nivel del agua en metros de una cisterna

#Si lleba a mas de 6; Desbordamiento de Agua en Cisterna
#Nivile de agua 6m "Apagar Bomba"
#Ente 4 y 6 m Desacelerar Bomba
#Entre 2 y 4M "Bomba Trabajando"
#entre 0 y 2, Acelerar Bomba de AGua
#Nivel de 0 "Encender bomba de agua
#Menor a 0 Fuga de cisterna

#ENTRADA DE DATOS

nivel_de_agua = int ( input ("Escribe el nivel de agua del Tinaco : ")) 

if (nivel_de_agua > 6):
    print("Desbordamiento de Tinaco")
elif(nivel_de_agua == 6):
    print("Apagar de inmediato la bomba")
elif(nivel_de_agua>=4 and nivel_de_agua<6):
    print("desacelerar bomba")
elif(nivel_de_agua>=2 and nivel_de_agua<4):
    print("Bomba Trabajando")
elif(nivel_de_agua>0 and nivel_de_agua<2):
    print("Acelerar la Bomba")
elif(nivel_de_agua==0):
    print ("Encender la Bomba de inmediato")
elif(nivel_de_agua<0):
    print ("Fuga en cisterna")

