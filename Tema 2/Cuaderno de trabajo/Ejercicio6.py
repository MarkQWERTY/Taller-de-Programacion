año = int(input("Introduce el año: "))

def es_bisiesto():
    if año > 1582 and año % 4 == 0:
        print(f"El año {año} si es bisiesto")
    elif año > 1582:
        print(f"El año {año} no es bisiesto")
    else:
        print("Error: Año inferior a 1582")



es_bisiesto()