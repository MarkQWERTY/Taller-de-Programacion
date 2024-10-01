#Primer ejercicio:

horas = int(input("Dime las horas en formato 24 horas: "))      # Damos las horas que queramos
minutos = int(input("Dime los minutos: "))                      # Damos los minutos que queramos
segundos = int(input("Dime los segundos: "))                    # Damos los segundos que queramos

horas2 = horas*3600                 # Pasamos las horas a segundos 
minutos2 = minutos*60               # Pasamos los minutos a segundos
sect = horas2+minutos2+segundos     # Sumamos todo en segundos
sect2 = 86400-sect                  # Restamos las 24H a los segundos totales 

print ("El total de segundos pasados desde la ultima medianoche son: ",sect)            # Imprimimos las soluciones
print ("El total de segundos que quedan para la siguiente medianoche son: ",sect2)      # Imprimimos las soluciones