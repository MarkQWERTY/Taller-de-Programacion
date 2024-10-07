hora = str(input("Introduce la hora en formato 24 horas: "))

try:
    hour=int(hora[0:2])
except:
    
    print(hora + " AM")
else:
    if hour >= 12:
        print(str(int(hora[0:2])-12)+hora[2::]+ " PM")