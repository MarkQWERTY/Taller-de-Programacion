seg=int(input("Introduce la cantidad en segundos: "))
dias = seg / (3600*24)
resto= seg % (3600*24)
horas = resto / 3600
resto1 = resto % 3600
minutos = resto1 / 60
segundos = resto1 % 60
print("Han transcurrido %.0f, dias, %.0f horas, %.0f minutos y %.0f segundos"%(dias, horas, minutos, segundos))