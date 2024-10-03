edad = input("Introduzca su edad: ")

try: 
    age = int(edad)
except:
    print("ERROR: Not a number")
else:
    if age >= 18:
        print("Usted es mayor de edad")
    else:
        print("Usted es menor de edad")