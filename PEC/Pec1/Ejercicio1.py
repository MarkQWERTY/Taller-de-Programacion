horas=int(input("Introduzca la hora (expresada en el formato 0-23): "))
minutos = int(input("Introduzca los minutos: "))
segundos = int(input("Introduzca los segundos: "))

total = horas * 3600 + minutos * 60 + segundos
medianocheB = (24*3600)-total 

print("Segundos transcurridos desde la última medianoche: %.0f segundos"%(total))
print("Segundos restantes para la última medianoche: %.0f segundos "%(medianocheB))
