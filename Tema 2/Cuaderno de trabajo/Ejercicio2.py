importe = input("Introduce el importe de la compra: ")
tarjeta = bool(input("Tarjeta?: "))

try:
    var=float(importe)
except:
    print("Error: Entrada no valida.")
else:
    if tarjeta == True and var > 100:
        print(f"El precio final es de {var*0.98}$")
    elif tarjeta == False and var >= 100:
        print(f"El precio final es de {var*0.95}$")
    else:
        print(f"El precio final es de {var}$")
