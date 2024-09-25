string=str(input("Introduzca un valor superior a 5: "))
if len(string) <= 5:
    print("Error: Longitud no valida")
else:
    print(string[:2]+string[-2:])